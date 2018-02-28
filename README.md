# PyVis
PyVis is a data visualization tool that is an extension of [pybaseball](https://github.com/jldbc/pybaseball).

## Getting Started
See below on how to start using PyVis.

### Prerequisites
First, you need to install `pybaseball` by typing the following into the command line: `pip install pybaseball`. If you don't have `pip`, install it [here](https://pip.pypa.io/en/stable/installing/).

It is recommended that you replace any local files installed by `pip` with the files from the `pybaseball` repo, as some functions in `PyVis` use updated functions that have not been updated in the `pip` installation.

## How PyVis Works
PyVis is split up into different files, depending on the user's needs. For instance, if the user needs to plot data points in a strike zone, the aptly named `strike_zone.py` file will do so. At the top of each function is a brief explanation as to what the function does. The `data.py` file is the "initializer" as it has all of the imports needed for all files and has the main function used to scrape the data for all other functions in PyVis. Hence, in all other files, the only import statement is `import data`. 

Browse through the files to learn more about the capabilities of PyVis. Have fun visualizing!

## Contributing
See [CONTRIBUTING.md](https://github.com/kunalcsc630/pyvis/blob/master/CONTRIBUTING) to learn how you can contribute to PyVis.

## License
The PyVis project is under the MIT License. See [LICENSE.md](https://github.com/kunalcsc630/pyvis/blob/master/LICENSE) for more.

## Acknowledgments
* [Dr. Nicholas Zufelt](https://github.com/nzufelt)
* [Mr. James LeDoux](https://github.com/jldbc)
* [Ms. Billie Thompson](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [CSC630 Classmates](nzufelt.github.io/open_source_movement_csc630/)
* Additional references available [here](https://github.com/kunalcsc630/pyvis/blob/master/REFERENCES.md)
