# Formula1-DNF-Stats [![Build Status](https://app.travis-ci.com/Adamouization/Formula1-Crash-Stats.svg?branch=master)](https://app.travis-ci.com/Adamouization/Formula1-Crash-Stats) [![GitHub issues](https://img.shields.io/github/issues/Adamouization/Formula1-Crash-Stats.svg)](https://github.com/Adamouization/Formula1-Crash-Stats/issues) [![GitHub license](https://img.shields.io/github/license/Adamouization/Formula1-Crash-Stats.svg)](https://github.com/Adamouization/Formula1-Crash-Stats/blob/master/LICENSE) #

## Features ##

**Formula1-DNF-Stats** is a web application that parses the source of each Wikipedia page for every Formula 1 season since 1950 in order to gather data about the all DNFs that occurred in the history of F1 and visualise them in plots and tables.

Types of DNFs that are visualised:
* Ret - Retirements
* NC - Not Classified
* DNQ - Did Not Qualify
* DNPQ - Did Not Pre Qualify
* DSQ - Disqualified
* DNS - Did Not Start
* DNP - Did Not Practice
* Ex - Excluded
* WD - Withdrawn

The app is written in Flask using Python 3.9 and hosted on Render using Gunicorn.

You can visit the website live here: [f1-dnf-stats.herokuapp.com](https://f1-dnf-stats.herokuapp.com/)

## Screenshot ##

*todo*

## Local Usage ##

Clone the repository (or download the zipped project):
`$ git clone https://github.com/Adamouization/Formula1-Crash-Stats`

Create a virtual environment for the project and activate it:

```
python3 -m venv ~/Environments/F1_DNF_Stats
source ~/Environments/F1_DNF_Stats/bin/activate
```

Once you have the virtualenv activated and set up, `cd` into the project directory and install the requirements needed to run the app:

```
pip3 install -r requirements.txt
```

You can now run the app:
```
python3 run.py
```

The app will be running (`Ctrl + C` to stop it) and you can visit it at: `127.0.0.1:4000`

To run tests: `nosetests -v`

## Releases ##

*todo*

## Features to Implement ##

* see [TODO Project Board (Initial Release)](https://github.com/Adamouization/Formula1-Crash-Stats/projects/1)
* see [TODO Project Board (Future Releases)](https://github.com/Adamouization/Formula1-Crash-Stats/projects/2)

## License ##

* see [LICENSE](https://github.com/Adamouization/Formula1-Crash-Stats/blob/master/LICENSE) file.

## Contact ##

* email: adam@jaamour.com
* website: www.adam.jaamour.com
* linkedin: [@adamjaamour](https://www.linkedin.com/in/adamjaamour/)
* twitter: [@Adamouization](https://twitter.com/Adamouization)

## Support ##

<a href="https://www.buymeacoffee.com/adamjaamour"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=adamjaamour&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>
