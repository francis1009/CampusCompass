<template>
    <div class="sidebar" :style="{ width: sidebarWidth }">
        <h1>
            <span v-if="collapsed">SR</span>
            <span v-else>
                <div>School</div>
                <div>Recommender</div>
            </span>
        </h1>

        <SidebarLink to="/viewSchools" icon="table">
            View Schools
        </SidebarLink>
        <SidebarLink to="/compare" icon="square-poll-vertical">
            Compare
        </SidebarLink>
        <SidebarLink to="/recommender" icon="heart">
            Recommender
        </SidebarLink>
        
        <span class="collapse-icon" :class="{ 'rotate-180': collapsed }" @click="toggleSidebar">
            <font-awesome-icon icon="fa-solid fa-angle-double-left" />
        </span>
    </div>
</template>

<script>
import SidebarLink from './SidebarLink.vue'
import { ref, computed } from 'vue'

export const collapsed = ref(false)
export const toggleSidebar = () => (collapsed.value = !collapsed.value)

export const SIDEBAR_WIDTH = 180
export const SIDEBAR_WIDTH_COLLAPSED = 50
export const sidebarWidth = computed(
  () => `${collapsed.value ? SIDEBAR_WIDTH_COLLAPSED : SIDEBAR_WIDTH}px`
)

export default {
    props: {},
    components: { SidebarLink },
    setup() {
        return { collapsed, toggleSidebar, sidebarWidth }
    }
}
</script>

<style scoped>
    .sidebar{
        color: white;
        background-color: #253028;
        float: left;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        bottom: 0;
        padding: 0.5em;
        transition: 0.3s ease;
        display: flex;
        flex-direction: column;
    }
    .sidebar h1{
        font-size: 25px;
        height: 3em;
        margin-bottom: 20px;
    }
    .collapse-icon {
        position: absolute;
        bottom: 0;
        padding: 0.75em;
        color: white;
        transition: 0.2s linear;
    }
    .rotate-180 {
        transform: rotate(180deg);
        transition: 0.2s linear;
    }
</style>