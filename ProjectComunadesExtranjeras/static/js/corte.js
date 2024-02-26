document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('PieChart').getContext('2d');
    var rows = document.querySelectorAll('table tbody tr');

    var labels = [];
    var dataValues = [];
    var backgroundColors = [];

    var colorPalette = [
        '#ff0000',
        '#ffff00',
        '#ffa500',
        '#008000',
        '#0000ff',
        '#ff69b4',
        '#800080'
    ];

    rows.forEach(function (row) {
        var cells = row.querySelectorAll('td');
        labels.push(cells[2].textContent); 
        dataValues.push(parseFloat(cells[1].textContent));

        var categoryIndex = labels.indexOf(cells[2].textContent);
        backgroundColors.push(colorPalette[categoryIndex]);
    });

    var data = {
        labels: labels,
        datasets: [{
            data: dataValues,
            backgroundColor: backgroundColors,
        }]
    };

    var ChartOptions = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            aspectRatio: 0.4,
        },
    });
});

var currentDate = new Date();
var printDateElement = document.getElementById('printDate');
var formattedDate = currentDate.toLocaleString();
printDateElement.textContent = formattedDate;