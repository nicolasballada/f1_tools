import matplotlib.pyplot as plt
import pandas as pd


def throttle_brake(session, driver, t1_color, t1_inv_color, lapN):

    d1_lap = session.laps.pick_driver(driver.identifier)[lapN]
    d2_lap = session.laps.pick_driver(driver.identifier).pick_fastest()

    d1_tel = d1_lap.get_car_data().add_distance()
    d2_tel = d2_lap.get_car_data().add_distance()

    fig, ax = plt.subplots()
    ax.plot(d1_tel(["Distance"] / 1000), d1_tel["Speed"],
            color=t1_color, label=f"{driver.identifier} Speed")
    ax.plot(d2_tel(["Distance"] / 1000), d2_tel["Speed"],
            color=t1_inv_color, label=f"PB Speed")
    ax.plot(d1_tel(["Distance"] / 1000), d1_tel["Throttle"],
            color='#4bbf81', label=f"{driver.identifier} Throttle %")
    ax.plot(d2_tel(["Distance"] / 1000), d2_tel["Throttle"],
            color='#6a4bbf', label=f"PB Throttle %")

    ax.set_xlabel("Distance in km")
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
    plt.suptitle(f"Current vs PB Comparison - {session.event['EventName']}, {session.name} {session.event.year} \n "
                 f"{d1_lap['Driver']} \n"
                 f"Lap: {d1_lap['LapNumber']}  S1: {d1_s1_f}  S2: {d1_s2_f}  S3: {d1_s3_f}  {driver1Lap_f} \n"
                 f"Lap: {d2_lap['LapNumber']}  S1: {d2_s1_f}  S2: {d2_s2_f}  S3: {d2_s3_f}  {driver2Lap_f} ")
