import time
import networkx as nx
from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.endpoints import playerdashptpass
from Graphing import create_player_graph, plot, bar, append_df, df_pass_to, eigenvector

# Season 1 Team & Analysis
game_1 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612759",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/14/2018", date_from_nullable="04,14,2018")
game_2 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612759",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/16/2018", date_from_nullable="04,16,2018")
game_3 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612759",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/19/2018", date_from_nullable="04,19,2018")
game_4 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612759",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/22/2018", date_from_nullable="04,22,2018")
game_5 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612759",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/24/2018", date_from_nullable="04,24,2018")
time.sleep(2)
game_6 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612740",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/28/2018", date_from_nullable="04,28,2018")
game_7 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612740",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/01/2018", date_from_nullable="05,01,2018")
game_8 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612740",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/04/2018", date_from_nullable="05,04,2018")
game_9 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612740",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/06/2018", date_from_nullable="05,06,2018")
game_10 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612740",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/08/2018", date_from_nullable="05,08,2018")
time.sleep(2)
game_11 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/14/2018", date_from_nullable="05,14,2018")
game_12 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/16/2018", date_from_nullable="05,16,2018")
game_13 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/20/2018", date_from_nullable="05,20,2018")
time.sleep(2)

# Season 1, Game 1
df_pass = df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612759",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/14/2018", date_from_nullable="04,14,2018"))
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612759",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/16/2018", date_from_nullable="04,16,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612759",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/19/2018", date_from_nullable="04,19,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612759",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/22/2018", date_from_nullable="04,22,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612759",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/24/2018", date_from_nullable="04,24,2018")), df_pass)
time.sleep(2)
# Season 1, Game 2
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612740",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/28/2018", date_from_nullable="04,28,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612740",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/01/2018", date_from_nullable="05,01,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612740",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/04/2018", date_from_nullable="05,04,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612740",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/06/2018", date_from_nullable="05,06,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612740",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/08/2018", date_from_nullable="05,08,2018")), df_pass)
time.sleep(2)
# Season 1, Game 3
df_pass =  append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/14/2018", date_from_nullable="05,14,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/16/2018", date_from_nullable="05,16,2018")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="05/20/2018", date_from_nullable="05,20,2018")), df_pass)

Graph = nx.Graph()

# Adding Team Player Names
# Graph.add_node('Iguodala, Andre')

for name in game_11.get_data_frames()[1]['PLAYER_NAME']:
     Graph.add_node(name)

# # Rebound
# df_rebound = game_6.get_data_frames()[1][['PLAYER_NAME', 'REB']]
# # df_rebound = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)
# # df_rebound = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'REB']], df_rebound)

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

# # Steal
# df_steal =  game_11.get_data_frames()[1][['PLAYER_NAME', 'STL']]
# # df_steal = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # # df_steal = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# # df_steal = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'STL']], df_steal)

# Field Points
df_fp = game_11.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']]
# df_fp = append_df(game_2.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_3.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_4.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_5.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# # df_fp = append_df(game_6.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_7.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_8.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_9.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_10.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_11.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_12.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
df_fp = append_df(game_13.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)

# Graphs 
Graph = create_player_graph(Graph, df_pass, df_assist, df_fp)

# Eigenvector
eigenvector_list = eigenvector(Graph)
eigenvector_list[0] = (eigenvector_list[0][0], eigenvector_list[0][1] / 13)

andre = [] 
andre.append(eigenvector_list[0])
print(andre)

# Plotting/Bar
plot(andre)