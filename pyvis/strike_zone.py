import breakdown
import matplotlib.patches as patches

# Plots strike zone of pitches for a batter
# Time can be a day or a range of dates (ex: batter_strike_zone('2016-05-01', 'david', 'ortiz') 
# or batter_strike_zone('2016-04-01 to 2016-05-01', 'david', 'ortiz'))
def batter_strike_zone(time, firstname, lastname):
    data = process_data(time, firstname, lastname, 'batter')
    general_strike_zone(data, firstname, lastname, 'batter')

# Plots strike zone of pitches for a pitcher
# Time can be a day or a range of dates (ex: pitcher_strike_zone('2017-05-30', 'chris', 'sale') 
# or pitcher_strike_zone('2017-05-01 to 2017-06-01', 'chris', 'sale'))
def pitcher_strike_zone(time, firstname, lastname):
    data = process_data(time, firstname, lastname, 'pitcher')
    general_strike_zone(data, firstname, lastname, 'pitcher')

# Plots strike zone of pitches for a specific batter vs. pitcher matchup from the umpire's perspective
# Time can be a day or a range of dates (ex: specific_matchup_strike_zone("2016-08-01", "mookie", "betts", "james", "paxton")
# or specific_matchup_strike_zone("2016-08-01 to 2016-08-02", "mookie", "betts", "james", "paxton")
def specific_matchup_strike_zone(time, batter_firstname, batter_lastname, pitcher_firstname, pitcher_lastname):
    data = process_data(time, batter_firstname, batter_lastname, 'batter')
    pitcherid = playerid_lookup(pitcher_lastname, pitcher_firstname)
    data = data[data['pitcher'] == pitcherid['key_mlbam'][0]]
    general_strike_zone(data, batter_firstname, batter_lastname, 'batter')

# Plot strike zone using given data
def general_strike_zone(data, firstname, lastname, posid):
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
    # personalize strike zone per player using https://baseballwithr.files.wordpress.com/2015/02/plate_dims.jpg
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
            if option == "hit into play": exclude.append("hit")
            elif option == "called strikes": exclude.append("called_strike")
            elif option == "swinging strikes & fouls": exclude.extend(["swinging_strike", "foul"])
            else: exclude.append(option[0:len(option)-1])
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
    if "foul" in exclude: exclude.pop(exclude.index("foul")) # helps later on
    blue = patches.Patch(color='blue', label='Hit Into Play')
    red = patches.Patch(color='red', label='Called Strike')
    brown = patches.Patch(color='brown', label='Foul/Swinging Strike')
    green = patches.Patch(color='green', label='Ball')
    colors = [blue, red, brown, green]
    # when creating labels, exception for "Foul/Swinging Strike" because of slash:
    labels = [patch.get_label().lower().replace(" ", "_") if i != 2 else patch.get_label().lower()[5:].replace(" ", "_") for i, patch in enumerate(colors)]
    # remove unwanted labels
    for elm in exclude:
        colors.pop(labels.index(elm))
    return colors

# Set color depending on type of outcome on pitch
def setColors(data):
    colors = []
    for row in data['description']:
        if "hit" in row: colors.append("blue")
        elif "called_strike" in row: colors.append("red")
        elif "foul" in row or "swinging_strike" in row: colors.append("brown")
        else: colors.append("green")
    return colors
