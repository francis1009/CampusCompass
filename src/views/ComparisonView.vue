<template>
  <div class="container-fluid" style="width:97vw">
    <div class="row">
      <div class="col-12">
        <h1 class="search-title">Search Your School</h1>
        <div class="search-box">
          <div class="search-input">
            <input
              type="text"
              class="form-control"
              v-model="search"
              placeholder="Search..."
              @input="showResults = search.length > 0"
            />
          </div>
          <div class="search-results" v-show="showResults">
            <ul class="list-group">
              <li
                v-for="(item, index) in filteredList"
                :key="index"
                @click="addSchoolFromSearch(item)"
                class="list-group-item list-group-item-action d-flex justify-content-start align-items-center"
              >
                <img :src="getSchoolLogo(item)" class="school-logo" alt="School Logo" />
                <span class="ml-3">{{ item }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-4">
      <div class="col-12">
        <h2>Chosen Schools</h2>
      </div>
    </div>

    <div class="row">
      <div class="col-12">
        <table class="table chosen-schools-table">
          <thead>
            
          </thead>
          <tbody>
            <draggable
              v-model="selectedSchools"
              :options="{ animation: 150 }"
              :element="'tbody'"
              group="compare_school"
            >
              <template v-slot:item="{ element, index }">
                <tr>
                  <td><img :src="getSchoolLogo(element)" class="school-logo" alt="School Logo" /></td>
                  <td>{{ element }}</td>
                  <td>
                    <button @click="removeSchool(index)" class="btn btn-danger">
                      <font-awesome-icon icon="fas fa-trash" />
                    </button>
                  </td>
                </tr>
              </template>
            </draggable>
          </tbody>
        </table>
      </div>
    </div>
    
  
        
        <div class="container-fluid ">
          <div class="row">
          <!-- Start of compare 1 -->
          <div class="comparison-box col-6 col-md-12">
            <div
              class="item-dropzone-area"
              style="height: 100vh;"
            >
              <h3>Compare School 1</h3>
              <draggable
                v-model="school_to_compare1"
                :tag="'ul'"
                :itemKey="customKey"
                group="compare_school"
                @change="getschooldetails1"
              >
                <template v-slot:item="{ element }">
                  <div id="drag"><h3>{{ element }}</h3></div>
                </template>
              </draggable>
              <!-- Content for Compare School 1 -->
              <div v-if="school_to_compare1.length > 0">
                <div class="table-container">
                  <table class="table table-bordered">
                    <tbody>
                      
                      <tr>
                        <td>Address</td>
                        <td>{{ sch1.School_Address }}</td>
                      </tr>
                      <tr>
                        <td>School Name</td>
                        <td>{{ sch1.School_Name }}</td>
                      </tr>
                      <tr>
                        <td>School Website</td>
                        <td>
                          <a
                            :href="sch1.School_Website"
                            target="_blank"
                          >{{ sch1.School_Website }}</a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="table-container">
                 
           
              <h4>Subjects Offered</h4>
          
       
              <div class="table-scroll">
                  <table class="table chosen-schools-table" >
                    <tbody>
                      <tr v-for="subject in subjects1">
                        <div v-bind:style="{ color: subjects2.includes(subject) ? 'green' : 'red' }">{{ subject }}</div>
                      </tr>
                    </tbody>
                  </table>
                  </div>
  
                </div>
                <br>
                <div class="table-container">
                  
                  <h4>PSLE Details</h4>
                  <div class="table-scroll">
                  <table class="table chosen-schools-table" >
                    <tbody>
                      <tr>
                        <th>Track</th>
                        <th>Cut-off</th>
                      </tr>
                      <!-- Customize the PSLE details here -->
                      <tr v-if="psle1.Express_Affiliation !== '-'">
                        <td>Express Affiliated</td>
                        <td>{{ psle1.Express_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle1.Express_NonAffiliation !== '-'">
                        <td>Express Non-Affiliated</td>
                        <td>{{ psle1.Express_NonAffiliation }}</td>
                      </tr>
                      <tr v-if="psle1.IP_Affiliation !== '-'">
                        <td>IP Affiliated</td>
                        <td>{{ psle1.IP_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle1.IP_NonAffiliation !== '-'">
                        <td>IP Non-Affiliated</td>
                        <td>{{ psle1.IP_NonAffiliation }}</td>
                      </tr>
                      <tr v-if="psle1.NA_Affiliation !== '-'">
                        <td>Normal Academic Affiliated</td>
                        <td>{{ psle1.NA_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle1.NA_NonAffiliation !== '-'">
                        <td>Normal Academic Non-Affiliated</td>
                        <td>{{ psle1.NA_NonAffiliation }}</td>
                      </tr>
                      <tr v-if="psle1.NT_Affiliation !== '-'">
                        <td>Normal Technical Affiliated</td>
                        <td>{{ psle1.NT_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle1.NT_NONAffiliation !== '-'">
                        <td>Normal Technical Non-Affiliated</td>
                        <td>{{ psle1.NT_NONAffiliation }}</td>
                      </tr>
                     
                    </tbody>
                  </table>
                </div>
                </div>  
                <br>
                <div class="table-container">
             
              <h4>CCA Offered</h4>
        
          <div class="table-scroll">
                  <table class="table chosen-schools-table">
                    <tbody>
                      <tr v-for="cca in cca1" :class="{ 'highlight-difference': sch1.CCA_Offered !== sch2.CCA_Offered }">
                        <div v-bind:style="{ color: cca2.includes(cca) ? 'green' : 'red' }">{{ cca }}</div>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            </div>  
          </div>
          <!-- End of compare 1 -->
          
          <!-- Start of compare 2 -->
          <div class="container comparison-box col-6 col-md-12">
          
            <div
              class="item-dropzone-area"
              style="height: 100vh;"
            >
              <h3 >Compare School 2</h3>
              <draggable
                v-model="school_to_compare2"
                :tag="'ul'"
                :itemKey="customKey"
                group="compare_school"
                @change="getschooldetails2"
              >
                <template v-slot:item="{ element }">
                  <div id="drag"><h3>{{ element }}</h3></div>
                </template>
              </draggable>
              <!-- Content for Compare School 2 -->
              <div v-if="school_to_compare2.length > 0">
                <div class="table-container">
                  <table class="table table-bordered">
                    <tbody>
                      
                      <tr>
                        <td>Address</td>
                        <td>{{ sch2.School_Address }}</td>
                      </tr>
                      <tr>
                        <td>School Name</td>
                        <td>{{ sch2.School_Name }}</td>
                      </tr>
                      <tr>
                        <td>School Website</td>
                        <td>
                          <a
                            :href="sch2.School_Website"
                            target="_blank"
                          >{{ sch2.School_Website }}</a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="table-container">
                  <table class="table table-bordered">
              <h4>Subjects Offered</h4>
                    
          </table>
          <div class="table-scroll">
                  <table class="table chosen-schools-table" >
                    <tbody>
                      <tr v-for="subject in subjects1" >
                        <div v-bind:style="{ color: subjects1.includes(subject) ? 'green' : 'red' }">{{ subject }}</div>
                      </tr>
                    </tbody>
                  </table>
                </div>
                </div>
                <br>
                <div class="table-container">
                  <h4>PSLE Details</h4>
                  <div class="table-scroll">
                  <table class="table chosen-schools-table" >
                    <tbody>
                      <tr>
                        <th>Track</th>
                        <th>Cut-off</th>
                      </tr>
                      <!-- Customize the PSLE details here -->
                      <tr v-if="psle2.Express_Affiliation !== '-'">
                        <td>Express Affiliated</td>
                        <td>{{ psle2.Express_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle2.Express_NonAffiliation !== '-'">
                        <td>Express Non-Affiliated</td>
                        <td>{{ psle2.Express_NonAffiliation }}</td>
                      </tr>
                      <tr v-if="psle2.IP_Affiliation !== '-'">
                        <td>IP Affiliated</td>
                        <td>{{ psle2.IP_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle2.IP_NonAffiliation !== '-'">
                        <td>IP Non-Affiliated</td>
                        <td>{{ psle2.IP_NonAffiliation }}</td>
                      </tr>
                      <tr v-if="psle2.NA_Affiliation !== '-'">
                        <td>Normal Academic Affiliated</td>
                        <td>{{ psle2.NA_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle2.NA_NonAffiliation !== '-'">
                        <td>Normal Academic Non-Affiliated</td>
                        <td>{{ psle2.NA_NonAffiliation }}</td>
                      </tr>
                      <tr v-if="psle2.NT_Affiliation !== '-'">
                        <td>Normal Technical Affiliated</td>
                        <td>{{ psle1.NT_Affiliation }}</td>
                      </tr>
                      <tr v-if="psle2.NT_NONAffiliation !== '-'">
                        <td>Normal Technical Non-Affiliated</td>
                        <td>{{ psle2.NT_NONAffiliation }}</td>
                      </tr>
                     
                    </tbody>
                  </table>
                </div>
              </div>
                <br>
                <div class="table-container">
                  <table class="table table-bordered">
              <h4>CCA Offered</h4>
    
          </table>
          <div class="table-scroll">
                  <table class="table chosen-schools-table">
                    <tbody>
                      <tr v-for="cca in cca2" >
                        <div v-bind:style="{ color: cca1.includes(cca) ? 'green' : 'red' }">{{ cca }}</div>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              </div>
     </div>
          </div>
          </div>
          <!-- End of compare 2 -->
        </div>
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
        cca1: [],
        psle1: {},
        cca2: [],
        psle2: {},
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
      axios.get('http://localhost:5000/cca/' + this.sch1id)
        .then(response => {
            console.log(response.data);
            this.cca1 = response.data.CCA_Offered;
            console.log(this.cca1);
        })
        .catch(error => {
            console.error(error);
        });
     axios.get('http://localhost:5000/psle/' + this.sch1id)
        .then(response => {
            console.log(response.data);
            this.psle1 = response.data;
            console.log(this.psle1);
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
        axios.get('http://localhost:5000/cca/' + this.sch2id)
        .then(response => {
            console.log(response.data);
            this.cca2 = response.data.CCA_Offered;
            console.log(this.cca2);
        })
        .catch(error => {
            console.error(error);
        });
     axios.get('http://localhost:5000/psle/' + this.sch2id)
        .then(response => {
            console.log(response.data);
            this.psle2 = response.data;
            console.log(this.psle2);
        })
        .catch(error => {
            console.error(error);
            
        });

        
    }
  },

};
</script>

<style scoped>

  .container-fluid {
  padding: 20px;
  width: 100%; /* Set the container to 100% width */
  max-width: none; /* Remove any maximum width constraint */
  margin-left: 0; /* Reset left margin */
  margin-right: 0; /* Reset right margin */
}


.search-title {
  font-size: 24px;
  text-align: center;
}

.search-box {
  text-align: center;
}

.search-input {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  padding: 10px;
}

.search-input input {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  box-shadow: none;
  font-size: 16px;
}

.search-results {
  position: absolute;
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  background: #fff;
  border: 1px solid #ccc;
  border-top: 0;
}

.search-results ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.search-results li {
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
}

.search-results li:last-child {
  border-bottom: none;
}

.school-logo {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

.chosen-schools-table {
  border: 1px solid #ccc;
  width: 100%;
}

.chosen-schools-table th {
  background-color: #f0f0f0;
  text-align: center;
  padding: 10px;
}

.chosen-schools-table td {
  text-align: center;
  padding: 10px;
}

.comparison-container {
  
  width: 100%;
  justify-content: space-between;
}

.comparison-box {
  
  margin: 10px;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  background-color: #f9f9f9;
}

.comparison-box h3 {
  text-align: center;
  background-color: #f0f0f0;
  padding: 10px;
  margin: 0;
}

.comparison-box ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.comparison-box li {
  padding: 5px;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
}






.comparison-box th, .comparison-box td {
  text-align: center;
  padding: 10px;
}
.table-container {
  overflow: auto;
  max-height: 300px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Adjust column width as needed */
  grid-gap: 10px; /* Adjust the gap between tables as needed */
}

/* Style for the header table (fixed) */
.header-table {
  width: 100%;
  position: sticky;
  top: 0;
  z-index: 1;
  background-color: #fff; /* You can change the background color as needed */
}

/* Style for the scrolling table body */
.table-scroll {
  max-height: 100%;
  overflow-y: auto;
}
.highlight-difference {
    background-color: yellow; /* You can choose any color for highlighting */
  }
/* Add responsive styles for different screen sizes here */

.comparison-container {
  display: flex;
  justify-content: space-between;
  overflow-x: auto; /* Enable horizontal scrolling if needed */
}

.comparison-box {
  flex: 1;
  margin: 10px;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  background-color: #f9f9f9;
  max-width: calc(50% - 20px); /* Adjust the width as needed */
}

</style>
