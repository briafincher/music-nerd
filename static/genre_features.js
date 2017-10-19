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
    $('#feature-info').children().hide();
    $(feature).show();
}

// Event listeners for feature mouseover
$('#a-label').on('mouseover', function() {
    var aVal = $('#a-value').data();
    var category = categorize('acousticness', aVal);
    console.log(category + ' acousticness');
    $('#a-category').html('This genre has ' + category.toUpperCase() + ' acousticness')
    display('#acousticness');
});
$('#d-label').on('mouseover', function() {
    var dVal = $('#d-value').data();
    var category = categorize('danceability', dVal);
    console.log(category + ' danceability');
    $('#d-category').html('This genre has ' + category.toUpperCase() + ' danceability')
    display('#danceability');
});
$('#e-label').on('mouseover', function() {
    var eVal = $('#e-value').data();
    var category = categorize('energy', eVal);
    console.log(category  + ' energy');
    $('#e-category').html('This genre has ' + category.toUpperCase() + ' energy')
    display('#energy');
});
$('#i-label').on('mouseover', function() {
    var iVal = $('#i-value').data();
    var category = categorize('instrumentalness', iVal);
    console.log(category + ' instrumentalness');
    $('#i-category').html('This genre has ' + category.toUpperCase() + ' instrumentalness')
    display('#instrumentalness');
});
$('#li-label').on('mouseover', function() {
    var liVal = $('#li-value').data();
    var category = categorize('liveness', liVal);
    console.log(category + ' liveness');
    $('#li-category').html('This genre has ' + category.toUpperCase() + ' liveness')
    display('#liveness');
});
$('#lo-label').on('mouseover', function() {
    var loVal = $('#lo-value').data();
    var category = categorize('loudness', loVal);
    console.log(category + ' loudness');
    $('#lo-category').html('This genre has ' + category.toUpperCase() + ' loudness')
    display('#loudness');
});
$('#m-label').on('mouseover', function() {
    var mVal = $('#m-value').data();
    var category = categorize('mode', mVal);
    console.log(category + ' mode');
    $('#m-category').html('This genre has ' + category.toUpperCase() + ' mode')
    display('#mode');
});
$('#s-label').on('mouseover', function() {
    var sVal = $('#s-value').data();
    var category = categorize('speechiness', sVal);
    console.log(category + ' speechiness');
    $('#s-category').html('This genre has ' + category.toUpperCase() + ' speechiness')
    display('#speechiness');
});
$('#t-label').on('mouseover', function() {
    var tVal = $('#t-value').data();
    var category = categorize('tempo', tVal);
    console.log(category + ' tempo');
    $('#t-category').html('This genre has ' + category.toUpperCase() + ' tempo')
    display('#tempo');
});
$('#v-label').on('mouseover', function() {
    var vVal = $('#v-value').data();
    var category = categorize('valence', vVal);
    console.log(category + ' valence');
    $('#v-category').html('This genre has ' + category.toUpperCase() + ' valence')
    display('#valence');
});



















