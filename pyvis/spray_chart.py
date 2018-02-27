import data # data.py

# Spray chart of a batter's hits
# Time can be a day or a range of dates (ex: sprayChart('2017-04-30', 'mookie', 'betts') 
# or sprayChart('2017-04-01 to 2017-05-01', 'mookie', 'betts'))
def sprayChart(time, firstname, lastname):
    data = processData(time, firstname, lastname, 'batter')
    if data.size == 0: return "Error: Did not find any data. Try again."
    data = data[np.isfinite(data['babip_value'])]
    drawChart(data, firstname, lastname)

# Draw baseball field and plot data points
def drawChart(data, firstname, lastname):
    fig = plt.figure()
    # foul lines & base paths
    print("Creating the spray chart.")
    leftFoulLine = lines.Line2D((0,1), (1.5,0), color='black', transform=fig.transFigure, figure=fig)
    rightFoulLine = lines.Line2D((1,2), (0,1.5), color='black', transform=fig.transFigure, figure=fig)
    leftBaseLine = lines.Line2D((0.85,1), (0.225,0.45), color='gray', transform=fig.transFigure, figure=fig)
    rightBaseLine = lines.Line2D((1,1.15), (0.45,0.225), color='gray', transform=fig.transFigure, figure=fig)
    fig.lines.extend([leftFoulLine, rightFoulLine, leftBaseLine, rightBaseLine])
    # infield curve
    infieldPts = [(0.8,0.3), (1,0.7), (1.2,0.3)]
    infieldDir = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
    infieldPath = Path(infieldPts, infieldDir)
    infield = patches.PathPatch(infieldPath, edgecolor='gray', facecolor='none', transform=fig.transFigure, lw=2)
    # outfield curve
    outfieldPts = [(0.35,0.975), (1,1.75), (1.65,0.975)]
    outfieldDir = [Path.MOVETO, Path.CURVE3, Path.CURVE3]
    outfieldPath = Path(outfieldPts, outfieldDir)
    outfield = patches.PathPatch(outfieldPath, edgecolor='gray', facecolor='none', transform=fig.transFigure, lw=2)
    fig.patches.extend([infield, outfield])
    # convert points to RJ Weise's coordinate system, then my coordinate system
    # based on above values for infield & outfield points: my_x ==> [0.4, 1.6] & my_y ==> [0, 1.75]
    x_arr = [((((x-125)/120)+1)/(2/1.2))+0.4 for x in data['hc_x'] if not np.isnan(x)]
    y_arr = [((y-200)*-1)/(200/1.75) for y in data['hc_y'] if not np.isnan(y)]
    for x, y in zip(x_arr, y_arr):
        cir = patches.Circle((x,y), radius=.003, transform=fig.transFigure, color='blue')
        fig.patches.extend([cir])
    plt.figtext(0.8, 1.75, "Spray Chart of " + firstname.title() + " " + lastname.title(), size='large')
    plt.show()
