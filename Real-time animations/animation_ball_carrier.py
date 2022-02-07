import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import matplotlib.image as mpimg
import pandas as pd
import os

file_path = "/Users/ysadre/Desktop/NBA Expected Point/Data/"

image = mpimg.imread(os.path.join(file_path + "court1.png"))
size = np.shape(image)
reshape_size = [size[0]/50, size[1]/100]

full_data = pd.read_csv(file_path+'train_logreg_prob.csv')


fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize = (7, 7), gridspec_kw={'height_ratios': [1, 3]})

ball = full_data[['ball_x', 'ball_y']].iloc[0]
home_players_columns = [f'player_h{i}x' for i in range(1, 6)] + [f'player_h{i}y' for i in range(1, 6)]
home_players = full_data[home_players_columns].iloc[0]
away_players_columns = [f'player_a{i}x' for i in range(1, 6)] + [f'player_a{i}y' for i in range(1, 6)]
away_players = full_data[away_players_columns].iloc[0]

closest_def = full_data['closest_def'].iloc[0]
closest_def_position = full_data[[f'player_a{closest_def}x'] + [f'player_a{closest_def}y']].iloc[0]

ball_carrier = full_data['ball_carrier'].iloc[0]
ball_carrier_position = full_data[[f'player_h{ball_carrier}x'] + [f'player_h{ball_carrier}y']].iloc[0]

ax2.set_ylim(0, size[0])
ax2.set_xlim(0, size[1])

ball_position = [ball[0]*reshape_size[1], ball[1]*reshape_size[0]]
home_team_positions = [home_players[:5]*reshape_size[1], home_players[5:]*reshape_size[0]]
away_team_positions = [away_players[:5]*reshape_size[1], away_players[5:]*reshape_size[0]]

x = list(home_team_positions[0]) + list(away_team_positions[0])
y = list(home_team_positions[1]) + list(away_team_positions[1])

s = [30]*10
c = ['r']*5 + ['blue']*5
scat0 = ax2.scatter(list([ball_position[0]]), list([ball_position[1]]) , s = 30, c = 'orange')
scat1 = ax2.scatter(x, y, s, c, marker = 'x')
scat2 = ax2.scatter([closest_def_position[0]*reshape_size[1]], [closest_def_position[1]*reshape_size[0]], s = 50, facecolors='none', edgecolors='blue', marker = 's', label = 'closest_def')
scat3 = ax2.scatter([ball_carrier_position[0]*reshape_size[1]], [ball_carrier_position[1]*reshape_size[0]], s = 50, facecolors='none', edgecolors='r', marker = 's', label = 'ball_carrier')
ax2.set_xticklabels([])
ax2.set_yticklabels([])
ax2.set_xticks([])
ax2.set_yticks([])

plt.legend()

proba_line, = ax1.plot(np.arange(0, 0+1, 1), [full_data['shoot_prob'].iloc[0]])
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 1)
ax1.set_xlabel('time in the play')
ax1.set_ylabel('shoot sucess probability')
ax1.set_xticklabels([str(0.16*l) + 's' for l in range(0, 50, 10)], minor = False)
ax1.set_xticks(np.arange(0, 50, 10))


def animation_frame(i):
    action_number = full_data['action'].iloc[i]
    frame_number = full_data['frame'].iloc[i]
    plt.title(f'play number {action_number}', y = 1.8)

    ball = full_data[['ball_x', 'ball_y']].iloc[i]
    home_players_columns = [f'player_h{i}x' for i in range(1, 6)] + [f'player_h{i}y' for i in range(1, 6)]
    home_players = full_data[home_players_columns].iloc[i]
    away_players_columns = [f'player_a{i}x' for i in range(1, 6)] + [f'player_a{i}y' for i in range(1, 6)]
    away_players = full_data[away_players_columns].iloc[i]

    closest_def = full_data['closest_def'].iloc[i]
    closest_def_position = full_data[[f'player_a{closest_def}x'] + [f'player_a{closest_def}y']].iloc[i]

    ball_carrier = full_data['ball_carrier'].iloc[i]
    ball_carrier_position = full_data[[f'player_h{ball_carrier}x'] + [f'player_h{ball_carrier}y']].iloc[i]

    ax2.set_ylim(0, size[0])
    ax2.set_xlim(0, size[1])

    ball_position = [ball[0]*reshape_size[1], ball[1]*reshape_size[0]]
    home_team_positions = [home_players[:5]*reshape_size[1], home_players[5:]*reshape_size[0]]
    away_team_positions = [away_players[:5]*reshape_size[1], away_players[5:]*reshape_size[0]]

    x = list(home_team_positions[0]) + list(away_team_positions[0])
    y = list(home_team_positions[1]) + list(away_team_positions[1])

    scat0.set_offsets([ball_position[0], ball_position[1]])
    scat1.set_offsets([[x[k], y[k]] for k in range(10)])
    scat2.set_offsets([closest_def_position[0]*reshape_size[1], closest_def_position[1]*reshape_size[0]]) #closest def
    scat3.set_offsets([ball_carrier_position[0]*reshape_size[1], ball_carrier_position[1]*reshape_size[0]]) #ball_carrier

    proba_line.set_data(np.arange(0, frame_number+1, 1), [full_data['shoot_prob'].iloc[l] for l in range(action_number*50, action_number*50+frame_number+1)])

    return scat0, scat1, scat2, scat3, proba_line, 

anim = animation.FuncAnimation(fig, func = animation_frame, frames = np.arange(0, 5000, 1), interval = 100)

ax2.imshow(image)
plt.show()