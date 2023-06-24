/* Encapsulates charts renderin in functions */

async function loadChart1(){
/*  Incomes Outcomes chart */
const response = await fetch('../get-table');
const data = await response.json();
const seriesData = [];
data.forEach(element => {
  seriesData.push({
    name:element.category,
    value:element.amount,
  })
});
console.log(seriesData);
// Initialize the echarts instance based on the prepared dom
 var myChart = echarts.init(document.getElementById('main'));
// Specify the configuration items and data for the chart
var option = {
  title: {
    text: 'ECharts Getting Started Example'
  },
  series: [
    {
      type: 'pie',
      radius: ['40%', '70%'],
      data: seriesData,
    }
  ],
};
  

// Display the chart using the configuration items and data just specified.
  myChart.setOption(option);
}

    