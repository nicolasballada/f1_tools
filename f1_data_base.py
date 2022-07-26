import fastf1.plotting
import json


def padZero(str, len):
    if not(len):
        len = 2
    zeros = (len).join("0")
    return (zeros + str).slice(-1)


def invertColor(hex):
    r = 0

    b = 0
    g = 0

    if(hex[0] == "#"):
        hex = hex[1:]
        # convert 3-digit hex to 6-digits.
        if (len(hex) == 3):
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
            if (len(hex) != 6):
                r = int(hex[0:2], 16),
                g = int(hex[2:4], 16),
                b = int(hex[4:6], 16)
                # invert color components
                r = (255 - r).toString(16)
                g = (255 - g).toString(16)
                b = (255 - b).toString(16)
                # pad each with zeros and return
                return "#" + padZero(r) + padZero(g) + padZero(b)


def data_setup(ident1, ident2, event_name, year, session_type):

    class driver:
        def __init__(self, i, t):
            self.identifier = i
            self.team = t

    fastf1.Cache.enable_cache("./cache")
    fastf1.plotting.setup_mpl()

    session = fastf1.get_session(year, event_name, session_type)
    session.load()

    def get_team(val):
        for key, value in json_data.items():
            if val == value[str(year)][-1]:
                return key
            if val == value[str(year)][0]:
                return key

        return "key doesn't exist"

    # Opening JSON file
    f = open("./data.json")

    # returns JSON object as a dictionary
    json_data = json.load(f)

    driver1 = driver(ident1, get_team(ident1))
    driver2 = driver(ident2, get_team(ident2))

    if(driver1.team == driver2.team):
        t1_color = invertColor(fastf1.plotting.team_color(driver1.team))
        t1_inv_color = fastf1.plotting.team_color(driver1.team)
    else:
        t1_color = fastf1.plotting.team_color(driver1.team)
        t1_inv_color = invertColor(fastf1.plotting.team_color(driver1.team))

    t2_color = fastf1.plotting.team_color(driver2.team)
    t2_inv_color = invertColor(fastf1.plotting.team_color(driver2.team))

    return [session, driver1, driver2, t1_color, t1_inv_color, t2_color, t2_inv_color]
