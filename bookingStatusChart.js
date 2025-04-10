// bookingStatusChart.js

let bookingStatusChartInstance;

async function renderBookingStatusChart() {
  const bookingsRef = db.collection("bookings");
  const snapshot = await bookingsRef.get();

  let total = 0, approved = 0, deleted = 0;

  snapshot.forEach(doc => {
    total++;
    const booking = doc.data();
    const status = booking.status?.toLowerCase();

    if (status === "approved") approved++;
    if (status === "deleted") deleted++;
  });

  const ctx = document.getElementById("bookingStatusChart").getContext("2d");

  // Destroy existing chart before rendering new
  if (bookingStatusChartInstance) {
    bookingStatusChartInstance.destroy();
  }

  bookingStatusChartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Total", "Approved", "Deleted"],
      datasets: [{
        label: "Booking Status Overview",
        data: [total, approved, deleted],
        backgroundColor: ["#007bff", "#28a745", "#dc3545"]
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
        legend: { display: false },
        title: {
          display: true,
          text: "Total Bookings | Approved | Deleted"
        }
      }
    }
  });
}

// Call it once on load
renderBookingStatusChart();
