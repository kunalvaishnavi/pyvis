# Change Log

## Jan 26
I've updated my README to be more like a README for an actual open source repo. I also looked more into `pybaseball` and discovered that the function works if you call it with specific syntax. I'm also noticing that I'm going to need to spend more time understanding the inner workings of `pybaseball` before I can begin working on my own open source library.

## Jan 28
Over the weekend, I worked on understanding `pybaseball`. I now have a fairly good idea of how it works. Now, I'll need to start working on my repo and writing improvements to it.

## Jan 29
In class today, I realized I'll need to learn the inner workings of `matplotlib` because there are so many different things you can do with it. That way, I'll know what kinds of graphs I want to quickly generate in my library. That is what I'll work on over the next two days.

## Jan 30
I'm getting a bit confused why the `statcast` function runs for certain dates and for the exact same dates, doesn't run. I am going to look into how the `statcast` function picks up the customized CSV file from [Baseball Savant](https://baseballsavant.mlb.com/statcast_search). Then, I'll get back to understanding `matplotlib`.

## Feb 2
I tried to figure out why I can't obtain the link to the CSV file. Eventually, Baseball Savant was put under maintenance, so I couldn't work any further on that. So, I started working on PyVis.

## Feb 6
I continued trying to figure out the link to the CSV file. I asked Dr. Z and he said to use [Selenium](http://selenium-python.readthedocs.io/) to simulate the `onclick` event to download the CSV. If it doesn't take too long, I'm going to use Selenium. Otherwise, I'm going to deal with the Statcast search issues because I need to make more progress on my own library.

## Feb 7
Today, I created my first function for PyVis called `hit_breakdown`, which gives you information regarding the events happening at a batter's plate appearance. It can take a singular day or a range of dates (in a certain format for the latter) and visualize the breakdown for the user via a pie chart. For aesthetic purposes, I decided to eliminate the tiny slices in the pie chart where the event happened less than 2% of the time and merged all of those events into a category called 'other'.

## Feb 8
I added a new function today called `pitch_breakdown`, which does what `hit_breakdown` does but for the type of pitch thrown.

## Feb 9
I compiled a list of other ideas I want to implement and posted that list as an issue. Over the weekend, I will clean up my repo so that it's ready for others to contribute to.

## Feb 11-17
As per the project requirements, I did not commit to or work on my project and only worked on a classmate's project.

## Feb 19
I realized that I was duplicating code in multiple functions, so I factored out code and wrote two general functions called `general_event_breakdown` and `process_data`. 

## Feb 20
I researched ways I can create a strike zone plotter that takes in data and plots the location of balls in the strike zone along with their outcome.

## Feb 22
I started creating the function and called it `batter_strike_zone_plotting`. I hope to also create an equivalent function for pitchers.

## Feb 23
The strike zone that my code was generating was behaving weirdly last night, as it was giving me a strike zone that looked like a wide rectangle instead of a tall rectangle. I'm still debugging the issue today.

## Feb 26
I finished creating the `batter_strike_zone_plotting` last night and today I'm making an equivalent function for pitchers.

## Feb 27 & 28
I added many more functions and put them into separate files. I also rearranged the code so all the necessary imports are in one file, updated the documentation in the repo, renamed functions because their names were too long, and added REFERENCES.md to cite my sources.
