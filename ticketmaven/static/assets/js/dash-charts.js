$(document).ready(function() {
    // Data for the first chart: High Performing Product
    var r1 = {
      chart: { height: 256, type: "bar", stacked: true },
      plotOptions: { bar: { horizontal: false, columnWidth: "20%" } },
      dataLabels: { enabled: false },
      stroke: { show: true, width: 0, colors: ["transparent"] },
      series: [
        { name: "Actual", data: [65, 59, 80, 81, 56, 89, 40, 32, 65, 59, 80, 81] },
        { name: "Projection", data: [890, 40, 32, 65, 59, 80, 81, 56, 89, 40, 65, 59] },
      ],
      zoom: { enabled: true },
      legend: { show: true },
      colors: ($("#high-performing-product").data("colors") || "").split(","),
      
      xaxis: {
        categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        axisBorder: { show: false },
      },
      yaxis: {
        labels: {
          formatter: function (val) {
            return val ;
          },
          offsetX: -15,
        },
      },
      fill: { opacity: 1 },
      tooltip: {
        y: {
          formatter: function (val) {
            return val ;
          },
        },
      },
    };

    // Data for the second chart: Debit Card Spending (Donut Chart)
    var r2 = {
      chart: { height: 256, type: "donut" },
      series: [30, 25, 20, 15, 28, 32, 22], // Example series data for debit card spending
      labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], // Days of the week
      colors: ($("#debit-card-spending").data("colors") || "").split(","),
      legend: { show: false },
    };

    // Initialize and render the first chart: High Performing Product
    var chart1 = new ApexCharts(document.querySelector("#high-performing-product"), r1);
    chart1.render();

    // Initialize and render the second chart: Debit Card Spending (Donut Chart)
    var chart2 = new ApexCharts(document.querySelector("#debit-card-spending"), r2);
    chart2.render();
  });