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
import axios from 'axios';

export default {
  data() {
    return {
      flow: 0, // Initialize to show the first scenario
      scenarios: [
        {
          question: "Question 1: Do you want us to recommend a secondary school for you?",
          options: [
            { text: 'Yes', type: 'btn btn-custom' },
            { text: 'No', type: 'btn btn-custom' },
          ],
        },
        {
          question: "Question 2: If yes is click",
          options: [
            { text: 'Option A', type: 'btn btn-custom' },
            { text: 'Option B', type: 'btn btn-custom' },
            // Add more options as needed
          ],
        },
        {
          question: "Question 3: If no is click",
          options: [
            { text: 'Option A', type: 'btn btn-custom' },
            { text: 'Option B', type: 'btn btn-custom' },
            // Add more options as needed
          ],
        },
        // Add more questions as needed
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
    };
  },
  methods: {
    handleOptionClick(option) {
      // Handle the click event for the selected option

      
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

