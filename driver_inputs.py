import matplotlib.pyplot as plt
import pandas as pd


def throttle_brake(session, driver, t1_color, t1_inv_color):

    d1_lap = session.laps.pick_driver(driver.identifier).pick_fastest()

    d1_tel = d1_lap.get_car_data().add_distance()

    fig, ax = plt.subplots()
    ax.plot((d1_tel["Distance"] / 1000), d1_tel["Throttle"],
            color=t1_color, label=f"Throttle")
    ax.plot((d1_tel["Distance"] / 1000), ((d1_tel["Brake"] + 1) * - 10),
            color=t1_inv_color, label=f"Braking")

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

    ax.legend()
    plt.suptitle(f"Fastest Lap Speed Comparison - {session.event['EventName']}, {session.name} {session.event.year} \n "
                 f"{d1_lap['Driver']} Lap: {d1_lap['LapNumber']}  S1: {d1_s1_f}  S2: {d1_s2_f}  S3: {d1_s3_f}  {driver1Lap_f} ")
