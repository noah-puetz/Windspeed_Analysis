import pandas as pd
import numpy as np
import pydeck as pdk
import streamlit as st

st.title("🌪 Overview")

"""Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et 
dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita 
kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur 
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet. """

chart_data = pd.DataFrame(
    np.random.randn(10, 2) * [1.75, 1.75] + [-6.19, 35.0],
    columns=['lat', 'lon'])
chart_data['windspeed'] = range(len(chart_data['lon']))
chart_data['color'] = [[142, 255, 104, 255],
                       [128, 137, 143, 255],
                       [128, 137, 143, 255],
                       [142, 255, 104, 255],
                       [142, 255, 104, 255],
                       [128, 137, 143, 255],
                       [128, 137, 143, 255],
                       [128, 137, 143, 255],
                       [142, 255, 104, 255],
                       [128, 137, 143, 255], ]
chart_data["lat"] = np.round(chart_data["lat"],2)
chart_data["lon"] = np.round(chart_data["lon"],2)



col1, col2 = st.columns([4, 2], gap="large")

tooltip = {
   "html": "</b> lon: {lon},</b> <br/>lat: {lat}, <br/> speed: {windspeed}",
   "style": {
        "backgroundColor": "#b6c0cc",
        "color": "#ffffff"
        }
    }

with col1:
    st.header("🌍 Locations")
    r = pdk.Deck(map_style=None,
                 initial_view_state=pdk.ViewState(latitude=-6.19,
                                                  longitude=35.0,
                                                  zoom=5,
                                                  pitch=45,
                                                  ),
                 layers=[pdk.Layer("ColumnLayer",
                                   data=chart_data,
                                   get_position='[lon, lat]',
                                   getFillColor='color',
                                   get_elevation='windspeed',
                                   elevation_scale=10000,
                                   radius=20000,
                                   pickable=True,
                                   auto_highlight=True
                                   ),],
                 tooltip=tooltip
                 )
    st.pydeck_chart(r)

with col2:
    st.header("🔋 Devices")
    st.metric("Sensor 1 Power", "70%", "- 1 % per day")
    st.metric("Sensor 2 Power", "68%", "- 1.3 % per day")
    st.metric("Sensor 3 Power", "45%", "- 1.5 % per day")
    st.metric("Sensor 4 Power", "32%", "- 1.1 % per day")
