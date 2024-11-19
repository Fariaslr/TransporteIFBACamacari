 // initialize global variables.
 var edges;
 var nodes;
 var allNodes;
 var allEdges;
 var nodeColors;
 var originalNodes;
 var network;
 var container;
 var filter = {
     item: '',
     property: '',
     value: []
 };


 // This method is responsible for drawing the graph, returns the drawn network
 function drawGraph() {
     var container = document.getElementById('mynetwork');

     nodes = new vis.DataSet([{
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Cama\u00e7ari (Sede)",
         "label": "Cama\u00e7ari (Sede)",
         "shape": "dot",
         "size": 38,
         "title": "Cama\u00e7ari (Sede)"
     }, {
         "color": "lightgreen",
         "font": {
             "color": "black"
         },
         "id": "Campus IFBA Cama\u00e7ari",
         "label": "Campus IFBA Cama\u00e7ari",
         "shape": "dot",
         "size": 94,
         "title": "Campus IFBA Cama\u00e7ari"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Salvador",
         "label": "Salvador",
         "shape": "dot",
         "size": 26,
         "title": "Salvador"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Mata de S\u00e3o Jo\u00e3o",
         "label": "Mata de S\u00e3o Jo\u00e3o",
         "shape": "dot",
         "size": 15,
         "title": "Mata de S\u00e3o Jo\u00e3o"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Dias D\u0027\u00c1vila",
         "label": "Dias D\u0027\u00c1vila",
         "shape": "dot",
         "size": 15,
         "title": "Dias D\u0027\u00c1vila"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Abrantes",
         "label": "Abrantes",
         "shape": "dot",
         "size": 15,
         "title": "Abrantes"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Parafuso",
         "label": "Parafuso",
         "shape": "dot",
         "size": 15,
         "title": "Parafuso"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Arembepe",
         "label": "Arembepe",
         "shape": "dot",
         "size": 15,
         "title": "Arembepe"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Sim\u00f5es Filho",
         "label": "Sim\u00f5es Filho",
         "shape": "dot",
         "size": 15,
         "title": "Sim\u00f5es Filho"
     }, {
         "color": "lightblue",
         "font": {
             "color": "black"
         },
         "id": "Pojuca",
         "label": "Pojuca",
         "shape": "dot",
         "size": 15,
         "title": "Pojuca"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Transporte p\u00fablico",
         "label": "Transporte p\u00fablico",
         "shape": "dot",
         "size": 58,
         "title": "Transporte p\u00fablico"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Transporte por aplicativo",
         "label": "Transporte por aplicativo",
         "shape": "dot",
         "size": 20,
         "title": "Transporte por aplicativo"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Ve\u00edculo pr\u00f3prio",
         "label": "Ve\u00edculo pr\u00f3prio",
         "shape": "dot",
         "size": 15,
         "title": "Ve\u00edculo pr\u00f3prio"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Transporte universit\u00e1rio",
         "label": "Transporte universit\u00e1rio",
         "shape": "dot",
         "size": 15,
         "title": "Transporte universit\u00e1rio"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Pego mais de duas op\u00e7\u00f5es; 2 onibus e um moto uber.",
         "label": "Pego mais de duas op\u00e7\u00f5es; 2 onibus e um moto uber.",
         "shape": "dot",
         "size": 15,
         "title": "Pego mais de duas op\u00e7\u00f5es; 2 onibus e um moto uber."
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Bicicleta",
         "label": "Bicicleta",
         "shape": "dot",
         "size": 15,
         "title": "Bicicleta"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Carona de amigou ou professores",
         "label": "Carona de amigou ou professores",
         "shape": "dot",
         "size": 15,
         "title": "Carona de amigou ou professores"
     }, {
         "color": "orange",
         "font": {
             "color": "black"
         },
         "id": "Caminhando",
         "label": "Caminhando",
         "shape": "dot",
         "size": 15,
         "title": "Caminhando"
     }, {
         "color": "brown",
         "font": {
             "color": "black"
         },
         "id": "Sim",
         "label": "Sim",
         "shape": "dot",
         "size": 36,
         "title": "Sim"
     }, {
         "color": "SlateBlue",
         "font": {
             "color": "black"
         },
         "id": "N\u00e3o",
         "label": "N\u00e3o",
         "shape": "dot",
         "size": 58,
         "title": "N\u00e3o"
     }]);

     edges = new vis.DataSet([{
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 19",
         "to": "Campus IFBA Cama\u00e7ari",
         "value": 19
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 13",
         "to": "Salvador",
         "value": 13
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 2",
         "to": "Mata de S\u00e3o Jo\u00e3o",
         "value": 2
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 6",
         "to": "Dias D\u0027\u00c1vila",
         "value": 6
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 2",
         "to": "Abrantes",
         "value": 2
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 1",
         "to": "Parafuso",
         "value": 1
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 2",
         "to": "Arembepe",
         "value": 2
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 1",
         "to": "Sim\u00f5es Filho",
         "value": 1
     }, {
         "from": "Campus IFBA Cama\u00e7ari",
         "title": "Frequ\u00eancia: 1",
         "to": "Pojuca",
         "value": 1
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 7",
         "to": "Transporte p\u00fablico",
         "value": 7
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 3",
         "to": "Ve\u00edculo pr\u00f3prio",
         "value": 3
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 7",
         "to": "Transporte por aplicativo",
         "value": 7
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 2",
         "to": "Bicicleta",
         "value": 2
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 3",
         "to": "Transporte universit\u00e1rio",
         "value": 3
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 4",
         "to": "Caminhando",
         "value": 4
     }, {
         "from": "Transporte p\u00fablico",
         "title": "Frequ\u00eancia: 12",
         "to": "Salvador",
         "value": 12
     }, {
         "from": "Transporte p\u00fablico",
         "title": "Frequ\u00eancia: 6",
         "to": "Dias D\u0027\u00c1vila",
         "value": 6
     }, {
         "from": "Transporte p\u00fablico",
         "title": "Frequ\u00eancia: 1",
         "to": "Abrantes",
         "value": 1
     }, {
         "from": "Transporte p\u00fablico",
         "title": "Frequ\u00eancia: 1",
         "to": "Parafuso",
         "value": 1
     }, {
         "from": "Transporte p\u00fablico",
         "title": "Frequ\u00eancia: 1",
         "to": "Pojuca",
         "value": 1
     }, {
         "from": "Transporte p\u00fablico",
         "title": "Frequ\u00eancia: 1",
         "to": "Arembepe",
         "value": 1
     }, {
         "from": "Salvador",
         "title": "Frequ\u00eancia: 1",
         "to": "Ve\u00edculo pr\u00f3prio",
         "value": 1
     }, {
         "from": "Salvador",
         "title": "Frequ\u00eancia: 1",
         "to": "Carona de amigou ou professores",
         "value": 1
     }, {
         "from": "Mata de S\u00e3o Jo\u00e3o",
         "title": "Frequ\u00eancia: 1",
         "to": "Transporte por aplicativo",
         "value": 1
     }, {
         "from": "Mata de S\u00e3o Jo\u00e3o",
         "title": "Frequ\u00eancia: 1",
         "to": "Pego mais de duas op\u00e7\u00f5es; 2 onibus e um moto uber.",
         "value": 1
     }, {
         "from": "Transporte por aplicativo",
         "title": "Frequ\u00eancia: 2",
         "to": "Dias D\u0027\u00c1vila",
         "value": 2
     }, {
         "from": "Abrantes",
         "title": "Frequ\u00eancia: 1",
         "to": "Transporte universit\u00e1rio",
         "value": 1
     }, {
         "from": "Arembepe",
         "title": "Frequ\u00eancia: 2",
         "to": "Transporte universit\u00e1rio",
         "value": 2
     }, {
         "from": "Transporte universit\u00e1rio",
         "title": "Frequ\u00eancia: 1",
         "to": "Sim\u00f5es Filho",
         "value": 1
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 9",
         "to": "Sim",
         "value": 9
     }, {
         "from": "Cama\u00e7ari (Sede)",
         "title": "Frequ\u00eancia: 10",
         "to": "N\u00e3o",
         "value": 10
     }, {
         "from": "Sim",
         "title": "Frequ\u00eancia: 5",
         "to": "Salvador",
         "value": 5
     }, {
         "from": "Sim",
         "title": "Frequ\u00eancia: 3",
         "to": "Dias D\u0027\u00c1vila",
         "value": 3
     }, {
         "from": "Sim",
         "title": "Frequ\u00eancia: 1",
         "to": "Pojuca",
         "value": 1
     }, {
         "from": "Salvador",
         "title": "Frequ\u00eancia: 8",
         "to": "N\u00e3o",
         "value": 8
     }, {
         "from": "Mata de S\u00e3o Jo\u00e3o",
         "title": "Frequ\u00eancia: 2",
         "to": "N\u00e3o",
         "value": 2
     }, {
         "from": "N\u00e3o",
         "title": "Frequ\u00eancia: 2",
         "to": "Abrantes",
         "value": 2
     }, {
         "from": "N\u00e3o",
         "title": "Frequ\u00eancia: 1",
         "to": "Parafuso",
         "value": 1
     }, {
         "from": "N\u00e3o",
         "title": "Frequ\u00eancia: 2",
         "to": "Arembepe",
         "value": 2
     }, {
         "from": "N\u00e3o",
         "title": "Frequ\u00eancia: 1",
         "to": "Sim\u00f5es Filho",
         "value": 1
     }, {
         "from": "N\u00e3o",
         "title": "Frequ\u00eancia: 3",
         "to": "Dias D\u0027\u00c1vila",
         "value": 3
     }]);


     nodeColors = {};
     allNodes = nodes.get({
         returnType: "Object"
     });
     for (nodeId in allNodes) {
         nodeColors[nodeId] = allNodes[nodeId].color;
     }
     allEdges = edges.get({
         returnType: "Object"
     });
     // adding nodes and edges to the graph
     data = {
         nodes: nodes,
         edges: edges
     };

     var options = {
         "configure": {
             "enabled": false,
             "filter": [
                 "physics"
             ]
         },
         "edges": {
             "color": {
                 "inherit": true
             },
             "smooth": {
                 "enabled": true,
                 "type": "dynamic"
             }
         },
         "interaction": {
             "dragNodes": true,
             "hideEdgesOnDrag": false,
             "hideNodesOnDrag": false
         },
         "physics": {
             "barnesHut": {
                 "gravitationalConstant": -26300,
                 "springLength": 45
             },
             "minVelocity": 0.75
         }

     };
     options.configure["container"] = document.getElementById("config");
     network = new vis.Network(container, data, options);
     return network;

 }
 drawGraph();