<template>
    <body>
        <h2>Search for School</h2>
        <div class="searchListMainDiv">
        <h1>Search Your School</h1>
        <input type="text" v-model="search" placeholder="Search...">
        <button v-on:click="AddSchool()">Add</button>
        <ul>
          <li v-for="(item, index) in filteredList" :key="index" @click="() => search = item" v-html="item.replace(search, `<strong>${search}</strong>`)"></li>
        </ul>
    </div>
    <ul v-for="school in selectedSchools">
        <li> {{ school }} </li>
    </ul>
    </body>
</template>

<script>
import axios from 'axios';
import { RouterLink } from 'vue-router';
export default {
    data() {
        return {
            search: "",
            schools: [],
            SchoolandIDpairs: [],
            searchID: "",
            selectedSchools: [],
            school_to_compare1: [],
            school_to_compare2: [],
        };
    },
    computed: {
        filteredList() {
            return this.schools.filter(item => {
                return (this.search && item.toLowerCase().includes(this.search.toLowerCase()));
            });
        },
    },
    mounted() {
        this.GetSchoolNames();
    },
    methods: {
        GetSchoolNames() {
            axios.get('http://localhost:5000/details')
                .then(response => {
                console.log(response.data);
                for (var school in response.data) {
                    this.schools.push(response.data[school].School_Name);
                    var schoolIDpair = {
                        schoolName: response.data[school].School_Name,
                        schoolID: response.data[school].School_Code
                    };
                    this.SchoolandIDpairs.push(schoolIDpair);
                }
                console.log(this.schools);
                console.log(this.SchoolandIDpairs);
            })
                .catch(error => {
                console.error(error);
            });
        },
        AddSchool() {
            this.selectedSchools.push(this.search);
        }
    },
    components: { RouterLink }
};
</script>