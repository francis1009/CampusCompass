<template>
    <body>
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
                <a class="btn btn-primary" @click="toggleCollapseSubjects" role="button" aria-expanded="isCollapsedSubjects"
                    aria-controls="collapseExampleSubjects">
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
                <a class="btn btn-primary" @click="toggleCollapseDSA" role="button" aria-expanded="isCollapsedDSA"
                    aria-controls="collapseExampleDSA">
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
                <a class="btn btn-primary" @click="toggleCollapseCCA" role="button" aria-expanded="isCollapsedCCA"
                    aria-controls="collapseExampleCCA">
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
                <a class="btn btn-primary" @click="toggleCollapseAffiliations" role="button"
                    aria-expanded="isCollapsedAffiliations" aria-controls="collapseExampleAffiliations">
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
                <a class="btn btn-primary" @click="toggleCollapsePSLE" role="button" aria-expanded="isCollapsedPSLE"
                    aria-controls="collapseExamplePSLE">
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
                <a class="btn btn-primary" @click="toggleCollapseElective" role="button" aria-expanded="isCollapsedElective"
                    aria-controls="collapseExampleElective">
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
            <div v-if="one_map">
                <p>
                    <a class="btn btn-primary" @click="toggleCollapseMap" role="button" aria-expanded="isCollapsedMap"
                        aria-controls="collapseExampleMap">
                        Map
                    </a>
                </p>
                <div :class="['collapse', { 'show': isCollapsedMap }]" id="collapseExampleMap">

                    <h2>Map</h2>
                    <img :src=one_map alt="map" />
                </div>
            </div>
        </div>

        <div>
            <div>
            <iframe :src=minimapsrc height="500" width="800" scrolling="no" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
            </div>
            <input type="text" v-model="inputpostalcode" placeholder="please input postal code">

        <button @click="updateminimapsrc">
            update
        </button>
        </div>
        

        <div>
            <h1>Routes</h1>
            <input type="text" v-model="originpostal" placeholder="please input origin postal code">
            <button @click="displayroutes">
                display routes
            </button>
            <div v-if="route_data">
                <div>Route</div>
                <div v-for="leg in route_steps">
                    
                    <div v-if="leg.mode == 'BUS'">   
                        <div>Take bus {{ leg.route }} from {{ leg.from.name }} to {{ leg.to.name }}</div>
                    </div>
                    <div v-else-if="leg.mode == 'SUBWAY'">
                        <div>Take the {{ leg.route_long_name }} from {{ leg.from.stopCode }} to {{ leg.to.stopCode }}</div>
                    </div>
                    <div v-else-if="leg.mode == 'WALK'">
                        <div>Walk from {{ leg.from.name }} to {{ leg.to.name }}</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
import axios from 'axios';


