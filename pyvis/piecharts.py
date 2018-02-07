from pybaseball import playerid_lookup
from pybaseball import statcast_batter
import numpy as np
import matplotlib.pyplot as plt

# Plate appearance breakdown
# Time can be a day or a range of dates (ex: hit_breakdown('2016-05-01', 'dustin', 'pedroia) 
# or hit_breakdown('2016-05-01 to 2017-05-01', 'dustin', 'pedroia'))
def PA_breakdown(time, firstname, lastname):
    playerid = playerid_lookup(lastname, firstname)
    print('Calculating hit breakdown. One moment please.')
    if "to" in time: data = statcast_batter(time[0:10], time[14:], player_id=int(playerid['key_mlbam'][0]))
    else: data = statcast_batter(time, player_id=int(playerid['key_mlbam'][0]))
    data = data[np.isfinite(data['babip_value'])]
    freq = data['events'].value_counts()
    print("Frequency of hit breakdown:")
    print(freq)
    print("Dropping infrequent events for pie chart.")
    total = sum(freq.tolist())
    freq_edited = [[elm1, elm2] for elm1, elm2 in zip(freq.keys().tolist(), freq.tolist()) if elm2 >= 0.02*total]
    other_total = [elm for elm in freq.tolist() if elm < 0.02*total]
    freq_edited.append(['other', sum(other_total)])
    print("Pie chart of hit breakdown:")
    plt.pie([row[1] for row in freq_edited], labels=[row[0] for row in freq_edited], autopct='%1.1f%%')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
