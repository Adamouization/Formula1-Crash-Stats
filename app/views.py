import os

from app import app
from flask import render_template

from .models import FormulaOneDNFParser


@app.route('/')
@app.route('/index')
def index():
    raw_data = list()
    categories = list()
    ret_series = list()
    nc_series = list()
    dnq_series = list()
    dnpq_series = list()
    dsq_series = list()
    dns_series = list()
    dnp_series = list()
    ex_series = list()
    wd_series = list()
    total_dnf_series = list()
    total_classified_finish_series = list()
    total_race_entries_series = list()

    # Get path to raw HTML data files
    raw_data_files_path = os.path.join(app.root_path, 'raw_data')

    # Check path is correct
    if os.path.exists(raw_data_files_path):

        # Loop through each file
        for filename in sorted(os.listdir(raw_data_files_path)):

            # Pars each line in file
            parser = FormulaOneDNFParser()
            with open(os.path.join(raw_data_files_path, filename), 'r') as file:
                for line in file:
                    parser.feed(line)
            season_data = parser.get_dnf_stats_json()

            # Save season year from filename
            season_data['season'] = filename

            # Save all extracted data in 1 go
            raw_data.append(season_data)

            # Save individual data pieces for chart
            categories.append(filename)
            ret_series.append(parser.get_ret())
            nc_series.append(parser.get_nc())
            dnq_series.append(parser.get_dnq())
            dnpq_series.append(parser.get_dnpq())
            dsq_series.append(parser.get_dsq())
            dns_series.append(parser.get_dns())
            dnp_series.append(parser.get_dnp())
            ex_series.append(parser.get_ex())
            wd_series.append(parser.get_wd())
            total_dnf_series.append(parser.get_total_dnf())
            total_classified_finish_series.append(parser.get_classified_finish())
            total_race_entries_series.append(parser.get_total_entries())
    else:
        print("The following path does not exist: {}".format(raw_data_files_path))

    return render_template(
        'index.html',
        raw_data=raw_data,
        categories=categories,
        ret_series=ret_series,
        nc_series=nc_series,
        dnq_series=dnq_series,
        dnpq_series=dnpq_series,
        dsq_series=dsq_series,
        dns_series=dns_series,
        dnp_series=dnp_series,
        ex_series=ex_series,
        wd_series=wd_series,
        total_dnf_series=total_dnf_series,
        total_classified_finish_series=total_classified_finish_series,
        total_race_entries_series=total_race_entries_series
    )


@app.route('/help')
def help_page():
    return render_template('help.html')


@app.route('/about')
def about_page():
    return render_template('about.html')
