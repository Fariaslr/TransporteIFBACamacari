import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')
G = nx.Graph()


for index, row in df.iterrows():
    cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
    auxilio = row['🩼 Você recebe algum auxílio?']

    if cidade and auxilio:
        if not G.has_node(cidade):
            G.add_node(cidade)
        if not G.has_node(auxilio):
            G.add_node(auxilio)

        G.add_edge(cidade, auxilio)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title('Relações entre cidades/distritos e tipos de auxílio')
plt.show()
