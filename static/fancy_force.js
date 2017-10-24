var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = d3.scaleOrdinal(d3.schemeCategory20);

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody().strength(-1))
    .force("center", d3.forceCenter(width / 2, height / 2));


function loadD3(path) {
  d3.json(path, function(error, graph) {
    if (error) throw error;

    var link = svg.append("g")
      .attr('transform', 'translate(450, 300)')
      .attr("class", "links")
      .selectAll("line")
      .data(graph.links)
      .enter().append("line")
        .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

    var node = svg.append("g")
      .attr('transform', 'translate(450, 300)')
      .attr("class", "nodes")
      .selectAll("circle")
      .data(graph.nodes)
      .enter().append("circle")
      .attr("r", 5)
      .attr("fill", function(d) { return color(d.group); })

    node.append("title")
        .text(function(d) { return d.id; });

    node.on('click', connectedNodes);
    node.on('dblclick', releasenode);
    
    var node_drag = d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended)

    node.call(node_drag);

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

    function ticked() {
      link
          .attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

      node
          .attr("cx", function(d) { return d.x; })
          .attr("cy", function(d) { return d.y; });

    }

    var toggle = 0;
    
    var linkedByIndex = {};
    for (i = 0; i < graph.nodes.length; i++) {
         linkedByIndex[i + "," + i] = 1;
    };
    graph.links.forEach(function (d) {
         linkedByIndex[d.source.index + "," + d.target.index] = 1;
     });
    
    function neighboring(a, b) {
         return linkedByIndex[a.index + "," + b.index];
    }
    function connectedNodes() {
         if (toggle == 0) {
    
            simulation.stop();
             d = d3.select(this).node().__data__;
             node.style("opacity", function (o) {
                 return neighboring(d, o) | neighboring(o, d) ? 1 : 0.1;
             });
             link.style("stroke-opacity", function (o) {
                 return d.index==o.source.index | d.index==o.target.index ? 1 : 0.1;
             });
    
             toggle = 1;
         } else {
    
             simulation.restart();
             node.style("opacity", 1);
             link.style("stroke-opacity", 1);
             toggle = 0;
         }
     }

    function dragstarted(d) {
      if (!d3.event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(d) {
      d.fx = d3.event.x;
      d.fy = d3.event.y;
    }

    function dragended(d) {
      if (!d3.event.active) simulation.alphaTarget(0);
    }

    function releasenode(d) {
      d.fx = null;
      d.fy = null;
    }

    simulation.restart();
    simulation.alpha(1);
  });
}

var path = '/static/genre_maps/10_plus.json';
loadD3(path);

$('#display').on('submit', function(evt) {

        evt.preventDefault();

        var features = {
          'a-level': $('#a-level').val(),
          'd-level': $('#d-level').val(),
          'e-level': $('#e-level').val(),
          'i-level': $('#i-level').val(),
          'l-level': $('#l-level').val(),
          'lo-level': $('#lo-level').val(),
          'm-level': $('#m-level').val(),
          's-level': $('#s-level').val(),
          't-level': $('#t-level').val(),
          'v-level': $('#v-level').val()
        };

        $.get('/features', features, function(data) {
          $('#svg').empty()
          loadD3(data);
          $('#display').trigger('reset')
        });
    });




$('#reset').on('click', function() {
  simulation.stop();
  simulation.restart();
  simulation.alpha(1);
})

