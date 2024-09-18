import pandas as pd
from pyvis.network import Network
from auxilio import grafo_cidades_auxilio
from cidades import grafo_cidades_campus
from transporte import grafo_cidades_transporte

df = pd.read_excel('Dados sobre transporte para o campus Camaçari (respostas).xlsx')

def gerar_grafo_interativo_combinado(G1, G2, G3, titulo, arquivo_html):
    net = Network(height='750px', width='100%', bgcolor='#ffffff', font_color='black', directed=True)
    net.set_edge_smooth('dynamic')

    added_nodes = set()  # Set para rastrear os nós já adicionados

    # Adicionar nós e arestas do Grafo 1 (Cidades-Campus)
    for node in G1.nodes:
        color = 'lightgreen' if G1.nodes[node].get('node_type') == 'campus' else 'lightblue'
        net.add_node(node, label=node, title=G1.nodes[node].get('node_type', 'Cidade'), color=color, size=20)
        added_nodes.add(node)

    for u, v, d in G1.edges(data=True):
        net.add_edge(u, v, title=f"Quantidade: {d['weight']}", value=d['weight'])

    # Adicionar nós e arestas do Grafo 2 (Cidades-Transportes)
    for node in G2.nodes:
        if node not in added_nodes:  # Verificar se o nó já foi adicionado
            color = 'orange' if G2.nodes[node].get('node_type') == 'transporte' else 'lightblue'
            net.add_node(node, label=node, title=G2.nodes[node].get('node_type', 'Cidade'), color=color, size=20)
            added_nodes.add(node)

    for u, v, d in G2.edges(data=True):
        net.add_edge(u, v, title=f"Quantidade: {d['weight']}", value=d['weight'])

    # Adicionar nós e arestas do Grafo 3 (Cidades-Auxílio)
    for node in G3.nodes:
        if node not in added_nodes:  # Verificar se o nó já foi adicionado
            node_type = G3.nodes[node].get('node_type', '')
            color = 'brown' if node_type == 'auxilio' else 'orange'  # Padronizando para orange
            net.add_node(node, label=node, title=node_type, color=color, size=20)
            added_nodes.add(node)

    for u, v, d in G3.edges(data=True):
        net.add_edge(u, v, title=f"Quantidade: {d['weight']}", value=d['weight'])

    # Adicionar o Campus IFBA como nó central
    if "Campus IFBA Camaçari" not in added_nodes:
        net.add_node("Campus IFBA Camaçari", label="Campus IFBA Camaçari", shape='box', color='lightgreen', size=30)

    # Configurar título e gerar HTML
    net.show_buttons(filter_=['physics'])
    net.force_atlas_2based()
    net.save_graph(arquivo_html)
    print(f'Grafo interativo salvo como {arquivo_html}')

    # Adicionar legenda ao HTML
    adicionar_legenda_ao_html(arquivo_html)

# Função para adicionar a legenda manualmente ao HTML gerado
def adicionar_legenda_ao_html(arquivo_html):
    legenda_html = """
    <div style="position: absolute; top: 20px; right: 20px; background: white; border: 1px solid #ccc; padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
        <h3>Legenda</h3>
        <ul style="list-style-type: none; padding: 0;">
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightgreen; border-radius: 50%; margin-right: 5px;"></span> Campus</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: lightblue; border-radius: 50%; margin-right: 5px;"></span> Cidades</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: orange; border-radius: 50%; margin-right: 5px;"></span> Meios de Transporte</li>
            <li><span style="display: inline-block; width: 15px; height: 15px; background: brown; border-radius: 50%; margin-right: 5px;"></span> Auxílio</li>
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

def adicionar_filtros_ao_html(arquivo_html):
    filtros_html = """
    <div style="position: absolute; top: 20px; left: 20px; background: white; border: 1px solid #ccc; padding: 10px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.3);">
        <label for="graphFilter">Selecione o grafo:</label>
        <select id="graphFilter" onchange="filterGraph()">
            <option value="todos">Todos</option>
            <option value="campus">Campus</option>
            <option value="transporte">Transporte</option>
            <option value="auxilio">Auxílio</option>
        </select>
    </div>

    <script type="text/javascript">
        function filterGraph() {
            var filter = document.getElementById("graphFilter").value;
            var nodes = document.querySelectorAll("[title]");

            // Mostrar todos os nós
            nodes.forEach(function(node) {
                node.style.display = "block";
            });

            // Aplicar filtros
            if (filter !== "todos") {
                nodes.forEach(function(node) {
                    var nodeType = node.getAttribute("title");

                    // Esconder nós que não correspondem ao filtro
                    if (filter === "campus" && nodeType !== "Campus") {
                        node.style.display = "none";
                    } else if (filter === "transporte" && nodeType !== "Transporte") {
                        node.style.display = "none";
                    } else if (filter === "auxilio" && nodeType !== "Auxílio") {
                        node.style.display = "none";
                    }
                });
            }
        }
    </script>
    """

    # Ler o conteúdo existente do arquivo HTML
    with open(arquivo_html, 'r', encoding='utf-8') as file:
        conteudo_html = file.read()

    # Adicionar os filtros antes do fechamento da tag </body>
    conteudo_html = conteudo_html.replace('</body>', filtros_html + '</body>')

    # Escrever o novo conteúdo de volta ao arquivo com a codificação correta
    with open(arquivo_html, 'w', encoding='utf-8') as file:
        file.write(conteudo_html)
