import math
import random

import pandas as pd
import streamlit as st
from numpy import random

"""
# Berlin Bike Theft Radar!
"""
"""
Theft period is from January 2021 to May 2022. The exact geo coordinates are approximated using the 
information from [data source](https://www.govdata.de/web/guest/suchen/-/details/fahrraddiebstahl-in-berlin).
The next enhancement will include the deep learning based prediction model to predict geo-coordinates where theft 
incident is about to occur.
"""


def get_updated_latitude(prev_latitude):
    earth_radius = 6378.137
    pi = math.pi
    m = (1 / ((2 * pi / 360) * earth_radius)) / 1000
    factor = 1 if random.randint(0, 1) % 2 == 0 else -1
    # Within 3 KM
    # my_meters = random.randint(1, 2000)

    my_meters = random.normal(loc=0, scale=1000, size=1)[0]

    # New Latitude
    return prev_latitude + factor * (my_meters * m)


def get_updated_longitude(longitude, latitude):
    earth_radius = 6378.137
    pi = math.pi

    # Within 3 KM
    # my_meters = random.randint(1, 3000)

    my_meters = random.normal(loc=0, scale=1000, size=1)[0]

    cos = math.cos
    m = (1 / ((2 * pi / 360) * earth_radius)) / 1000
    # New Longitude
    return longitude + (my_meters * m) / cos(latitude * (pi / 180))


"#### Number of samples"
samples = st.slider("", min_value=100, max_value=25000)


def load_data():
    df = pd.read_csv("data/bicycle_theft_berlin.csv", sep=",", header=0, encoding="utf-8").sample(samples)

    # Sub-district Longitudes and Latitudes
    # Debug using -> df["lat"] = df["sub_district_lat"].astype(float)
    df["lat"] = df["sub_district_lat"].astype(float).apply(lambda x: get_updated_latitude(x))
    # Debug using ->  df["lon"] = df["sub_district_long"].astype(float)
    df["lon"] = df.apply(lambda row: get_updated_longitude(row.sub_district_long, row.sub_district_lat), axis=1)
    # df.apply(lambda row: row.a + row.b)
    return df


data = load_data()

"#### Theft Map"
st.map(data)

agree = st.checkbox('Show raw data')

if agree:
    "#### Source Data"
    data

"#### Contact Developer"

st.markdown("Programmed with ❤️ by [Muhammad Ahsan](https://www.linkedin.com/in/muhammad-ahsan/)")
