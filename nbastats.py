import numpy
import pandas as pd
import requests


season_id = '2022-23'
per_mode = 'Totals'
player_info_season_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + \
    season_id+'&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
player_info_recent_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=5&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2022-23&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

season_response = requests.get(
    url=player_info_season_url, headers=headers).json()
recent_response = requests.get(
    url=player_info_recent_url, headers=headers).json()
player_season_info = season_response['resultSets'][0]['rowSet']
player_recent_info = recent_response['resultSets'][0]['rowSet']
columns_list = [
    'player_id',
    'player_name',
    'nickname',
    'team_id',
    'team_abbreviation',
    'age',
    'gp',
    'w',
    'l',
    'w_pct',
    'min',
    'fgm',
    'fga',
    'fg_pct',
    'fg3m',
    'fg3a',
    'fg3_pct',
    'ftm',
    'fta',
    'ft_pct',
    'oreb',
    'dreb',
    'reb',
    'ast',
    'tov',
    'stl',
    'blk',
    'blka',
    'pf',
    'pfd',
    'pts',
    'plus_minus',
    'nba_fantasy_pts',
    'dd2',
    'td3',
    'gp_rank',
    'w_rank',
    'l_rank',
    'w_pct_rank',
    'min_rank',
    'gm_rank',
    'fga_rank',
    'fg_pct_rank',
    'fg3m_rank',
    'fg3a_rank',
    'fg3_pct_rank',
    'ftm_rank',
    'fta_rank',
    'ft_pct_rank',
    'oreb_rank',
    'dreb_rank',
    'reb_rank',
    'ast_rank',
    'tov_rank',
    'stl_rank',
    'blk_rank',
    'blka_rank',
    'pf_rank',
    'pfd_rank',
    'pts_rank',
    'plus_minus_rank',
    'nba_fantasy_pts_rank',
    'dd2_rank',
    'td3_rank',
    'wnba_fantasy_pts_rank',
    'leaguedashplayerstats'
]
season_df = pd.DataFrame(player_season_info, columns=columns_list)
recent_df = pd.DataFrame(player_recent_info, columns=columns_list)

player_name = ""


def printPoints(season_player_stats, recent_player_stats):
    print("Season = ", season_player_stats.iloc[0]['pts'])
    print("Recent = ", recent_player_stats.iloc[0]['pts'])
    season_pts = season_player_stats.iloc[0]['pts']
    recent_pts = recent_player_stats.iloc[0]['pts']
    if recent_pts > season_pts:
        difference = recent_pts - season_pts
        difference = numpy.around(difference, 2)
        print("This player is hot!")
        print(player_name + " has been scoring very well in the last 5 games!")
        print(player_name + "'s points average in the last 5 games has been " + str(difference) +
              " points higher than his season average!")
        print("this player sucks, season average: " +
              str(season_pts) + " recent average: " + str(recent_pts))


def printRebounds(season_player_stats, recent_player_stats):
    print("Season = ", season_player_stats.iloc[0]['reb'])
    print("Recent = ", recent_player_stats.iloc[0]['reb'])
    season_reb = season_player_stats.iloc[0]['reb']
    recent_reb = recent_player_stats.iloc[0]['reb']
    if recent_reb > season_reb:
        difference = recent_reb - season_reb
        difference = numpy.around(difference, 2)
        print("This player can rebound!")
        print(player_name + " has been rebounding very well in the last 5 games!")
        print(player_name + "'s rebounding average in the last 5 games has been " + str(difference) +
              " rebounds higher than his season average!")


def printAssists(season_player_stats, recent_player_stats):
    print("Season = ", season_player_stats.iloc[0]['ast'])
    print("Recent = ", recent_player_stats.iloc[0]['ast'])
    season_ast = season_player_stats.iloc[0]['ast']
    recent_ast = recent_player_stats.iloc[0]['ast']
    if recent_ast > season_ast:
        difference = recent_ast - season_ast
        difference = numpy.around(difference, 2)
        print("This player can assist!")
        print(player_name + " has been assisting very well in the last 5 games!")
        print(player_name + "'s assists average in the last 5 games has been " + str(difference) +
              " assists higher than his season average!")


def printThrees(season_player_stats, recent_player_stats):
    print("Season = ", season_player_stats.iloc[0]['fg3m'])
    print("Recent = ", recent_player_stats.iloc[0]['fg3m'])
    season_threes = season_player_stats.iloc[0]['ast']
    recent_threes = recent_player_stats.iloc[0]['ast']
    if recent_threes > season_threes:
        difference = recent_threes - season_threes
        difference = numpy.around(difference, 2)
        print("This player can shoot the rock!")
        print(player_name + " has been shooting very well in the last 5 games!")
        print(player_name + "'s three point shots made in the last 5 games has been " + str(difference) +
              " threes higher than his season average!")


same_player_diff_stat = False
while True:
    if not same_player_diff_stat:
        player_name = input("Enter player name: ").lower()
    season_player_stats = season_df.loc[season_df['player_name'].str.lower(
    ) == player_name]
    recent_player_stats = recent_df.loc[recent_df['player_name'].str.lower(
    ) == player_name]
    if season_player_stats.empty:
        print("Player not found. Please try again: ")
        continue
    response = input(
        "Would you like to check points, rebounds, assists, or threes? ")
    print(response)
    if response == 'points':
        printPoints(season_player_stats, recent_player_stats)
    elif response == 'rebounds':
        printRebounds(season_player_stats, recent_player_stats)
    elif response == 'assists':
        printAssists(season_player_stats, recent_player_stats)
    elif response == 'threes':
        printThrees(season_player_stats, recent_player_stats)

    another_search = input(
        "Would you like to search for another stat of this player? (y/n): ")
    if another_search.lower() == 'y':
        same_player_diff_stat = True
        continue
    another_search = input(
        "Would you like to search for another player? (y/n): ")
    same_player_diff_stat = False
    if another_search.lower() == 'n':
        break

print("Thanks for using the NBA keenan stats bot!")
