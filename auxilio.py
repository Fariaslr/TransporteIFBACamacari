import networkx as nx
import pandas as pd

# Função para gerar o grafo de auxílios recebidos
def grafo_cidades_auxilio(df):
    G = nx.Graph()  # Usar grafo direcionado

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
        auxilio = row['🩼 Você recebe algum auxílio?']

        if cidade and pd.notna(auxilio):
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade', frequency=0)

            # Adicionar "Sim" ou "Não" como um nó
            if auxilio == "Sim":
                auxilio_node = "Sim"
            elif auxilio == "Não":
                auxilio_node = "Não"
            else:
                continue  # Ignorar se não for "Sim" ou "Não"

            if not G.has_node(auxilio_node):
                G.add_node(auxilio_node, node_type='auxilio', frequency=0)

            # Ajustar o direcionamento das arestas para que auxilio aponte para cidade
            if G.has_edge(auxilio_node, cidade):
                G[auxilio_node][cidade]['weight'] += 1
            else:
                G.add_edge(auxilio_node, cidade, weight=1)

            G.nodes[cidade]['frequency'] += 1
            G.nodes[auxilio_node]['frequency'] += 1

    return G



