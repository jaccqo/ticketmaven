$(document).ready(function() {
    // Data for the first chart: High Performing Product
    var r1 = {
      chart: { height: 256, type: "bar", stacked: true },
      plotOptions: { bar: { horizontal: false, columnWidth: "20%" } },
      dataLabels: { enabled: false },
      stroke: { show: true, width: 0, colors: ["transparent"] },
      series: [
        { name: "Actual", data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] },
        { name: "Projection", data: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] },
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
      series: [0, 0, 0, 0, 0, 0, 2], // Example series data for debit card spending
      labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], // Days of the week
      colors: ($("#debit-card-spending").data("colors") || "").split(","),
      legend: { show: false },
    };

  

    // Initialize and render the second chart: Debit Card Spending (Donut Chart)
    var chart2 = new ApexCharts(document.querySelector("#debit-card-spending"), r2);
    chart2.render();

  
    var authToken = $('#high-performing-product').data('auth-token');
    var chartId = 'high-performing-product';
    var chart1 = null; // Variable to hold the chart instance
    
    function fetchDataAndUpdateChart() {
        // Make AJAX request to fetch data
        $.ajax({
            url: '/api/ticket-purchases/',
            headers: { 'Authorization': 'Token ' + authToken }, // Use the retrieved token
            success: function(data) {
                // Format data and populate r1
                var categories = [];
                var actualData = [];
                var projectionData = [];
                $.each(data, function(index, item) {
                    categories.push(item.month);
                    actualData.push(item.quantity);
                    projectionData.push(item.projection);
                });
            
                // Update the chart data
                chart1.updateSeries([
                    { data: actualData },
                    { data: projectionData }
                ]);
    
                // Update the chart x-axis categories
                chart1.updateOptions({
                    xaxis: { categories: categories }
                });
            },
            error: function(xhr, status, error) {
                console.error('Error fetching data:', error);
            }
        });
    }
    
    // Render the chart
    chart1 = new ApexCharts(document.querySelector("#" + chartId), r1);
    chart1.render();
    
    // Set interval to fetch data and update chart every 19 seconds
    setInterval(fetchDataAndUpdateChart, 19000); // 19 seconds in milliseconds
    


  });