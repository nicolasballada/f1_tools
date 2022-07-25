import sys
import matplotlib.pyplot as plt
import f1_data_base
import fastest_speed
import gear_map
import lap_speed
import input_compare
import driver_inputs
import time_trial_inputs
import time_trial

FASTESTDRIVER = 0
GEARMAP = 0
LAPSPEED = 0
INPUTCOMPARE = 0
DRIVERINPUT = 0
TIMETRIAL = 1

if(len(sys.argv) > 1):
    if(sys.argv[1] == '-h' or sys.argv[1] == 'help'):
        print('run.py [DR1] [DR2] [Year] [Session Type] [Lap] [Event Name]')
    else:
        print('nopls')
        d1 = sys.argv[1]
        d2 = sys.argv[2]
        yr = sys.argv[3]
        sn = sys.argv[4]
        lp = sys.argv[5]
        ev = sys.argv[6:]
else:
    #####################################
    d1 = "RUS"                          #
    d2 = "HAM"                          #
    yr = 2021                           #
    sn = "Q"                            #
    ev = "Belgian Grand Prix"           #
    lp = 11                             #
    #####################################

session, driver1, driver2, t1_color, t1_inv_color, t2_color, t2_inv_color = f1_data_base.data_setup(
    d1, d2, ev, yr, sn)

if(FASTESTDRIVER):
    fastest_speed.fastest_speed(
        session, driver1, driver2, t1_color, t2_color)
if(GEARMAP):
    gear_map.map_gears(session, driver1)
if(LAPSPEED):
    lap_speed.measured_speed(session, driver1, yr)
if(INPUTCOMPARE):
    input_compare.throttle_brake(
        session, driver1, driver2, t1_color, t1_inv_color, t2_color, t2_inv_color)
if(DRIVERINPUT):
    driver_inputs.throttle_brake(session, driver1, t1_color, t1_inv_color)
if(TIMETRIAL):
    time_trial_inputs.throttle_brake(
        session, driver1, t1_color, t1_inv_color, lp)
    time_trial.throttle_brake(session, driver1, t1_color, t1_inv_color, lp)

plt.show()
