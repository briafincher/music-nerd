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
        $('#low').removeClass('bold');
        $('#medium').removeClass('bold');
        $('#high').addClass('bold');
        return 'high';
    } else if (value < upper && value >= lower) {
        $('#low').removeClass('bold');
        $('#high').removeClass('bold');
        $('#medium').addClass('bold');
        return 'medium';
    } else {
        $('#medium').removeClass('bold');
        $('#high').removeClass('bold');
        $('#low').addClass('bold')
        return 'low';
    }
}

// function display(feature) {
//     $('#feature-info').children().hide();
//     $(feature).show();
// }

function find_info(feature) {
    if (feature === 'acousticness') {
        return "A confidence measure from 0.0 to 1.0 of whether the track is acoustic."
    } else if (feature === 'danceability') {
        return "Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity."
    } else if (feature === 'energy') {
        return "Energy represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy."
    } else if (feature === 'instrumentalness') {
        return "Predicts whether a track contains no vocals. 'Ooh' and 'aah' sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly 'vocal'. The higher the instrumentalness value, the greater likelihood the track contains no vocal content."
    } else if (feature === 'liveness') {
        return "Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live."
    } else if (feature === 'loudness') {
        return "Loudness values are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude)."
    } else if (feature === 'speechiness') {
        return "Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the higher the attribute value."
    } else if (feature === 'tempo') {
        return "The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration."
    } else {
        return "A measure describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)."
    }
}

$('#a-label').on('mouseover', function() {
    var info = find_info('acousticness')
    $('#info').html(info)

    var aVal = $('#a-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', aVal);
    $('#slider').trigger('change');

    var category = categorize('acousticness', aVal);
});
$('#d-label').on('mouseover', function() {
    var info = find_info('danceability')
    $('#info').html(info)

    var dVal = $('#d-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', dVal);
    $('#slider').trigger('change');

    var category = categorize('danceability', dVal);
});
$('#e-label').on('mouseover', function() {
    var info = find_info('energy')
    $('#info').html(info)

    var eVal = $('#e-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', eVal);
    $('#slider').trigger('change');

    var category = categorize('energy', eVal);
});
$('#i-label').on('mouseover', function() {
    var info = find_info('instrumentalness')
    $('#info').html(info)

    var iVal = $('#i-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', iVal);
    $('#slider').trigger('change');

    var category = categorize('instrumentalness', iVal);
});
$('#li-label').on('mouseover', function() {
    var info = find_info('liveness')
    $('#info').html(info)

    var liVal = $('#li-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', liVal);
    $('#slider').trigger('change');

    var category = categorize('liveness', liVal);
});
$('#lo-label').on('mouseover', function() {
    var info = find_info('loudness')
    $('#info').html(info)

    var loVal = $('#lo-value').data();
    // $('#slider').prop('step', 10);
    $('#slider').prop('min', -60);
    $('#slider').prop('max', 0);
    $('#slider').prop('value', loVal);
    $('#slider').trigger('change');

    var category = categorize('loudness', loVal);
});
$('#s-label').on('mouseover', function() {
    var info = find_info('speechiness')
    $('#info').html(info)

    var sVal = $('#s-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', sVal);
    $('#slider').trigger('change');

    var category = categorize('speechiness', sVal);
});
$('#t-label').on('mouseover', function() {
    var info = find_info('tempo')
    $('#info').html(info)

    var tVal = $('#t-value').data();
    // $('#slider').prop('step', 10);
    $('#slider').prop('min', 50);
    $('#slider').prop('max', 200);
    $('#slider').prop('value', tVal);
    $('#slider').trigger('change');

    var category = categorize('tempo', tVal);
});
$('#v-label').on('mouseover', function() {
    var info = find_info('valence')
    $('#info').html(info)

    var vVal = $('#v-value').data();
    $('#slider').prop('min', 0);
    $('#slider').prop('max', 1);
    $('#slider').prop('value', vVal);
    $('#slider').trigger('change');

    var category = categorize('valence', vVal);
});

// Event listeners for feature mouseover
// $('#a-label').on('mouseover', function() {
//     var aVal = $('#a-value').data();
//     var category = categorize('acousticness', aVal);
//     console.log(category + ' acousticness');
//     $('#a-category').html('This genre has ' + category.toUpperCase() + ' acousticness')
//     display('#acousticness');
// });
// $('#d-label').on('mouseover', function() {
//     var dVal = $('#d-value').data();
//     var category = categorize('danceability', dVal);
//     console.log(category + ' danceability');
//     $('#d-category').html('This genre has ' + category.toUpperCase() + ' danceability')
//     display('#danceability');
// });
// $('#e-label').on('mouseover', function() {
//     var eVal = $('#e-value').data();
//     var category = categorize('energy', eVal);
//     console.log(category  + ' energy');
//     $('#e-category').html('This genre has ' + category.toUpperCase() + ' energy')
//     display('#energy');
// });
// $('#i-label').on('mouseover', function() {
//     var iVal = $('#i-value').data();
//     var category = categorize('instrumentalness', iVal);
//     console.log(category + ' instrumentalness');
//     $('#i-category').html('This genre has ' + category.toUpperCase() + ' instrumentalness')
//     display('#instrumentalness');
// });
// $('#li-label').on('mouseover', function() {
//     var liVal = $('#li-value').data();
//     var category = categorize('liveness', liVal);
//     console.log(category + ' liveness');
//     $('#li-category').html('This genre has ' + category.toUpperCase() + ' liveness')
//     display('#liveness');
// });
// $('#lo-label').on('mouseover', function() {
//     var loVal = $('#lo-value').data();
//     var category = categorize('loudness', loVal);
//     console.log(category + ' loudness');
//     $('#lo-category').html('This genre has ' + category.toUpperCase() + ' loudness')
//     display('#loudness');
// });
// $('#m-label').on('mouseover', function() {
//     var mVal = $('#m-value').data();
//     var category = categorize('mode', mVal);
//     console.log(category + ' mode');
//     $('#m-category').html('This genre has ' + category.toUpperCase() + ' mode')
//     display('#mode');
// });
// $('#s-label').on('mouseover', function() {
//     var sVal = $('#s-value').data();
//     var category = categorize('speechiness', sVal);
//     console.log(category + ' speechiness');
//     $('#s-category').html('This genre has ' + category.toUpperCase() + ' speechiness')
//     display('#speechiness');
// });
// $('#t-label').on('mouseover', function() {
//     var tVal = $('#t-value').data();
//     var category = categorize('tempo', tVal);
//     console.log(category + ' tempo');
//     $('#t-category').html('This genre has ' + category.toUpperCase() + ' tempo')
//     display('#tempo');
// });
// $('#v-label').on('mouseover', function() {
//     var vVal = $('#v-value').data();
//     var category = categorize('valence', vVal);
//     console.log(category + ' valence');
//     $('#v-category').html('This genre has ' + category.toUpperCase() + ' valence')
//     display('#valence');
// });




















