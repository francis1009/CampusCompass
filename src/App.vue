<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div id="app">
    <Sidebar></Sidebar>
  </div>
  <header>
    <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/test">Test</RouterLink>
        <RouterLink to="/search">Search</RouterLink>
        <RouterLink to="/test2">Test2</RouterLink>
      </nav>
  </header>
  <RouterView />
</template>

<script>
import Sidebar from "@/components/sidebar/Sidebar.vue";
import SchoolCard from "@/components/SchoolCard.vue"

export default {
  components: {
    Sidebar,
  },
};
</script>

<style scoped>
#app {
  padding-left: 0px;
  padding-right: 0px;
}
</style>
