<template>
  <div class="carousel-container">
    <!-- Background Carousel -->
    <div id="carouselBackground" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div v-for="(imageSrc, index) in carouselImages" :key="index" :class="{ 'carousel-item': true, active: index === 0 }">
          <img :src="imageSrc" class="d-block w-100 image">
          <!-- Content (Question and Options) in the middle of each carousel item -->
          <div class="content">
            <div class="question">
              {{ scenarios[flow].text }}
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
          text: "Question 1: Do you want us to recommend a secondary school for you?",
          options: [
            { text: 'Yes', type: 'btn btn-custom' },
            { text: 'No', type: 'btn btn-custom' },
          ],
        },
        {
          text: "Question 2: Another question text",
          options: [
            { text: 'Option A', type: 'btn btn-custom' },
            { text: 'Option B', type: 'btn btn-custom' },
            // Add more options as needed
          ],
        },
        // Add more questions as needed
      ],
      carouselImages: [
        'src/assets/CHS.jpg',
        'src/assets/NYGH.jpg',
      ],
    };
  },
  methods: {
    handleOptionClick(option) {
      // Handle the click event for the selected option
      console.log('Selected option:', option);

      // Change the flow to the next scenario
      this.flow++;

      // You can add more logic here if needed, e.g., check for the end of scenarios.
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
}

.content {
  position: absolute;
  top: 50%; /* Center vertically */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%); /* Center both horizontally and vertically */
  background: rgba(255, 255, 255, 0.8); /* Add a semi-transparent background to make text more readable */
  padding: 20px; /* Add padding for spacing */
}

.question {
  font-size: 24px;
  color: #253028;
}

.options {
  margin-top: 20px; /* Add spacing between question and options */
}

/* Other CSS styles for buttons */
</style>
