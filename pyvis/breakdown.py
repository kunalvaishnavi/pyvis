from pybaseball import playerid_lookup
from pybaseball import statcast_batter
from pybaseball import statcast_pitcher
import numpy as np
import matplotlib.pyplot as plt

# Hit breakdown
# Time can be a day or a range of dates (ex: hit_breakdown('2016-05-01', 'dustin', 'pedroia) 
# or hit_breakdown('2016-05-01 to 2017-05-01', 'dustin', 'pedroia'))
def hit_breakdown(time, firstname, lastname):
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

# Pitch selection breakdown
# Time can be a day or a range of dates (ex: pitch_breakdown('2016-05-01', 'chris', 'sale') 
# or pitch_breakdown('2016-01-01 to 2017-01-01', 'chris', 'sale'))
def pitch_breakdown(time, firstname, lastname):
    playerid = playerid_lookup(lastname, firstname)
    if "to" in time: data = statcast_pitcher(time[0:10], time[14:], player_id=int(playerid['key_mlbam'][0]))
    else: data = statcast_pitcher(time, player_id=int(playerid['key_mlbam'][0]))
    freq = data['pitch_type'].value_counts()
    print("Frequency of pitch breakdown:")
    print(freq)
    names = {'FF': '4 Seam Fastball', 'FA': '4 Seam Fastball', 'FT': '2 Seam Fastball', 'FC': 'Cutter', 
             'FS': 'Splitter', 'FO': 'Forkball', 'SI': 'Sinker', 'SL': 'Slider', 'CU': 'Curveball', 
             'KC': 'Knuckle Curve', 'EP': 'Eephus', 'CH': 'Changeup', 'SC': 'Screwball', 'KN': 'Knuckleball', 
             'IN': 'Unidentified', 'UN': 'Unidentified'}
    freq_edited = []
    for elm1, elm2 in zip(freq.keys().tolist(), freq.tolist()):
        if names[elm1] not in [r[0] for r in freq_edited]:
            freq_edited.append([names[elm1], elm2])
        else:
            for i, r in enumerate(freq_edited):
                if r[0] == names[elm1]:
                    freq_edited[i][1] += elm2
    print("Pie chart of pitch selection:")
    plt.pie([row[1] for row in freq_edited], labels=[row[0] for row in freq_edited], autopct='%1.1f%%')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
