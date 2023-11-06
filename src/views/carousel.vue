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
      selectedMainArea: [],
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

      if (this.flow === 1) {
        this.selectedMainArea.push(option.text);
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
          this.selectedSubjects.push('Drama');
          this.selectedSubjects.push('Music');
        }
      }

      if (this.flow === 3) {
        if (option.text === 'Sports') {
          this.selectedCCAs.push('Basketball (Girls and Boys)');
          this.selectedCCAs.push('Badminton (Girls and Boys)');
          this.selectedCCAs.push('Football (Girls and Boys)');
          this.selectedCCAs.push('Table Tennis (Girls and Boys)');
        } else if (option.text === 'Arts') {
          this.selectedCCAs.push('Arts and Crafts (Girls and Boys)');
          this.selectedCCAs.push('Concert Band (Girls and Boys)');
          this.selectedCCAs.push('Modern Dance (Girls and Boys)');
          this.selectedCCAs.push('English Drama (Girls and Boys)');
        } else if (option.text === 'Uniform Group') {
          this.selectedCCAs.push('Boys\' Brigade (Boys)');
          this.selectedCCAs.push('St John Brigade (Girls and Boys)');
          this.selectedCCAs.push('National Police Cadet Corps (NPCC) (Girls and Boys)');
          this.selectedCCAs.push('National Cadet Corps (NCC) (Land) (Girls and Boys)');
        }
      }

      if (this.flow === this.scenarios.length - 2) {
        // Give enough time for the user to read the last scenario
        setTimeout(() => {
          // Use VueCookies to store the user responses for 1 year
          VueCookies.set('userData', this.userResponses, '1y');
          // Check if the cookie is set
          var myCookieValue = VueCookies.get('userData');
          console.log('Retrieved Cookie:', myCookieValue);
          this.$emit('scrollToRecommend');
        }, 4000);
      }

      if (option.text === 'Click here to redo the question') {
        this.flow = 0;
        this.userResponses = [];

        // Remove the 'userResponses' cookie when redoing the question
        VueCookies.remove('userData');
        // Check if the cookie is removed
        var myCookieValue = VueCookies.get('userData');
        console.log('Retrieved Cookie:', myCookieValue);
      }
      this.flow++;
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

