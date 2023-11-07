<template>
    <div class="album py-5 bg-white recommend-wrapper">
        <h1 ref="recommend" id="recommend" >View All Schools:</h1>
        <br />
        <div class="container-fluid">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

            <div class="col" v-for="(school, index) in schoolsList" :key="index">
            <SchoolCard :school="school" />
            </div>

        </div>
        </div>
  </div>
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';
import SchoolCard from "../components/schoolcard/SchoolCard.vue";

export default {
    components: {
        
        RouterLink,
        SchoolCard,
    },
    data() {
        return {
            schoolsList: [],
        };
    },
    mounted() {
        this.GetSchoolNames();
    },
    methods: {
        GetSchoolNames() {
            axios.get('http://localhost:5000/details')
                .then(response => {
                var variable = response.data;
                for (var i = 0; i < variable.length; i++) {
                    this.schoolsList.push(variable[i].School_Code);
                }
            })
                .catch( error => {
                console.error(error);
            });
        },
    },
};
</script>

<style scoped>
    img {
        width: auto;
        height: 30px;
        padding-right: 5px;
    }
    form {
        margin-left: 150px;
        margin-right: 100px;
        margin-top: 50px;
    }
    .school-list li {
        list-style-type: none; 
    }
    .school-list li:hover {
        background-color: yellow;
    }
    .school-info {
        display: flex; 
        align-items: center; 
        padding: 5px;
    }
    .recommend-wrapper {
        margin-left: 150px;
        margin-right: 100px;
    }
</style>