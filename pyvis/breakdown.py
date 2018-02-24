# Breakdown file
from pybaseball import playerid_lookup
from pybaseball import statcast_batter
from pybaseball import statcast_pitcher
import numpy as np
import matplotlib.pyplot as plt

# Time can be a day or a range of dates (ex: batter_event_breakdown('2016-05-01', 'dustin', 'pedroia) 
# or batter_event_breakdown('2016-05-01 to 2017-05-01', 'dustin', 'pedroia'))
# Displays a pie chart of the data
def batter_event_breakdown(time, firstname, lastname):
    data = process_data(time, firstname, lastname, 'batter')
    general_event_breakdown(data, 'hit event')
    
# Time can be a day or a range of dates (ex: pitcher_event_breakdown('2016-05-01', 'chris', 'sale') 
# or pitcher_event_breakdown('2016-01-01 to 2017-01-01', 'chris', 'sale'))
# Displays a pie chart of the data
def pitcher_event_breakdown(time, firstname, lastname):
    data = process_data(time, firstname, lastname, 'pitcher')
    general_event_breakdown(data, 'pitch event')
    
# Pitch selection breakdown
# Time can be a day or a range of dates (ex: pitch_selection_breakdown('2016-05-01', 'chris', 'sale') 
# or pitch_selection_breakdown('2016-01-01 to 2017-01-01', 'chris', 'sale'))
def pitch_selection_breakdown(time, firstname, lastname):
    data = process_data(time, firstname, lastname, 'pitcher')
    freq = data['pitch_type'].value_counts()
    print("Frequency of pitch breakdown:")
    print(freq)
    # Add to dict below as needed
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
    
# General event breakdown
# Takes in data from statcast function and displays pie chart of data
def general_event_breakdown(data, name):
    data = data[np.isfinite(data['babip_value'])]
    freq = data['events'].value_counts()
    print("Frequency of " + name + " breakdown:")
    print(freq)
    print("Dropping infrequent events for pie chart.")
    total = sum(freq.tolist())
    freq_edited = [[elm1, elm2] for elm1, elm2 in zip(freq.keys().tolist(), freq.tolist()) if elm2 >= 0.02*total]
    other_total = [elm for elm in freq.tolist() if elm < 0.02*total]
    freq_edited.append(['other', sum(other_total)])
    print("Pie chart of " + name + " breakdown:")
    plt.pie([row[1] for row in freq_edited], labels=[row[0] for row in freq_edited], autopct='%1.1f%%')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    
# Returns correct type of data (dependent on player and his type)
def process_data(time, firstname, lastname, pos):
    playerid = playerid_lookup(lastname, firstname)
    if "to" in time:
        if pos == 'batter': return statcast_batter(time[0:10], time[14:], player_id=int(playerid['key_mlbam'][0]))
        elif pos == 'pitcher': return statcast_pitcher(time[0:10], time[14:], player_id=int(playerid['key_mlbam'][0]))
        else: return None
    else: 
        if pos == 'batter': return statcast_batter(time, player_id=int(playerid['key_mlbam'][0]))
        elif pos == 'pitcher': return statcast_pitcher(time, player_id=int(playerid['key_mlbam'][0]))
        else: return None
