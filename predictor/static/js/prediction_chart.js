// prediction_chart.js

document.addEventListener('DOMContentLoaded', function () {
    // Function to create and show the pie chart
    function createAndShowPieChart() {
        // Retrieve prediction data from the script tag
        const predictionDataScript = document.getElementById('predictionData');
        const predictionData = JSON.parse(predictionDataScript.textContent);

        // Extract relevant data for the pie chart
        const positivePredictions = predictionData.filter(data => data.prediction === 1).length;
        const negativePredictions = predictionData.filter(data => data.prediction === 0).length;

        // Get the canvas element
        const pieChartCanvas = document.getElementById('predictionPieChart').getContext('2d');

        // Create the pie chart using Chart.js
        new Chart(pieChartCanvas, {
            type: 'pie',
            data: {
                labels: ['Positive Predictions', 'Negative Predictions'],
                datasets: [{
                    data: [positivePredictions, negativePredictions],
                    backgroundColor: ['#36A2EB', '#FF6384'],
                }],
            },
        });
    }

    // Additional initialization or setup code can go here
    // ...
});