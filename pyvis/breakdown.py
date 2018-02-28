import data # data.py

# BR in function names = breakdown (ex: batterBR = batter breakdown)

# Batter event breakdown in pie chart
# Time can be a day or a range of dates (ex: batterBR('2016-05-01', 'dustin', 'pedroia') 
# or batterBR('2016-05-01 to 2017-05-01', 'dustin', 'pedroia'))
def batterBR(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'batter')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    generalBR(data, 'hit event')
    
# Pitcher event breakdown in pie chart
# Time can be a day or a range of dates (ex: pitcherBR('2016-05-01', 'chris', 'sale') 
# or pitcherBR('2016-01-01 to 2017-01-01', 'chris', 'sale'))
def pitcherBR(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'pitcher')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    generalBR(data, 'pitch event')
    
# Pitch selection breakdown in pie chart
# Time can be a day or a range of dates (ex: pitchSelectionBR('2016-05-01', 'chris', 'sale') 
# or pitchSelectionBR('2016-01-01 to 2017-01-01', 'chris', 'sale'))
def pitchSelectionBR(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'pitcher')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
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
    
# Takes in data from above functions and displays pie chart of data
def generalBR(data, name):
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
