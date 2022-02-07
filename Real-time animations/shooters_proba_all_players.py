import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd

image = mpimg.imread("/Users/ysadre/Desktop/court1.png")

size = np.shape(image)
reshape_size = [size[0]/50, size[1]/100]

full_data = pd.read_csv('/Users/ysadre/shoot_proba.csv')
fig, (ax4, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize = (9, 9), gridspec_kw={'height_ratios': [1, 3]})


def animation_frame(i):

    player_no = [1,2,3,4,5]
    home_players_columns = [f'player_h{i}x' for i in range(1, 6)] + [f'player_h{i}y' for i in range(1, 6)]
    home_players = full_data[home_players_columns].iloc[i]
    away_players_columns = [f'player_a{i}x' for i in range(1, 6)] + [f'player_a{i}y' for i in range(1, 6)]
    away_players = full_data[away_players_columns].iloc[i]
    ax2.set_ylim(0, size[0])
    ax2.set_xlim(0, size[1])
    home_team_positions = [home_players[:5]*reshape_size[1], home_players[5:]*reshape_size[0]]
    away_team_positions = [away_players[:5]*reshape_size[1], away_players[5:]*reshape_size[0]]
    x = list(home_team_positions[0]) + list(away_team_positions[0])
    y = list(home_team_positions[1]) + list(away_team_positions[1])
    for n in range(5):
        ax2.text(home_team_positions[0][n], home_team_positions[1][n], str(n+1), style='italic',
        bbox={'facecolor': 	'#4DBEEE', 'alpha': 2, 'pad': 5})
    s = [30]*10
    c = ['blue']*5 + ['r']*5
    scat1 = ax2.scatter(x, y, s, c, marker = 'x')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_xticks([])
    ax2.set_yticks([])

    proba_shoot = []
    for h in range(1,6): 
        proba_shoot.append(full_data[f"p{h}_shoot_prob"][i])
    ax4.set_ylabel('Probability to score')
    ax4.set_xlabel('Player number')
    ax4.bar(player_no,proba_shoot)
    

    plt.legend()
    return scat1

animation_frame(0)

ax2.imshow(image)
plt.show()