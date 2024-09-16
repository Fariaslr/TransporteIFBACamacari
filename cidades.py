import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

G = nx.Graph()

for index, row in df.iterrows():
    cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
    campus = 'Campus IFBA Camaçari'

    if cidade and not G.has_node(cidade):
        G.add_node(cidade)
    if not G.has_node(campus):
        G.add_node(campus)

    if cidade:
        G.add_edge(cidade, campus)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title('Conexões entre cidades/distritos e o campus')
plt.show()