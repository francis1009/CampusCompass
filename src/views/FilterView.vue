<template>
    <!--<div>
        <h2>Search for School</h2>
            <div class="searchListMainDiv">
            <h1>Search Your School</h1>
            <input type="text" v-model="search" placeholder="Search...">
            <button v-on:click="SearchforSchool()">Search</button>
            <ul>
            <li v-for="(item, index) in filteredList" :key="index" @click="() => search = item" v-html="item.replace(search, `<strong>${search}</strong>`)"></li>
            </ul>
        </div>
    </div>-->
    <!-- <div>
    <div class="search-box">
      <h1 class="search-title">Search Your School</h1>
      <div class="search-input">
        <input type="text" v-model="search" placeholder="Search...">
       
      </div>
      <ul class="school-list">
  <li v-for="(item, index) in filteredList" :key="index"  @click="() => search = item" v-html="item.replace(search, `<strong>${search}</strong>`)">
    <div class="school-info">
      <img :src="getSchoolLogo(item)" class="school-logo" alt="School Logo" />
      <div class="school-name" v-html="highlightSearchTerm(item)"></div>
    </div>
  </li>
</ul>
    </div>
  </div> -->
    <Filter />
</template>

<script>
    import axios from 'axios';
    import { RouterLink } from 'vue-router';
    import Filter from '../components/filter/Filter.vue'

    export default {
        components: {
            Filter,
            RouterLink
        },
        data(){
            return {
                search: "",
                schools: [],
                SchoolandIDpairs: [],
                searchID: ""
            };
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
            SearchforSchool() {
                console.log(this.search);
                for (var pair in this.SchoolandIDpairs) {
                    if (this.SchoolandIDpairs[pair].schoolName == this.search) {
                        console.log(this.SchoolandIDpairs[pair].schoolID);
                        this.searchID = this.SchoolandIDpairs[pair].schoolID;
                        console.log(this.searchID)

                        this.$router.push('/indivschool/' + this.searchID);
                    }
                }
            }
        },
    };
</script>