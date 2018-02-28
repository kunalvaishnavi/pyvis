import data # data.py

# A dynamic scatterplot for a batter or pitcher, depending on user input
# Time can be a day or a range of dates (ex: scatterPlot("2017-09-30", "mookie", "betts", 'batter')
# or scatterPlot('2016-04-01 to 2016-05-01', 'chris', 'sale', 'pitcher'))
# Pos is either 'pitcher' or 'batter'
def scatterPlot(time, firstname, lastname, pos):
    data = processData(time, firstname, lastname, pos)
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    generalPlot(data, firstname, lastname)

# Generates a scatterplot based on user's input
def generalPlot(data, firstname, lastname):
    options = ['spin rate', 'release speed', 'launch speed', 'launch angle', 'hit distance', 'release extension']
    user = askUser(options)
    x_data = getRightData(data, int(user[0]))
    y_data = getRightData(data, int(user[1]))
    
    drop = []
    for i, (x, y) in enumerate(zip(x_data, y_data)):
        if np.isnan([x]) or np.isnan([y]):
            drop.append(i)
    x_data.drop(drop, inplace=True)
    y_data.drop(drop, inplace=True)
    
    print("Matching data points to type of pitch.")
    # get summary of pitches
    pitch_types = data.iloc[x_data.keys().tolist()]['pitch_type'].value_counts().keys().tolist()
    cmap = plt.get_cmap('viridis')
    # map a pitch to a specific color
    colors = cmap(np.linspace(0, 1, len(pitch_types)))
    
    names = {'FF': '4 Seam Fastball', 'FA': '4 Seam Fastball', 'FT': '2 Seam Fastball', 'FC': 'Cutter', 
             'FS': 'Splitter', 'FO': 'Forkball', 'SI': 'Sinker', 'SL': 'Slider', 'CU': 'Curveball', 
             'KC': 'Knuckle Curve', 'EP': 'Eephus', 'CH': 'Changeup', 'SC': 'Screwball', 'KN': 'Knuckleball', 
             'IN': 'Unidentified', 'UN': 'Unidentified'}
    allPatches = []
    for i, color in enumerate(colors):
        allPatches.append(patches.Patch(color=color, label=names[pitch_types[i]]))
    plt.scatter(x_data, y_data, c=colors)
    plt.xlabel(options[int(user[0])].title())
    plt.ylabel(options[int(user[1])].title())
    plt.title(options[int(user[1])].title() + " vs. " + options[int(user[0])].title() + " for " + firstname.title() + " " + lastname.title())

    print("Would you like a trendline (a.k.a. line of best fit) for this scatterplot? (yes/no)")
    trendline_decision = input()
    if trendline_decision.lower() in ["y", "yes"]:
        z = np.polyfit(x_data, y_data, 1)
        p = np.poly1d(z)
        plt.plot(x_data, p(x_data))
        print("y=%.6fx+(%.6f)"%(z[0],z[1]))
    plt.legend(handles=allPatches)
    plt.show()
    
# Asks user what two topics to plot
def askUser(options):
    print("Choose two topics to compare. Type the number next to the topic below, along with the axis you want it on.")
    print("For example, if you want to visualize spin rate (y-axis) vs. launch speed (x-axis), type '20' starting with \nthe x axis number.")
    for i, option in enumerate(options):
        if option == 'spin rate':
            print(i, option, '(rpm)')
        elif option == 'release speed':
            print(i, option, '(mph)')
        elif option == 'launch speed':
            print(i, option, '(mph)')
        elif option == 'launch angle':
            print(i, option, '(degrees)')
        elif option == 'hit distance':
            print(i, option, '(feet)')
        elif option == 'release extension':
            print(i, option, '(feet)')
    user = input()
    if user[0] == user[1]:
        print("You put the same topic twice. Try again.")
        user = input()
    return user
    
# Get data based on user's input
def getRightData(data, choice):
    if choice == 0:
        return data['release_spin_rate']
    elif choice == 1:
        return data['release_speed']
    elif choice == 2:
        return data['launch_speed']
    elif choice == 3:
        return data['launch_angle']
    elif choice == 4:
        return data['hit_distance_sc']
    elif choice == 5:
        return data['release_extension']
    else:
        return None
