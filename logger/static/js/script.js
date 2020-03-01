graphData = [] // data returned from '/graph_data' page is stored in this variable
var timeFormat = 'MM/DD/YYYY';
var color = Chart.helpers.color; // chart.js colors

// Configuration of Chart of dashboard
var config = {
    type: 'line',
    data: {
        datasets: [{
            label: 'Number of requests',
            backgroundColor: color('rgb(54, 162, 235)').alpha(0.5).rgbString(),
            borderColor: 'rgb(54, 162, 235)',
            fill: false,
            data: graphData,
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: ''
        },
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    parser: timeFormat,
                    unit: 'day',
                    tooltipFormat: 'll'
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Date'
                },
                ticks: {
                    major: {
                        fontStyle: 'bold',
                        fontColor: '#FF0000'
                    }
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Requests'
                },
                ticks: {
                    stepSize: 1,
                }
            }]
        }
    }
};

// Getting chart data from server 
$.ajax({
    type: "GET",
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    url: "/graph_data",
    success: function(data) {
        data = JSON.parse(data);
        data.forEach((key, value) => {
            // pushing chart data in graphData variable
            graphData.push({
                'x': moment(key.timestamp).format(timeFormat),
                'y': key.total,
            })
        });
        var ctx_day_chart = document.getElementById('per-day-chart').getContext('2d');
        window.myLine = new Chart(ctx_day_chart, config); // initialising Chart
    },
    error: function(err) {
        console.log("Error:" + err);
    }
})

// this function get number of request logged on particular date
function getRequestsOnDate(that) {
    $.ajax({
        type: "GET",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: {
            date: that.value,
        },
        url: "/request_on_date",
        success: function(data) {
            $('#requests_on_date').html(data.requests_on_date);
            console.log(data.requests_on_date);
        },
        error: function(err) {
            console.log("Error:" + err);
        }
    });
}

// this function get number of request logged between two dates
function getNumRequestsBetween(that) {
    from_date = $('#from_date').val();
    to_date = $('#to_date').val();
    $.ajax({
        type: "GET",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: {
            from_date: from_date,
            to_date: to_date,
        },
        url: "/requests_between_dates",
        success: function(data) {
            $('#requests_between_dates').html(data.requests_between_dates);
            console.log(data.requests_between_dates);
        },
        error: function(err) {
            console.log("Error:" + err);
        }
    })
}

// this function get number of requests that came from diffent locations (countries)
function getRequestFromCountry(that) {
    var country = that.value
    console.log(country);
    $.ajax({
        type: "GET",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: {
            country: country,
        },
        url: "/requests_from_countries",
        success: function(data) {
            $('#requests_from_countries').html(data.requests_from_countries);
            console.log(data.requests_from_countries);
        },
        error: function(err) {
            console.log("Error:" + err);
        }
    });
}