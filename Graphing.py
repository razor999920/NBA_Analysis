import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict

from networkx.algorithms.shortest_paths import weighted
from networkx.classes.function import edges


def create_graph(G, passes, reb_edge_list, ast_edge_list, fp_edge_list, tov_edge_list, stl_edge_list):
    # Adding addtioanl nodes
    fg = 'Field Goals'
    fga = 'Field Goals Attempted'
    reb_node = 'Rebound'
    ast_node = 'Assist'
    tov = 'Turnover'
    steal = 'Steal'

    # G.add_node(fg)
    # G.add_node(fga)
    # G.add_node(tov)
    # G.add_node(reb_node)
    # G.add_node(ast_node)
    # G.add_node(steal)

    # Adding player edges
    weight = []
    pos = nx.spring_layout(G)

    for x in passes.iterrows():
        value = x[1][2]
        if (',' in x[1][0]):
            from_player = swap_name(x[1][0])
        else:
            from_player = x[1][0]
        if (',' in x[1][1]):
            to_player = swap_name(x[1][1])
        else:
            to_player = x[1][1]

        if (G.has_edge(from_player, to_player)):
            edge_data = G.get_edge_data(from_player, to_player)
            value = value + edge_data[' ']

        G.add_edge(from_player, to_player, weight=value)

    # # Rebound Edges
    # for edge in reb_edge_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, reb_node, weight=edge[1][1])

    # # Assist Edges
    # for edge in ast_edge_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, ast_node, weight=edge[1][1])

    # # Field Point edges
    # for edge in fp_edge_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, fg, weight=edge[1][1])
    #     G.add_edge(player_node, fga, weight=edge[1][2])

    # # Turnover
    # for edge in tov_edge_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, tov, weight=edge[1][1])

    # # Steal
    # for edge in stl_edge_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, steal, weight=edge[1][1])

    # Edges and their weight
    dict = nx.get_edge_attributes(G, 'weight')
    # Adding the weight in dict
    for key, value in dict.items():
        weight.append(value)

    # Generating Graph
    nx.draw_networkx_nodes(G, pos, node_color="r", node_size=200)
    nx.draw_networkx_edges(G, pos, width=weight)
    nx.draw_networkx_labels(G, pos, font_size=15)
    # nx.draw_networkx_edge_labels(G, pos, font_size=10, edge_labels=dict)
    plt.show()

    return G


def plot(list):
    names = player_values_from_list(list, 0)
    values = player_values_from_list(list, 1)

    fig, ax = plt.subplots(figsize=(16, 6))
    # x = np.linspace(0, 10, 1000)
    # ax.plot(names, values, 'o', color='red', linestyle='solid')
    ax.plot(names, values, 'o', color='red')
    plt.xlabel("players")
    plt.ylabel("Eigenvector Values")
    plt.title("Player Progression")
    plt.show()


def plot_allPlayers(edges, edge_connection):
    player_name = player_values_from_list(edges, 0)
    season = player_values_from_list(edges, 2)
    values = player_values_from_list(edges, 1)

    fig, ax = plt.subplots(figsize=(16, 6))
    ax.scatter(season, values)
    # Label points
    for i, txt in enumerate(player_name):
        ax.annotate(txt, (season[i], values[i]))
    # Add edges
    has_edge = True

    for x in edge_connection: 
        x1, x2 = x[0][2], x[1][2]
        y1, y2 = x[0][1], x[1][1]

        if (x1 == 'Season_1' and x2 == 'Season_3'):
            for e in edges:
                if (e[0] == x[0][0] and (not (e[1] == x[0][1])) and e[2] == 'Season_2'):
                    print(e[2])
                    has_edge = False
            
        if (has_edge == True):
            plt.plot([x1, x2], [y1, y2], 'k-')

        has_edge = True

    plt.xlabel("players")
    plt.ylabel("Eigenvector Values")
    plt.title("Player Progression")
    plt.show()


def bar(list):
    names = player_values_from_list(list, 0)
    values = player_values_from_list(list, 1)

    fig = plt.figure(figsize=(20, 5))
    plt.bar(names, values)
    plt.xlabel("Players")
    plt.ylabel("Eigenvector Values")
    plt.title("Assist")
    plt.show()


def player_values_from_list(eigenvector, element):
    list = []
    for e in eigenvector:
        list.append(e[element])
    return list

def get_edges_data(edges, season_index, index):
    list = []
    for x in edges:
        list.append(x[season_index][index])
    return list

def swap_name(name):
    space = name.index(' ') + 1

    first_name = name[space: len(name)]
    last_name = name[0: space - 2]
    full_name = (first_name + " " + last_name)
    return full_name


def eigenvector(G):
    centrality = nx.eigenvector_centrality(G, max_iter=2000, weight='weight')
    return sorted(centrality.items(), key=lambda v: v[1], reverse=True)


def edge_betweenness(G):
    betweenness = OrderedDict(sorted(nx.edge_betweenness_centrality(
        G).items(), key=lambda kv: kv[0][1], reverse=True))
    betweenness_list = []
    for K, V in betweenness.items():
        if (len(betweenness_list) < 25):
            element = (K, V)
            betweenness_list.append(element)

    return betweenness_list


def append_df(df, player):
    for x in player.iterrows():
        df = df.append(x[1])
    return df


def df_pass_to(series):
    return series.get_data_frames()[0][['PLAYER_NAME_LAST_FIRST', 'PASS_TO', 'PASS']]


def df_pass_from(series):
    return series.get_data_frames()[1][['PLAYER_NAME_LAST_FIRST', 'PASS_FROM', 'PASS']]


def create_player_graph(G, passes):
    # Adding player edges
    for x in passes.iterrows():
        value = x[1][2]
        if (',' in x[1][0]):
            from_player = swap_name(x[1][0])
        else:
            from_player = x[1][0]
        if (',' in x[1][1]):
            to_player = swap_name(x[1][1])
        else:
            to_player = x[1][1]

        if (G.has_edge(from_player, to_player)):
            edge_data = G.get_edge_data(from_player, to_player)
            value = value + edge_data['weight']

        G.add_edge(from_player, to_player, weight=value)

    # Edges and their weight
    passes_dict = nx.get_edge_attributes(G, 'weight')
    names = []
    weight = []
    # Adding the weight in dict
    for key, value in passes_dict.items():
        names.append(key[1])
        weight.append(value)

    # fig = plt.figure(figsize=(18, 5))
    # plt.bar(names, weight)
    # plt.xlabel("Players")
    # plt.ylabel("Eigenvector Values")
    # plt.title("Passes From Andre Iguodala")
    # plt.show()

    # # Assist Edges
    # for edge in assist_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, 'Assist', weight=edge[1][1])

    # # Field Point edges
    # for edge in fp_list.iterrows():
    #     player_node = edge[1][0]
    #     G.add_edge(player_node, 'Field Points', weight=edge[1][1])
    #     # G.add_edge(player_node, 'Field Points', weight=edge[1][2])

    
    return G


def create_team_graph(G, passes):
    # print(passes)
    # print('\n')

    pass_node = 'PASS'
    G.add_node(pass_node)
    
    # Adding player edges
    for x in passes.iterrows():
        player = x[1][0]
        value = x[1][1]
        G.add_edge(player, pass_node, weight=value)
        
    # Edges and their weight
    passes_dict = nx.get_edge_attributes(G, 'weight')
    names = []
    weight = []
    # Adding the weight in dict
    for key, value in passes_dict.items():
        names.append(key[1])
        weight.append(value)

    eigenvector_list = eigenvector(G)
    eigenvector_list.pop(0)

    return eigenvector_list
    # return G
