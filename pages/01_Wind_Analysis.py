import streamlit as st
import numpy as np
import pydeck as pdk
import pandas as pd
import plotly.express as px

st.title("🌪 Wind Analysis")

chart_data = pd.DataFrame(
    np.random.randn(10, 2) * [1.75, 1.75] + [-6.19, 35.0],
    columns=['lat', 'lon'])
chart_data['windspeed'] = range(len(chart_data['lon']))
chart_data['color'] = [[142, 255, 104, 100],
                       [128, 137, 143, 100],
                       [128, 137, 143, 100],
                       [142, 255, 104, 100],
                       [142, 255, 104, 100],
                       [128, 137, 143, 100],
                       [128, 137, 143, 255],
                       [128, 137, 143, 100],
                       [142, 255, 104, 100],
                       [128, 137, 143, 100], ]
chart_data["lat"] = np.round(chart_data["lat"],2)
chart_data["lon"] = np.round(chart_data["lon"],2)

tooltip = {
   "html": "</b> lon: {lon},</b> <br/>lat: {lat}, <br/> speed: {windspeed}",
   "style": {
        "backgroundColor": "#b6c0cc",
        "color": "#ffffff"
        }
    }

st.selectbox('Pick a Location ID', ('A1', 'A2', 'A3'))

col1, col2 = st.columns([1,1], gap="large")
col1.header("🌍 Locations")
col2.header("🎚 Aggregated Information")

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
    st.subheader("Wind Rose")
    df = px.data.wind()
    fig = px.bar_polar(df, r="frequency", theta="direction",
                       color="strength",
                       color_discrete_sequence=px.colors.sequential.Plasma_r)

    st.plotly_chart(fig, use_container_width=True)

    #chart_data = pd.DataFrame(
    #    np.random.randn(20, 1)+15,
    #    columns=['a'])
    #st.line_chart(chart_data)

col1, col5 = st.columns([4,4])
col1.subheader("Current Metrics")
col5.subheader("Power Potential")

col1, col2, col3, col4, col5 = st.columns([1,1,1,1,4])
col1.metric("Wind speed", "9 mph", "-8%")
col2.metric("Wind direction", "178°", "+5°")
col3.metric("Humidity", "86%", "4%")
col4.metric("Temperature", "21°C", "-1.2°C")

with col5:
    chart_data = pd.DataFrame(
        np.random.randn(20, 1) + 0.5,
        columns=['b'])
    st.area_chart(chart_data)