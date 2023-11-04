<template>
    <start/>
    <div class="album py-5 bg-white">
        <h1>These are your recommended schools:</h1>
    <div class="container-fluid">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

        <div class="col" v-for="(school, index) in schools" :key="index">
          <SchoolCard :school="school" />
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import SchoolCard from "../components/SchoolCard.vue";
import start from "./start.vue";

export default {
    components: {
        SchoolCard,
        start
    },
    data() {
        return {
            schools: [
                { name: "School1", info: "SchoolInfo", imageUrl: "https://via.placeholder.com/150" },
                { name: "School2", info: "SchoolInfo", imageUrl: "https://via.placeholder.com/150" },
                { name: "School3", info: "SchoolInfo", imageUrl: "https://via.placeholder.com/150" },
                { name: "School4", info: "SchoolInfo", imageUrl: "https://via.placeholder.com/150" },
                { name: "School5", info: "SchoolInfo", imageUrl: "https://via.placeholder.com/150" },
                { name: "School6", info: "SchoolInfo", imageUrl: "https://via.placeholder.com/150" },
            ]
        };
    },
};
</script>

<style scoped>
    h1{
        text-align: center;
    }
</style>