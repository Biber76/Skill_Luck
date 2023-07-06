import numpy as np
import pandas as pd

def varianceLuck(games_played, p=0.5):
    return p * ((1-p) / games_played)

df = pd.read_csv('./Data/men_season23.csv')
df = df[['Rg.', 'Team', 'Sp', 'S', 'SnV']]
df['S_tot'] = df['S'] + df['SnV']

df['win_ratio'] = df['S_tot'] / df['Sp']

# calculate the observed variance (var_winRatio)
std_winRatio = df['win_ratio'].std()
var_winRatio = df['win_ratio'].var()
print('Observed Standard Deviation (Win-Ratio): ', std_winRatio, 
      '\nObserved Variance (Win-Ratio): ', var_winRatio, sep='\n')

games_played = df.iloc[0, 2]
print('\nGames played: ',games_played)

# calculate the variance of luck for the number of games played
var_luck = varianceLuck(games_played, p=0.5)
print('\nVariance Luck' ,var_luck)

# calculate the variance of skill
var_skill = var_winRatio - var_luck
print('\nVariance Skill',var_skill)

# calculate the contribution of luck
contribution_luck = var_luck / var_winRatio
print('\nContribution of Luck in %: ' ,contribution_luck * 100)