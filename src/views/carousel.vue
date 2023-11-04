<template>
  <div class="carousel-container">
    <!-- Background Carousel -->
    <div id="carouselBackground" class="carousel slide" data-bs-ride="carousel" :data-bs-interval="5000">
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
          question: "What subject is your child interested in?",
          options: [
            { text: 'Option A', type: 'btn btn-custom' },
            { text: 'Option B', type: 'btn btn-custom' },
          ],
        },
        {
          question: "What hobbies does your child interested in?",
          options: [
            { text: 'Sports', type: 'btn btn-custom' },
            { text: 'Arts', type: 'btn btn-custom' },
            { text: 'Uniform Group', type: 'btn btn-custom' },
            { text: 'Clubs and Societies', type: 'btn btn-custom' },
          ],
        },
        {
          question: "Which schools' range of PSLE scores are you interested in?",
          options: [
            { text: '4-10', type: 'btn btn-custom' },
            { text: '11-17', type: 'btn btn-custom' },
            { text: '18-24', type: 'btn btn-custom' },
            { text: '25-32', type: 'btn btn-custom' },
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
          image: 'src/assets/CHS.jpg',
          school: 'Catholic High School',
          description: 'Boys School is a messy place. Everyday got fighting',
        },
        {
          image: 'src/assets/NYGH.jpg',
          school: 'Nan Yang Girls School',
          description: 'Girls School',
        },
        // Add more carousel items as needed
      ],
      userResponses: [],
    };
  },
  methods: {
    handleOptionClick(option) {
      if (this.flow === 0 && option.text === 'No') {
        this.$emit('scrollToRecommend');
        return;
      }

      if (this.flow !== 0) {
        this.userResponses.push(option.text);
      }

      if (this.flow === this.scenarios.length - 2) {
        // Give enough time for the user to read the last scenario
        setTimeout(() => {
          this.$emit('scrollToRecommend');
        }, 2000);
      }

      if (option.text === 'Click here to redo the question') {
        this.flow = 0;
        this.userResponses = [];
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
}

.image {
  width: 100%;
  height: auto;
  opacity: 0.1;
  height: 500px; /* Limit the height of the image */
}

.content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
}

.question {
  font-size: 24px;
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

