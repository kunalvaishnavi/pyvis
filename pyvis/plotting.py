import breakdown
import matplotlib.patches as patches

# Plots strike zone of pitches for a batter
# Time can be a day or a range of dates (ex: batter_strike_zone_plotting('2016-05-01', 'david', 'ortiz') 
# or batter_strike_zone_plotting('2016-04-01 to 2016-05-01', 'david', 'ortiz'))
def batter_strike_zone_plotting(time, firstname, lastname):
    data = process_data(time, firstname, lastname, 'batter')
    print("Finding strike zone dimensions for player.")
    top = np.round(np.mean(data['sz_top']), 3) # height from ground to top of strike zone
    bot = np.round(np.mean(data['sz_bot']), 3) # height from ground to bottom of strike zone
    print("Creating strike zone for player from umpire's perspective.")
    plt.figure(figsize=(6,6))
    ax = plt.subplot(111)
    ax.scatter(data['plate_x'], data['plate_z'], c=setColors(data), marker='o')
    # Dimensions: https://baseballwithr.files.wordpress.com/2015/02/plate_dims.jpg
    ax.add_patch(patches.Rectangle((-20.14/24,bot), 20.14/12, top-bot, fill=False)) # personalize strike zone per batter
    ax.set_xlim(-2,2)
    ax.set_ylim(0,6)
    blue_patch = patches.Patch(color='blue', label='Hit into play')
    red_patch = patches.Patch(color='red', label='Strike/foul')
    green_patch = patches.Patch(color='green', label='Ball')
    plt.legend(handles=[blue_patch, red_patch, green_patch])
    plt.xlabel("Distance Away from Center of Plate (feet)")
    plt.ylabel("Height of Pitch (feet)")
    plt.title("Strike Zone of " + firstname.title() + " " + lastname.title() + " from Umpire's Perspective")
    plt.show()
    
# Set color depending on type of outcome on pitch
def setColors(data):
    colors = []
    for row in data['description']:
        if "hit" in row: colors.append("blue")
        elif "strike" in row or "foul" in row: colors.append("red")
        else: colors.append("green")
    return colors
