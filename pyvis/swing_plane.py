import data # data.py

# Swing plane of player's hits
# Time can be a day or a range of dates (ex: swingPlane('2017-04-30', 'mookie', 'betts') 
# or swingPlane('2017-04-01 to 2017-05-01', 'mookie', 'betts'))
def swingPlane(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'batter')
    if data.size == 0: 
        return "Error: Did not find any data. Try again."
    indices = []
    for i, row in enumerate(data['description']):
        if row == 'hit_into_play_score' or row == 'hit_into_play_no_out': 
            indices.append(i)
    data = data.iloc[indices]
    data['launch_angle'] = data['launch_angle'].round()
    freq = data['launch_angle'].value_counts()
    drawPlane(freq, firstname, lastname)
        
# Draws swing plane based on given data from above
def drawPlane(data, firstname, lastname): 
    print("Generating swing plane for " + firstname.title() + " " + lastname.title() + ":")
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, polar=True)
    ax.bar(data.keys().tolist(), data.tolist(), color='red', width=.075, linewidth=0.1, label='Hits')
    ax.set_thetamin(-80)
    ax.set_thetamax(80)
    ax.legend()
    plt.show()
