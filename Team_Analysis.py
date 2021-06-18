import time
import networkx as nx
from nba_api.stats.endpoints import teamplayerdashboard, teamdashptpass
from nba_api.stats.endpoints import playerdashptpass
from Graphing import create_team_graph, plot_allPlayers, append_df

def add_player_names (G, names):
    for name in names:
        G.add_node(name)

def append_dataFrame (data):
    append_df(data, data)

def label_seasons_ev(list, season):
    ev = []
    for x in list:
        ev.append((x[0], x[1], season))
    
    return ev
# Teams Data
game_ah_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612737", opponent_team_id="1610612744",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/02/2019", date_from_nullable="12/02/2019")
game_ah_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612737", opponent_team_id="1610612752", season="2018-19",  season_type_all_star="Regular Season", date_to_nullable="12/21/2018", date_from_nullable="12,21,2018")
game_ah_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612737", opponent_team_id="1610612753",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/06/2017", date_from_nullable="12,06,2017")
time.sleep(2)
# #boston celtics
# game_bc_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612738", opponent_team_id="1610612752",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12,01,2019")
# game_bc_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612738", opponent_team_id="1610612764",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/12/2018", date_from_nullable="12,12,2018")
# game_bc_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612738", opponent_team_id="1610612759",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/08/2017", date_from_nullable="12,08,2017")
# time.sleep(2)
# #Brooklyn nets
# game_bn_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612751", opponent_team_id="1610612748",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12,01,2019")
# game_bn_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612751", opponent_team_id="1610612755",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/12/2018", date_from_nullable="12,12,2018")
# game_bn_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612751", opponent_team_id="1610612761",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/15/2017", date_from_nullable="12/15/2017")
time.sleep(2)
#dallas mavericks
game_dm_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612742", opponent_team_id="1610612747",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12/01/2019")
game_dm_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612742", opponent_team_id="1610612756",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/13/2018", date_from_nullable="12,13,2018")
game_dm_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612742", opponent_team_id="1610612744",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/14/2017", date_from_nullable="12/14/2017")
#houston rockets
game_hr_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612745", opponent_team_id="1610612761",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/05/2019", date_from_nullable="12/05/2019")
game_hr_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612745", opponent_team_id="1610612762",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/06/2018", date_from_nullable="12,06,2018")
game_hr_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612745", opponent_team_id="1610612747",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/03/2017", date_from_nullable="12/03/2017")
# #Lakers
# game_lkr_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612747", opponent_team_id="1610612742",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12/01/2019")
# game_lkr_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612747", opponent_team_id="1610612740",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/21/2018", date_from_nullable="12,21,2018")
# game_lkr_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612747", opponent_team_id="1610612745",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/03/2017", date_from_nullable="12/03/2017")
# time.sleep(2)
# # Raptors
# game_hr_s3_rev = teamdashptpass.TeamDashPtPass(team_id="1610612761", opponent_team_id="1610612745",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/05/2019", date_from_nullable="12/05/2019")
# game_cc_s2_rev = teamdashptpass.TeamDashPtPass(team_id="1610612761", opponent_team_id="1610612739",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/21/2018", date_from_nullable="12,21,2018")
# game_bn_s1_rev = teamdashptpass.TeamDashPtPass(team_id="1610612761", opponent_team_id="1610612751",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="12/15/2017", date_from_nullable="12/15/2017")
# #Milwaukee Bucks
# game_mb_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612749", opponent_team_id="1610612753",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/09/2019", date_from_nullable="12/09/2019")
# game_mb_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612749", opponent_team_id="1610612765",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/17/2018", date_from_nullable="12,17,2018")
# game_mb_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612749", opponent_team_id="1610612752",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="02/06/2018", date_from_nullable="02/06/2018")
# #Los Angeles Clippers
# game_lac_s3 = teamdashptpass.TeamDashPtPass(team_id="1610612746", opponent_team_id="1610612764",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12/01/2019")
# game_lac_s2 = teamdashptpass.TeamDashPtPass(team_id="1610612746", opponent_team_id="1610612763",  season="2018-19", season_type_all_star="Regular Season", date_to_nullable="12/05/2018", date_from_nullable="12,05,2018")
# game_lac_s1 = teamdashptpass.TeamDashPtPass(team_id="1610612746", opponent_team_id="1610612755",  season="2017-18", season_type_all_star="Regular Season", date_to_nullable="02/10/2018", date_from_nullable="02/10/2018")
time.sleep(2)

