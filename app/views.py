import os

from app import app
from flask import render_template

from .models import FormulaOneDNFParser


# flask guide: https://www.makeuseof.com/tag/python-javascript-communicate-json/
# flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-the-heroku-cloud-legacy
# python flask host solution 1 https://www.pythonanywhere.com/details/flask_hosting OR heroku


@app.route('/')
@app.route('/index')
def index():
    response_data = []
    for filename in sorted(os.listdir(os.path.join(os.getcwd(), 'raw_data'))):
        parser = FormulaOneDNFParser()
        with open(os.path.join(os.getcwd(), 'raw_data', filename), 'r') as file:
            for line in file:
                parser.feed(line)
        # print("{} Season".format(filename))
        # parser.print_dnf_stats()
        season_data = parser.get_dnf_stats_json()
        season_data['season'] = filename
        response_data.append(season_data)
    return render_template('index.html', title='F1 Crash Stats', data=response_data)
