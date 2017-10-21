//Constants for the SVG
var width = 1000,
    height = 1000;

//Set up the colour scale
var color = d3.scaleOrdinal(d3.schemeCategory20);

//Set up the force layout
var force = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody().strength(-1))
    .force("center", d3.forceCenter(width / 2, height / 2));

//---Insert-------

    function dragstart(d, i) {
        force.stop() // stops the force auto positioning before you start dragging
    }

    function dragmove(d, i) {
        d.px += d3.event.dx;
        d.py += d3.event.dy;
        d.x += d3.event.dx;
        d.y += d3.event.dy;
    }

    function dragend(d, i) {
        d.fixed = true; // of course set the node to fixed so the force doesn't include the node in its auto positioning stuff
        force.resume();
    }

    function releasenode(d) {
        d.fixed = false; // of course set the node to fixed so the force doesn't include the node in its auto positioning stuff
        //force.resume();
    }

    var node_drag = d3.drag()
        .on("start", dragstart)
        .on("drag", dragmove)
        .on("end", dragend);


//---End Insert------

//Append a SVG to the body of the html page. Assign this SVG as an object to svg
var svg = d3.select("body").append("svg")
    .attr('id', 'd3_svg')
    .attr("width", width)
    .attr("height", height);

//Read the data from the appropriate json file
// var mis = document.getElementById('mis').innerHTML;
// var data =
function loadD3(path) {

    $('#input-json').attr('src', path)

    graph = JSON.parse();

    //Creates the graph data structure out of the json data
    force.nodes(graph.nodes)
        .links(graph.links)
        .start();

    //Create all the line svgs but without locations yet
    var link = svg.selectAll(".link")
        .data(graph.links)
        .enter().append("line")
        .attr("class", "link")
        .style("stroke-width", function (d) {
        return Math.sqrt(d.value);
    });

    //Do the same with the circles for the nodes - no
    var node = svg.selectAll(".node")
        .data(graph.nodes)
        .enter().append("circle")
        .attr("class", "node")
        .attr("r", 5)
        .style("fill", function (d) {
        return color(d.group);
    })
        .on('dblclick', releasenode)
        .call(node_drag); //Added

    // Adds title to each node
    node.append('title')
        .text(function(d) { return d.id; });



    //Now we are giving the SVGs co-ordinates - the force layout is generating the co-ordinates which this code is using to update the attributes of the SVG elements
    force.on("tick", function () {
        link.attr("x1", function (d) {
            return d.source.x;
        })
            .attr("y1", function (d) {
            return d.source.y;
        })
            .attr("x2", function (d) {
            return d.target.x;
        })
            .attr("y2", function (d) {
            return d.target.y;
        });

        node.attr("cx", function (d) {
            return d.x;
        })
            .attr("cy", function (d) {
            return d.y;
        });
    });

    force.restart();
};

loadD3('/static/genre_maps/10_plus.json')

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
          $('#d3_svg').empty()
          loadD3(data);
          $('#display').trigger('reset')
        });
    });