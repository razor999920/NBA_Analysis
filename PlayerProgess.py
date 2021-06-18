import time
import networkx as nx
from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.endpoints import playerdashptpass
from Graphing import create_player_graph, plot, bar, append_df, df_pass_to, eigenvector

Graph_Seaon_1 = nx.Graph()
andre = [] 

# Season 1 Team & Analysis
game_1 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612759",  team_id="1610612744", season="2017-18",  season_type_all_star="Playoffs", date_to_nullable="04/14/2018", date_from_nullable="04,14,2018")
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
time.sleep(2)

for name in game_1.get_data_frames()[1]['PLAYER_NAME']:
     Graph_Seaon_1.add_node(name)

# Graphs 
Graph_Seaon_1 = create_player_graph(Graph_Seaon_1, df_pass)
# Eigenvector
eigenvector_list = eigenvector(Graph_Seaon_1)
eigenvector_list[0] = ('2018', eigenvector_list[0][1] / 13)

# Adding to the List
andre.append(eigenvector_list[0])

Graph_Seaon_2 = nx.Graph()

# Season 2 Team & Analysis
game_1 = teamplayerdashboard.TeamPlayerDashboard(opponent_team_id="1610612746",  team_id="1610612744", season="2018-19",
                                                 season_type_all_star="Playoffs", date_to_nullable="04/13/2019", date_from_nullable="04,13,2019")

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

for name in game_1.get_data_frames()[1]['PLAYER_NAME']:
    Graph_Seaon_2.add_node(name)

Graph_Seaon_2 = create_player_graph(
    Graph_Seaon_2, df_pass)

# Eigenvector
eigenvector_list = eigenvector(Graph_Seaon_2)
eigenvector_list[0] = ('2019', eigenvector_list[0][1] / 19)

andre.append(eigenvector_list[0])

Graph_Seaon_3 = nx.Graph()

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

# Graphs 
Graph_Seaon_3 = create_player_graph(Graph_Seaon_3, df_pass)

# Eigenvector
eigenvector_list = eigenvector(Graph_Seaon_3)
eigenvector_list[0] = ('2020', eigenvector_list[0][1] / 21)

andre.append(eigenvector_list[0])
print(andre)

# Plotting/Bar
plot(andre)