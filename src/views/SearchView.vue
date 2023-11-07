<template>
        <!--<h2>Search for School</h2>
        <div class="searchListMainDiv">
        <h1>Search Your School</h1>
        <input type="text" v-model="search" placeholder="Search...">
        <button v-on:click="SearchforSchool()">Search</button>
        <ul>
          <li v-for="(item, index) in filteredList" :key="index" @click="() => search = item" v-html="item.replace(search, `<strong>${search}</strong>`)"></li>
        </ul>
    </div>-->
    <form>
        <div class="form-group">
        <div>
            <div class="search-box">
            <h1 class="search-title">Search Your School</h1>
            <div class="search-input">
                <input type="text" v-model="search" placeholder="Search..." class="form-control">
                <!-- <button @click="AddSchool">Add</button> -->
            </div>
            <ul class="school-list">
            <li v-for="(item, index) in filteredList" :key="index"  @click="SearchforSchool(item)">
                <div class="school-info">
                <img :src="getSchoolLogo(item)" class="school-logo" alt="School Logo" />
                <div class="school-name" v-html="highlightSearchTerm(item)"></div>
                </div>
            </li>
            </ul>
                </div>
            </div>
        </div>
    </form>
    <br /> <br />
    <Filter />

    <div class="album py-5 bg-white recommend-wrapper">
        <h1 ref="recommend" id="recommend" >These are your recommended schools:</h1>
        <br />
        <div class="container-fluid">
        <div class="row row-cols-xl-3 row-cols-md-2 row-cols-1 g-3">

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
import Filter from '../components/filter/Filter.vue';
import SchoolCard from "../components/SchoolCard.vue";

export default {
    components: {
        Filter,
        RouterLink,
        SchoolCard,
    },
    props: {
        schoolsList: {
            type: Array,
            required: false,
            default: () => []
        }
    },
    data() {
        return {
            search: "",
            schools: [],
             school_logo_pairs: [],
            SchoolandIDpairs: [],
            searchID: ""
        };
    },
    computed: {
        filteredList() {
      return this.schools.filter((item) => {
        return this.search && item.toLowerCase().startsWith(this.search.toLowerCase());
      });
    },
    },
    mounted() {
        this.GetSchoolNames();

        this.$router.push({
            name: 'search', 
            query: { schoolsList: JSON.stringify([]) }
        });
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
                    var school_logo_pair = {
              schoolName: response.data[school].School_Name,
              schoollogo: response.data[school].School_Image_Source
                    };
                    this.SchoolandIDpairs.push(schoolIDpair);
                    this.school_logo_pairs.push(school_logo_pair);
                }
                console.log(this.schools);
                console.log(this.SchoolandIDpairs);
            })
                .catch(error => {
                console.error(error);
            });
        },
        SearchforSchool(schoolName) {
            console.log(schoolName);
            for (var pair in this.SchoolandIDpairs) {
                if (this.SchoolandIDpairs[pair].schoolName == schoolName) {
                    console.log(this.SchoolandIDpairs[pair].schoolID);
                    this.searchID = this.SchoolandIDpairs[pair].schoolID;
                    console.log(this.searchID)

                    this.$router.push('/indivschool/' + this.searchID);
                }
            }
        },
         getSchoolLogo(schoolName) {
      const schoolLogoPair = this.school_logo_pairs.find(pair => pair.schoolName === schoolName);
      console.log(schoolLogoPair);
      return schoolLogoPair.schoollogo;
    },
    highlightSearchTerm(item) {
    // Use regular expression to match and replace the search term with the highlighted version
    if (this.search) {
      const searchRegex = new RegExp(this.search, 'ig');
      return item.replace(searchRegex, match => `<strong>${match}</strong>`);
    } else {
      return item; // If there's no search term, return the original text
    }
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
    .school-list {
        width: 100%; 
        z-index: 10; 
        max-height: 300px;
        overflow-y: auto;
        top: 100%; 
        left: 0;
        margin: 0; 
        padding: 0; 
        border: 1px solid #ccc;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
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