<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div id="app">
    <Sidebar></Sidebar>
  </div>
  <RouterView />
</template>

<script>
import SchoolCard from "@/components/SchoolCard.vue"
</script>

<style scoped>

</style>
