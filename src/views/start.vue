<template>
    <!-- BS carousel: start -->
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div v-for="(item, index) in carouselItems" :key="index" :class="{ 'carousel-item': true, active: index === 0 }">
          <img :src="item.src" class="d-block w-100 image" :alt="item.alt">
          <!-- Overlay the {{ test }} text on top of the image -->
          <div class="question">
            {{ question }}
          </div>
          <div class="">
            <button type="button" class="btn btn-primary">Yes</button>
            <button type="button" class="btn btn-primary">No</button>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <!-- BS carousel: end -->
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        flow: 1,
        question: "Do you want us to recommend a secondary school for you?",
        carouselItems: [
          { src: 'src/assets/CHS.jpg', alt: 'Image 1' },
          { src: 'src/assets/NYGH.jpg', alt: 'Image 2' },
          { src: '', alt: 'Image 3' },
          // Add more items as needed
        ],
      };
    },
    methods: {},
  };
  </script>
  
  <style scoped>
  /* CSS for the overlay text */
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
  
  /* CSS for the fading effect on the images */
  .image {
    height: 500px;
    opacity: 0.1; /* Adjust the opacity value as needed for the images */
  }
  </style>
  
  
