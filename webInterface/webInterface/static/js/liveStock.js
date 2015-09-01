  window.onload = function(){
            var dataPoints = [];
            var y = 0;
            var limit = 50000;

            for( var i=0; i<limit; i++){
                y+= Math.round(10+ Math.random() * (-10 -10));
                dataPoints.push({y: y});
            }

            var chart = new CanvasJS.Chart("chartContainer",
             {
             animationEnabled : true,
             zoomEnabled: true,

            title: {
                text: "BSE SENSEX"
            },
            data: [
            {
                type: "line",
                "dataPoints": dataPoints
            }
            ]
            });




            chart.render();
        }();
