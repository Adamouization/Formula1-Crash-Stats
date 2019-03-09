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

    raw_data_files_path = os.path.join(app.root_path, 'raw_data')
    if os.path.exists(raw_data_files_path):
        for filename in sorted(os.listdir(raw_data_files_path)):
            parser = FormulaOneDNFParser()
            with open(os.path.join(raw_data_files_path, filename), 'r') as file:
                for line in file:
                    parser.feed(line)
            # raw data
            season_data = parser.get_dnf_stats_json()
            season_data['season'] = filename
            raw_data.append(season_data)
            # chart data
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
