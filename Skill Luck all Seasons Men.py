import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def varianceLuck(games_played, p=0.5):
    return p * ((1-p) / games_played)

seasons = [i for i in range(7, 21)] + [23]
list_contribution_luck = []
for season in seasons:
    df = pd.read_csv(f'./Data/men_season{season}.csv')
    df = df[['Rg.', 'Team', 'Sp', 'S', 'SnV']]
    df['S_tot'] = df['S'] + df['SnV']

    df['win_ratio'] = df['S_tot'] / df['Sp']
            
    # calculate the observed variance (var_winRatio)
    std_winRatio = df['win_ratio'].std()
    var_winRatio = df['win_ratio'].var()
    # print('Observed Standard Deviation (Win-Ratio): ', std_winRatio, 
    #     '\nObserved Variance (Win-Ratio): ', var_winRatio, sep='\n')

    games_played = df.iloc[0, 2]
    # print('\nGames played: ',games_played)

    # calculate the variance of luck for the number of games played
    var_luck = varianceLuck(games_played, p=0.5)
    # print('\nVariance Luck' ,var_luck)

    # calculate the variance of skill
    var_skill = var_winRatio - var_luck
    # print('\nVariance Skill',var_skill)

    # calculate the contribution of luck
    contribution_luck = var_luck / var_winRatio
    # print('\nContribution of Luck in %: ' ,contribution_luck * 100)
    list_contribution_luck.append(round(contribution_luck*100,1))
# print(seasons)
# print(list_contribution_luck)

df_luck_contribution = pd.DataFrame({'Season': seasons, 'LuckContribution': list_contribution_luck}
                                    ).set_index('Season')
# print(df_luck_contribution)

print(round(np.mean(df_luck_contribution.LuckContribution),1))

# fig, ax = plt.subplots(1,2)
# ax[0].plot(df_luck_contribution.index, df_luck_contribution.LuckContribution)
# ax[0].hlines(np.mean(df_luck_contribution.LuckContribution), xmin=7, xmax=23, color='black', label=f'Mean {round(np.mean(df_luck_contribution.LuckContribution),1)}')
# ax[1].hist(df_luck_contribution.LuckContribution, bins=4)
# ax[1].vlines(np.mean(df_luck_contribution.LuckContribution), ymin=0, ymax=5, color='black', label=f'Mean {round(np.mean(df_luck_contribution.LuckContribution),1)}')
# # df_luck_contribution.hist(bins=5)
# ax[0].legend()
# ax[1].legend()
# plt.show()

fig, ax = plt.subplots(1,2, figsize=(12,8))
fig.suptitle('Luck Contribution CH-Floorball Men 2007 - 2023')
ax[0].plot(df_luck_contribution.index, df_luck_contribution.LuckContribution)
ax[0].hlines(np.mean(df_luck_contribution.LuckContribution), xmin=7, xmax=23, color='red', label=f'Mean {round(np.mean(df_luck_contribution.LuckContribution),1)}')
ax[0].hlines(np.median(df_luck_contribution.LuckContribution), xmin=7, xmax=23, color='orange', label=f'Median {round(np.median(df_luck_contribution.LuckContribution),1)}')
ax[0].set_title('Luck Contribuion per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Luck Contribution in %')

ax[1].hist(df_luck_contribution.LuckContribution, bins=4)
ax[1].vlines(np.mean(df_luck_contribution.LuckContribution), ymin=0, ymax=6, color='red', label=f'Mean {round(np.mean(df_luck_contribution.LuckContribution),1)}')
ax[1].vlines(np.median(df_luck_contribution.LuckContribution), ymin=0, ymax=6, color='orange', label=f'Median {round(np.median(df_luck_contribution.LuckContribution),1)}')
ax[1].set_title('Frequency Distribution of Luck Contribution')
ax[1].set_xlabel('Luck Contribution in % 4 bins')
ax[1].set_ylabel('Frequency')
# df_luck_contribution.hist(bins=5)
ax[0].legend()
ax[1].legend()
plt.savefig('./Pictures/men.jpg')
plt.show()
