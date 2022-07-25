import matplotlib.pyplot as plt
import pandas as pd


def throttle_brake(session, driver1, driver2, t1_color, t1_inv_color, t2_color, t2_inv_color):

    d1_lap = session.laps.pick_driver(driver1.identifier).pick_fastest()
    d2_lap = session.laps.pick_driver(driver2.identifier).pick_fastest()

    d1_tel = d1_lap.get_car_data().add_distance()
    d2_tel = d2_lap.get_car_data().add_distance()

    fig, ax = plt.subplots()
    ax.plot(d1_tel["Distance"], d1_tel["Speed"],
            color=t1_color, label=f"{driver1.identifier} Speed")
    ax.plot(d2_tel["Distance"], d2_tel["Speed"],
            color=t2_color, label=f"{driver2.identifier} Speed")
    ax.plot(d1_tel["Distance"], d1_tel["Throttle"],
            color=t1_inv_color, label=f"{driver1.identifier} Throttle %")
    ax.plot(d2_tel["Distance"], d2_tel["Throttle"],
            color=t2_inv_color, label=f"{driver2.identifier} Throttle %")

    ax.set_xlabel("Distance in m")
    ax.set_ylabel("Speed in km/h")

    d1_s1 = d1_lap['Sector1Time'].components
    d1_s1_f = f"{d1_s1.seconds}.{d1_s1.milliseconds}{d1_s1.microseconds}"
    d1_s2 = d1_lap['Sector2Time'].components
    d1_s2_f = f"{d1_s2.seconds}.{d1_s2.milliseconds}{d1_s2.microseconds}"
    d1_s3 = d1_lap['Sector3Time'].components
    d1_s3_f = f"{d1_s3.seconds}.{d1_s3.milliseconds}{d1_s3.microseconds}"

    driver1Lap = d1_lap['LapTime'].components
    driver1Lap_f = f"{driver1Lap.minutes}:{driver1Lap.seconds}.{driver1Lap.milliseconds}{driver1Lap.microseconds}"

    d2_s1 = d2_lap['Sector1Time'].components
    d2_s1_f = f"{d2_s1.seconds}.{d2_s1.milliseconds}{d2_s1.microseconds}"
    d2_s2 = d2_lap['Sector2Time'].components
    d2_s2_f = f"{d2_s2.seconds}.{d2_s2.milliseconds}{d2_s2.microseconds}"
    d2_s3 = d2_lap['Sector3Time'].components
    d2_s3_f = f"{d2_s3.seconds}.{d2_s3.milliseconds}{d2_s3.microseconds}"

    driver2Lap = d2_lap['LapTime'].components
    driver2Lap_f = f"{driver2Lap.minutes}:{driver2Lap.seconds}.{driver2Lap.milliseconds}{driver2Lap.microseconds}"

    ax.legend()
    plt.suptitle(f"Fastest Lap Speed Comparison - {session.event['EventName']}, {session.name} {session.event.year} \n "
                 f"{d1_lap['Driver']} Lap: {d1_lap['LapNumber']}  S1: {d1_s1_f}  S2: {d1_s2_f}  S3: {d1_s3_f}  {driver1Lap_f} \n"
                 f"{d2_lap['Driver']} Lap: {d2_lap['LapNumber']}  S1: {d2_s1_f}  S2: {d2_s2_f}  S3: {d2_s3_f}  {driver2Lap_f} ")
