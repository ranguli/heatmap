#!/usr/bin/env/python3

from decouple import config
import folium
import numpy as np
from folium.plugins import HeatMap

api_key = config('API_KEY')

data = (
    np.random.normal(size=(100,3))*
    np.array([[1,1,1,]])+
    np.array([[48,5,1]])
).tolist()

m = folium.Map(
    [48.,5.],
    tiles='cartodbdark_matter',
    zoom_start=6
)

HeatMap(data).add_to(m)
html = m._repr_html_()
f = open("map.html", "w")
f.write(html)
f.close()
#html.save('map.html')