export default {
    props: ['searchID'],
    data() {
        return {
            school: {},
            new_postal_code: "",
            school_image: "",
            subjects: [],
            dsa: [],
            cca: [],
            special_ed: [],
            affiliations: [],
            psle: {},
            electives: [],
            one_map: "",
            isCollapsedSubjects: false,
            isCollapsedDSA: false,
            isCollapsedCCA: false,
            isCollapsedAffiliations: false,
            isCollapsedPSLE: false,
            isCollapsedElective: false,
            isCollapsedMap: false,
            minimapsrc: "",
            subset: "",
            inputpostalcode: "",
            originpostal: "",
            originlat: "",
            originlong:"",
            destlat: "",
            destlong: "",
            route_data: {},
            route_steps: []



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
        this.getmap();
        this.getminimapsource();
    }, // mounted
    // computed: {
    //     postal_code(){
    //         return this.school.School_Postal_Code.slice(0,8);
    //     }

    // },
    methods: {
        async GetSchoolDetails() {
            console.log(this.searchID)
            console.log(this.searchID);
            try {
            await axios.get('http://localhost:5000/details/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.school = response.data;
                    this.school_image = response.data.School_Image_Source;
                    console.log(this.school);
                    this.new_postal_code = response.data.School_Postal_Code.slice(1,7);
                    console.log(this.new_postal_code);

                })
            }
                catch(error) {
                    console.error(error);
                };
        },
        GetSubjectDetails() {
            axios.get('http://localhost:5000/subjects/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.subjects = response.data.Subjects_Offered;
                    console.log(this.subjects);

                })
                .catch(error => {
                    console.error(error);
                });
        },
        GetDSADetails() {
            axios.get('http://localhost:5000/dsa/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.dsa = response.data.DSA_CCA;
                    console.log(this.dsa);

                })
                .catch(error => {
                    console.error(error);
                });
        },
        GetCCADetails() {
            axios.get('http://localhost:5000/cca/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.cca = response.data.CCA_Offered;
                    console.log(this.cca);
                })
                .catch(error => {
                    console.error(error);
                });
        },
        getspecialed() {
            axios.get('http://localhost:5000/special_ed/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.special_ed = response.data.Special_Ed_Programmes;
                    console.log(this.special_ed)
                })
                .catch(error => {
                    console.error(error);
                });
        },
        getaffiliated() {
            axios.get('http://localhost:5000/affiliations/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.affiliations = response.data.Affiliated_Schools;
                    console.log(this.affiliations)

                })
                .catch(error => {
                    console.error(error);
                });
        },
        getpslescores() {
            axios.get('http://localhost:5000/psle/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.psle = response.data;
                    console.log(this.psle);
                })
                .catch(error => {
                    console.error(error);
                });
        },
        getelectives() {
            axios.get('http://localhost:5000/electives/' + this.searchID)
                .then(response => {
                    console.log(response.data);
                    this.electives = response.data.Electives;
                    console.log(this.electives);
                })
                .catch(error => {
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
        },
        toggleCollapseMap() {
            this.isCollapsedMap = !this.isCollapsedMap;
        },
        async getmap() {
           await this.GetSchoolDetails();
           try {
                console.log(this.new_postal_code)
                axios.get(`https://www.onemap.gov.sg/api/staticmap/getStaticImage?layerchosen=default&zoom=17&width=400&height=512&postal=${this.new_postal_code}`)
                    .then(response => {
                        console.log(response.data);
                        this.one_map = response.config.url;
                        console.log(response.config.url);
                    })
                
           }
            
                catch(error) {
    
                    console.log("ONE MAP ERROR");
                    console.error(error);
                };

        },
        async getminimapsource() {
            await this.GetSchoolDetails();
            try {
                this.minimapsrc = `https://www.onemap.gov.sg/amm/amm.html?mapStyle=Night&zoomLevel=15&marker=postalcode:${this.new_postal_code}!colour:red&popupWidth=200`
                console.log(this.minimapsrc)    
            }
            catch(error) {
    
                    console.log("ONE MAP ERROR");
                    console.error(error);
                };  
        }, 
        updateminimapsrc() {
            if (this.inputpostalcode.length != 6) {
                alert("Please input a valid postal code");
                return;
            }
            var length = this.minimapsrc.length;
            this.subset = this.minimapsrc.slice(0, length-14);
            console.log(this.subset);
            this.minimapsrc = this.subset + `marker=postalcode:${this.inputpostalcode}!colour:red&popupWidth=200`;
            console.log(this.minimapsrc);
        },
        async displayroutes() {
            if (this.originpostal.length != 6) {
                alert("Please input a valid postal code");
                return;
            }
            await this.GetSchoolDetails();
            try {
                axios.get(`https://www.onemap.gov.sg/api/common/elastic/search?searchVal=${this.originpostal}&returnGeom=Y&getAddrDetails=Y&pageNum=1`)
                    .then(response => {
                        console.log(response.data);
                        this.originlat = response.data.results[0].LATITUDE;
                        this.originlong = response.data.results[0].LONGITUDE;
                        console.log(this.originlat);
                        console.log(this.originlong);
                        axios.get(`https://www.onemap.gov.sg/api/common/elastic/search?searchVal=${this.new_postal_code}&returnGeom=Y&getAddrDetails=Y&pageNum=1`)
                            .then(response => {
                                console.log(response.data);
                                this.destlat = response.data.results[0].LATITUDE;
                                this.destlong = response.data.results[0].LONGITUDE;
                                console.log(this.destlat);
                                console.log(this.destlong);
                                var current_date = new Date();
                                console.log(current_date)
                                var month = ("0" + (current_date.getMonth() + 1)).slice(-2);
                                var day = ("0" + current_date.getDate()).slice(-2);
                                var year = current_date.getFullYear();  
                                var hours = current_date.getHours();
                                var minutes = current_date.getMinutes();
                                var seconds = current_date.getSeconds();
                                console.log(month);
                                console.log(day);
                                axios.get(`https://www.onemap.gov.sg/api/public/routingsvc/route?start=${this.originlat}%2C${this.originlong}&end=${this.destlat}%2C${this.destlong}&routeType=pt&date=${month}-${day}-${year}&time=${hours}%3A${minutes}%3A${seconds}&mode=TRANSIT`, {
                                            headers: {
                                                "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjNmFlMDQwNDU5MjA5MjkyMGNlMTU3NzU4Mzg3Njc3YyIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjk5MTkzMDIyLCJleHAiOjE2OTk0NTIyMjIsIm5iZiI6MTY5OTE5MzAyMiwianRpIjoiQTY0TjJ1RXZOMmNxTzlPdiIsInVzZXJfaWQiOjExNTQsImZvcmV2ZXIiOmZhbHNlfQ.B_OzEzNfZnRldrr94HlxNLaBVJ3_khLYQpXZYjb6_Qo"
                                            }
                                        })
                                    .then(response => {
                                        console.log(response.data);
                                        this.route_data = response.data;
                                        console.log(this.route_data)
                                        this.route_steps = response.data.plan.itineraries[0].legs;
                                        console.log(this.route_steps)
                                        
                                    })
                                
                            })
                    })
            }
            catch(error) {
                console.log("ONE MAP ERROR");
                console.error(error);
            };
        
        }

    } // methods
};

</script>

<style>
</style>
