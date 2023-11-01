<template>
    <div>
      <div class="searchListMainDiv">
        <h1>Search Your School</h1>
        <input type="text" v-model="search" placeholder="Search...">
        <button v-on:click="AddSchool()">Add</button>
        <ul>
          <li v-for="(item, index) in filteredList" :key="index" @click="() => search = item" v-html="item.replace(search, `<strong>${search}</strong>`)"></li>
        </ul>
      </div>
      <h2>Chosen Schools</h2>
      <draggable v-model="selectedSchools" tag="ul" :itemKey="customKey" group="compare_school">
        <template v-slot:item="{ element }">
          <li>{{ element }}</li>
        </template>
      </draggable>
      <div class="comparison-container">
        <div class="comparison-section" style="height: 100vh;" >
          <h3>Compare School 1</h3>
          <draggable v-model="school_to_compare1" :tag="'ul'" :itemKey="customKey" group="compare_school" @change="getschooldetails1">
            <template v-slot:item="{ element }">
              <li>{{ element }}</li>
            </template>
          </draggable>
          <div v-if="school_to_compare1.length > 0">
            <!-- Content for Compare School 1 -->
            <div v-if="school_to_compare1.length > 0">
  
    <ul>
        <li v-for="attribute in sch1">
            {{ attribute}}
        </li>
    </ul>
    
        <div v-for="subject in subjects1">
            <div v-bind:style="{ color : subjects2.includes(subject) ? 'green' : 'red'}"> 
            {{ subject}}
            </div>
            
        </div>
  </div>
            <ul>
              <li v-for="attribute in sch1">
                {{ attribute }}
              </li>
            </ul>
            <div v-for="subject in subjects1">
              <div v-bind:style="{ color : subjects2.includes(subject) ? 'green' : 'red' }">
                {{ subject }}
              </div>
            </div>
          </div>
        </div>
        <div class="comparison-section" style="height: 100vh;" >
          <h3>Compare School 2</h3>
          <draggable v-model="school_to_compare2" :tag="'ul'" :itemKey="customKey" group="compare_school" @change="getschooldetails2">
            <template v-slot:item="{ element }">
              <li>{{ element }}</li>
            </template>
          </draggable>
          <div v-if="school_to_compare2.length > 0">
            <!-- Content for Compare School 2 -->
            <div v-if="school_to_compare2.length > 0">
  
    <ul>
        <li v-for="attribute in sch2">
            {{ attribute}}
        </li>
    </ul>
    
        <div v-for="subject in subjects2">
            <div v-bind:style="{ color : subjects1.includes(subject) ? 'green' : 'red'}"> 
            {{ subject}}
            </div>
        </div>
  </div>
            <ul>
              <li v-for="attribute in sch2">
                {{ attribute }}
              </li>
            </ul>
            <div v-for="subject in subjects2">
              <div v-bind:style="{ color : subjects1.includes(subject) ? 'green' : 'red' }">
                {{ subject }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <style>
    .comparison-container {
      display: flex;
      justify-content: space-between;
      border: 1px solid black;
    }
  
    .comparison-section {
      flex: 1;
      border: 1px solid black;
    }
  </style>
  

    

<script>
import draggable from 'vuedraggable';
import axios from 'axios';
import { RouterLink } from 'vue-router';
export default {
    components: {
    draggable,
  },
    data() {
        return {
            search: "",
            schools: [],
            SchoolandIDpairs: [],
            searchID: "",
            selectedSchools: [],
            school_to_compare1: [],
            school_to_compare2: [],
            sch1id: "",
            sch2id: "",
            sch1: {},
            sch2: {},
            subjects1: [],
            subjects2: []
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
        },
        customKey(item) {
            return item.id; // Specify a unique identifier for each item
        },
        getschooldetails1() {
            console.log(this.school_to_compare1);
            console.log(this.school_to_compare1[0]);
            for (var pair in this.SchoolandIDpairs) {
                
                if (this.SchoolandIDpairs[pair].schoolName == this.school_to_compare1[0]) {
                    this.sch1id = this.SchoolandIDpairs[pair].schoolID;
                    
                }
            }
            console.log(this.sch1id)
            axios.get('http://localhost:5000/details/' + this.sch1id)
                .then(response => {
                    console.log(response.data);
                    this.sch1 = response.data;
                    console.log(this.sch1);

                })
                .catch( error => {
                    console.error(error);
                });
            axios.get('http://localhost:5000/subjects/' + this.sch1id)
                .then(response => {
                    console.log(response.data);
                    this.subjects1 = response.data.Subjects_Offered;
                    console.log(this.subjects1);

                })
                .catch( error => {
                    console.error(error);
                });

        },
        getschooldetails2() {
            console.log(this.school_to_compare2);
            console.log(this.school_to_compare2[0]);
            for (var pair in this.SchoolandIDpairs) {
                
                if (this.SchoolandIDpairs[pair].schoolName == this.school_to_compare2[0]) {
                    this.sch2id = this.SchoolandIDpairs[pair].schoolID;
                    
                }
            }
            console.log(this.sch2id)
            axios.get('http://localhost:5000/details/' + this.sch2id)
                .then(response => {
                    console.log(response.data);
                    this.sch2 = response.data;
                    console.log(this.sch2);

                })
                .catch( error => {
                    console.error(error);
                });
            axios.get('http://localhost:5000/subjects/' + this.sch2id)
                .then(response => {
                    console.log(response.data);
                    this. subjects2 = response.data.Subjects_Offered;
                    console.log(this.subjects2);

                })
                .catch( error => {
                    console.error(error);
                });

        }
    },
    
};
</script>