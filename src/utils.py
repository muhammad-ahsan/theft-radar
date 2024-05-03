import math
import random
import numpy as np
import pandas as pd


def get_updated_latitude(prev_latitude):
    earth_radius = 6378.137
    pi = math.pi
    m = (1 / ((2 * pi / 360) * earth_radius)) / 1000
    factor = 1 if random.randint(0, 1) % 2 == 0 else -1
    # Within 3 KM
    # my_meters = random.randint(1, 2000)

    my_meters = np.random.normal(loc=0, scale=1000, size=1)[0]

    # New Latitude
    return prev_latitude + factor * (my_meters * m)


def get_updated_longitude(longitude, latitude):
    earth_radius = 6378.137
    pi = math.pi

    # Within 3 KM
    # my_meters = random.randint(1, 3000)

    my_meters = np.random.normal(loc=0, scale=1000, size=1)[0]

    cos = math.cos
    m = (1 / ((2 * pi / 360) * earth_radius)) / 1000
    # New Longitude
    return longitude + (my_meters * m) / cos(latitude * (pi / 180))


def load_data(data_path: str, samples: int):
    df = pd.read_csv(data_path,
                     sep=",",
                     header=0,
                     encoding="utf-8").sample(samples)

    # Sub-district Longitudes and Latitudes
    # Debug using -> df["lat"] = df["sub_district_lat"].astype(float)
    df["lat"] = df["sub_district_lat"].astype(float).apply(lambda x: get_updated_latitude(x))
    # Debug using ->  df["lon"] = df["sub_district_long"].astype(float)
    df["lon"] = df.apply(lambda row: get_updated_longitude(row.sub_district_long, row.sub_district_lat), axis=1)
    # df.apply(lambda row: row.a + row.b)
    return df
