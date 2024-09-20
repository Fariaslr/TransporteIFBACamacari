import networkx as nx
import pandas as pd

# Função para gerar o grafo de cidades conectadas a meios de transporte
def grafo_cidades_transporte(df):
    G = nx.Graph()  # Usar grafo não direcionado

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
        transportes = row['🚋 Qual meio de transporte você utiliza para chegar ao campus?']

        if cidade and transportes:
            transportes_list = [t.strip() for t in transportes.split(',')]
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade', frequency=0)

            for transporte in transportes_list:
                if not G.has_node(transporte):
                    G.add_node(transporte, node_type='transporte', frequency=0)

                if G.has_edge(cidade, transporte):
                    G[cidade][transporte]['weight'] += 1
                else:
                    G.add_edge(cidade, transporte, weight=1)

                G.nodes[cidade]['frequency'] += 1
                G.nodes[transporte]['frequency'] += 1

    return G


