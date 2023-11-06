<template>
  <div class="carousel-container">
    <!-- Background Carousel -->
    <div id="carouselBackground" class="carousel slide">
      <div class="carousel-inner">
        <div v-for="(carousel, index) in carousels" :key="index" :class="{ 'carousel-item': true, active: index === 0 }">
          <img :src="carousel.image" class="d-block w-100 image">
          <!-- Content (Question and Options) in the middle of each carousel item -->
          <div class="content">
            <div class="question">
              {{ scenarios[flow].question }}
            </div>
            <div class="options">
              <button
                v-for="(option, optionIndex) in scenarios[flow].options"
                :key="optionIndex"
                :class="option.type"
                @click="handleOptionClick(option)"
              >
                {{ option.text }}
              </button>
            </div>
          </div>
          <!-- School and Description at the bottom left -->
          <div class="school-description">
            <div class="school-name">{{ carousel.school }}</div>
            <div class="description">{{ carousel.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      flow: 0, // Initialize to show the first scenario
      scenarios: [
        {
          question: "Do you want us to recommend a secondary school for you?",
          options: [
            { text: 'Yes', type: 'btn btn-custom' },
            { text: 'No', type: 'btn btn-custom' },
          ],
        },
        {
          question: "Where do you live?",
          options: [
            { text: 'North', type: 'btn btn-custom' },
            { text: 'Northeast', type: 'btn btn-custom' },
            { text: 'Central', type: 'btn btn-custom' },
            { text: 'East', type: 'btn btn-custom' },
            { text: 'West', type: 'btn btn-custom' },       
          ],
        },
        {
          question: "What subject are you/is your child interested in?",
          options: [
            { text: 'Language', type: 'btn btn-custom' },
            { text: 'Math', type: 'btn btn-custom' },
            { text: 'Science', type: 'btn btn-custom' },
            { text: 'Humanities', type: 'btn btn-custom' },
            { text: 'Art', type: 'btn btn-custom' },
            { text: 'Others', type: 'btn btn-custom' },
          ],
        },
        {
          question: "What hobbies are you/is your child interested in?",
          options: [
            { text: 'Sports', type: 'btn btn-custom' },
            { text: 'Arts', type: 'btn btn-custom' },
            { text: 'Uniform Group', type: 'btn btn-custom' },
            { text: 'Clubs and Societies', type: 'btn btn-custom' },
          ],
        },
        {
          question: "Thank you!",
          options: [
            { text: 'Click here to redo the question', type: 'btn btn-custom' },
          ]
        },
      ],
      carousels: [
        {
          image: 'src/assets/NYGH.jpg',
        },
        // Add more carousel items as needed
      ],
      userResponses: [],
      selectedAreas: [],
      selectedSubjects: [],
      selectedCCAs: [],
      filteredSchools: []
    };
  },
  mounted() {
    // Check if the user has answered the questions before
  },
  methods: {
    handleOptionClick(option) {
      if (this.flow === 0 && option.text === 'No') {
        this.$router.push('/search');
        return;
      }

      if (option.text === 'Click here to redo the question') {
        this.flow = 0;
        this.userResponses = [];
        this.selectedAreas = [];
        this.selectedSubjects = [];
        this.selectedCCAs = [];
        this.filteredSchools = [];
      }

      if (this.flow === 1) {
        if (option.text === 'North') {
          this.selectedAreas.push('Ang Mo Kio');
          this.selectedAreas.push('Woodlands');
          this.selectedAreas.push('Sembawang');
          this.selectedAreas.push('Yishun');
        } else if (option.text === 'Northeast') {
          this.selectedAreas.push('Hougang');
          this.selectedAreas.push('Punggol');
          this.selectedAreas.push('Seng Kang');
          this.selectedAreas.push('Serangoon');
        } else if (option.text === 'Central') {
          this.selectedAreas.push('Bukit Timah');
          this.selectedAreas.push('Toa Payoh');
          this.selectedAreas.push('Bukit Merah');
          this.selectedAreas.push('Bishan');
          this.selectedAreas.push('Queenstown');
          this.selectedAreas.push('Marine Parade');
          this.selectedAreas.push('Novena');
          this.selectedAreas.push('Central');
        } else if (option.text === 'West') {
          this.selectedAreas.push('Jurong East');
          this.selectedAreas.push('Clementi');
          this.selectedAreas.push('Bukit Batok');
          this.selectedAreas.push('Bukit Panjang');
          this.selectedAreas.push('Choa Chu Kang');
          this.selectedAreas.push('Jurong West');
        } else if (option.text === 'East') {
          this.selectedAreas.push('Kallang');
          this.selectedAreas.push('Bedok');
          this.selectedAreas.push('Geylang');
          this.selectedAreas.push('Tampines');
          this.selectedAreas.push('Pasir Ris');
        }
      }

      if (this.flow === 2) {
        if (option.text === 'Language') {
          this.selectedSubjects.push('English Language');
          this.selectedSubjects.push('Chinese Language');
          this.selectedSubjects.push('Malay Language');
          this.selectedSubjects.push('Tamil Language');
        } else if (option.text === 'Math') {
          this.selectedSubjects.push('Additional Mathematics');
          this.selectedSubjects.push('Mathematics');
        } else if (option.text === 'Science') {
          this.selectedSubjects.push('Biology');
          this.selectedSubjects.push('Chemistry');
          this.selectedSubjects.push('Physics');
        } else if (option.text === 'Humanities') {
          this.selectedSubjects.push('Geography');
          this.selectedSubjects.push('History');
          this.selectedSubjects.push('Literature in English');
        } else if (option.text === 'Art') {
          this.selectedSubjects.push('Art');
          this.selectedSubjects.push('Design & Technology');
        }
      }

      if (this.flow === 3) {
        if (option.text === 'Sports') {
          this.selectedCCAs.push('Basketball (Girls and Boys)');
          this.selectedCCAs.push('Badminton (Girls and Boys)');
        } else if (option.text === 'Arts') {
          this.selectedCCAs.push('Concert Band (Girls and Boys)');
          this.selectedCCAs.push('Modern Dance (Girls and Boys)');
          this.selectedCCAs.push('English Drama (Girls and Boys)');
        } else if (option.text === 'Uniform Group') {
          this.selectedCCAs.push('St John Brigade (Girls and Boys)');
          this.selectedCCAs.push('National Police Cadet Corps (NPCC) (Girls and Boys)');
          this.selectedCCAs.push('National Cadet Corps (NCC) (Land) (Girls and Boys)');
        }

        this.getSchoolsByCriteria();
      }

      if (this.flow === this.scenarios.length - 2) {
        // Give enough time for the user to read the last scenario
        setTimeout(() => {
          this.$emit('scrollToRecommend');
        }, 4000);
      }
      this.flow++;
    },
    async getSchoolsByCriteria() {
                this.filteredSchools = [];
                this.$router.push({
                    name: 'recommended', 
                    query: { schoolsList: JSON.stringify([]) }
                });
                console.log("started");
                try  {
                    
                    const schoolsResponse = await axios.get('http://localhost:5000/details');
                    const allSchools = schoolsResponse.data;

                    const areaPromises = this.selectedAreas.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/details/${school.School_Code}`).catch(e => e)) : [];
                    const subjectPromises = this.selectedSubjects.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/subjects/${school.School_Code}`).catch(e => e)) : [];
                    const ccaPromises = this.selectedCCAs.length !== 0 ? allSchools.map(school => axios.get(`http://localhost:5000/cca/${school.School_Code}`).catch(e => e)) : [];
                    
                    const [areas, subjects, ccas] = await Promise.all([
                        Promise.all(areaPromises),
                        Promise.all(subjectPromises),   
                        Promise.all(ccaPromises),
                    ]);

                    for (let i = 0; i < allSchools.length; i++) {
                      console.log(i)
                        const school = allSchools[i];
                        const hasSelectedRegion = this.selectedAreas.length === 0 || this.selectedAreas.includes(areas[i]?.data?.School_Region);
                        const hasAllSelectedSubjects = this.selectedSubjects.length === 0 || this.selectedSubjects.every(subject => subjects[i]?.data?.Subjects_Offered.includes(subject));
                        const hasAllSelectedCCAs = this.selectedCCAs.length === 0 || this.selectedCCAs.every(cca => ccas[i]?.data?.CCA_Offered.includes(cca));
                        if (hasSelectedRegion && hasAllSelectedSubjects && hasAllSelectedCCAs) {
                            this.filteredSchools.push(school.School_Code);
                        }
                    }
                } catch (error) {
                    console.error('Error fetching data:', error);
                }
                console.log("filtered schools: " + this.filteredSchools);
                this.loading=false;
                this.$router.push({
                    name: 'recommended', 
                    query: { schoolsList: JSON.stringify(this.filteredSchools) }
                });
    },
  },
};
</script>

<style scoped>
.carousel-container {
  position: relative;
}

.carousel-item {
  position: relative;
  text-align: center; /* Center-align the content within each carousel item */
  height: 100vh;
}

.image {
  width: 100%;
  height: auto;
  opacity: 0.1;
  object-fit: cover;
  /* height: 500px; Limit the height of the image */
}

.btn-custom {
  background-color: #253028;
  color: #fff;
  border: 1px solid #253028;
  border-radius: 10px;
  padding: 10px 20px;
  margin: 10px;
  font-size: 20px;
  font-weight: bold;
}

.content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
}

.question {
  font-size: 56px;
  color: #253028;
  font-weight: bold;
}

.options {
  margin-top: 20px;
}

/* Position school and description at the bottom left */
.school-description {
  position: absolute;
  bottom: 0;
  left: 0;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 10px;
  text-align: left;
}

.school-name {
  font-size: 18px;
  font-weight: bold;
}

.description {
  font-size: 16px;
  max-width: 300px; /* Adjust the maximum width as needed */
  word-wrap: break-word; /* Break the text into multiple lines */
}
</style>

