// userLoginsChart.js

let userLoginsChartInstance;

document.getElementById("userLoginsYearFilter").addEventListener("change", renderUserLoginsChart);

async function renderUserLoginsChart() {
  const selectedYear = parseInt(document.getElementById("userLoginsYearFilter").value);
  const loginsRef = db.collection("userLogins"); // Ensure this collection exists
  const snapshot = await loginsRef.get();

  const monthlyCounts = new Array(12).fill(0);

  snapshot.forEach(doc => {
    const data = doc.data();
    const timestamp = data.timestamp ? new Date(data.timestamp) : null;

    if (timestamp && timestamp.getFullYear() === selectedYear) {
      const month = timestamp.getMonth(); // 0 = Jan, 11 = Dec
      monthlyCounts[month]++;
    }
  });

  const ctx = document.getElementById("userLoginsChart").getContext("2d");

  if (userLoginsChartInstance) userLoginsChartInstance.destroy();

  userLoginsChartInstance = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      datasets: [{
        label: `User Logins in ${selectedYear}`,
        data: monthlyCounts,
        borderColor: "#4bc0c0",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          ticks: { precision: 0 }
        }
      },
      plugins: {
        title: {
          display: true,
          text: "User Logins Per Month"
        },
        legend: {
          display: true
        }
      }
    }
  });
}

// Load on first render
window.addEventListener("load", () => {
  const currentYear = new Date().getFullYear();
  document.getElementById("userLoginsYearFilter").value = currentYear;
  renderUserLoginsChart();
});
