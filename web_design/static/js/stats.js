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
// Initialize the echarts instance based on the prepared dom
 var myChart = echarts.init(document.getElementById('pie-plot'));
// Specify the configuration items and data for the chart
var option = {
  title: {
    text: 'ECharts Getting Started Example'
  },
  tooltip: {
    trigger: 'item'
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



async function loadChart2(){
  /*  Incomes Outcomes chart */
  const response = await fetch('../get-table');
  const data = await response.json();
 
  accountStatuses=[]
  actualStatus=0
  dates=[]
  /* preprocesing data */
  data.reverse().forEach(element => { 
    if(element.type=='Egreso'){element.amount= -element.amount};
    actualStatus+=element.amount;
    accountStatuses.push(actualStatus);
    dates.push(element.set_at)
  });
  // Initialize the echarts instance based on the prepared dom
   var myChart = echarts.init(document.getElementById('line-plot'));

  // Specify the configuration items and data for the chart
  option = {
    title: {
      text: 'Ahorros'
    },
    tooltip: {
      trigger: 'axis'
    },
    xAxis: {
      data: dates,
    },
    yAxis: {min:'dataMin',
          max:'dataMax'
  },
    series: [
      {
        name:'Total ahorrado',
        data: accountStatuses,
        type: 'line',
        areaStyle: {}
      },
    ]
  };
  // Display the chart using the configuration items and data just specified.
    myChart.setOption(option);
  }
    