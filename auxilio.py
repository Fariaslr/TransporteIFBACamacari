import networkx as nx
import pandas as pd

# Função para gerar o grafo de auxílios recebidos
def grafo_cidades_auxilio(df):
    G = nx.DiGraph()  # Usar grafo direcionado

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
        auxilio = row['🩼 Você recebe algum auxílio?']

        if cidade and pd.notna(auxilio):
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade', frequency=0)
            if not G.has_node(auxilio):
                G.add_node(auxilio, node_type='auxilio', frequency=0)

            # Ajustar o direcionamento das arestas para que auxilio aponte para cidade
            if G.has_edge(auxilio, cidade):
                G[auxilio][cidade]['weight'] += 1
            else:
                G.add_edge(auxilio, cidade, weight=1)

            G.nodes[cidade]['frequency'] += 1
            G.nodes[auxilio]['frequency'] += 1

    return G



