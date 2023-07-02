/* Encapsulates charts renderin in functions */

async function loadChart1(){
/*  Incomes Outcomes chart */

const outcomes = await fetch('../get-filter-aggregate/outcomes/category');
const outcomes_data = await outcomes.json();

const  incomes= await fetch('../get-filter-aggregate/incomes/category');
const incomes_data = await incomes.json();

const IncomesPlotData = [];
const OutcomesPlotData = [];

outcomes_data.forEach(element => {
  OutcomesPlotData.push({
    name:element.category,
    value:element.total,
  })
});

incomes_data.forEach(element => {
  IncomesPlotData.push({
    name:element.category,
    value:element.total,
  })
});

console.log(IncomesPlotData)
// Initialize the echarts instance based on the prepared dom
 var myChartIncomes = echarts.init(document.getElementById('pie-plot-incomes'));
 var myChartOutcomes = echarts.init(document.getElementById('pie-plot-outcomes'));
// Specify the configuration items and data for the chart
var colorPaletteIncomes = ['#9ef01a','#70e000','#38b000','#008000','#007200']
var optionIncomes = {
  title: {
    text: 'Ingresos',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  series: [
    { name:'Ingresos',
    type: 'pie',
    color:colorPaletteIncomes,
    radius: ['40%', '70%'],
    center: ['50%', '50%'],
    data: IncomesPlotData,
  }
],
};

var colorPaletteOutcomes = ['#e40b0b','#c30e0e','#a21112','#821415','#821415']
var optionOutcomes = {
  title: {
    text: 'Egresos',
    left: 'center',
  },
  tooltip: {
    trigger: 'item'
  },
  series: [ 
    { name:'Egresos',
    type: 'pie',
    radius: ['40%', '70%'],
    center: ['50%', '50%'],
    color:colorPaletteOutcomes,
    data: OutcomesPlotData,
  }
],
};


// Display the chart using the configuration items and data just specified.
  myChartIncomes.setOption(optionIncomes);
  myChartOutcomes.setOption(optionOutcomes);
}



async function loadChart2(){
  /*  Incomes Outcomes chart */
  const response = await fetch('../get-raw-transactions');
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
      text: 'Ahorro',
    left: 'center',
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
    