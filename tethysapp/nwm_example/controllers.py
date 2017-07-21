from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

import datetime as dt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from tethys_sdk.gizmos import MapView, Button, MVLayer, MVLegendClass
import plotly.graph_objs as go
from tethys_sdk.gizmos import PlotlyView
from .helpers import get_nwm_forecast

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    # Tiled ArcGIS REST Layer
    arc_gis_layer2 = MVLayer(
        source='TileArcGISRest',
        options={'url': 'https://services.nationalmap.gov/arcgis/rest/services/wbd/MapServer'},
        legend_title='Watershed Boundaries',
        legend_extent=[-173, 17, -65, 72]
    )

    nwm_example_map = MapView(
        height='100%',
        width='100%',
        layers=[arc_gis_layer2],
        basemap='OpenStreetMap',
        legend = True
    )

    medium_range_button = Button(
        display_text='Medium Range',
        name='medium-range-button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('nwm_example:medium_range')
    )

    short_range_button = Button(
        display_text='Short Range',
        name='short-range-button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('nwm_example:short_range')
    )

    context = {
        'nwm_example_map': nwm_example_map,
        'medium_range_button': medium_range_button,
        'short_range_button': short_range_button
    }

    return render(request, 'nwm_example/home.html', context)


@login_required()
def medium_range(request):
    """
    Controller for the Medium Range page.
    """
    dateraw = []
    date1 = []
    value1 = []
    comid = '18228725'
    config = 'medium_range'
    startdate = '2017-07-20'
    enddate = '2017-07-21'  # not needed for medium range
    forecasttime = '00'
    watermlstring = str(get_nwm_forecast(config, comid, startdate, enddate, forecasttime))
    waterml = watermlstring.split('dateTimeUTC="')
    waterml.pop(0)
    for e in waterml:
        parser = e.split('"  methodCode="1"  sourceCode="1"  qualityControlLevelCode="1" >')
        dateraw.append(parser[0])
        value1.append(parser[1].split('<')[0])

    for e in dateraw:
        date1.append(dt.datetime.strptime(e, "%Y-%m-%dT%H:%M:%S"))

    nwm_plot = PlotlyView([go.Scatter(x=date1, y=value1)])

    context = {
        'nwm_plot': nwm_plot
    }

    return render(request, 'nwm_example/medium_range.html', context)


def short_range(request):
    """
    Controller for the Short Range page.
    """

    dateraw = []
    date1 = []
    value1 = []
    comid = '18228725'
    config = 'short_range'
    startdate = '2017-07-20'
    enddate = '2017-07-21'
    forecasttime = '12'
    watermlstring = str(get_nwm_forecast(config, comid, startdate, enddate, forecasttime))
    waterml = watermlstring.split('dateTimeUTC="')
    waterml.pop(0)
    for e in waterml:
        parser = e.split('"  methodCode="1"  sourceCode="1"  qualityControlLevelCode="1" >')
        dateraw.append(parser[0])
        value1.append(parser[1].split('<')[0])

    for e in dateraw:
        date1.append(dt.datetime.strptime(e, "%Y-%m-%dT%H:%M:%S"))

    nwm_plot = PlotlyView([go.Scatter(x=date1, y=value1)])

    context = {
        'nwm_plot': nwm_plot
    }

    return render(request, 'nwm_example/short_range.html', context)
