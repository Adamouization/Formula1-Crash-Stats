# Formula1-Crash-Stats [![Build Status](https://travis-ci.org/Adamouization/Formula1-Crash-Stats.svg?branch=master)](https://travis-ci.org/Adamouization/Formula1-Crash-Stats) [![GitHub issues](https://img.shields.io/github/issues/Adamouization/Formula1-Crash-Stats.svg)](https://github.com/Adamouization/Formula1-Crash-Stats/issues) [![GitHub license](https://img.shields.io/github/license/Adamouization/Formula1-Crash-Stats.svg)](https://github.com/Adamouization/Formula1-Crash-Stats/blob/master/LICENSE)

**Formula1-Crash-Stats** is a software that displays Formula 1 DNF statistics by retrieving and parsing data from the source HTML behind each Formula 1 season Wikipedia page.

The software backend is written in Flask using Python 3.7 and hosted on Heroku using Gunicorn.

You can visit the website live here: [f1-dnf-stats.herokuapp.com](https://f1-dnf-stats.herokuapp.com/)

#### Screenshot

*todo*

## Usage

Clone the repository (or download the zipped project):
`$ git clone https://github.com/Adamouization/Formula1-Crash-Stats`

Create a virtual environment for the project and activate it:

```
virtualenv ~/Environments/F1-Crash-Stats
source F1-Crash-Stats/bin/activate
```

Once you have the virtualenv activated and set up, `cd` into the project directory and install the requirements needed to run the app:

```
pip install -r requirements.txt
```

You can now run the app:
```
python run.py
```

The app will now be running (`Ctrl + C` to stop it) and you can visit it at: `127.0.0.1:4000`

To run tests: `nosetests -v`

## TODO
* see [TODO Project Board (Initial Release)](https://github.com/Adamouization/Formula1-Crash-Stats/projects/1)
* see [TODO Project Board (Future Releases)](https://github.com/Adamouization/Formula1-Crash-Stats/projects/2)

## License 
* see [LICENSE](https://github.com/Adamouization/Formula1-Crash-Stats/blob/master/LICENSE) file.

## Contact
* email: adam@jaamour.com
* website: www.adam.jaamour.com
* linkedin: [@adamjaamour](https://www.linkedin.com/in/adamjaamour/)
* twitter: [@Adamouization](https://twitter.com/Adamouization)
