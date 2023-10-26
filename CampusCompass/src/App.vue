<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="app">
    <Sidebar></Sidebar>
  </div>
        <RouterLink to="/"></RouterLink>
        <RouterLink to="/indivschool"></RouterLink>
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