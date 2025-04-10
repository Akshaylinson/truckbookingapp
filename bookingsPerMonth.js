document.addEventListener("DOMContentLoaded", async () => {
    const ctx = document.getElementById("bookingsPerMonthChart").getContext("2d");
  
    const monthLabels = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];
  
    const bookingsPerMonth = new Array(12).fill(0); // Initialize count array
  
    try {
      const snapshot = await db.collection("bookings").get();
  
      snapshot.forEach(doc => {
        const data = doc.data();
        if (data.bookingDate) {
          const date = new Date(data.bookingDate);
          const month = date.getMonth(); // 0 to 11
          bookingsPerMonth[month]++;
        }
      });
  
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: monthLabels,
          datasets: [{
            label: "Number of Bookings",
            data: bookingsPerMonth,
            backgroundColor: "#007bff",
            borderRadius: 5
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
            title: {
              display: true,
              text: "Total Bookings Per Month"
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Bookings"
              }
            }
          }
        }
      });
    } catch (error) {
      console.error("Error loading booking data:", error);
    }
  });
  
