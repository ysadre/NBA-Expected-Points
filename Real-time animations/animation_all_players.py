import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import matplotlib.image as mpimg
import pandas as pd
import time
import os
from pandas.core import frame

file_path = "/Users/ysadre/Desktop/NBA Expected Point/Data/"

image = mpimg.imread(file_path + "court1.png")
size = np.shape(image)
reshape_size = [size[0]/50, size[1]/100]
full_data = pd.read_csv(file_path + "shoot_proba_final.csv")
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize = (9, 9), gridspec_kw={'height_ratios': [1, 2]})


ball = full_data[['ball_x', 'ball_y']].iloc[0]
home_players_columns = [f'player_h{i}x' for i in range(1, 6)] + [f'player_h{i}y' for i in range(1, 6)]
home_players = full_data[home_players_columns].iloc[0]
away_players_columns = [f'player_a{i}x' for i in range(1, 6)] + [f'player_a{i}y' for i in range(1, 6)]
away_players = full_data[away_players_columns].iloc[0]

ax2.set_ylim(0, size[0])
ax2.set_xlim(0, size[1])

ball_position = [ball[0]*reshape_size[1], ball[1]*reshape_size[0]]
home_team_positions = [home_players[:5]*reshape_size[1], home_players[5:]*reshape_size[0]]
away_team_positions = [away_players[:5]*reshape_size[1], away_players[5:]*reshape_size[0]]

x = list(home_team_positions[0]) + list(away_team_positions[0])
y = list(home_team_positions[1]) + list(away_team_positions[1])

s = [30]*10
c = ["#00008B", "#8F6A23","#228B22","#B23AEE","#528B8B","red","red","red","red","red"]
scat0 = ax2.scatter(list([ball_position[0]]), list([ball_position[1]]) , s = 30, c = 'orange')
scat1 = ax2.scatter(x, y, s, c, marker = 'X')
ax2.set_xticklabels([])
ax2.set_yticklabels([])
ax2.set_xticks([])
ax2.set_yticks([])

plt.legend()

p1_proba_line, = ax1.plot(np.arange(0, 0+1, 1), [full_data[f"p1_shoot_prob"].iloc[0]], color = '#00008B') # Blue
p2_proba_line, = ax1.plot(np.arange(0, 0+1, 1), [full_data[f"p2_shoot_prob"].iloc[0]], color = '#8F6A23') # Brown
p3_proba_line, = ax1.plot(np.arange(0, 0+1, 1), [full_data[f"p3_shoot_prob"].iloc[0]], color = '#228B22') # Green
p4_proba_line, = ax1.plot(np.arange(0, 0+1, 1), [full_data[f"p4_shoot_prob"].iloc[0]], color='#B23AEE') # Magenta
p5_proba_line, = ax1.plot(np.arange(0, 0+1, 1), [full_data[f"p5_shoot_prob"].iloc[0]], color = '#528B8B') #Light blue
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 1)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Shoot sucess probability')
ax1.set_xticklabels([str(0.16*l) + 's' for l in range(0, 50, 10)], minor = False)
ax1.set_xticks(np.arange(0, 50, 10))

def animation_frame(i):
    action_number = full_data['action'].iloc[i]
    frame_number = full_data['frame'].iloc[i]

    ball = full_data[['ball_x', 'ball_y']].iloc[i]
    home_players_columns = [f'player_h{i}x' for i in range(1, 6)] + [f'player_h{i}y' for i in range(1, 6)]
    home_players = full_data[home_players_columns].iloc[i]
    away_players_columns = [f'player_a{i}x' for i in range(1, 6)] + [f'player_a{i}y' for i in range(1, 6)]
    away_players = full_data[away_players_columns].iloc[i]

    ax2.set_ylim(0, size[0])
    ax2.set_xlim(0, size[1])

    ball_position = [ball[0]*reshape_size[1], ball[1]*reshape_size[0]]
    home_team_positions = [home_players[:5]*reshape_size[1], home_players[5:]*reshape_size[0]]
    away_team_positions = [away_players[:5]*reshape_size[1], away_players[5:]*reshape_size[0]]

    x = list(home_team_positions[0]) + list(away_team_positions[0])
    y = list(home_team_positions[1]) + list(away_team_positions[1])
    scat0.set_offsets([ball_position[0], ball_position[1]])
    scat1.set_offsets([[x[k], y[k]] for k in range(10)])

    # for n in range(5):
    #     ax2.text(home_team_positions[0][n], home_team_positions[1][n], str(n+1), style='italic',
    #     bbox={'facecolor': 	'#4DBEEE', 'alpha': 2, 'pad': 5})
    p1_proba_line.set_data(np.arange(0, frame_number+1, 1), [full_data[f"p1_shoot_prob"].iloc[l] for l in range(action_number*50, action_number*50+frame_number+1)])
    p2_proba_line.set_data(np.arange(0, frame_number+1, 1), [full_data[f"p2_shoot_prob"].iloc[l] for l in range(action_number*50, action_number*50+frame_number+1)])
    p3_proba_line.set_data(np.arange(0, frame_number+1, 1), [full_data[f"p3_shoot_prob"].iloc[l] for l in range(action_number*50, action_number*50+frame_number+1)])
    p4_proba_line.set_data(np.arange(0, frame_number+1, 1), [full_data[f"p4_shoot_prob"].iloc[l] for l in range(action_number*50, action_number*50+frame_number+1)])
    p5_proba_line.set_data(np.arange(0, frame_number+1, 1), [full_data[f"p5_shoot_prob"].iloc[l] for l in range(action_number*50, action_number*50+frame_number+1)])
    return scat0, scat1, p1_proba_line, p2_proba_line, p3_proba_line, p4_proba_line, p5_proba_line

anim = animation.FuncAnimation(fig, func = animation_frame, frames = np.arange(0, 5000, 1), interval = 100)

ax2.imshow(image)
plt.show()