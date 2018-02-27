# All imports needed for pyvis
from pybaseball import playerid_lookup
from pybaseball import statcast_batter
from pybaseball import statcast_pitcher
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.path import Path

# Returns correct type of data (dependent on player and his type)
def process_data(time, firstname, lastname, pos):
    playerid = playerid_lookup(lastname, firstname)
    if "to" in time:
        if pos == 'batter': return statcast_batter(time[0:10], time[14:], player_id=int(playerid['key_mlbam'][0]))
        elif pos == 'pitcher': return statcast_pitcher(time[0:10], time[14:], player_id=int(playerid['key_mlbam'][0]))
        else: return None
    else: 
        if pos == 'batter': return statcast_batter(time, player_id=int(playerid['key_mlbam'][0]))
        elif pos == 'pitcher': return statcast_pitcher(time, player_id=int(playerid['key_mlbam'][0]))
        else: return None
