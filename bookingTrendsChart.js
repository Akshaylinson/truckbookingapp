// bookingTrendsChart.js

const trendTypeSelect = document.getElementById("trendType");

let bookingTrendsChartInstance;

async function renderBookingTrendsChart() {
  const selectedTrend = trendTypeSelect.value; // 'daily' or 'weekly'
  const bookingsRef = db.collection("bookings");

  const snapshot = await bookingsRef.get();

  const dateCounts = {};

  snapshot.forEach(doc => {
    const booking = doc.data();
    if (booking.timestamp && booking.status !== 'deleted') {
      const date = booking.timestamp.toDate();

      let key;
      if (selectedTrend === "daily") {
        key = date.toISOString().split("T")[0]; // yyyy-mm-dd
      } else if (selectedTrend === "weekly") {
        const startOfWeek = new Date(date);
        const day = startOfWeek.getDay(); // Sunday = 0
        const diff = startOfWeek.getDate() - day + (day === 0 ? -6 : 1); // Monday as first day
        startOfWeek.setDate(diff);
        key = startOfWeek.toISOString().split("T")[0]; // Week start date
      }

      if (key) {
        dateCounts[key] = (dateCounts[key] || 0) + 1;
      }
    }
  });

  const sortedKeys = Object.keys(dateCounts).sort();
  const data = sortedKeys.map(key => dateCounts[key]);

  // Destroy old chart instance
  if (bookingTrendsChartInstance) {
    bookingTrendsChartInstance.destroy();
  }

  const ctx = document.getElementById("bookingTrendsChart").getContext("2d");
  bookingTrendsChartInstance = new Chart(ctx, {
    type: "line",
    data: {
      labels: sortedKeys,
      datasets: [{
        label: `Bookings (${selectedTrend})`,
        data: data,
        borderColor: "#007bff",
        fill: false,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: true },
        title: {
          display: true,
          text: `Booking ${selectedTrend === 'daily' ? 'Daily' : 'Weekly'} Trends`
        }
      },
      scales: {
        x: { title: { display: true, text: "Date" } },
        y: { title: { display: true, text: "Number of Bookings" }, beginAtZero: true }
      }
    }
  });
}

trendTypeSelect.addEventListener("change", renderBookingTrendsChart);

// Initial render
renderBookingTrendsChart();
