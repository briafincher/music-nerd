var ctx = $('#ctx')

var one = $('#related-one').data();
var two = $('#related-two').data();
var three = $('#related-three').data();
var four = $('#related-four').data();
var five = $('#related-five').data();

var allGenres = [one, two, three, four, five];
var genres = [];
for (var i = 0; i < allGenres.length; i++) {
    var genre = allGenres[i];
    if (genre.shared > 0) {
        genres.push(genre);
    }
}

var labelsList = [];
var dataList = [];

for (var i = 0; i < genres.length; i++) {
    var genre = genres[i];
    labelsList.push(genre.upper);
    dataList.push(genre.shared);
}

var relatedChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: labelsList,
        datasets: [{
            backgroundColor: '#3e95cd',
            data: dataList
        }]
    }, 
    options: {
        legend: { display: false },
        title: { display: false },
        scales: {
            xAxes: [{ display: false }],
            yAxes: [{
                ticks: {
                    fontSize: 30,

                }
            }]
        }
    }
});

$('#ctx').on('click', function(evt){

    var base = relatedChart.scales['y-axis-0'].right;
    var height = relatedChart.chart.height;

    if(evt.offsetX < base){

        var count = relatedChart.scales['y-axis-0'].ticks.length;
        
        var bar_height = height / count;
        var bar_index = Math.floor(evt.offsetY / bar_height);

        var label = relatedChart.data.labels[bar_index];
        var genre = label.toLowerCase();

        $.get('/genres/' + genre, function() {
            window.location = '/genres/' + genre;
        });
    }

}); 