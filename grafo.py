import pandas as pd
import networkx as nx
from pyvis.network import Network

# Ler o arquivo Excel
df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

# Função para gerar o grafo interativo com Pyvis e salvar em HTML
def gerar_grafo_interativo_combinado(G1, G2, G3, titulo, arquivo_html):
    net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='black', directed=True)
    net.set_edge_smooth('dynamic')

    # Adicionar nós e arestas do Grafo 1
    for node in G1.nodes:
        if G1.nodes[node].get('node_type') == 'campus':
            color = 'lightgreen'
        else:
            color = 'lightblue'
        net.add_node(node, label=node, title=node, color=color, size=20)

    for u, v, d in G1.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    # Adicionar nós e arestas do Grafo 2
    for node in G2.nodes:
        if node not in net.nodes:
            if G2.nodes[node].get('node_type') == 'transporte':
                color = 'orange'
            else:
                color = 'lightblue'
            net.add_node(node, label=node, title=node, color=color, size=20)

    for u, v, d in G2.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    # Adicionar nós e arestas do Grafo 3
    for node in G3.nodes:
        if node not in net.nodes:
            node_type = G3.nodes[node].get('node_type', '')
            if node_type == 'auxilio':
                color = 'darkgreen'
            elif node_type == 'Não':
                color = 'brown'
            elif node_type == 'Sim':
                color = 'brown'
            else:
                color = 'lightblue'
            net.add_node(node, label=node, title=node, color=color, size=20)

    for u, v, d in G3.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    # Adicionar o IFBA como nó central
    if not net.get_node("Campus IFBA Camaçari"):
        net.add_node("Campus IFBA Camaçari", label="Campus IFBA Camaçari", shape='box', color='lightgreen', size=30)

    # Configurar título e gerar HTML
    net.show_buttons(filter_=['physics'])
    net.force_atlas_2based()
    net.save_graph(arquivo_html)
    print(f'Grafo interativo salvo como {arquivo_html}')

    # Adicionar legenda ao HTML
    adicionar_legenda_ao_html(arquivo_html)

def adicionar_legenda_ao_html(arquivo_html):
    legenda_html = """
    <div style="position: absolute; top: 20px; right: 20px; background: white; border: 1px solid #ccc; padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
        <h3>Legenda</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightgreen; border-radius: 50%; margin-right: 5px;"></span> Campus</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightblue; border-radius: 50%; margin-right: 5px;"></span> Cidades</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: orange; border-radius: 50%; margin-right: 5px;"></span> Meios de Transporte</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: brown; border-radius: 50%; margin-right: 5px;"></span> Auxilio</li>
        </ul>
    </div>
    """

    # Adicionar a legenda ao HTML
    with open(arquivo_html, 'r') as file:
        html_content = file.read()

    # Inserir a legenda antes do fechamento da tag </body>
    html_content = html_content.replace('</body>', legenda_html + '</body>')

    with open(arquivo_html, 'w') as file:
        file.write(html_content)

# Grafo 1: Cidades conectadas ao Campus IFBA Camaçari
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

# Grafo 2: Cidades conectadas a meios de transporte
def grafo_cidades_transporte(df):
    G = nx.DiGraph()  # Usar grafo direcionado

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
        transportes = row['🚋 Qual meio de transporte você utiliza para chegar ao campus?']

        if cidade and transportes:
            transportes_list = [t.strip() for t in transportes.split(',')]
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade')

            for transporte in transportes_list:
                if not G.has_node(transporte):
                    G.add_node(transporte, node_type='transporte')

                if G.has_edge(cidade, transporte):
                    G[cidade][transporte]['weight'] += 1
                else:
                    G.add_edge(cidade, transporte, weight=1)

    return G

# Grafo 3: Cidades conectadas a auxílios recebidos
def grafo_cidades_auxilio(df):
    G = nx.DiGraph()  # Usar grafo direcionado

    for index, row in df.iterrows():
        cidade = row['🏠 De qual cidade/distrito você sai para chegar ao campus?']
        auxilio = row['🩼 Você recebe algum auxílio?']

        if cidade and pd.notna(auxilio):
            if not G.has_node(cidade):
                G.add_node(cidade, node_type='cidade')
            if not G.has_node(auxilio):
                G.add_node(auxilio, node_type=auxilio)  # Aqui estamos usando o valor real

            if G.has_edge(cidade, auxilio):
                G[cidade][auxilio]['weight'] += 1
            else:
                G.add_edge(cidade, auxilio, weight=1)

    return G

# Execução dos três grafos e geração de um HTML combinado
G1 = grafo_cidades_campus(df)
G2 = grafo_cidades_transporte(df)
G3 = grafo_cidades_auxilio(df)

gerar_grafo_interativo_combinado(G1, G2, G3, 'Conexões entre cidades, transportes e auxílios',
                                 'grafos/grafo_combinado.html')
