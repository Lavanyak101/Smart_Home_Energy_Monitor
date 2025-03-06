let energyChart;

function fetchEnergyData() {
    fetch('http://127.0.0.1:5000/get_energy_data')
        .then(response => response.json())
        .then(data => {
            updateChart(data);
            document.getElementById("acUsage").innerText = data["Air Conditioner"] + "W";
            document.getElementById("fridgeUsage").innerText = data["Refrigerator"] + "W";
            document.getElementById("tvUsage").innerText = data["TV"] + "W";
            document.getElementById("lightsUsage").innerText = data["Lights"] + "W";
        });
}

function updateChart(data) {
    const ctx = document.getElementById('energyChart').getContext('2d');
    if (energyChart) energyChart.destroy();
    energyChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Energy Usage (Watts)',
                data: Object.values(data),
                backgroundColor: ['lime', 'cyan', 'yellow', 'red']
            }]
        }
    });
}

function toggleTheme() {
    document.body.classList.toggle("light-mode");
    localStorage.setItem("theme", document.body.classList.contains("light-mode") ? "light" : "dark");
}

window.onload = () => {
    if (localStorage.getItem("theme") === "light") document.body.classList.add("light-mode");
};

fetchEnergyData();
setInterval(fetchEnergyData, 10000);




