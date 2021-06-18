import time
import networkx as nx
from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.endpoints import playerdashptpass
from Graphing import create_player_graph, plot, bar, append_df, df_pass_to, eigenvector

# Season 2 Team & Analysis
game_1 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
                                                 season_type_all_star="Playoffs", date_to_nullable="04/13/2019", date_from_nullable="04,13,2019")
# game_2 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/15/2019", date_from_nullable="04,15,2019")
# game_3 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/18/2019", date_from_nullable="04,18,2019")
# game_4 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/21/2019", date_from_nullable="04,21,2019")
# game_5 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/24/2019", date_from_nullable="04,24,2019")
# game_6 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/26/2019", date_from_nullable="04,26,2019")
# time.sleep(2)
# game_7 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/28/2019", date_from_nullable="04,28,2019")
# game_8 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="04/30/2019", date_from_nullable="04,30,2019")
# game_9 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="05/04/2019", date_from_nullable="05,04,2019")
# game_10 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2018-19",
#                                                  season_type_all_star="Playoffs", date_to_nullable="05/06/2019", date_from_nullable="05,06,2019")
# game_11 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="05/08/2019", date_from_nullable="05,08,2019")
# game_12 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612745",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="05/10/2019", date_from_nullable="05,10,2019")
# time.sleep(2)
# game_13 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612757",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="05/14/2019", date_from_nullable="05,14,2019")
# game_14 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612757",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="05/16/2019", date_from_nullable="05,16,2019")
# game_15 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612757",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="05/18/2019", date_from_nullable="05,18,2019")
# time.sleep(2)
# game_16 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612761",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="05/30/2019", date_from_nullable="05,30,2019")
# game_17 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612761",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="06/02/2019", date_from_nullable="06,02,2019")
# game_18 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612761",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="06/05/2019", date_from_nullable="06,05,2019")
# game_19 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612761",  team_id="1610612744", season="2018-19",
#                                                   season_type_all_star="Playoffs", date_to_nullable="06/07/2019", date_from_nullable="06,07,2019")
# time.sleep(2)

# Season 2, Game 1
df_pass = df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612746",  team_id="1610612744", player_id="2738",
                                                       season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/13/2019", date_from_nullable="04,13,2019"))
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612746",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/15/2019", date_from_nullable="04,15,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612746",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/18/2019", date_from_nullable="04,18,2019")), df_pass)

df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612746",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/21/2019", date_from_nullable="04,21,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612746",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/24/2019", date_from_nullable="04,24,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612746",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/26/2019", date_from_nullable="04,26,2019")), df_pass)
time.sleep(2)
# # Season 2, Game 2
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/28/2019", date_from_nullable="04,28,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="04/30/2019", date_from_nullable="04,30,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/04/2019", date_from_nullable="05,04,2019")), df_pass)
time.sleep(2)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/06/2019", date_from_nullable="05,06,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/08/2019", date_from_nullable="05,08,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612745",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/10/2019", date_from_nullable="05,10,2019")), df_pass)
time.sleep(2)
# # Season 2, Game 3
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612757",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/14/2019", date_from_nullable="05,14,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612757",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/16/2019", date_from_nullable="05,16,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612757",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/18/2019", date_from_nullable="05,18,2019")), df_pass)
time.sleep(2)
# Season 2, Game 4
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612761",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="05/30/2019", date_from_nullable="05,30,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612761",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="06/02/2019", date_from_nullable="06,02,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612761",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs", date_to_nullable="06/05/2019", date_from_nullable="06,05,2019")), df_pass)
df_pass = append_df(df_pass_to(playerdashptpass.PlayerDashPtPass(opponent_team_id="1610612761",  team_id="1610612744", player_id="2738",
                                                                 season="2018-19",  season_type_all_star="Playoffs",  date_to_nullable="06/07/2019", date_from_nullable="06,07,2019")), df_pass)

Graph = nx.Graph()

# Adding Team Player Names
# Graph.add_node('Iguodala, Andre')

for name in game_1.get_data_frames()[1]['PLAYER_NAME']:
    Graph.add_node(name)

# # Rebound
# df_rebound = game_1.get_data_frames()[1][['PLAYER_NAME', 'REB']]
# df_rebound = append_df(game_2.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_3.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_4.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_5.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_6.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_7.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_8.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_9.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_10.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_11.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_12.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_13.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_14.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_15.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_16.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_17.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_18.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)
# df_rebound = append_df(game_19.get_data_frames()[
#                        1][['PLAYER_NAME', 'REB']], df_rebound)

# Assist
df_assist = game_1.get_data_frames()[1][['PLAYER_NAME', 'AST']]
# df_assist = append_df(game_2.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_3.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_4.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_5.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_6.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_7.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_8.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_9.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_10.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_11.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_12.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_13.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_14.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_15.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_16.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_17.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_18.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)
# df_assist = append_df(game_19.get_data_frames()[
#                       1][['PLAYER_NAME', 'AST']], df_assist)

# # Steal
# df_steal = game_1.get_data_frames()[1][['PLAYER_NAME', 'STL']]
# df_steal = append_df(game_2.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_3.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_4.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_5.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_6.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_7.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_8.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_9.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_10.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_11.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_12.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_13.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_14.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_15.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_16.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_17.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_18.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)
# df_steal = append_df(game_19.get_data_frames()[
#                      1][['PLAYER_NAME', 'STL']], df_steal)

# Field Points
df_fp = game_1.get_data_frames()[1][['PLAYER_NAME', 'FGM', 'FGA']]
# df_fp = append_df(game_2.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_3.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_4.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_5.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_6.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_7.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_8.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_9.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_10.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_11.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_12.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_13.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_14.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_15.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_16.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_17.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_18.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)
# df_fp = append_df(game_19.get_data_frames()[
#                   1][['PLAYER_NAME', 'FGM', 'FGA']], df_fp)

# Graphs
Graph = create_player_graph(
    Graph, df_pass, df_assist, df_fp)

# Eigenvector
eigenvector_list = eigenvector(Graph)
eigenvector_list[0] = (eigenvector_list[0][0], eigenvector_list[0][1] / 19)

andre = [] 
andre.append(eigenvector_list[0])
print(andre)

# Plotting/Bar
plot(andre)
