import pandas as pd
import networkx as nx
from pyvis.network import Network

# Ler o arquivo Excel
df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

# Criar o grafo com NetworkX
G = nx.Graph()

# Adicionar nós e arestas, tratando listas de meios de transporte
for index, row in df.iterrows():
    cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
    transportes = row['🚋 Qual meio de transporte você utiliza para chegar ao campus?']

    if cidade and transportes:
        # Dividir a lista de meios de transporte
        transportes_list = [t.strip() for t in transportes.split(',')]

        # Adicionar arestas entre a cidade e cada meio de transporte
        for transporte in transportes_list:
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade')
            if not G.has_node(transporte):
                G.add_node(transporte, node_type='transporte')

            if G.has_edge(cidade, transporte):
                G[cidade][transporte]['weight'] += 1
            else:
                G.add_edge(cidade, transporte, weight=1)

# Criar o grafo com Pyvis
net = Network(notebook=True)

# Adicionar nós ao Pyvis Network
for node in G.nodes:
    node_type = G.nodes[node].get('node_type', 'default')
    color = 'skyblue' if node_type == 'cidade' else 'lightgreen'
    net.add_node(node, color=color, size=20, label=node)

# Adicionar arestas ao Pyvis Network
for u, v, d in G.edges(data=True):
    net.add_edge(u, v, width=d['weight'], title=f"Weight: {d['weight']}")

# Exibir o grafo interativo
net.show('grafos/grafo_transporte.html')
