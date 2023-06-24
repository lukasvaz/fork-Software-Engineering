const response = await fetch('../get-table');
const data = await response.json();
    
$.ajax({url:'../get-table'}).done(function (response){
        console.log(typeof(response))
        // Initialize the echarts instance based on the prepared dom
        var data = JSON.parse(response);
        var myChart = echarts.init(document.getElementById('main'));
  
        // Specify the configuration items and data for the chart
        var option = {
          title: {
            text: 'ECharts Getting Started Example'
          },
          series: [
            {
              type: 'pie',
              data: data.amount
            }
          ]
        };
  
        // Display the chart using the configuration items and data just specified.
        myChart.setOption(option);
      
      })
        