// trucksAddedChart.js

const categoryFilter = document.getElementById('categoryFilter');
const companyFilter = document.getElementById('companyFilter');

// Chart reference
let trucksChartInstance;

async function renderTrucksAddedChart() {
  const trucksRef = db.collection("trucks");

  let query = trucksRef;

  // Apply filters if selected
  const selectedCategory = categoryFilter.value;
  const selectedCompany = companyFilter.value;

  if (selectedCategory !== 'all') {
    query = query.where("category", "==", selectedCategory);
  }

  if (selectedCompany !== 'all') {
    query = query.where("company", "==", selectedCompany);
  }

  const snapshot = await query.get();

  const adminCounts = {};
  snapshot.forEach(doc => {
    const truck = doc.data();
    const addedBy = truck.addedBy || "Unknown";

    adminCounts[addedBy] = (adminCounts[addedBy] || 0) + 1;
  });

  const labels = Object.keys(adminCounts);
  const data = Object.values(adminCounts);

  // Destroy old chart instance if it exists
  if (trucksChartInstance) {
    trucksChartInstance.destroy();
  }

  // Draw the chart
  const ctx = document.getElementById("trucksAddedChart").getContext("2d");
  trucksChartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Trucks Added by Admin",
        data: data,
        backgroundColor: "#28a745"
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        title: {
          display: true,
          text: "Trucks Added by Each Admin"
        }
      }
    }
  });
}

// Event listeners
categoryFilter.addEventListener("change", renderTrucksAddedChart);
companyFilter.addEventListener("change", renderTrucksAddedChart);

// Initial render
renderTrucksAddedChart();
