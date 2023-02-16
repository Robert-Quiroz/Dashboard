// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Direct", "Referral", "Social"],
    datasets: [{
      data: [55, 30, 15],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Chart MySQL</title>

//     <style>        
//     </style>
// </head>
// <body>
    
//     <canvas id="myChart" style="position: relative; height: 40vh; width: 80vw;"></canvas>

//     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

//     <script>
//         var ctx = document.getElementById('myChart')
//         var myChart = new Chart(ctx, {
//             type:'bar',
//             data:{
//                 datasets: [{
//                     label: 'Stock de Productos',
//                     backgroundColor: ['#6bf1ab','#63d69f', '#438c6c', '#509c7f', '#1f794e', '#34444c', '#90CAF9', '#64B5F6', '#42A5F5', '#2196F3', '#0D47A1'],
//                     borderColor: ['black'],
//                     borderWidth:1
//                 }]
//             },
//             options:{
//                 scales:{
//                     y:{
//                         beginAtZero:true
//                     }
//                 }
//             }
//         })

//         let url = 'http://localhost/apirest/articulos.php'
//         fetch(url)
//             .then( response => response.json() )
//             .then( datos => mostrar(datos) )
//             .catch( error => console.log(error) )


//         const mostrar = (articulos) =>{
//             articulos.forEach(element => {
//                 myChart.data['labels'].push(element.descripcion)
//                 myChart.data['datasets'][0].data.push(element.stock)
//                 myChart.update()
//             });
//             console.log(myChart.data)