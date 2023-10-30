<template>
  <div>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div v-for="(question, index) in questions" :key="index" :class="{ 'carousel-item': true, active: index === 0 }">
          <img :src="question.imageSrc" class="d-block w-100 image" :alt="question.imageAlt">
          <div class="question">
            {{ question.text }}
          </div>
          <div class="button">
            <button v-for="(option, optionIndex) in question.options" :key="optionIndex" :class="option.type" @click="handleOptionClick(option)">
              {{ option.text }}
            </button>
          </div>
        </div>
      </div>
      <!-- Add your carousel controls here -->
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      flow: 1,
      questions: [
        {
          text: "Question 1: Do you want us to recommend a secondary school for you?",
          imageSrc: 'src/assets/CHS.jpg',
          imageAlt: 'Image 1',
          options: [
            { text: 'Yes', type: 'btn btn-primary' },
            { text: 'No', type: 'btn btn-primary' },
          ],
        },
        {
          text: "Question 2: Another question text",
          imageSrc: 'src/assets/NYGH.jpg',
          imageAlt: 'Image 2',
          options: [
            { text: 'Option A', type: 'btn btn-primary' },
            { text: 'Option B', type: 'btn btn-primary' },
            // Add more options as needed
          ],
        },
        // Add more questions as needed
      ],
    };
  },
  methods: {
    handleOptionClick(option) {
      // Handle the click event for the selected option
      console.log('Selected option:', option);
      // You can add logic here to handle different options as needed.
    },
  },
};
</script>

<style scoped>
/* CSS for the overlay text and image fading */
.question {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -80%);
  text-align: center;
  font-size: 30px;
  color: #253028;
  font-weight: bold;
}

.button {
  position: absolute;
  top: 50%;
  left: 50%;
}

.image {
  height: 500px;
  opacity: 0.1;
}
</style>

  
  
