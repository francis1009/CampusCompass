<template>
    <div>help lah</div>
    <div>{{ receivedMessage }}</div>
    <div v-if="receivedMessage">
        <h1>Test</h1>
    </div>
    <div>
        <button @click="removecookie">
            remove cookie
        </button>
    </div>
  </template>
  
  <script>
  import { eventBus } from '../main.js';
  import VueCookies from 'vue-cookies';
  
  export default {
    data() {
      return {
        receivedMessage: ''
      };
    },
    mounted() {
      // Listen for the event and capture the data
      //eventBus.on('what', payload => {
        //console.log(payload)
        //this.$set(this, 'receivedMessage', payload.message);
        //console.log(this.receivedMessage)
        //this.$forceUpdate();
        this.getCookies();
      },
    methods: {
        getCookies() {
            // Retrieve a cookie using VueCookies
      var myCookieValue = VueCookies.get('myCookie');
      console.log('Retrieved Cookie:', myCookieValue);
      this.receivedMessage = myCookieValue;
      // Do something with the retrieved cookie value
    },
        removecookie() {

            const cookies = VueCookies.get(); // Get all cookies
                for (const cookie in cookies) {
                VueCookies.remove(cookie); // Remove each cookie
                VueCookies.set(cookie, '', -1);
                    }
            console.log('Removed all cookies');
            this.receivedMessage = '';  
        }
      
    },
    beforeDestroy() {
    // Make sure to remove the cookie when the component is destroyed
    console.log('God damn you');
    VueCookies.remove('myCookie');
    }
  };
  </script>
  