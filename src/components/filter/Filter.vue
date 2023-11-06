<template>
    <div class="filter-wrapper">
    <h2>
        Filter
        <font-awesome-icon :icon="['fas', 'filter']" />
    </h2>
    <div class="d-flex container">
        <div class="filter-criteria">
            <div>
                <a class="btn btn-filter" data-bs-toggle="collapse" data-bs-target="#areaCollapse" role="button" 
                    aria-expanded="false" aria-controls="areaCollapse"
                    style="border-radius:20px;" 
                    :class="{'btn-black': !collapses.area, 'btn-green': collapses.area}" 
                    @click="toggleCollapse('area')">
                    Areas  
                    <font-awesome-icon :icon="['fas', 'angle-up']" :class="{'rotate-icon': collapses.area}"/>
                </a>
            </div>
            <div class="checkbox-list collapse" id="areaCollapse">
                <div v-for="area in areas" :key="area">
                    <input type="checkbox" :value="area" v-model="selectedAreas">
                    {{ area }}
                </div>
            </div>
        </div>
        <div class="filter-criteria">
            <div>
                <a class="btn btn-filter" data-bs-toggle="collapse" data-bs-target="#subjectCollapse" role="button" aria-expanded="false" aria-controls="subjectCollapse"
                    style="border-radius:20px" 
                    :class="{'btn-black': !collapses.subject, 'btn-green': collapses.subject}" 
                    @click="toggleCollapse('subject')">
                    Subjects  
                    <font-awesome-icon :icon="['fas', 'angle-up']" :class="{'rotate-icon': collapses.subject}"/>
                </a>
            </div>
            <div class="checkbox-list collapse" id="subjectCollapse">
            <div v-for="subject in subjects" :key="subject">
                <input type="checkbox" :value="subject" v-model="selectedSubjects">
                {{ subject }}
            </div>
            </div>
        </div>
        <div class="filter-criteria">
            <div>
                <a class="btn btn-filter" data-bs-toggle="collapse" data-bs-target="#ccaCollapse" role="button" aria-expanded="false" aria-controls="ccaCollapse"
                    style="border-radius:20px" 
                    :class="{'btn-black': !collapses.cca, 'btn-green': collapses.cca}" 
                    @click="toggleCollapse('cca')">
                    CCA  
                    <font-awesome-icon :icon="['fas', 'angle-up']" :class="{'rotate-icon': collapses.cca}"/>
                </a>
            </div>
            <div class="checkbox-list collapse" id="ccaCollapse">
            <div v-for="cca in ccas" :key="cca">
                <input type="checkbox" :value="cca" v-model="selectedCCAs">
                {{ cca }}
            </div>
            </div>
        </div>
        <div class="filter-criteria">
            <div>
                <a class="btn btn-filter" data-bs-toggle="collapse" data-bs-target="#dsaCollapse" role="button" aria-expanded="false" aria-controls="dsaCollapse"
                    style="border-radius:20px" 
                    :class="{'btn-black': !collapses.dsa, 'btn-green': collapses.dsa}"
                     @click="toggleCollapse('dsa')">
                    DSA  
                    <font-awesome-icon :icon="['fas', 'angle-up']" :class="{'rotate-icon': collapses.dsa}"/>
                </a>
            </div>
            <div class="checkbox-list collapse" id="dsaCollapse">
            <div v-for="dsa in dsas" :key="dsa">
                <input type="checkbox" :value="dsa" v-model="selectedDSAs">
                {{ dsa }}
            </div>
            </div>
        </div>
        <div class="filter-criteria">
            <div>
                <a class="btn btn-filter" data-bs-toggle="collapse" data-bs-target="#speEdCollapse" role="button" aria-expanded="false" aria-controls="speEdCollapse"
                    style="border-radius:20px" 
                    :class="{'btn-black': !collapses.speEd, 'btn-green': collapses.speEd}" 
                    @click="toggleCollapse('speEd')">
                    Special Education  
                    <font-awesome-icon :icon="['fas', 'angle-up']" :class="{'rotate-icon': collapses.speEd}"/>
                </a>
            </div>
            <div class="checkbox-list collapse" id="speEdCollapse">
            <div v-for="se in specialEducations" :key="se">
                <input type="checkbox" :value="se" v-model="selectedSpecialEducations">
                {{ se }}
            </div>
            </div>
        </div>
    <!--    <div>
            <label for="psle-slider">PSLE Score: {{ psle }}</label>
            <input
            id="psle-slider"
            type="range"
            min="4"
            max="32"
            v-model="psle"
            class="form-range"
            />
        </div>-->
    </div>
    <div>
        <center>
            <button @click="getSchoolsByCriteria" class="btn btn-secondary">Apply Filters</button>
        </center>
    </div>
    <div v-if="loading" class="loading-text">Filters are being applied...</div>
    <div v-if="noSchools" class="noSchools-text">No schools match your filters, please try something else :(</div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        components: {
        },
        data(){
            return{
                loading: false,
                noSchools: false,
                collapses: {
                    area: false,
                    subject: false,
                    cca: false,
                    dsa: false,
                    speEd: false
                },
                allSchoolInfo: [],
                mainAreas: ['North', 'North-East', 'Central', 'East', 'West'],
                areas: ['Ang Mo Kio','Bedok','Bishan','Bukit Batok','Bukit Merah','Bukit Panjang',
                    'Bukit Timah','Central','Choa Chu Kang','Clementi','Geylang','Hougang','Jurong East',
                    'Jurong West','Kallang','Marine Parade','Novena','Pasir Ris','Punggol','Queenstown',
                    'Sembawang','Seng Kang','Serangoon','Tampines','Toa Payoh','Woodlands','Yishun'],
                areasNorth: ['Ang Mo Kio', 'Woodlands', 'Sembawang', 'Yishun'],
                areasNorthEast: ['Hougang', 'Punggol', 'Seng Kang','Serangoon'],
                areasCentral:["Bukit Timah","Toa Payoh", "Bukit Merah", "Bishan", "Queenstown","Marine Parade","Novena", "Central"],
                areasEast: ["Jurong East", "Clementi","Bukit Batok","Bukit Panjang","Choa Chu Kang","Jurong West"],
                areasWest: ["Kallang", "Bedok", "Geylang", "Tampines", "Pasir Ris"],
                subjects: ['Additional Mathematics','Aesthetics(Art)','Aesthetics(Design & Technology)',
                    'Aesthetics(Food & Consumer Education)','Aesthetics(Music)','Applied Learning Programme',
                    'Appreciation of Chinese Culture','Art','Art & Design','Art (Ip)','Basic Chinese Language','Basic Malay Language',
                    'Basic Tamil Language','Biology','Chemistry','Chinese Language','Chinese Language (Special Programme)',
                    'Chinese Language Syllabus B','Computer Applications','Computing','Design & Technology','Drama','Elements of Business Skills',
                    'English Language','Exercise & Sports Science','Food & Consumer Education','Geography','Higher Art',
                    'Higher Chinese Language','Higher Malay Language','Higher Music','Higher Tamil Language','History',
                    'Humanities (Ss, Geography)','Humanities (Ss, History)','Humanities (Ss, Literature)','Infocom Technology',
                    'Literature in Chinese','Literature in English','Malay Language','Mathematics','Mobile Robotics','Monfort Development Program',
                    'Music','Music Prepatory Course','Nutrition and Food Science','Performing Arts','Physical Education','Physics','Principles of Accounts',
                    'Regional Studies Programme','Science','Science (Chem, Bio)','Science (Phy, Bio)','Science (Phy, Chem)','Sip: Basic Baking Skills',
                    'Smart Electrical Technology','Social Studies','Tamil Language'],
                ccas: ['Aero-Modelling (Girls and Boys)', 'Angklung/Kulintang Ensemble (Girls and Boys)', 'Angklung/Kulintang Ensemble (Girls)', 
                    'Arts and Crafts (Girls and Boys)','Arts and Crafts (Girls)','Artistic Gymnastics (Girls)','Audio Visual Aid (Boys)',
                    'Audio Visual Aid (Girls and Boys)','Audio Visual Aid (Girls)','Badminton (Girls and Boys)','Badminton (Boys)',
                    'Badminton (Girls)','Band - Military (Girls and Boys)','Basketball (Girls and Boys)','Basketball (Boys)',
                    'Basketball (Girls)','Biological Science (Girls and Boys)','Bowling (Boys)','Bowling (Girls)','Boys\' Brigade (Boys)','Canoeing (Girls and Boys)',
                    'Canoeing (Boys)','Canoeing (Girls)','Chinese Calligraphy and Brush Paiting (Girls and Boys)','Chinese Chess (Boys)','Chinese Chess (Girls and Boys)',
                    'Chinese Culture and Language (Girls)','Chinese Dance (Girls and Boys)','Chinese Dance (Girls and Boys)','Chinese Drama (Girls and Boys)',
                    'Chinese Drama (Girls)','Chinese Drums (Girls and Boys)','Chinese Language, Drama and Debating (Girls)','Chinese Orchestra (Boys)',
                    'Chinese Orchestra (Girls and Boys)','Chinese Orchestra (Girls)','Choir (Boys)','Choir (Girls and Boys)','Choir (Girls)','Community Service (Girls and Boys)',
                    'Community Service (Rotary-Sponsored) (Girls and Boys)','Concert Band (Boys)','Concert Band (Girls and Boys)','Concert Band (Girls)',
                    'Cricket (Boys)','Cross Country (Girls and Boys)','Cross Country (Boys)','Cross Country Girls',
                    'Debating and Public Speaking (Boys)','Debating and Public Speaking (Girls and Boys)','Debating and Public Speaking (Girls)',
                    'Design and Innovation (Boys)','Design and Innovation (Girls and Boys)','Digital Media (Girls and Boys)',
                    'Dragon Boat (Boys)','English Drama (Boys)','English Drama (Girls and Boys)','English Drama (Girls)','English Language, Drama and Debating (Girls and Boys)',
                    'English Language, Drama and Debating (Girls)','Entrepreneurship (Girls and Boys)','Entrepreneurship (Girls)','Environmental Science (Boys)',
                    'Environmental Science (Girls and Boys)','Environmental Science (Girls)','Fencing (Girls and Boys)',
                    'Fencing (Girls)','Floorball (Girls and Boys)','Floorball (Boys)','Floorball (Girls)','Food and Consumer Education (Girls)',
                    'Football (Girls and Boys)','Football (Boys)','Football (Girls)','Gamelan Ensemble (Girls and Boys)','Girl Guides (Girls)',
                    'Golf (Girls and Boys)','Golf (Boys)','Guitar Ensemble (Boys)','Guitar Ensemble (Girls and Boys)','Guitar Ensemble (Girls)',
                    'Guzheng Ensemble (Girls and Boys)','Guzheng Ensemble (Girls)','Handbell Ensemble (Girls)','Harmonica Ensemble (Girls and Boys)','Heritage (Girls)',
                    'Hockey (Girls and Boys)','Hockey (Boys)','Hockey (Girls)',
                    'Indian Dance (Girls and Boys)','Indian Language, Drama and Debating (Girls)','Infocomm Technology (Computing) (Boys)','Infocomm Technology (Computing) (Girls and Boys)',
                    'Infocomm Technology (Computing) (Girls)','Infocomm Technology (Media Production) (Boys)','Infocomm Technology (Media Production) (Girls and Boys)',
                    'Lion and Dragon Dance (Girls and Boys)','Infocomm Technology (Media Production) (Girls)','International Chess (Boys)','International Chess (Girls)','Journalism','Judo (Girls and Boys)',
                    'Karate (Boys)','Malay Culture and Language (Girls and Boys)', 'Malay Dance (Girls and Boys)', 'Malay Dance (Girls)', 'Malay Language, Drama and Debating (Girls)', 
                    'Marching Band (Girls and Boys)','Mathematics (Boys)','Media Resource Library (Boys)','Media Resource Library (Girls and Boys)', 
                    'Media Resource Library (Girls)','Modern Dance (Boys)','Modern Dance (Girls and Boys)','Modern Dance (Girls)','Modular CCA (C&S) (Girls and Boys)', 
                    'Modular CCA (Sports) (Boys)','Modular CCA (Sports) (Girls)','Modular CCA (Vpa) (Boys)','National Cadet Corps (NCC) (Air) (Boys)',
                    'National Cadet Corps (NCC) (Air) (Girls and Boys)','National Cadet Corps (NCC) (Land) (Boys)','National Cadet Corps (NCC) (Land) (Girls and Boys)',
                    'National Cadet Corps (NCC) (Land) (Girls)','National Cadet Corps (NCC) (Sea) (Boys)','National Cadet Corps (NCC) (Sea) (Girls and Boys)',
                    'National Cadet Corps (NCC) (Sea) (Girls)','National Civil Defence Cadet Corps (NCDCC) (Boys)','National Civil Defence Cadet Corps (NCDCC) (Girls',
                    'National Civil Defence Cadet Corps (NCDCC) (Girls)','National Police Cadet Corps (NPCC) (Boys)','National Police Cadet Corps (NPCC) (Girls and Boys',
                    'National Police Cadet Corps (NPCC) (Girls)','National Police Cadet Corps (NPCC) (Sea) (Girls and Boys)','Netball (Girls)',
                    'Outdoor Adventure (Girls and Boys)','Percussion Ensemble (Girls and Boys)', 'Photography (Boys)', 'Photography (Girls and Boys)', 'Photography (Girls)',
                    'Physical Science (Boys)', 'Physical Science (Girls and Boys)', 'Publication (Boys)', 'Red Cross Youth (Girls and Boys)', 'Red Cross Youth (Girls)',
                    'Rhythmic Gymnastics (Girls)', 'Robotics (Boys)', 'Robotics (Girls and Boys)', 'Robotics (Girls)',
                    'Rugby (Boys)', 'Sailing (Boys)', 'Sailing (Girls and Boys)', 'Scouts (Boys)', 'Scouts (Girls and Boys)',
                    'Sepaktakraw (Boys)', 'Shooting (Boys)', 'Shooting (Girls and Boys)', 'Shooting (Girls)',
                    'Singapore Youth Flying Club (Girls and Boys)', 'Softball (Boys)', 'Softball (Girls and Boys)', 'Softball (Girls)',
                    'Space Science (Boys)', 'Speech and Drama (Girls)', 'Squash (Boys)', 'St John Brigade (Boys)', 'St John Brigade (Girls and Boys)', 'St John Brigade (Girls)',
                    'Strategy Games (Girls and Boys)', 'Strategy Games (Girls)', 'String Ensemble (Boys)', 'String Ensemble (Girls and Boys)', 'String Ensemble (Girls)',
                    'Student Leadership (Council) (Girls and Boys)', 'Student Leadership (House) (Girls and Boys)', 'Student Leadership (Prefect) (Girls and Boys)',
                    'Swimming (Boys)', 'Swimming (Girls and Boys)', 'Table Tennis (Boys)', 'Table Tennis (Girls and Boys)', 'Table Tennis (Girls)',
                    'Taekwondo (Girls and Boys)', 'Tamil Drama (Girls and Boys)', 'Tchoukball', 'Tchoukball (Girls and Boys)', 'Tchoukball (Girls)',
                    'Tennis (Boys)', 'Tennis (Girls)', 'Touch Rugby (Girls)', 'Track and Field (Boys)', 'Track and Field (Girls and Boys)', 'Track and Field (Girls)',
                    'Volleyball (Boys)', 'Volleyball (Girls and Boys)', 'Volleyball (Girls)', 'Water Polo (Boys)', 'Wushu (Boys)', 'Wushu (Girls and Boys)'
                    ],
                dsas:[
                    'Aerospace (Girls and Boys)', 'Angklung/Kulintang Ensemble (Girls and Boys)', 'Angklung/Kulintang Ensemble (Girls)', 'Applied Sciences - Forensic Science (Girls and Boys)', 
                    'Art Elective Programme (Boys)', 'Art Elective Programme (Boys) - IP', 'Art Elective Programme (Girls and Boys)', 'Artistic Gymnastics (Girls)', 'Artistic Gymnastics (Girls) - IP', 
                    'Artistic Swimming (Girls)', 'Artistic Swimming (Girls) - IP', 'Badminton (Boys)', 'Badminton (Boys) - IP', 'Badminton (Girls and Boys)', 'Badminton (Girls)', 
                    'Badminton (Girls) - IP', 'Basketball (Boys)', 'Basketball (Boys) - IP', 'Basketball (Girls and Boys)', 'Basketball (Girls)', 'Basketball (Girls) - IP', 'Bilingualism (Boys)', 
                    'Bilingualism (Girls and Boys)', 'Bowling (Boys)', 'Bowling (Boys) - IP', 'Bowling (Girls and Boys)', 'Bowling (Girls)', 'Boys\' Brigade (Boys)', 'Canoeing (Boys)', 
                    'Canoeing (Boys) - IP', 'Canoeing (Girls and Boys)', 'Canoeing (Girls)', 'Chemical and Applied Sciences (Fragrance) (Girls and Boys)', 'Chinese and Modern Dance (Girls and Boys)', 
                    'Chinese and Modern Dance (Girls)', 'Chinese Calligraphy (Girls and Boys)', 'Chinese Dance (Girls and Boys)', 'Chinese Dance (Girls)', 'Chinese Drama (Girls and Boys)', 
                    'Chinese Drama (Girls)', 'Chinese Drama (Girls) - IP', 'Chinese Language (Boys)', 'Chinese Language (Girls and Boys)', 'Chinese Language (Girls)', 'Chinese Language (Girls) - IP', 
                    'Chinese Orchestra (Boys)', 'Chinese Orchestra (Boys) - IP', 'Chinese Orchestra (Girls and Boys)', 'Chinese Orchestra (Girls)', 'Chinese Painting (Girls and Boys)', 
                    'Chinese Weiqi (Boys)', 'Choir (Boys)', 'Choir (Boys) - IP', 'Choir (Girls and Boys)', 'Choir (Girls)', 'Choir (Girls) - IP', 'Coding (Girls and Boys)', 'Communication (Girls and Boys)', 
                    'Community Youth Leadership (Girls and Boys)', 'Community Youth Leadership (Girls)', 'Computational Thinking Skills (Girls and Boys)', 'Concert Band (Boys)', 'Concert Band (Boys) - IP', 
                    'Concert Band (Girls and Boys)', 'Concert Band (Girls)', 'Concert Band (Girls) - IP', 'Cricket (Boys)', 'Cricket (Boys) - IP', 'Critical Social Inquiry and Media Literacy (Girls and Boys)', 
                    'Cross Country (Boys)', 'Cross Country (Boys) - IP', 'Cross Country (Girls and Boys)', 'Debate and Theatre (Boys)', 'Debate and Theatre (Boys) - IP', 'Debating (Boys)', 
                    'Debating (Girls and Boys)', 'Debating (Girls)', 'Debating And Public Speaking (Girls and Boys)', 'Debating And Public Speaking (Girls)', 'Design, Technology and Engineering (DTE) (Girls and Boys)', 
                    'Digital Media (Girls and Boys)', 'Electronics (Girls and Boys)', 'Engineering Innovation and Solutions (Girls and Boys)', 'English Drama (Boys)', 'English Drama (Girls and Boys)', 
                    'English Drama (Girls)', 'English Drama (Girls) - IP', 'English Language (Boys)', 'English Language (Girls and Boys)', 'English Language (Girls)', 'English Language (Girls) - IP', 
                    'Entrepreneurship (Girls and Boys)', 'Environmental Science (Girls and Boys)', 'Fencing (Boys)', 'Fencing (Girls and Boys)', 'Floorball (Boys)', 'Floorball (Boys) - IP', 
                    'Floorball (Girls and Boys)', 'Floorball (Girls)', 'Food Science and Technology (Girls and Boys)', 'Football (Boys)', 'Football (Boys) - IP', 'Football (Girls and Boys)', 
                    'Football (Girls)', 'Girl Guides (Girls)', 'Girls\' Brigade (Girls)', 'Golf (Boys)', 'Golf (Boys) - IP', 'Golf (Girls and Boys)', 'Guitar Ensemble (Boys)', 'Guitar Ensemble (Girls and Boys)', 
                    'Guitar Ensemble (Girls)', 'Guzheng Ensemble (Girls and Boys)', 'Guzheng Ensemble (Girls)', 'Handbell Ensemble (Girls)', 'Handbell Ensemble (Girls) - IP', 'Harmonica Ensemble (Girls and Boys)', 
                    'Harp Ensemble (Girls and Boys)', 'Hockey (Boys)', 'Hockey (Boys) - IP', 'Hockey (Girls and Boys)', 'Hockey (Girls)', 'Humanities (Boys)', 'Humanities (Boys) - IP', 
                    'Humanities (Girls and Boys)', 'Indian Dance (Girls and Boys)', 'Indian Dance (Girls)', 'Infocomm (Boys)', 'Innovation (Girls and Boys)', 'International Chess (Boys)', 
                    'International Chess (Boys) - IP', 'Journalism (Girls and Boys)', 'Judo (Boys)', 'Judo (Girls and Boys)', 'Leadership (Boys)', 'Leadership (Boys) - IP', 'Leadership (Girls and Boys)', 
                    'Leadership (Girls)', 'Leadership (Girls) - IP', 'Leadership and Character (Boys)', 'Leadership and Character (Girls and Boys)', 'Malay Dance (Girls and Boys)', 'Malay Language (Boys)', 
                    'Malay Language (Girls and Boys)', 'Malay Language (Girls)', 'Malay Language (Girls) - IP', 'Marching Band (Girls and Boys)', 'Mathematics (Boys)', 'Mathematics (Boys) - IP', 
                    'Mathematics (Girls and Boys)', 'Mathematics (Girls)', 'Mathematics (Girls) - IP', 'Mechatronics, Aeronautics and Robotics (Girls and Boys)', 'Media (Girls and Boys)', 
                    'Media Arts/Film/Photography (Girls and Boys)', 'Media/Journalism (Girls and Boys)', 'Military Band (Girls and Boys)', 'Modern Dance (Girls and Boys)', 'Modern Dance (Girls)', 
                    'Modern Dance (Girls) - IP', 'Music (Boys)', 'Music (Girls and Boys)', 'Music Elective Programme (Boys)', 'Music Elective Programme (Boys) - IP', 'Music Elective Programme (Girls and Boys)', 
                    'Music Elective Programme (Girls)', 'National Cadet Corps (NCC) Land (Boys)', 'National Cadet Corps (NCC) Sea (Boys)', 'National Cadet Corps (NCC) Sea (Girls and Boys)', 
                    'National Civil Defence Cadet Corps (NCDCC) (Girls and Boys)', 'National Police Cadet Corps (NPCC) (Boys)', 'Netball (Girls and Boys)', 'Netball (Girls)', 'Outdoor Activities (Boys)', 
                    'Outdoor Activities (Girls and Boys)', 'Outdoor Adventure (Girls and Boys)', 'Outdoor Adventure (Girls)', 'Painting (Girls and Boys)', 'Performing Arts (Girls and Boys)', 
                    'Performing Arts (Girls)', 'Piano (Girls and Boys)', 'Public Speaking and Debate (Girls and Boys)', 'Red Cross (Girls and Boys)', 'Robotics (Girls and Boys)', 
                    'Science and Mathematics (Girls and Boys)', 'Scouts (Boys)', 'Scouts (Girls and Boys)', 'Shooting (Boys)', 'Shooting (Boys) - IP', 'Shooting (Girls and Boys)', 'Shooting (Girls)', 
                    'Softball (Boys)', 'Softball (Girls and Boys)', 'Softball (Girls)', 'Speech and Drama (Girls and Boys)', 'St. John Brigade (Girls and Boys)', 'Strings Ensemble (Girls and Boys)', 
                    'Strings Ensemble (Girls)', 'Student Leadership (Girls and Boys)', 'Swimming (Boys)', 'Swimming (Boys) - IP', 'Swimming (Girls and Boys)', 'Swimming (Girls)', 'Swimming (Girls) - IP', 
                    'Synchronized Swimming (Girls)', 'Table Tennis (Boys)', 'Table Tennis (Boys) - IP', 'Table Tennis (Girls and Boys)', 'Table Tennis (Girls)', 'Table Tennis (Girls) - IP', 
                    'Taekwondo (Boys)', 'Taekwondo (Girls and Boys)', 'Taekwondo (Girls)', 'Tamil Language (Boys)', 'Tamil Language (Girls and Boys)', 'Tamil Language (Girls)', 'Tamil Language (Girls) - IP', 
                    'Tennis (Boys)', 'Tennis (Boys) - IP', 'Tennis (Girls and Boys)', 'Tennis (Girls)', 'Track and Field (Boys)', 'Track and Field (Boys) - IP', 'Track and Field (Girls and Boys)', 
                    'Track and Field (Girls)', 'Volleyball (Boys)', 'Volleyball (Boys) - IP', 'Volleyball (Girls and Boys)', 'Volleyball (Girls)', 'Visual Arts (Girls and Boys)', 'Visual Arts (Girls)', 
                    'Wind Orchestra (Girls and Boys)', 'Wind Orchestra (Girls)', 'Woodwind Ensemble (Girls and Boys)', 'Woodwind Ensemble (Girls)', 'Wushu (Boys)', 'Wushu (Boys) - IP', 'Wushu (Girls and Boys)', 
                    'Wushu (Girls)'
                ],
                specialEducations: ['Barrier-free accessibility', 'Moderate to profound hearing loss (Oral Approach)', 
                    'Moderate to profound hearing loss (Signing Approach)','Moderate to profound visual impairment',
                    'Special Educational Needs Officers'],
                psle: 15,
                selectedAreas: [],
                selectedSubjects: [],
                selectedCCAs: [],
                selectedDSAs:[],
                selectedSpecialEducations: [],
                filteredSchools: []
            }
        },
        mounted() {
        },
        methods: {
            toggleCollapse(section) {
                this.collapses[section] = !this.collapses[section];
                
            },
            async getSchoolsByCriteria() {
                this.noSchools = false;
                this.filteredSchools = [];
                this.$router.push({
                    name: 'search', 
                    query: { schoolsList: JSON.stringify([]) }
                });
                console.log("started");
                this.loading = true;
                try  {
                    
                    const schoolsResponse = await axios.get('http://localhost:5000/details');
                    const allSchools = schoolsResponse.data;
            

                    const areaPromises = this.selectedAreas.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/details/${school.School_Code}`).catch(e => e)) : [];
                    const subjectPromises = this.selectedSubjects.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/subjects/${school.School_Code}`).catch(e => e)) : [];
                    const ccaPromises = this.selectedCCAs.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/cca/${school.School_Code}`).catch(e => e)) : [];
                    const dsaPromises = this.selectedDSAs.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/dsa/${school.School_Code}`).catch(e => e)) : [];
                    const speEdPromises = this.selectedSpecialEducations.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/special_ed/${school.School_Code}`).catch(e => e)) : [];

                    const [areas, subjects, ccas, dsas, speEds] = await Promise.all([
                        Promise.all(areaPromises),
                        Promise.all(subjectPromises),   
                        Promise.all(ccaPromises),
                        Promise.all(dsaPromises),
                        Promise.all(speEdPromises)
                    ]);


                    for (let i = 0; i < allSchools.length; i++) {
                        const school = allSchools[i];
                        const hasSelectedRegion = this.selectedAreas.length === 0 || this.selectedAreas.includes(areas[i]?.data?.School_Region);
                        const hasAllSelectedSubjects = this.selectedSubjects.length === 0 || this.selectedSubjects.every(subject => subjects[i]?.data?.Subjects_Offered.includes(subject));
                        const hasAllSelectedCCAs = this.selectedCCAs.length === 0 || this.selectedCCAs.every(cca => ccas[i]?.data?.CCA_Offered.includes(cca));
                        const hasAllSelectedDSAs = this.selectedDSAs.length === 0 || this.selectedDSAs.every(dsa => dsas[i]?.data?.DSA_CCA.includes(dsa));
                        const hasAllSelectedSpeEd = this.selectedSpecialEducations.length === 0 || this.selectedSpecialEducations.every(se => speEds[i]?.data?.Special_Education_Support.includes(se));

                        if (hasSelectedRegion && hasAllSelectedSubjects && hasAllSelectedCCAs && hasAllSelectedDSAs && hasAllSelectedSpeEd) {
                            this.filteredSchools.push(school.School_Code);
                        }
                    }
                } catch (error) {
                    console.error('Error fetching data:', error);
                }
                console.log("filtered schools: "+this.filteredSchools);
                this.loading=false;
                if(this.filteredSchools.length == 0){
                    this.noSchools = true;
                }
                this.$router.push({
                    name: 'search', 
                    query: { schoolsList: JSON.stringify(this.filteredSchools) }
                });
            },
        },
    };
</script>

<style scoped>
    h2{
        margin-bottom: 30px;
    }
    .filter-criteria {
        margin: 20px;
        width: 250px;
        height: 350px;
        position: relative;
    }
    .checkbox-list {
        max-height: 225px;
        overflow-y: auto;
        
    }
    .filter-wrapper {
        margin-left: 150px;
        margin-right: 100px;
        margin-bottom: 20px;
    }
    .checkbox-list::-webkit-scrollbar-track,
    .checkbox-list::-webkit-scrollbar {
        width: 10px; 
        background-color: #f5f5f5; 
    }

    .checkbox-list::-webkit-scrollbar-thumb {
        background-color: #888; 
        border-radius: 5px; 
        border: 2px solid #f5f5f5; 
    }

    .checkbox-list::-webkit-scrollbar-thumb:hover {
        background-color: #555;
    }

    label {
        font-size: 
    }

    .btn-green {
        background-color: #50ad82;
        color: white;
        margin: 20px
    }
    .btn-black {
        background-color: #4d4d4d;
        color: white;
        margin: 20px
    }
    .loading-text {
        text-align: center;
        margin: 20px;
    }
    .collapse-icon {
        position: absolute;
        bottom: 0;
        color: white;
        transition: 0.2s linear;
    }
    .rotate-icon {
        transform: rotate(180deg);
        transition: transform 0.2s;
    }
</style>