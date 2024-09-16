import pandas as pd
import networkx as nx
from pyvis.network import Network

# Ler o arquivo Excel
df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

# Selecionar um subconjunto de 47 registros
df_subset = df.head(47)

# Criar o grafo com NetworkX
G_subset = nx.Graph()

# Adicionar nós e arestas com base no subconjunto de dados
for index, row in df_subset.iterrows():
    cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
    auxilio = row['🩼 Você recebe algum auxílio?']

    if pd.notna(cidade) and pd.notna(auxilio):
        if not G_subset.has_node(cidade):
            G_subset.add_node(cidade, node_type='cidade')
        if not G_subset.has_node(auxilio):
            G_subset.add_node(auxilio, node_type='auxilio')

        if G_subset.has_edge(cidade, auxilio):
            G_subset[cidade][auxilio]['weight'] += 1
        else:
            G_subset.add_edge(cidade, auxilio, weight=1)

# Criar o grafo com Pyvis
net_subset = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='black', notebook=False, cdn_resources='remote')

# Adicionar nós ao Pyvis Network
for node in G_subset.nodes:
    node_type = G_subset.nodes[node].get('node_type', 'default')
    color = 'skyblue' if node_type == 'cidade' else 'lightgreen'
    net_subset.add_node(node, color=color, size=20, label=node)

# Adicionar arestas ao Pyvis Network
for u, v, d in G_subset.edges(data=True):
    net_subset.add_edge(u, v, width=d['weight'], title=f"Weight: {d['weight']}")

# Gerar o HTML para o grafo
grafo_html_subset = 'grafos/grafo_auxilio.html'
try:
    net_subset.save_graph(grafo_html_subset)
    print(f"Grafo interativo salvo no arquivo: {grafo_html_subset}")
except Exception as e:
    print(f"Erro ao gerar o HTML: {e}")
