import pandas as pd
from pyvis.network import Network
from auxilio import grafo_cidades_auxilio
from cidades import grafo_cidades_campus
from transporte import grafo_cidades_transporte

df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

def gerar_grafo_interativo_combinado(G1, G2, G3, titulo, arquivo_html):
    net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='black', directed=True)
    net.set_edge_smooth('dynamic')

    def get_node_size(frequency):
        # Ajuste o tamanho dos nós conforme necessário
        return max(15, frequency * 2)

    # Adicionar nós e arestas do Grafo 1
    for node in G1.nodes:
        if G1.nodes[node].get('node_type') == 'campus':
            color = 'lightgreen'
        else:
            color = 'lightblue'
        size = get_node_size(G1.nodes[node].get('frequency', 1))
        net.add_node(node, label=node, title=node, color=color, size=size)

    for u, v, d in G1.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    # Adicionar nós e arestas do Grafo 2
    for node in G2.nodes:
        if node not in net.nodes:
            if G2.nodes[node].get('node_type') == 'transporte':
                color = 'orange'
            else:
                color = 'lightblue'
            size = get_node_size(G2.nodes[node].get('frequency', 1))
            net.add_node(node, label=node, title=node, color=color, size=size)

    for u, v, d in G2.edges(data=True):
        net.add_edge(u, v, title=f"Frequência: {d['weight']}", value=d['weight'])

    # Adicionar nós e arestas do Grafo 3
    for node in G3.nodes:
        if node not in net.nodes:
            if G3.nodes[node].get('node_type') == 'auxilio':
                color = 'brown'
            elif G3.nodes[node].get('node_type') == 'Não':
                color = 'red'
            elif G3.nodes[node].get('node_type') == 'Sim':
                color = 'green'
            else:
                color = 'lightblue'
            size = get_node_size(G3.nodes[node].get('frequency', 1))
            net.add_node(node, label=node, title=node, color=color, size=size)

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

    adicionar_legenda_ao_html(arquivo_html)

# Função para adicionar a legenda manualmente ao HTML gerado
def adicionar_legenda_ao_html(arquivo_html):
    legenda_html = """
    <div style="position: absolute; top: 20px; right: 20px; background: white; border: 1px solid #ccc; padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
        <h3>Legenda</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightgreen; border-radius: 50%; margin-right: 5px;"></span> IFBA</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightblue; border-radius: 50%; margin-right: 5px;"></span> Minicípios</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: orange; border-radius: 50%; margin-right: 5px;"></span> Meios de transporte</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: brown; border-radius: 50%; margin-right: 5px;"></span> Auxílio transporte</li>
        </ul>
    </div>
    """

    # Ler o conteúdo existente do arquivo HTML
    with open(arquivo_html, 'r', encoding='utf-8') as file:
        conteudo_html = file.read()

    # Adicionar a legenda antes do fechamento da tag </body>
    conteudo_html = conteudo_html.replace('</body>', legenda_html + '</body>')

    # Escrever o novo conteúdo de volta ao arquivo com a codificação correta
    with open(arquivo_html, 'w', encoding='utf-8') as file:
        file.write(conteudo_html)

# Executar a geração dos grafos e o HTML combinado
if __name__ == '__main__':
    G1 = grafo_cidades_campus(df)
    G2 = grafo_cidades_transporte(df)
    G3 = grafo_cidades_auxilio(df)
    adicionar_legenda_ao_html('paginas/index.html')
    gerar_grafo_interativo_combinado(G1, G2, G3, 'Grafo de Conexões ao Campus', 'paginas/index.html')
