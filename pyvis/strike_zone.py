import data # data.py

# SZ in function names = strike zone (ex: batterSZ = batter strike zone)

# Plots strike zone of pitches for a batter
# Time can be a day or a range of dates (ex: batterSZ('2016-05-01', 'david', 'ortiz') 
# or batterSZ('2016-04-01 to 2016-05-01', 'david', 'ortiz'))
def batterSZ(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'batter')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    generalSZ(data, firstname, lastname, 'batter')

# Plots strike zone of pitches for a pitcher
# Time can be a day or a range of dates (ex: pitcherSZ('2017-05-30', 'chris', 'sale') 
# or pitcherSZ('2017-05-01 to 2017-06-01', 'chris', 'sale'))
def pitcherSZ(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'pitcher')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    generalSZ(data, firstname, lastname, 'pitcher')

# Plots strike zone of pitches for a specific batter vs. pitcher matchup from the umpire's perspective
# Time can be a day or a range of dates (ex: matchupSZ("2016-08-01", "mookie", "betts", "james", "paxton")
# or matchupSZ("2016-08-01 to 2016-08-02", "mookie", "betts", "james", "paxton")
def matchupSZ(time, batter_firstname, batter_lastname, pitcher_firstname, pitcher_lastname):
    data = processData(time, batter_firstname, batter_lastname, 'batter')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    pitcherid = playerid_lookup(pitcher_lastname, pitcher_firstname)
    data = data[data['pitcher'] == pitcherid['key_mlbam'][0]]
    generalSZ(data, batter_firstname, batter_lastname, 'batter')

# Takes in data from above functions and plots strike zone
def generalSZ(data, firstname, lastname, posid):
    print("Finding strike zone dimensions for player.")
    top = np.round(np.mean(data['sz_top']), 3) # height from ground to top of strike zone
    bot = np.round(np.mean(data['sz_bot']), 3) # height from ground to bottom of strike zone
    
    exclude = checkUser(data)
    data = fixData(data, exclude)
    labels = setLabels(exclude)
    
    print("Creating strike zone from player's perspective.")
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111)
    if posid == 'batter': ax.scatter(data['plate_x'], data['plate_z'], c=setColors(data), marker='o')
    # default is x coords in batter's perspective, so multiply by -1 to reverse direction for pitcher
    elif posid == 'pitcher': ax.scatter([x_pos*-1 for x_pos in data['plate_x']], data['plate_z'], c=setColors(data), marker='o')
    # personalize strike zone per player
    ax.add_patch(patches.Rectangle((-20.14/24,bot), 20.14/12, top-bot, fill=False))
    ax.set_xlim(-2,2)
    ax.set_ylim(0,6)
    plt.legend(handles=labels)
    plt.xlabel("Horizontal Distance Away from Center of Plate (feet)")
    plt.ylabel("Height of Pitch (feet)")
    if posid == 'batter': plt.title("Strike Zone of " + firstname.title() + " " + lastname.title() + " from Umpire's Perspective")
    elif posid == 'pitcher': plt.title("Strike Zone of " + firstname.title() + " " + lastname.title() + " from Pitcher's Perspective")
    plt.show()

# Determine which options the user wants to see
def checkUser(data):
    options = ["hit into play", "called strikes", "swinging strikes & fouls", "balls"]
    exclude = []
    for option in options:
        print("Include pitches that are " + option + "? (yes/no)")
        ans = input()
        if ans.lower() in ["n", "no"]: 
            if option == "hit into play": 
                exclude.append("hit")
            elif option == "called strikes": 
                exclude.append("called_strike")
            elif option == "swinging strikes & fouls": 
                exclude.extend(["swinging_strike", "foul"])
            elif option == "balls": 
                exclude.append(option[0:len(option)-1])
    return exclude

# Remove unwanted data based on user's input
def fixData(data, exclude):
    options = data['description'].value_counts().keys().tolist()
    indices = []
    for i, r in enumerate(data['description']):
        for elm in exclude:
            if elm in r:
                indices.append(i)
    data.drop(data.index[indices], inplace=True)
    return data

# Set labels for graph
def setLabels(exclude):
    if "foul" in exclude: 
        exclude.pop(exclude.index("foul"))
        
    blue = patches.Patch(color='blue', label='Hit Into Play')
    red = patches.Patch(color='red', label='Called Strike')
    brown = patches.Patch(color='brown', label='Foul/Swinging Strike')
    green = patches.Patch(color='green', label='Ball')
    colors = [blue, red, brown, green]
    labels = [patch.get_label() for patch in colors]
    
    for elm in exclude:
        if elm == "hit": 
            colors.pop(labels.index("Hit Into Play"))
        elif elm == "called_strike": 
            colors.pop(labels.index("Called Strike"))
        elif elm == "swinging_strike": 
            colors.pop(labels.index("Foul/Swinging Strike"))
        elif elm == "ball": 
            colors.pop(labels.index("Ball"))
    return colors

# Set color depending on type of outcome on pitch
def setColors(data):
    colors = []
    for row in data['description']:
        if "hit" in row: 
            colors.append("blue")
        elif "called_strike" 
        in row: colors.append("red")
        elif "foul" in row or "swinging_strike" in row: 
            colors.append("brown")
        else: 
            colors.append("green")
    return colors
