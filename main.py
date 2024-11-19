import pandas as pd
from pyvis.network import Network
from auxilio import grafo_cidades_auxilio
from cidades import grafo_cidades_campus
from transporte import grafo_cidades_transporte

df = pd.read_excel('Dados.xlsx')

def gerar_grafo_interativo_combinado(G1, G2, G3, titulo, arquivo_html):
    net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='black', directed=False)
    net.set_edge_smooth('dynamic')

    def get_node_size(frequency):
        return max(15, frequency * 2)

    for node in G1.nodes:
        color = 'lightgreen' if G1.nodes[node].get('node_type') == 'campus' else 'lightblue'
        size = get_node_size(G1.nodes[node].get('frequency', 1))
        net.add_node(node, label=node, title=node, color=color, size=size)

    for u, v, d in G1.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    for node in G2.nodes:
        if node not in net.nodes:
            color = 'orange' if G2.nodes[node].get('node_type') == 'transporte' else 'lightblue'
            size = get_node_size(G2.nodes[node].get('frequency', 1))
            net.add_node(node, label=node, title=node, color=color, size=size)

    for u, v, d in G2.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    for node in G3.nodes:
        if node not in net.nodes:
            node_type = G3.nodes[node].get('node_type', '')
            if node == 'Sim':
                color = 'brown'   
            elif node == 'Não':
                color = 'SlateBlue' 
            elif node_type == 'cidade':
                color = 'lightblue'  
            else:
                color = 'lightblue'  
            size = get_node_size(G3.nodes[node].get('frequency', 1))
            net.add_node(node, label=node, title=node, color=color, size=size)

    for u, v, d in G3.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    if not net.get_node("Campus IFBA Camaçari"):
        net.add_node("Campus IFBA Camaçari", label="Campus IFBA Camaçari", shape='box', color='lightgreen', size=30)

    net.show_buttons(filter_=['physics'])
    net.force_atlas_2based()
    net.save_graph(arquivo_html)
    print(f'Grafo interativo salvo como {arquivo_html}')

    adicionar_legenda_ao_html(arquivo_html)

def adicionar_legenda_ao_html(arquivo_html):
    legenda_html = """
    <div style="position: absolute; top: 20px; right: 20px; background: white; border: 1px solid #ccc; padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
        <h3>Legenda</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightgreen; border-radius: 50%; margin-right: 5px;"></span> IFBA</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightblue; border-radius: 50%; margin-right: 5px;"></span> Municípios</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: orange; border-radius: 50%; margin-right: 5px;"></span> Meios de transporte</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: brown; border-radius: 50%; margin-right: 5px;"></span> Com Auxílio transporte</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: SlateBlue; border-radius: 50%; margin-right: 5px;"></span> Sem Auxílio transporte</li>
        </ul>
    </div>
    """

    with open(arquivo_html, 'r', encoding='utf-8') as file:
        conteudo_html = file.read()

    conteudo_html = conteudo_html.replace('</body>', legenda_html + '</body>')

    with open(arquivo_html, 'w', encoding='utf-8') as file:
        file.write(conteudo_html)


if __name__ == '__main__':
    df = pd.read_excel('Dados.xlsx')
    G1 = grafo_cidades_campus(df)
    G2 = grafo_cidades_transporte(df)
    G3 = grafo_cidades_auxilio(df)
    gerar_grafo_interativo_combinado(G1, G2, G3, 'Grafo de Conexões ao Campus', 'site_gerado.html')
