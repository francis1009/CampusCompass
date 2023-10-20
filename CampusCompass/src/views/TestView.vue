<template>
    <body>
    <h2>TEST</h2>
    <ul v-if="details">
        <li v-for="school in details" :key="details.School_Code">
            {{ school.School_Name }}
        </li>
    
    </ul>
    </body>
</template>

<script>
import axios from 'axios';
export default{
    data() {
        return{
            details: []
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
        }
    }
}


</script>