import networkx as nx
import pandas as pd

# Função para gerar o grafo de cidades conectadas ao campus
def grafo_cidades_campus(df):
    G = nx.Graph()  # Usar grafo direcionado
    campus = 'Campus IFBA Camaçari'

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']

        if cidade:
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade', frequency=0)
            if not G.has_node(campus):
                G.add_node(campus, node_type='campus', frequency=0)

            if G.has_edge(campus, cidade):
                G[campus][cidade]['weight'] += 1
            else:
                G.add_edge(campus, cidade, weight=1)

            G.nodes[cidade]['frequency'] += 1
            G.nodes[campus]['frequency'] += 1

    return G
