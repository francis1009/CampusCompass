<template>
  <div style="width:95vw">
    <div class="search-box">
      <h1 class="search-title">Search Your School</h1>
      <div class="search-input">
        <input type="text" v-model="search" placeholder="Search..." @input="showResults = search.length > 0" />
      </div>
      <div class="search-results" v-show="showResults">
        <ul class="search-results-list">
          <li v-for="(item, index) in filteredList" :key="index" @click="addSchoolFromSearch(item)">
            <img :src="getSchoolLogo(item)" class="school-logo" alt="School Logo" />
            <span>{{ item }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <h2>Chosen Schools</h2>

<table class="chosen-schools-table">
  <thead>
    <!-- <tr v-if="selectedSchools.length > 0">
      <th>School Logo</th>
      <th>School Name</th>
      <th></th>
    </tr> -->
  </thead>
  <tbody>
    <draggable v-model="selectedSchools" :options="{ animation: 150 }" :element="'tbody'" group="compare_school">
          <template v-slot:item="{ element, index }">
            <tr>
              <td><img :src="getSchoolLogo(element)" class="school-logo" alt="School Logo" /></td>
              <td>{{ element }}</td>
              <td>
                <button @click="removeSchool(index)"><font-awesome-icon icon="fa-solid fa-angle-double-left" /></button>
              </td>
            </tr>
          </template>
        </draggable>
  </tbody>
</table>

  <!-- <div class="container fluid"></div>
  <draggable v-model="selectedSchools" tag="ul" :itemKey="customKey" group="compare_school">
    <template v-slot:item="{ element }" :move="handleMoveItem" @end="handleDragEndItem">
      <div class="school-item">
        <img :src="getSchoolLogo(element)" class="school-logo" alt="School Logo" />
        {{ element }}
        <button @click="removeSchool(element)"><font-awesome-icon icon="fa-solid fa-angle-double-left" /></button>
      </div>
    </template>
  </draggable>
   -->
  <div class="comparison-container">
    <!-- Start of compare 1 -->
    <div class="comparison-box">
      <div class="item-dropzone-area" style="height: 100vh;">
        <h3 style="text-align: center;">Compare School 1</h3>
        <draggable v-model="school_to_compare1" :tag="'ul'" :itemKey="customKey" group="compare_school"
          @change="getschooldetails1" :move="handleMoveItem" @end="handleDragEndItem">
          <template v-slot:item="{ element }">
            <div id="drag">{{ element }}</div>
          </template>
        </draggable>
        <!-- Content for Compare School 1 -->
        <div v-if="school_to_compare1.length > 0">
          <ul>
            <div v-for="attribute in sch1">{{ attribute }}</div>
          </ul>
          <div v-for="subject in subjects1">
            <div v-bind:style="{ color: subjects2.includes(subject) ? 'green' : 'red' }">{{ subject }}</div>
          </div>
        </div>
      </div>
    </div>
    <!-- End of compare 1 -->
    <!-- Start of compare 2 -->
    <div class="comparison-box">
      <div class="item-dropzone-area" style="height: 100vh;">
        <h3 style="text-align: center;">Compare School 2</h3>
        <draggable v-model="school_to_compare2" :tag="'ul'" :itemKey="customKey" group="compare_school"
          @change="getschooldetails2" :move="handleMoveItem" @end="handleDragEndItem">
          <template v-slot:item="{ element }">
            <li>{{ element }}</li>
          </template>
        </draggable>
        <!-- Content for Compare School 2 -->
        <div v-if="school_to_compare2.length > 0">
          <ul>
            <li v-for="attribute in sch2">{{ attribute }}</li>
          </ul>
          <div v-for="subject in subjects2">
            <div v-bind:style="{ color: subjects1.includes(subject) ? 'green' : 'red' }">{{ subject }}</div>
          </div>
        </div>
      </div>
    </div>
    <!-- End of compare 2 -->
  </div>
</template>



<script>
import draggable from 'vuedraggable';
import axios from 'axios';
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
      subjects2: [],
      compare_value1: false,
      compare_value2: false,
      showResults: false,
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
    removeSchool(index) {
      // Use this method to remove the selected school from the list
      // const index = this.selectedSchools.indexOf(school);
      // if (index !== -1) {
      //   this.selectedSchools.splice(index, 1);
      // }
      this.selectedSchools.splice(index, 1);
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
      //this.compare_value1 = true; 
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
      //this.compare_value2 = true; 
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

<style scoped>
.comparison-container {
  display: flex;
  justify-content: space-between;
  border: 1px solid black;
}

.comparison-box {
  flex: 1;
  border: 1px solid black;
  height: auto;
}

.search-results {
  position: absolute;
  width: 100%;
  max-height: 300px; /* Adjust the maximum height as needed */
  overflow-y: auto; /* Enable vertical scrolling when needed */
  background: #fff;
  border: 1px solid #ccc;
  border-top: 0;
}

.search-results-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.search-results-list li {
  padding: 5px 10px;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
}

.search-results-list li:last-child {
  border-bottom: none;
}
.school-logo {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

</style>