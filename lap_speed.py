import fastf1 as ff1
import numpy as np
import matplotlib as mpl

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection


def measured_speed(session, driver_data, year):

    driver = driver_data.identifier

    lap = session.laps.pick_driver(driver).pick_fastest()
    colormap = mpl.cm.plasma

    x = lap.telemetry['X']              # values for x-axis
    y = lap.telemetry['Y']              # values for y-axis
    color = lap.telemetry['Speed']      # value to base color gradient on

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    s1 = lap['Sector1Time'].components
    s1_f = f"{s1.seconds}.{s1.milliseconds}{s1.microseconds}"
    s2 = lap['Sector2Time'].components
    s2_f = f"{s2.seconds}.{s2.milliseconds}{s2.microseconds}"
    s3 = lap['Sector3Time'].components
    s3_f = f"{s3.seconds}.{s3.milliseconds}{s3.microseconds}"

    driverLap = lap['LapTime'].components
    driverLap_f = f"{driverLap.minutes}:{driverLap.seconds}.{driverLap.milliseconds}{driverLap.microseconds}"

    fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))
    fig.suptitle(
        f"Fastest Lap Speed Visualization \n"
        f"{session.event['EventName']}, {session.name} {session.event.year} \n "
        f"{lap['Driver']} Lap: {lap['LapNumber']}  S1: {s1_f}  S2: {s2_f}  S3: {s3_f}  {driverLap_f}")

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.12)
    ax.axis('off')

    ax.plot(lap.telemetry['X'], lap.telemetry['Y'],
            color='black', linestyle='-', linewidth=16, zorder=0)

    norm = plt.Normalize(color.min(), color.max())
    lc = LineCollection(segments, cmap=colormap, norm=norm,
                        linestyle='-', linewidth=5)

    lc.set_array(color)

    line = ax.add_collection(lc)

    cbaxes = fig.add_axes([0.25, 0.05, 0.5, 0.05])
    normlegend = mpl.colors.Normalize(vmin=color.min(), vmax=color.max())
    legend = mpl.colorbar.ColorbarBase(
        cbaxes, norm=normlegend, cmap=colormap, orientation="horizontal")
