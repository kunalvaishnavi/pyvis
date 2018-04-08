# Explaining PyVis

PyVis is split up into different files, depending on the user's needs. For instance, if the user needs to plot data points 
in a strike zone, the aptly named `strike_zone.py` file will do so. At the top of each function is a brief explanation as to 
what the function does. The `data.py` file is the "initializer" as it has all of the imports needed for all files and has the 
main function used to scrape the data for all other functions in PyVis. Hence, in all other files, the only import statement 
is `import data`.

All core functions of PyVis that the user can utilize are listed below, along with an explanation of what each does:
* `batterBR(time, firstname, lastname)`: Creates a pie chart of the events that happen in a batter's plate appearances during the given timeframe.
  * `batterBR('2016-05-01', 'dustin', 'pedroia')`
  * `batterBR('2016-05-01 to 2017-05-01', 'dustin', 'pedroia')`
* `pitcherBR(time, firstname, lastname)`: Creates a pie chart of the events that happen after a pitcher's pitch during the given timeframe.
  * `pitcherBR('2016-05-01', 'chris', 'sale')`
  * `pitcherBR('2016-05-01 to 2017-05-01', 'chris', 'sale')`
* `pitchSelectionBR(time, firstname, lastname)`: Creates a pie chart of the types of pitches a pitcher throws during the given timeframe.
  * `pitchSelectionBR('2016-05-01', 'chris', 'sale')`
  * `pitchSelectionBR('2016-05-01 to 2017-05-01', 'chris', 'sale')`
* `scatterPlot(time, firstname, lastname, pos)`: A dynamic scatterplot for a batter or pitcher, depending on user input. Options for the
scatterplot's axes are: spin rate, release speed, launch speed, launch angle, hit distance, release extension.
  * `scatterPlot('2017-09-30', 'mookie', 'betts', 'batter')`
  * `scatterPlot('2016-04-01 to 2016-05-01', 'chris', 'sale', 'pitcher')`
* `sprayChart(time, firstname, lastname)`: Creates a spray chart of a batter's hits during the given timeframe.
  * `sprayChart('2017-04-30', 'mookie', 'betts')`
  * `sprayChart('2017-04-01 to 2017-05-01', 'mookie', 'betts')`
* `batterSZ(time, firstname, lastname)`: Plots strike zone of pitches that a batter sees from the umpire's perspective.
  * `batterSZ('2016-05-01', 'david', 'ortiz')`
  * `batterSZ('2016-04-01 to 2016-05-01', 'david', 'ortiz')`
* `pitcherSZ(time, firstname, lastname)`: Plots strike zone of pitches that a pitcher throws from the pitcher's perspective.
  * `pitcherSZ('2017-05-30', 'chris', 'sale')`
  * `pitcherSZ('2017-05-01 to 2017-06-01', 'chris', 'sale')`
* `matchupSZ(time, batter_firstname, batter_lastname, pitcher_firstname, pitcher_lastname)`: Plots strike zone of pitches for a specific 
batter vs. pitcher matchup from the umpire's perspective.
  * `matchupSZ('2016-08-01', 'mookie', 'betts', 'james', 'paxton')`
  * `matchupSZ('2016-08-01 to 2016-08-02', 'mookie', 'betts', 'james', 'paxton')`
* `swingPlane(time, firstname, lastname)`: Creates a spray chart of a batter's hits during the given timeframe.

All core functions of PyVis that are hidden to the user but assist the above user functions are listed below, along with an explanation 
of what each does:
* `process_data(time, firstname, lastname, pos)`: Gathers data for a certain timeframe for the assigned player.
* `generalBR(data, name)`: Takes data from any of the BR (a.k.a. breakdown) functions and displays pie chart of data. Note that name
in this instance is not firstname/lastname, but rather it is the label for the type of BR function called to obtain the data.
* `generalPlot(data, firstname, lastname)`: Takes data from `scatterPlot` and generates a scatterplot based on user's input. Options for
the user include choosing the data for the axes and adding a trendline to the scatterplot.
* `drawChart(data, firstname, lastname)`: Draws a baseball field and plots data points. Accounts for changes in coordinate system between
MLB's Statcast and the coordinate system used to draw the baseball field.
* `generalSZ(data, firstname, lastname, posid)`: Takes data from any of the SZ (a.k.a. strike zone) functions and displays strike zone
with data. Note that `posid` identifies whether the player is a batter or pitcher.
* `drawPlane(data, firstname, lastname)`: Draws a swing plane based on data given from `swingPlane`.
