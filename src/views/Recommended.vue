<template>
    <!-- <start/> -->
    <carousel @scrollToRecommend="scrollToRecommend" />
    <div class="album py-5 bg-white">
        <h1 ref="recommend" id="recommend" >These are your recommended schools:</h1>
        <br />
        <div class="container-fluid">
            <div class="row row-cols-xl-3 row-cols-md-2 row-cols-1 g-3">

                <div class="col" v-for="(school, index) in schoolsList" :key="index">
                <SchoolCard :school="school" />
                </div>

            </div>
        </div>
  </div>
</template>

<script>
import SchoolCard from "../components/schoolcard/SchoolCard.vue";
import carousel from "../components/carousel/carousel.vue";
import Filter from "../components/filter/Filter.vue";
import { RouterLink } from 'vue-router';

export default {
    components: {
        SchoolCard,
        carousel,
        Filter,
        RouterLink
    },
    props: {
        schoolsList: {
            type: Array,
            required: false,
            default: () => []
        }
    },
    mounted() {
        this.$router.push({
            name: 'recommended', 
            query: { schoolsList: JSON.stringify([]) }
        });
    },
    methods: {
        // Scroll to the recommend section if user clicks no or finished all questions
        scrollToRecommend() {
            this.$nextTick(() => {
            // Get the DOM element for the 'recommend' section
            const recommendElement = this.$refs.recommend;

            if (recommendElement) {
                // Calculate the Y position of the recommend section relative to the viewport
                const yOffset = recommendElement.getBoundingClientRect().top;

                // Scroll to the recommend section with a smooth animation
                window.scrollTo({
                    top: window.scrollY + yOffset,
                    behavior: 'smooth'
                });
            }
        });
        }
    },
    data() {
        return {
        };
    },
};
</script>

<style scoped>
    h1{
        text-align: center;
    }
</style>