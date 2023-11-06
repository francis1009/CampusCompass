import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

createApp(App).use(router).mount("#app");

// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.12.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.12.1/firebase-analytics.js";
import { getDatabase, ref, onValue, set, update, get, push, child } from "https://www.gstatic.com/firebasejs/9.12.1/firebase-database.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBTz07CsUuC8llduTdGo_e81mWjQcdw8oI",
    authDomain: "wad2-tripplanner.firebaseapp.com",
    projectId: "wad2-tripplanner",
    storageBucket: "wad2-tripplanner.appspot.com",
    messagingSenderId: "1078917579599",
    appId: "1:1078917579599:web:d59344d7b81a0cb1e97b3a",
    databaseURL: "https://wad2-tripplanner-default-rtdb.asia-southeast1.firebasedatabase.app/"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export { app };