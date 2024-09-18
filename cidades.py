import networkx as nx
import pandas as pd

# Função para gerar o grafo de cidades conectadas ao campus
def grafo_cidades_campus(df):
    G = nx.DiGraph()  # Usar grafo direcionado
    campus = 'Campus IFBA Camaçari'

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']

        if cidade:
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade')
            if not G.has_node(campus):
                G.add_node(campus, node_type='campus')

            if G.has_edge(campus, cidade):
                G[campus][cidade]['weight'] += 1
            else:
                G.add_edge(campus, cidade, weight=1)

    return G