#Graph
s1_graph = nx.Graph()
s2_graph = nx.Graph()
s3_graph = nx.Graph()

# s1_t2_graph = nx.Graph()
# s2_t2_graph = nx.Graph()
# s3_t2_graph = nx.Graph()

# s1_t3_graph = nx.Graph()
# s2_t3_graph = nx.Graph()
# s3_t3_graph = nx.Graph()

# s1_t4_graph = nx.Graph()
# s2_t4_graph = nx.Graph()
# s3_t4_graph = nx.Graph()

# s1_t5_graph = nx.Graph()
# s2_t5_graph = nx.Graph()
# s3_t5_graph = nx.Graph()

# s1_t6_graph = nx.Graph()
# s2_t6_graph = nx.Graph()
# s3_t6_graph = nx.Graph()

# s1_t7_graph = nx.Graph()
# s2_t7_graph = nx.Graph()
# s3_t7_graph = nx.Graph()

# s1_t8_graph = nx.Graph()
# s2_t8_graph = nx.Graph()
# s3_t8_graph = nx.Graph()

# s1_t9_graph = nx.Graph()
# s2_t9_graph = nx.Graph()
# s3_t9_graph = nx.Graph()

time.sleep(2)

# Season 1
add_player_names(s1_graph, game_ah_s1.get_data_frames()[0]['PASS_FROM'])
df = game_ah_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
ev_s1 = create_team_graph(s1_graph, df)
ev_s1 = label_seasons_ev(ev_s1, 'Season_1')

# add_player_names(s1_t2_graph, game_bc_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_bc_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t2 = create_team_graph(s1_t2_graph, df)
# ev_s1_t2 = label_seasons_ev(ev_s1_t2, 'Season_1')

# add_player_names(s1_t3_graph, game_bn_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_bn_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t3 = create_team_graph(s1_t3_graph, df)
# ev_s1_t3 = label_seasons_ev(ev_s1_t3, 'Season_1')

# add_player_names(s1_t4_graph, game_dm_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_dm_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t4 = create_team_graph(s1_t4_graph, df)
# ev_s1_t4 = label_seasons_ev(ev_s1_t4, 'Season_1')

# add_player_names(s1_t5_graph, game_hr_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_hr_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t5 = create_team_graph(s1_t5_graph, df)
# ev_s1_t5 = label_seasons_ev(ev_s1_t5, 'Season_1')

# add_player_names(s1_t6_graph, game_bn_s1_rev.get_data_frames()[0]['PASS_FROM'])
# df = game_bn_s1_rev.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t6 = create_team_graph(s1_t6_graph, df)
# ev_s1_t6 = label_seasons_ev(ev_s1_t6, 'Season_1')

# add_player_names(s1_t7_graph, game_lkr_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_lkr_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t7 = create_team_graph(s1_t7_graph, df)
# ev_s1_t7 = label_seasons_ev(ev_s1_t7, 'Season_1')

# add_player_names(s1_t8_graph, game_mb_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_mb_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t8 = create_team_graph(s1_t8_graph, df)
# ev_s1_t8 = label_seasons_ev(ev_s1_t8, 'Season_1')

# add_player_names(s1_t9_graph, game_lac_s1.get_data_frames()[0]['PASS_FROM'])
# df = game_lac_s1.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s1_t9 = create_team_graph(s1_t9_graph, df)
# ev_s1_t9 = label_seasons_ev(ev_s1_t9, 'Season_1')

time.sleep(2)
# Season 2
add_player_names(s2_graph, game_ah_s2.get_data_frames()[0]['PASS_FROM'])
df = game_ah_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
ev_s2 = create_team_graph(s2_graph, df)
ev_s2 = label_seasons_ev(ev_s2, 'Season_2')

# add_player_names(s2_t2_graph, game_bc_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_bc_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t2 = create_team_graph(s2_t2_graph, df)
# ev_s2_t2 = label_seasons_ev(ev_s2_t2, 'Season_2')

# add_player_names(s2_t3_graph, game_bn_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_bn_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t3 = create_team_graph(s2_t3_graph, df)
# ev_s2_t3 = label_seasons_ev(ev_s2_t3, 'Season_2')

# add_player_names(s2_t4_graph, game_dm_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_dm_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t4 = create_team_graph(s2_t4_graph, df)
# ev_s2_t4 = label_seasons_ev(ev_s2_t4, 'Season_2')

