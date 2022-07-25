import fastf1

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np


fastf1.Cache.enable_cache('./cache')


def map_gears(session, driver):

    lap = session.laps.pick_driver(driver.identifier).pick_fastest()
    tel = lap.get_telemetry()

    x = np.array(tel['X'].values)
    y = np.array(tel['Y'].values)

    plt.figure()

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    gear = tel['nGear'].to_numpy().astype(float)

    cmap = cm.get_cmap('Paired')
    lc_comp = LineCollection(
        segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
    lc_comp.set_array(gear)
    lc_comp.set_linewidth(4)

    plt.gca().add_collection(lc_comp)
    plt.axis('equal')
    plt.tick_params(labelleft=False, left=False,
                    labelbottom=False, bottom=False)

    s1 = lap['Sector1Time'].components
    s1_f = f"{s1.seconds}.{s1.milliseconds}{s1.microseconds}"
    s2 = lap['Sector2Time'].components
    s2_f = f"{s2.seconds}.{s2.milliseconds}{s2.microseconds}"
    s3 = lap['Sector3Time'].components
    s3_f = f"{s3.seconds}.{s3.milliseconds}{s3.microseconds}"

    driverLap = lap['LapTime'].components
    driverLap_f = f"{driverLap.minutes}:{driverLap.seconds}.{driverLap.milliseconds}{driverLap.microseconds}"

    title = plt.suptitle(
        f"Gear Shift Visualization \n"
        f"{session.event['EventName']}, {session.name} {session.event.year} \n "
        f"{lap['Driver']} Lap: {lap['LapNumber']}  S1: {s1_f}  S2: {s2_f}  S3: {s3_f}  {driverLap_f}")

    cbar = plt.colorbar(mappable=lc_comp, label="Gear",
                        boundaries=np.arange(1, 10))
    cbar.set_ticks(np.arange(1.5, 9.5))
    cbar.set_ticklabels(np.arange(1, 9))
