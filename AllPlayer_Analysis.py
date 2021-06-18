import time
import networkx as nx
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import teamplayerdashboard, teamdashptpass
from nba_api.stats.endpoints import playerdashptpass
from Graphing import create_team_graph, create_player_graph, plot, bar, append_df, df_pass_to, eigenvector 

def add_player_names (names):
    for name in names:
        Graph.add_node(name)

#atlanta hawks
ah_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612737", opponent_team_id="1610612744",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/02/2019", date_from_nullable="12/02/2019")
time.sleep(2)
#boston celtics
bc_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612738", opponent_team_id="1610612752",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12,01,2019")
time.sleep(2)
#Brooklyn nets
bn_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612751", opponent_team_id="1610612748",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12,01,2019")
time.sleep(2)
#charlotte hronets
ch_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612766", opponent_team_id="1610612756",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/02/2019", date_from_nullable="12/02/2019")
#chicago bulls
cb_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612741", opponent_team_id="1610612758",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/02/2019", date_from_nullable="12/02/2019")
time.sleep(2)
#cleveland cavaliers
cc_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612739", opponent_team_id="1610612765",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/03/2019", date_from_nullable="12/03/2019")
time.sleep(2)
#dallas mavericks
dm_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612739", opponent_team_id="1610612765",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/03/2019", date_from_nullable="12/03/2019")
#denver nuggets
dn_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612743", opponent_team_id="1610612755",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/10/2019", date_from_nullable="12/10/2019")
#houston rockets
hr_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612745", opponent_team_id="1610612761",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/05/2019", date_from_nullable="12/05/2019")
#indiana pacers
ip_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612754", opponent_team_id="1610612763",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/02/2019", date_from_nullable="12/02/2019")
#Los Angeles Clippers
lac_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612754", opponent_team_id="1610612764",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12/01/2019")
time.sleep(2)
#Milwaukee Bucks
mb_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612749", opponent_team_id="1610612753",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/09/2019", date_from_nullable="12/09/2019")
#pelicans
peli_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612740", opponent_team_id="1610612756",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/05/2019", date_from_nullable="12/05/2019")
#lakers
time.sleep(2)
lkr_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612747", opponent_team_id="1610612742",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/01/2019", date_from_nullable="12/01/2019")
#raptors
rptrs_2020 = teamdashptpass.TeamDashPtPass(team_id="1610612745", opponent_team_id="1610612761",  season="2019-20", season_type_all_star="Regular Season", date_to_nullable="12/05/2019", date_from_nullable="12/05/2019")


#Graph
Graph = nx.Graph()

time.sleep(2)

# Atlana Hawks
add_player_names(ah_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(bc_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(bn_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(ch_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(cb_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(cc_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(dm_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(dn_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(hr_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(lac_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(mb_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(peli_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(lkr_2020.get_data_frames()[0]['PASS_FROM'])
add_player_names(rptrs_2020.get_data_frames()[0]['PASS_FROM'])

time.sleep(2)

df = ah_2020.get_data_frames()[0][['PASS_FROM', 'PASS']]
df = append_df(bc_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(ch_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(cb_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(cc_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(dm_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(dn_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(hr_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(lac_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(mb_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(peli_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(lkr_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)
df = append_df(rptrs_2020.get_data_frames()[0][['PASS_FROM', 'PASS']], df)

Graph = create_team_graph(Graph, df)

# Eigenvector
eigenvector_list = eigenvector(Graph)
# print(eigenvector_list)
players = []

for p in eigenvector_list:
    if not (p[0] is 'PASS') and len(players) <= 20:
        players.append(p)

print(players)

# Plotting/Bar
plot(players)