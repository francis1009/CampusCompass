<template>
    <body>
  <!--Ask why this does not work-->
  <p>
  <a class="btn btn-primary" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Link with href
  </a>
  <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-target
  </button>
</p>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.
  </div>
</div>





    
        <div v-if="school">
            <img width=200 height=200 :src=school_image>
            <h2>general info</h2>
            
            <ul>
                <li>{{ school.School_Name }}</li>
                <li>{{ school.School_Address }}</li>
                <li>{{ school.School_Code }}</li>
                <li>{{ school.School_Postal_Code }}</li>
            </ul>
        </div>
        
         
      
    
        <div v-if="subjects">
            <p>
      <a class="btn btn-primary" @click="toggleCollapseSubjects" role="button" aria-expanded="isCollapsedSubjects" aria-controls="collapseExampleSubjects">
        Subjects
      </a>
         </p>
            <div :class="['collapse', { 'show': isCollapsedSubjects }]" id="collapseExampleSubjects">
            <h2>subjects</h2>
            <ul>
                <li v-for="subject of subjects">
                    {{ subject }}
                </li>
            </ul>
        </div>
    </div>
    
         
        <div v-if="dsa">
            <p>
      <a class="btn btn-primary" @click="toggleCollapseDSA" role="button" aria-expanded="isCollapsedDSA" aria-controls="collapseExampleDSA">
        DSA
      </a>
         </p>
            <div :class="['collapse', { 'show': isCollapsedDSA }]" id="collapseExampleDSA">
            <h2>dsa</h2>
            <ul>
                <li v-for="dsa of dsa">
                    {{ dsa }}
                </li>
            </ul>
            </div>
        </div>
       
    
        <div v-if="cca">
            <p>
      <a class="btn btn-primary" @click="toggleCollapseCCA" role="button" aria-expanded="isCollapsedCCA" aria-controls="collapseExampleCCA">
        CCA
      </a>
         </p>
            <div :class="['collapse', { 'show': isCollapsedCCA }]" id="collapseExampleCCA">
            <h2>cca</h2>
            <ul>
                <li v-for="cca of cca">
                    {{ cca }}
                </li>
            </ul>
        </div>
        </div>
        <div v-if="affiliations">
            <p>
                <a class="btn btn-primary" @click="toggleCollapseAffiliations" role="button" aria-expanded="isCollapsedAffiliations" aria-controls="collapseExampleAffiliations">
                    Affiliated Schools
                </a>
            </p>
            <div :class="['collapse', { 'show': isCollapsedAffiliations }]" id="collapseExampleAffiliations">
            <h2>affiliations</h2>
            <ul>
                <li v-for="affiliation of affiliations">
                    {{ affiliation }}
                </li>
            </ul>   
            </div>
        </div>
        <div v-if="psle">
            <p>
                <a class="btn btn-primary" @click="toggleCollapsePSLE" role="button" aria-expanded="isCollapsedPSLE" aria-controls="collapseExamplePSLE">
                    PSLE scores
                </a>
            </p>
            <div :class="['collapse', { 'show': isCollapsedPSLE }]" id="collapseExamplePSLE">
            <h2>psle</h2>
            <ul>
                <li>IP: {{ psle.IP_NonAffiliation }}</li>
                <li>Express: {{ psle.Express_NonAffiliation }}</li>
                <li>Normal(A): {{ psle.NA_NonAffiliation }}</li>
                <li>Normal(T): {{ psle.NT_NonAffiliation }}</li>
            </ul>
        </div>
        </div>
        <div v-if="electives">
            <p>
                <a class="btn btn-primary" @click="toggleCollapseElective" role="button" aria-expanded="isCollapsedElective" aria-controls="collapseExampleElective">
                    Electives
                </a>
            </p>
            <div :class="['collapse', { 'show': isCollapsedElective }]" id="collapseExampleElective">
            
            <h2>electives</h2>
            <ul v-for="elective of electives">
                <li v-for="elective_desc of elective">
                    {{ elective_desc }}
                </li>
            </ul>
            </div>
        </div>
    </body>
