<template>
  <div>
    <div class="search-box">
      <h1 class="search-title">Search Your School</h1>
      <div class="search-input">
        <input type="text" v-model="search" placeholder="Search...">
        <!-- <button @click="AddSchool">Add</button> -->
      </div>
      <ul class="school-list">
  <li v-for="(item, index) in filteredList" :key="index"  @click="addSchoolFromSearch(item)">
    <div class="school-info">
      <img :src="getSchoolLogo(item)" class="school-logo" alt="School Logo" />
      <div class="school-name" v-html="highlightSearchTerm(item)"></div>
    </div>
  </li>
</ul>
    </div>
  </div>





  <h2>Chosen Schools</h2>
  <draggable v-model="selectedSchools" tag="ul" :itemKey="customKey" group="compare_school">
    <template v-slot:item="{ element }">
      <li id="drag">
        <div class="school-item">
          <img :src="getSchoolLogo(element)" class="school-logo" alt="School Logo" />
          {{ element }}
          <button @click="removeSchool(element)">Delete</button>
        </div>
      </li>
    </template>
  </draggable>
  <div class="comparison-container">
    <div class="item-dropzone-area" style="height: 100vh;">
      <h3>Compare School 1</h3>
      <draggable v-model="school_to_compare1" :tag="'ul'" :itemKey="customKey" group="compare_school"
        @change="getschooldetails1">
        <template v-slot:item="{ element }">
          <li id="drag">{{ element }}</li>
        </template>
      </draggable>
      <div v-if="school_to_compare1.length > 0">
        <!-- Content for Compare School 1 -->
        <div v-if="school_to_compare1.length > 0">

          <ul>
            <li v-for="attribute in sch1">
              {{ attribute }}
            </li>
          </ul>

          <div v-for="subject in subjects1">
            <div v-bind:style="{ color: subjects2.includes(subject) ? 'green' : 'red' }">
              {{ subject }}
            </div>

          </div>
        </div>
        <ul>
          <li v-for="attribute in sch1">
            {{ attribute }}
          </li>
        </ul>
        <div v-for="subject in subjects1">
          <div v-bind:style="{ color: subjects2.includes(subject) ? 'green' : 'red' }">
            {{ subject }}
          </div>
        </div>
      </div>
    </div>
    <div class="item-dropzone-area" style="height: 100vh;">
      <h3>Compare School 2</h3>
      <draggable v-model="school_to_compare2" :tag="'ul'" :itemKey="customKey" group="compare_school"
        @change="getschooldetails2">
        <template v-slot:item="{ element }">
          <li>{{ element }}</li>
        </template>
      </draggable>
      <div v-if="school_to_compare2.length > 0">
        <!-- Content for Compare School 2 -->
        <div v-if="school_to_compare2.length > 0">

          <ul>
            <li v-for="attribute in sch2">
              {{ attribute }}
            </li>
          </ul>

          <div v-for="subject in subjects2">
            <div v-bind:style="{ color: subjects1.includes(subject) ? 'green' : 'red' }">
              {{ subject }}
            </div>
          </div>
        </div>
        <ul>
          <li v-for="attribute in sch2">
            {{ attribute }}
          </li>
        </ul>
        <div v-for="subject in subjects2">
          <div v-bind:style="{ color: subjects1.includes(subject) ? 'green' : 'red' }">
            {{ subject }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<style scoped>
.comparison-container {
  display: flex;
  justify-content: space-between;
  border: 1px solid black;
}

.comparison-section {
  flex: 1;
  border: 1px solid black;
}

#drag {
  list-style-image: "";
  background-color: grey;
  margin: 10px;
  height: 100px;
  background: rgba(black, 0.4);
  transition: ease-out;

  /* items grabbed state */
  &[aria-grabbed="true"] {
    background: #5cc1a6;
    color: #fff;
  }
}

.item-dropzone-area {
  height: 6rem;
  background: #888;
  opacity: 0.8;
  animation-duration: 0.5s;
  animation-name: nodeInserted;
  margin-left: 0.6rem;
  margin-right: 0.6rem;
}


.search-box {
  background-color: #007bff;
  color: #fff;
  padding: 20px;
  text-align: center;
}

.search-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.search-input {
  display: flex;
  justify-content: center;
  align-items: center;
}

input {
  width: 70%;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-bottom: 1px solid #fff;
  background: transparent;
  color: #fff;
  outline: none;
}

button {
  background: #fff;
  color: #007bff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.school-list-container {
  background: rgba(0, 0, 0, 0.8);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.school-list {
  list-style: none;
  padding: 0;
  margin: 0;
  max-width: 600px;
}

li {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
  padding: 5px;
  cursor: pointer;
  background: #fff;
  color: #333;
}

.school-logo {
  width: 60px;
  height: 60px;
  margin-right: 10px;
}

.school-name {
  font-size: 18px;
}

strong {
  font-weight: bold;
}
</style>
  

    

<script>
import draggable from 'vuedraggable';
import axios from 'axios';
import { RouterLink } from 'vue-router';
import { faTurkishLiraSign } from '@fortawesome/free-solid-svg-icons';
export default {
  components: {
    draggable,
  },
  data() {
    return {
      search: "",
      schools: [],
      school_logo_pairs: [],
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
        return (this.search && item.toLowerCase().startsWith(this.search.toLowerCase()));
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
            var school_logo_pair = {
              schoolName: response.data[school].School_Name,
              schoollogo: response.data[school].School_Image_Source
            };
            this.SchoolandIDpairs.push(schoolIDpair);
            this.school_logo_pairs.push(school_logo_pair);
          }
          console.log(this.schools);
          console.log(this.SchoolandIDpairs);
          console.log(this.school_logo_pairs);
        })
        .catch(error => {
          console.error(error);
        });
    },
    // AddSchool() {
    //   if (this.search != "" && this.selectedSchools.includes(this.search) == false) {
    //     this.selectedSchools.push(this.search);
    //     this.search = "";
    //   }
    //   else {
    //     alert("Please enter a valid school name")
    //     this.search = "";
    //   }
    // },
    addSchoolFromSearch(schoolName) {
    if (schoolName && !this.selectedSchools.includes(schoolName)) {
      this.selectedSchools.push(schoolName);
      this.search = ""; 
    } else {
      alert("Please enter a valid school name");
    }
  },
    removeSchool(school) {
      // Use this method to remove the selected school from the list
      const index = this.selectedSchools.indexOf(school);
      if (index !== -1) {
        this.selectedSchools.splice(index, 1);
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
        .catch(error => {
          console.error(error);
        });
      axios.get('http://localhost:5000/subjects/' + this.sch1id)
        .then(response => {
          console.log(response.data);
          this.subjects1 = response.data.Subjects_Offered;
          console.log(this.subjects1);

        })
        .catch(error => {
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
        .catch(error => {
          console.error(error);
        });
      axios.get('http://localhost:5000/subjects/' + this.sch2id)
        .then(response => {
          console.log(response.data);
          this.subjects2 = response.data.Subjects_Offered;
          console.log(this.subjects2);

        })
        .catch(error => {
          console.error(error);
        });

    }
  },

};
</script>