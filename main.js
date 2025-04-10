// Firebase config — REPLACE with your Firebase project details
const firebaseConfig = {
    apiKey: "AIzaSyCuhbxnhqUZnbfYELDHTCJEI1k-LP1eKBo",
    authDomain: "truckbooking-ab4d0.firebaseapp.com",
    databaseURL: "https://console.firebase.google.com/u/2/project/truckbooking-ab4d0/firestore/databases/-default-/rules",
    projectId: "truckbooking-ab4d0",
    storageBucket: "truckbooking-ab4d0.firebasestorage.app",
    messagingSenderId: "249339346525",
    appId: "1:249339346525:web:c3f2a1ce605eeccb2357b4"
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  const auth = firebase.auth();
  const db = firebase.database();
  
  // Form toggle (login/signup)
  let isSignup = false;
  
  function toggleForm() {
    isSignup = !isSignup;
    document.getElementById('formTitle').innerText = isSignup ? "Sign Up" : "Login";
    document.querySelector('.toggle').innerText = isSignup ? "Already have an account? Login" : "Don't have an account? Sign Up";
    document.getElementById('userTypeSelect').style.display = isSignup ? "block" : "none";
  }
  
  // Handle login or signup
  function handleAuth() {
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
  
    if (!email || !password) {
      alert("Please fill all fields");
      return;
    }
  
    if (isSignup) {
      const userType = document.getElementById('userTypeSelect').value;
      auth.createUserWithEmailAndPassword(email, password)
        .then(userCred => {
          const uid = userCred.user.uid;
          return db.ref('users/' + uid).set({
            email: email,
            userType: userType
          });
        })
        .then(() => {
          alert("Signup successful! Please login.");
          toggleForm();
        })
        .catch(err => alert(err.message));
    } else {
      auth.signInWithEmailAndPassword(email, password)
        .then(userCred => {
          const uid = userCred.user.uid;
          return db.ref('users/' + uid).once('value');
        })
        .then(snapshot => {
          const userData = snapshot.val();
          if (!userData || !userData.userType) {
            alert("User type not found. Please sign up again.");
            return;
          }
          if (userData.userType === 'admin') {
            window.location.href = "admin.html";
          } else {
            window.location.href = "userdashboard.html";
          }
        })
        .catch(err => alert(err.message));
    }
  }
  
