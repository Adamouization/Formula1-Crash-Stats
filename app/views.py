import os

from app import app
from flask import render_template

from .models import FormulaOneDNFParser


@app.route('/')
@app.route('/index')
def index():
    response_data = []
    raw_data_files_path = os.path.join(app.root_path, 'raw_data')
    if os.path.exists(raw_data_files_path):
        for filename in sorted(os.listdir(raw_data_files_path)):
            parser = FormulaOneDNFParser()
            with open(os.path.join(raw_data_files_path, filename), 'r') as file:
                for line in file:
                    parser.feed(line)
            season_data = parser.get_dnf_stats_json()
            season_data['season'] = filename
            response_data.append(season_data)
    else:
        print("The following path does not exist: {}".format(raw_data_files_path))
    return render_template('index.html', data=response_data)
