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
# from .helpers import get_nwm_forecast

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

    context = {
        'nwm_example_map': nwm_example_map
    }

    return render(request, 'nwm_example/home.html', context)
