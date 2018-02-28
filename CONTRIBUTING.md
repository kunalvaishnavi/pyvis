# Contributing

Ideas:

- ~~Strike zone plotting like [here](https://baseballsavant.mlb.com/visuals/profile?pitch_type=&batter=&pitcher=&balls=&strikes=&year=2016&min_strikes=0&bucket_size=.5&chart_type=swings&player_id=&position=&player_name=) (plotting where pitches fall using coordinates from Statcast data, plotting pitch speed zones, plotting pitch type zones)~~
- A 3D view of a [baseball field](https://baseballsavant.mlb.com/hr_derby) (to make a spray chart of a player's at-bats to show things like distance of fly ball)
- ~~Swing plane to show the launch angle at which a batter swings like [here](https://www.google.com/search?biw=1280&bih=639&tbm=isch&sa=1&ei=6MB9WuLsKcGyzwK6g7bwBg&q=launch+angle+baseball&oq=launch+angle+baseball&gs_l=psy-ab.3..0j0i24k1l3.24808.26328.0.26453.12.12.0.0.0.0.83.781.12.12.0....0...1c.1.64.psy-ab..0.12.774...0i7i30k1j0i67k1j0i13k1j0i8i7i30k1j0i8i30k1.0.pQgnhiXo93w#imgrc=T7I-AFy7qRGFGM:)~~
- 25-man dream rosters based on [WAR](https://www.fangraphs.com/library/misc/war/)
- Compiling batting averages per zone in the strike zone like [this](https://baseballsavant.mlb.com/visuals/profile?pitch_type=&batter=&pitcher=&balls=&strikes=&year=2016&min_strikes=0&bucket_size=.5&chart_type=swings&player_id=&position=&player_name=)
- Customizing strike zone plotting for things like type of pitch thrown or count in at-bat

To Fix:
- In `breakdown.py`, the pie charts are simplified such that very small values are combined. It would be nice to see all of the values in a better looking way.
- There is a CSV issue in `pybaseball` where if you run one of its functions that gathers Statcast data, it sometimes won't grab all of the data and instead return an error. See the comment on line 43 [here](https://github.com/jldbc/pybaseball/blob/master/pybaseball/statcast.py). It's hard to explain over words so start an issue if you're still confused.

If you have any additional ideas, feel free to implement them and then send a pull request. Make sure to use the format used for all other functions and files. If you're unaware, see [Explaining PyVis](https://github.com/kunalcsc630/pyvis/blob/master/pyvis/Explaining%20PyVis.md) for example formats. Make sure you also update that file with new documentation. Open an issue if you have any questions.
