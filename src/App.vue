<script setup>
import { RouterView } from 'vue-router'

</script>

<template>
  <div id="app">
    <Sidebar></Sidebar>
  </div>
  <RouterView />
</template>

<script>
import Sidebar from "@/components/sidebar/Sidebar.vue";

export default {
  components: {
    Sidebar,
  },
};
</script>

<style scoped>

</style>
