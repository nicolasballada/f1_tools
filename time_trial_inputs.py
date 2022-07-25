import matplotlib.pyplot as plt
import pandas as pd
import csv


def throttle_brake(session, driver, t1_color, t1_inv_color, lapN):

    driver_laps = session.laps.pick_driver(driver.identifier)

    driver_laps.to_csv('./output.csv', encoding='utf-8')

    d1_lap = driver_laps.iloc[[lapN - 1]]
    d2_lap = session.laps.pick_driver(driver.identifier).pick_fastest()

    print(d1_lap, d2_lap)

    d1_tel = d1_lap.get_car_data().add_distance()
    d2_tel = d2_lap.get_car_data().add_distance()

    fig, ax = plt.subplots()
    ax.plot((d1_tel["Distance"] / 1000), d1_tel["Throttle"],
            color=t1_color, label=f"Lap {lapN} Acc")
    ax.plot((d2_tel["Distance"] / 1000), d2_tel["Throttle"],
            color=t1_inv_color, label=f"PB Acc")
    ax.plot((d1_tel["Distance"] / 1000), ((d1_tel["Brake"] + 1) * - 10),
            color='#4bbf81', label=f"Lap {lapN} Dec")
    ax.plot((d2_tel["Distance"] / 1000), ((d2_tel["Brake"] + 1) * - 10),
            color='#6a4bbf', label=f"PB Dec")

    ax.set_xlabel("Distance km")
    ax.set_ylabel("Throttle %")

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
