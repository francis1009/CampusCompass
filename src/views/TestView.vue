<template>
    <body>
    <h2>TEST</h2>
    <ul v-if="details">
        <li v-for="school in details" :key="details.School_Code">
            {{ school.School_Name }}
        </li>
    
    </ul>
    <RouterLink to="/test2">
    <button @click="triggerMethod">
        click
    </button>
    </RouterLink>
    </body>
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';
import VueCookies from 'vue-cookies';

export default{
    data() {
        return{
            details: [],
            placeholder: "Test"
        }
    },
    mounted() {
        this.GetSchoolDetails();
    },
    methods: {
        GetSchoolDetails() {
            axios.get('http://localhost:5000/details')
                .then(response => {
                console.log(response.data);
                this.details = response.data;
            })
                .catch( error => {
                console.error(error);
    });
        },
        triggerMethod() {
            VueCookies.set('myCookie', 'insanity', '1d');
            //this.$router.push('/test2');
        }
    }
}


</script>