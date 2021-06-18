import time
import networkx as nx
from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.endpoints import playerdashptpass
from Graphing import create_player_graph, plot, bar, append_df, df_pass_to, eigenvector

# # Season 1 Team & Analysis
# game_1 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612754",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/18/2020", date_from_nullable="08,14,2020")
# game_2 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612754",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/20/2020", date_from_nullable="08,02,2020")
# game_3 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612754",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/22/2020", date_from_nullable="08,22,2020")
# game_4 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612754",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/24/2020", date_from_nullable="08,24,2020")
# game_5 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612754",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/31/2020", date_from_nullable="08,31,2020")
# time.sleep(2)
# game_6 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612749",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/31/2020", date_from_nullable="08,31,2020")
# game_7 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612749",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/02/2020", date_from_nullable="09,02,2020")
# game_8 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612749",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/04/2020", date_from_nullable="09,04,2020")
# game_9 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612749",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/06/2020", date_from_nullable="09,06,2020")
# game_10 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612749",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/08/2020", date_from_nullable="09,08,2020")
# time.sleep(2)
game_11 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612738",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/15/2020", date_from_nullable="09,15,2020")
game_12 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612738",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/17/2020", date_from_nullable="09,17,2020")
game_13 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612738",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/19/2020", date_from_nullable="09,19,2020")
game_14 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612738",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/23/2020", date_from_nullable="09,23,2020")
game_15 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612738",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/25/2020", date_from_nullable="09,25,2020")
game_16 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612738",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/27/2020", date_from_nullable="09,27,2020")
# time.sleep(2)
# game_17 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612747",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/30/2020", date_from_nullable="09,30,2020")
# game_18 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612747",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/02/2020", date_from_nullable="10,02,2020")
# game_19 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612747",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/04/2020", date_from_nullable="10,04,2020")
# game_20 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612747",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/06/2020", date_from_nullable="10,06,2020")
# game_21 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612747",  team_id="1610612748", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/09/2020", date_from_nullable="10,09,2020")
# time.sleep(2)

# Season 3, Game 1
df_pass = df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612754",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/18/2020", date_from_nullable="08,14,2020"))
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612754",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/20/2020", date_from_nullable="08,02,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612754",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/22/2020", date_from_nullable="08,22,2020")), df_pass)
time.sleep(2)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612754",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/24/2020", date_from_nullable="08,24,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612754",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/31/2020", date_from_nullable="08,31,2020")), df_pass)
time.sleep(2)
# # Season 3, Game 2
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612749",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="08/31/2020", date_from_nullable="08,31,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612749",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/02/2020", date_from_nullable="09,02,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612749",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/04/2020", date_from_nullable="09,04,2020")), df_pass)
time.sleep(2)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612749",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/06/2020", date_from_nullable="09,06,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612749",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/08/2020", date_from_nullable="09,08,2020")), df_pass)
time.sleep(2)
# # Season 3, Game 3
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612738",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/15/2020", date_from_nullable="09,15,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612738",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/17/2020", date_from_nullable="09,17,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612738",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/19/2020", date_from_nullable="09,19,2020")), df_pass)
time.sleep(2)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612738",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/23/2020", date_from_nullable="09,23,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612738",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/25/2020", date_from_nullable="09,25,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612738",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/27/2020", date_from_nullable="09,27,2020")), df_pass)
time.sleep(2)
# # Season 3, Game 4
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612747",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="09/30/2020", date_from_nullable="09,30,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612747",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/02/2020", date_from_nullable="10,02,2020")), df_pass)
time.sleep(2)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612747",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/04/2020", date_from_nullable="10,04,2020")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612747",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/06/2020", date_from_nullable="10,06,2020")), df_pass)
time.sleep(2)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612747",  team_id="1610612748", player_id="2738", season="2019-20",  season_type_all_star="Playoffs", date_to_nullable="10/09/2020", date_from_nullable="10,09,2020")), df_pass)

Graph = nx.Graph()

# # Adding Team Player Names
# Graph.add_node('Iguodala, Andre')

for name in game_11.get_data_frames()[1]['PLAYER_NAME']:
     Graph.add_node(name)

# # Rebound
# df_rebound = game_1.get_data_frames()[1][['PLAYER_NAME', 'REB']]
# df_rebound = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_14.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_15.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_16.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_17.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_18.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_19.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_20.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_21.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)

# Assist
df_assist = game_11.get_data_frames()[1][['PLAYER_NAME', 'AST']]
# df_assist = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
df_assist = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
df_assist = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
df_assist = append_df(game_14.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
df_assist = append_df(game_15.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
df_assist = append_df(game_16.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_17.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_18.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_19.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_20.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_21.get_data_frames()[1][['PLAYER_NAME', 'AST']], df_assist)

# # Steal
# df_steal =  game_1.get_data_frames()[1][['PLAYER_NAME', 'STL']]
# df_steal = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_14.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_15.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_16.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_17.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_18.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_19.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_20.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_21.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)

# Field Points
df_fp = game_11.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']]
# df_fp = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_14.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_15.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_16.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_17.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_18.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_19.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_20.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_21.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)

# Graphs 
Graph = create_player_graph(Graph, df_pass, df_assist, df_fp)

# Eigenvector
eigenvector_list = eigenvector(Graph)
eigenvector_list[0] = (eigenvector_list[0][0], eigenvector_list[0][1] / 21)

andre = [] 
andre.append(eigenvector_list[0])
print(andre)

# Plotting/Bar
plot(andre)