# add_player_names(s2_t5_graph, game_hr_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_hr_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t5 = create_team_graph(s2_t5_graph, df)
# ev_s2_t5 = label_seasons_ev(ev_s2_t5, 'Season_2')

# add_player_names(s2_t6_graph, game_cc_s2_rev.get_data_frames()[0]['PASS_FROM'])
# df = game_cc_s2_rev.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t6 = create_team_graph(s2_t6_graph, df)
# ev_s2_t6 = label_seasons_ev(ev_s2_t6, 'Season_2')

# add_player_names(s2_t7_graph, game_lkr_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_lkr_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t7 = create_team_graph(s2_t7_graph, df)
# ev_s2_t7 = label_seasons_ev(ev_s2_t7, 'Season_2')

# add_player_names(s2_t8_graph, game_mb_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_mb_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t8 = create_team_graph(s2_t8_graph, df)
# ev_s2_t8 = label_seasons_ev(ev_s2_t8, 'Season_2')

# add_player_names(s2_t9_graph, game_lac_s2.get_data_frames()[0]['PASS_FROM'])
# df = game_lac_s2.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s2_t9 = create_team_graph(s2_t9_graph, df)
# ev_s2_t9 = label_seasons_ev(ev_s2_t9, 'Season_2')

time.sleep(2)
# Season 3
add_player_names(s3_graph, game_ah_s3.get_data_frames()[0]['PASS_FROM'])
df = game_ah_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
ev_s3 = create_team_graph(s3_graph, df)
ev_s3 = label_seasons_ev(ev_s3, 'Season_3')

# add_player_names(s3_t2_graph, game_bc_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_bc_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t2 = create_team_graph(s3_t2_graph, df)
# ev_s3_t2 = label_seasons_ev(ev_s3_t2, 'Season_3')

# add_player_names(s3_t3_graph, game_bn_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_bn_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t3 = create_team_graph(s3_t3_graph, df)
# ev_s3_t3 = label_seasons_ev(ev_s3_t3, 'Season_3')

# add_player_names(s3_t4_graph, game_dm_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_dm_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t4 = create_team_graph(s3_t4_graph, df)
# ev_s3_t4 = label_seasons_ev(ev_s3_t4, 'Season_3')

# add_player_names(s3_t5_graph, game_hr_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_hr_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t5 = create_team_graph(s3_t5_graph, df)
# ev_s3_t5 = label_seasons_ev(ev_s3_t5, 'Season_3')

# add_player_names(s3_t6_graph, game_hr_s3_rev.get_data_frames()[0]['PASS_FROM'])
# df = game_hr_s3_rev.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t6 = create_team_graph(s3_t6_graph, df)
# ev_s3_t6 = label_seasons_ev(ev_s3_t6, 'Season_3')

# add_player_names(s3_t7_graph, game_lkr_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_lkr_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t7 = create_team_graph(s3_t7_graph, df)
# ev_s3_t7 = label_seasons_ev(ev_s3_t7, 'Season_3')

# add_player_names(s3_t8_graph, game_mb_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_mb_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t8 = create_team_graph(s3_t8_graph, df)
# ev_s3_t8 = label_seasons_ev(ev_s3_t8, 'Season_3')

# add_player_names(s3_t9_graph, game_lac_s3.get_data_frames()[0]['PASS_FROM'])
# df = game_lac_s3.get_data_frames()[0][['PASS_FROM', 'PASS']]
# ev_s3_t9 = create_team_graph(s3_t9_graph, df)
# ev_s3_t9 = label_seasons_ev(ev_s3_t9, 'Season_3')

# All Seasons Eigenvector List
ev = ev_s1 + ev_s2 + ev_s3 
print(len(ev)) 

players_graph = nx.Graph()

for t in ev:
    players_graph.add_node(t)

pos = nx.spring_layout(players_graph)

for name, value, season in players_graph.nodes():
    for n, v, s in players_graph.nodes(): 
        if (name == n and not (value== v)):
            players_graph.add_edge((name, value, season), (n, v, s))

# Remove node if doesnt have an edge
nodes_with_edges = []
nodes_without_edges = []
edge_list = []
for e in players_graph.edges():
    nodes_with_edges.append(e[0][0])
    edge_list.append(e[0])
    edge_list.append(e[1])

for n in players_graph.nodes():
    if (not (n[0] in nodes_with_edges)):
        nodes_without_edges.append(n)

players_graph.remove_nodes_from(nodes_without_edges)

plot_allPlayers(edge_list ,players_graph.edges)
