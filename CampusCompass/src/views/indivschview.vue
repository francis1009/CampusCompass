<template>
    <body>
        <div v-if="school">
            <img :src=school_image>
            <h2>general info</h2>
            <ul>
                <li>{{ school.School_Name }}</li>
                <li>{{ school.School_Address }}</li>
                <li>{{ school.School_Code }}</li>
                <li>{{ school.School_Postal_Code }}</li>
            </ul>
        </div>
        <div v-if="subjects">
            <h2>subjects</h2>
            <ul>
                <li v-for="subject of subjects">
                    {{ subject }}
                </li>
            </ul>
        </div>
        <div v-if="dsa">
            <h2>dsa</h2>
            <ul>
                <li v-for="dsa of dsa">
                    {{ dsa }}
                </li>
            </ul>
        </div>
        <div v-if="cca">
            <h2>cca</h2>
            <ul>
                <li v-for="cca of cca">
                    {{ cca }}
                </li>
            </ul>
        </div>
        <div v-if="affiliations">
            <h2>affiliations</h2>
            <ul>
                <li v-for="affiliation of affiliations">
                    {{ affiliation }}
                </li>
            </ul>   
        </div>
        <div v-if="psle">
            <h2>psle</h2>
            <ul>
                <li>IP: {{ psle.IP_NonAffiliation }}</li>
                <li>Express: {{ psle.Express_NonAffiliation }}</li>
                <li>Normal(A): {{ psle.NA_NonAffiliation }}</li>
                <li>Normal(T): {{ psle.NT_NonAffiliation }}</li>
            </ul>
        </div>
        <div v-if="electives">
            <h2>electives</h2>
            <ul v-for="elective of electives">
                <li v-for="elective_desc of elective">
                    {{ elective_desc }}
                </li>
            </ul>
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
              electives: []
            
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
                    //this.school_image = response.data.School_Image_Source;
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
        }
    } // methods
};

</script>