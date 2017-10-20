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
        .attr("class", "links")
      .selectAll("line")
      .data(graph.links)
      .enter().append("line")
        .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

    var node = svg.append("g")
        .attr("class", "nodes")
      .selectAll("circle")
      .data(graph.nodes)
      .enter().append("circle")
      .attr("r", 5)
      .attr("fill", function(d) { return color(d.group); })
      // new drag
      // .on('dblclick', releasenode)
      //   .call(node_drag)

      // Original drag
      // .call(d3.drag()
      //     .on("start", dragstarted)
      //     .on("drag", dragged)
      //     .on("end", dragended));

      // New drag


      // Node highlighting
      // .call(force.drag()
      //     .on('dblclick', connectedNodes));

    node.append("title")
        .text(function(d) { return d.id; });

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

    // fisheye feature
    // var fisheye = d3.fisheye.circular()
    //       .radius(120);
    // svg.on("mousemove", function() {
    //       simulation.stop();
    //       fisheye.focus(d3.mouse(this));
    //       d3.selectAll("circle").each(function(d) { d.fisheye = fisheye(d); })
    //           .attr("cx", function(d) { return d.fisheye.x; })
    //           .attr("cy", function(d) { return d.fisheye.y; })
    //           .attr("r", function(d) { return d.fisheye.z * 8; });
    //       link.attr("x1", function(d) { return d.source.fisheye.x; })
    //           .attr("y1", function(d) { return d.source.fisheye.y; })
    //           .attr("x2", function(d) { return d.target.fisheye.x; })
    //           .attr("y2", function(d) { return d.target.fisheye.y; });
    //     });

    // //Toggle stores whether the highlighting is on
    // var toggle = 0;
    // //Create an array logging what is connected to what
    // var linkedByIndex = {};
    // for (i = 0; i < graph.nodes.length; i++) {
    //     linkedByIndex[i + "," + i] = 1;
    // };
    // graph.links.forEach(function (d) {
    //     linkedByIndex[d.source.index + "," + d.target.index] = 1;
    // });
    // //This function looks up whether a pair are neighbours
    // function neighboring(a, b) {
    //     return linkedByIndex[a.index + "," + b.index];
    // }
    // function connectedNodes() {
    //     if (toggle == 0) {
    //         //Reduce the opacity of all but the neighbouring nodes
    //         d = d3.select(this).node().__data__;
    //         node.style("opacity", function (o) {
    //             return neighboring(d, o) | neighboring(o, d) ? 1 : 0.1;
    //         });
    //         link.style("opacity", function (o) {
    //             return d.index==o.source.index | d.index==o.target.index ? 1 : 0.1;
    //         });
    //         //Reduce the op
    //         toggle = 1;
    //     } else {
    //         //Put them back to opacity=1
    //         node.style("opacity", 1);
    //         link.style("opacity", 1);
    //         toggle = 0;
    //     }
    // }

    // node search on click
    // var optArray = [];
    // for (var i = 0; i < graph.nodes.length - 1; i++) {
    //     optArray.push(graph.nodes[i].id);
    // }
    // optArray = optArray.sort();
    // $(function () {
    //     $("#search").autocomplete({
    //         source: optArray
    //     });
    // });
    // function searchNode() {
    //     //find the node
    //     var selectedVal = document.getElementById('search').value;
    //     var node = svg.selectAll(".node");
    //     if (selectedVal == "none") {
    //         node.style("stroke", "white").style("stroke-width", "1");
    //     } else {
    //         var selected = node.filter(function (d, i) {
    //             return d.id != selectedVal;
    //         });
    //         selected.style("opacity", "0");
    //         var link = svg.selectAll(".link")
    //         link.style("opacity", "0");
    //         d3.selectAll(".node, .link").transition()
    //             .duration(5000)
    //             .style("opacity", 1);
    //     }
    // }

    // $('#search-button').on('click', searchNode)

    simulation.restart();
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


// original drag functions
// function dragstarted(d) {
//   if (!d3.event.active) simulation.alphaTarget(0.3).restart();
//   console.log(d.id)
//   d.fx = d.x;
//   d.fy = d.y;
// }

// function dragged(d) {
//   d.fx = d3.event.x;
//   d.fy = d3.event.y;
// }

// function dragended(d) {
//   if (!d3.event.active) simulation.alphaTarget(0);
//   d.fx = null;
//   d.fy = null;
// }

