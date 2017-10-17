function categorize(feature, data) {

    var value = data[feature];

    var maximum, upper, lower, minimum;

    if (feature === 'loudness') {
        maximum = 0;
        upper = -20;
        lower = -40;
        minimum = -60;
    } else if (feature === 'tempo') {
        maximum = 200;
        upper = 150;
        lower = 100;
        minimum = 50;
    } else {
        maximum = 1;
        upper = 0.66;
        lower = 0.33;
        minimum = 0;
    }

    console.log(feature);
    console.log(value);

    if (value >= upper) {
        console.log('value')
        return 'high';
    } else if (value < upper && value >= lower) {
        return 'medium';
    } else {
        return 'low';
    }
}

function display(feature) {
    $('#feature-info').children().hide()
    $(feature).show()
}