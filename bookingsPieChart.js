// bookingsPieChart.js

const bookingsPieYearSelect = document.getElementById("bookingsPieYear");
let bookingsPieChartInstance;

bookingsPieYearSelect.addEventListener("change", renderBookingsPieChart);

async function renderBookingsPieChart() {
  const selectedYear = parseInt(bookingsPieYearSelect.value);
  if (isNaN(selectedYear)) return;

  const bookingsRef = db.collection("bookings");
  const snapshot = await bookingsRef.get();

  const monthCounts = Array(12).fill(0);

  snapshot.forEach(doc => {
    const booking = doc.data();
    if (booking.timestamp && booking.status !== 'deleted') {
      const date = booking.timestamp.toDate();
      const year = date.getFullYear();
      const month = date.getMonth(); // 0 = Jan, 11 = Dec

      if (year === selectedYear) {
        monthCounts[month]++;
      }
    }
  });

  const monthLabels = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
  ];

  // Destroy old chart instance if exists
  if (bookingsPieChartInstance) {
    bookingsPieChartInstance.destroy();
  }

  const ctx = document.getElementById("bookingsPieChart").getContext("2d");

  bookingsPieChartInstance = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: monthLabels,
      datasets: [{
        label: `Bookings in ${selectedYear}`,
        data: monthCounts,
        backgroundColor: [
          "#007bff", "#28a745", "#ffc107", "#dc3545",
          "#17a2b8", "#6610f2", "#6f42c1", "#fd7e14",
          "#20c997", "#e83e8c", "#343a40", "#6c757d"
        ]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'right' },
        title: {
          display: true,
          text: `Bookings Per Month - ${selectedYear}`
        }
      }
    }
  });
}

// Initial render
renderBookingsPieChart();
