
---

## 🌐 Live Preview

> *(Add your hosted link here if deployed, e.g., Firebase Hosting or GitHub Pages)*

---

## 📂 Project Structure

```
📁 TRUCK-BOOKING
├── admin.html             # Admin dashboard for managing trucks and bookings
├── booking.html           # User interface for booking trucks
├── contact.html           # Contact form or information page
├── index.html             # Landing or homepage
├── main.js                # Core JavaScript logic (Firebase & app logic)
├── mybookings.html        # Displays user's previous bookings
├── trucks.html            # Shows available trucks to book
├── userdashboard.html     # Unified dashboard for user profile & actions
└── userprofile.html       # (Legacy) standalone user profile page
```

---

## 🔐 Features

### 👤 User Features
- User Registration and Login using Firebase Authentication
- Book a truck with required details (pickup/drop location, date, etc.)
- View and manage previous bookings
- Upload and update profile picture (stored in Firebase Storage)
- Secure password change via Firebase Auth
- Update personal profile info (name, phone number, DOB, address, etc.)
- Access unified dashboard (`userdashboard.html`) for complete experience

### 🛠️ Admin Features
- Admin login for secured access
- Add, update, or remove truck listings
- View and manage user bookings from the `admin.html` page

---

## 💡 Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Vanilla JS)
- **Authentication**: Firebase Authentication
- **Database**: Firebase Firestore
- **Storage**: Firebase Storage

---

## 🚫 Project Notes

- ❌ No use of `localStorage` to avoid data inconsistencies across pages.
- ✅ Firebase Firestore and Auth used for consistent, real-time backend support.
- 🔁 The `userprofile.html` page is now merged into `userdashboard.html` for a streamlined user experience.

---

## 🚀 Getting Started

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/truck-booking-app.git
   cd truck-booking-app
   ```

2. **Open the project in a live server or browser:**
   - You can directly open `index.html`
   - Or use a VSCode Live Server extension

3. **Configure Firebase:**
   - Go to [Firebase Console].
   - Create a new project
   - Enable **Authentication**, **Firestore Database**, and **Storage**
   - Replace the Firebase config in `main.js` with your own project's credentials.

4. **Set Firebase Rules (for development):**

   **Firestore Rules:**
   ```js
   service cloud.firestore {
     match /databases/{database}/documents {
       match /{document=**} {
         allow read, write: if true;
       }
     }
   }
   ```

   **Storage Rules:**
   ```js
   service firebase.storage {
     match /b/{bucket}/o {
       match /{allPaths=**} {
         allow read, write: if request.auth != null;
       }
     }
   }
   ```

---
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to fork this project and submit a pull request.

---

## 📧 Contact

For queries or feedback, reach out via:

- 📩 Email: [akshaylinson24@gmail.com]
- 💬 GitHub: [github.com/Akshaylinson](https://github.com/Akshaylinson)

---

---

```