</template>

<script>
import axios from 'axios';


export default {
    data() { 
        return { 
              school: {},
              school_image: "",
              subjects: [],
              dsa: [],
              cca: [],
              special_ed: [],
              affiliations: [],
              psle: {},
              electives: [],
              isCollapsedSubjects: false,
              isCollapsedDSA: false,
              isCollapsedCCA: false,
              isCollapsedAffiliations: false,
              isCollapsedPSLE: false,
              isCollapsedElective: false
            
        };
    }, // data
    mounted() {
        this.GetSchoolDetails();
        this.GetSubjectDetails();
        this.GetCCADetails();
        this.GetDSADetails();
        this.getspecialed();
        this.getaffiliated();
        this.getpslescores();
        this.getelectives();
    }, // mounted
    methods: {
        GetSchoolDetails() {
            axios.get('http://localhost:5000/details/7020')
                .then(response => {
                    console.log(response.data);
                    this.school = response.data;
                    this.school_image = response.data.School_Image_Source;
                    console.log(this.school);

                })
                .catch( error => {
                    console.error(error);
                });
        },
        GetSubjectDetails() {
            axios.get('http://localhost:5000/subjects/7020')
                .then(response => {
                    console.log(response.data);
                    this.subjects = response.data.Subjects_Offered;
                    console.log(this.subjects);

                })
                .catch( error => {
                    console.error(error);
                });
        },
        GetDSADetails() {
            axios.get('http://localhost:5000/dsa/7020')
                .then(response => {
                    console.log(response.data);
                    this.dsa = response.data.DSA_CCA;
                    console.log(this.dsa);
                    
                })
                .catch( error => {
                    console.error(error);
                });
        },
        GetCCADetails() {
            axios.get('http://localhost:5000/cca/7020')
                .then(response => {
                    console.log(response.data);
                    this.cca = response.data.CCA_Offered;
                    console.log(this.cca);
                })
                .catch( error => {
                    console.error(error);
                });
        },
        getspecialed() {
            axios.get('http://localhost:5000/special_ed/7020')
                .then(response => {
                    console.log(response.data);
                    this.special_ed = response.data.Special_Ed_Programmes;
                    console.log(this.special_ed)
                })
                .catch( error => {
                    console.error(error);
                });
        },
        getaffiliated() {
            axios.get('http://localhost:5000/affiliations/7020')
                .then(response => {
                    console.log(response.data);
                    this.affiliations = response.data.Affiliated_Schools;
                    console.log(this.affiliations)
    
                })
                .catch( error => {
                    console.error(error);
                });
        },
        getpslescores() {
            axios.get('http://localhost:5000/psle/7020')
                .then(response => {
                    console.log(response.data);
                    this.psle = response.data;
                    console.log(this.psle);
                })
                .catch( error => {
                    console.error(error);
                });
        },
        getelectives() {
            axios.get('http://localhost:5000/electives/7020')
                .then(response => {
                    console.log(response.data);
                    this.electives = response.data.Electives;
                    console.log(this.electives);
                })
                .catch( error => {
                    console.error(error);
                });
        },
        toggleCollapseSubjects() {
            this.isCollapsedSubjects = !this.isCollapsedSubjects;
        },
        toggleCollapseDSA() {
            this.isCollapsedDSA = !this.isCollapsedDSA;
        },
        toggleCollapseCCA() {
            this.isCollapsedCCA = !this.isCollapsedCCA;
        },
        toggleCollapseAffiliations() {
            this.isCollapsedAffiliations = !this.isCollapsedAffiliations;
        },
        toggleCollapsePSLE() {
            this.isCollapsedPSLE = !this.isCollapsedPSLE;
        },
        toggleCollapseElective() {
            this.isCollapsedElective = !this.isCollapsedElective;
        }

    } // methods
};

</script>

