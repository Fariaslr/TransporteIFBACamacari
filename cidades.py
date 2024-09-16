import pandas as pd
import networkx as nx
from pyvis.network import Network

# Ler o arquivo Excel
df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

# Criar o grafo com NetworkX
G = nx.Graph()

# Contar as respostas por cidade
cidade_counts = df['🏠 De qual cidade/distrito você sai para chegar ao campus?'].value_counts()

# Adicionar nós e arestas com base nos dados
for index, row in df.iterrows():
    cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
    transportes = row['🚋 Qual meio de transporte você utiliza para chegar ao campus?']

    if cidade and transportes:
        # Dividir a lista de meios de transporte
        transportes_list = [t.strip() for t in transportes.split(',')]

        for transporte in transportes_list:
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade')
            if not G.has_node(transporte):
                G.add_node(transporte, node_type='transporte')

            # Ajustar a espessura da aresta com base na quantidade de respostas
            weight = int(cidade_counts[cidade]) if cidade in cidade_counts else 1

            if G.has_edge(cidade, transporte):
                G[cidade][transporte]['weight'] += weight
            else:
                G.add_edge(cidade, transporte, weight=weight)

# Criar o grafo interativo com Pyvis
net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='black', notebook=False, cdn_resources='remote')

# Adicionar nós ao Pyvis Network
for node in G.nodes:
    node_type = G.nodes[node].get('node_type', 'default')
    color = 'skyblue' if node_type == 'cidade' else 'lightgreen'
    net.add_node(node, color=color, size=20, label=node)

# Adicionar arestas ao Pyvis Network com espessura proporcional
for u, v, d in G.edges(data=True):
    net.add_edge(u, v, width=int(d['weight']))  # Converter weight para int

# Gerar o HTML para o grafo interativo
grafo_html = 'grafos/grafo_cidades.html'
try:
    net.save_graph(grafo_html)
    print(f"Grafo interativo salvo no arquivo: {grafo_html}")
except Exception as e:
    print(f"Erro ao gerar o HTML: {e}")
