import streamlit as st
import numpy as np
import pydeck as pdk
import pandas as pd


st.title("Device Health")

st.selectbox('Pick a Sensor', ('S1', 'S2', 'S3', "S4"))

chart_data = pd.DataFrame(
    np.random.randn(4, 2) * [1.75, 1.75] + [-6.19, 35.0],
    columns=['lat', 'lon'])
chart_data['windspeed'] = range(len(chart_data['lon']))
chart_data['color'] = [[142, 255, 104, 255],
                       [142, 255, 104, 255],
                       [142, 255, 104, 255],
                       [142, 255, 104, 255],]
chart_data["lat"] = np.round(chart_data["lat"],2)
chart_data["lon"] = np.round(chart_data["lon"],2)

tooltip = {
   "html": "</b> lon: {lon},</b> <br/>lat: {lat}, <br/> speed: {windspeed}",
   "style": {
        "backgroundColor": "#b6c0cc",
        "color": "#ffffff"
        }
    }

col1, col2 = st.columns([1,1], gap="large")
col1.header("🌍 Current Sensor Location")
col2.header("🔋 Sensor Status")

col1, col3  = st.columns([3, 3], gap="large")
with col1:
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
                                   ), ],
                 tooltip=tooltip
                 )
    st.pydeck_chart(r)

with col3:
    chart_data = pd.DataFrame(
        np.random.randn(20, 1)+10,
        columns=["Battery Percentage"])

    st.bar_chart(chart_data)

col1, col2, col4, col5 = st.columns([1,1,1,3])
col1.metric("Power Generation", "56%", "-1.1%")
col2.metric("Power Supply", "0", "0")
col4.metric("Device Temperature", "21°C", "-1.2°C")