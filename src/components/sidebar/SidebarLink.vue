<template>
    <Router-link :to="to" class="link" :class="{ active: isActive }">
      <font-awesome-icon class="icon" :icon="faIcon" />
      <transition name="fade">
        <span v-if="!collapsed">
          <slot />
        </span>
      </transition>
    </Router-link>
  </template>
  
  <script>
  import { computed } from 'vue'
  import { useRoute } from 'vue-router'
  import { collapsed } from './Sidebar.vue'
  
  export default {
    props: {
      to: { type: String, required: true },
      icon: { type: String, required: true }
    },
    setup(props) {
      const route = useRoute()
      const isActive = computed(() => route.path === props.to)
  
      const faIcon = computed(() => ['fas', props.icon])
      return { isActive, collapsed, faIcon }
    }
  }
  </script>
  
  <style scoped>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.1s;
  }
  
  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }
  
  .link {
    display: flex;
    align-items: center;
    cursor: pointer;
    position: relative;
    font-weight: 400;
    user-select: none;
    margin: 0.1em 0;
    padding: 0.4em;
    border-radius: 0.25em;
    height: 3em;
    color: white;
    text-decoration: none;
  }
  
  .link:hover {
    background-color: #8bb092;
  }
  
  .link.active {
    background-color: #50ad82;
  }
  
  .link .icon {
    flex-shrink: 0;
    width: 25px;
    margin-right: 10px;
  }
  </style>