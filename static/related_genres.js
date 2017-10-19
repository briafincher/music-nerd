// var parent = $('#related-genres').children() // 1, 3, 5, 7, 9

// var one = '#' + $('#related-genres').children()[1].id
// var two = '#' + $('#related-genres').children()[3].id
// var three = '#' + $('#related-genres').children()[5].id
// var four = '#' + $('#related-genres').children()[7].id
// var five = '#' + $('#related-genres').children()[9].id

// var GENRES = [
//             $(one).data().capitalized,
//             $(two).data().capitalized,
//             $(three).data().capitalized,
//             $(four).data().capitalized,
//             $(five).data().capitalized
//         ];

// var color = Chart.helpers.color;
// var horizontalBarChartData = {
//     labels: GENRES,
//     datasets: [{
//         backgroundColor: 'rgba(49, 79, 111)',
//         borderColor: 'rgba(49, 79, 111)',
//         borderWidth: 1,
//         data: [
//             $(one).data().shared,
//             $(two).data().shared,
//             $(three).data().shared,
//             $(four).data().shared,
//             $(five).data().shared
//         ]
//     }]
// };

// window.onload = function() {
//     var ctx = document.getElementById('related-graph').getContext('2d');
//     window.myHorizontalBar = new Chart(ctx, {
//         type: 'horizontalBar',
//         data: horizontalBarChartData,
//         option: {
//             elements: {
//                 rectangle: {
//                     borderWidth: 2,
//                 }
//             },
//             responsive: true,
//             // legend: {
//             //     position: 'right',
//             // },
//             title: {
//                 display: false,
//                 text: 'Shared Artists'
//             }
//         }
//     });
// };




var canvas = document.getElementById('related-graph');
var ctx = canvas.getContext('2d');

var one = $('#related-one').data();
var two = $('#related-two').data();
var three = $('#related-three').data();
var four = $('#related-four').data();
var five = $('#related-five').data();

ctx.font = '20px Helvetica';
ctx.fillText(one.upper, 10, 10);
ctx.fillText(two.upper, 10, 40);
ctx.fillText(three.upper, 10, 70);
ctx.fillText(four.upper, 10, 100);
ctx.fillText(five.upper, 10, 130);