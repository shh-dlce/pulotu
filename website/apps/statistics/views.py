from time import mktime
from datetime import datetime
from django.shortcuts import render
from website.apps.statistics.models import StatisticalValue
from website.apps.statistics import statistic

GRAPH_START_TIME = datetime.strptime("01 Apr 2013 00:00:00", "%d %b %Y %H:%M:%S")


def format_time_struct(date):
    return int(mktime(date)) * 1000  # I have no idea why * 1000 is needed


def get_xy(label, get_latest=False):
    x = [format_time_struct(GRAPH_START_TIME.timetuple())]
    y = [0]

    for row in StatisticalValue.objects.get_all_with_dates(label):
        x.append(format_time_struct(row[1].timetuple()))
        y.append(row[0])

    # get_latest
    if get_latest:
        x.append(format_time_struct(datetime.now().timetuple()))
        y.append(float(statistic.get_statistic(label)))
    return {'x': x, 'y': y, 'name': label}


def statistics(request):
    """Shows statistics"""
    out = {'charts': []}
    # add line graphs
    for i, label in enumerate(statistic.get_graphing(), 1):
        out['charts'].append({
            'label': label,
            'type': "lineChart",
            'id': 'chart_id_%d' % i,
            'data': get_xy(label, get_latest=True)
        })

    return render(request, 'statistics/details.html', out)
