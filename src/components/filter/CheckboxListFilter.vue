<template>
    <div>
        <label>{{ label }}</label>
        <div class="checkbox-list">
        <div v-for="item in items" :key="item">
            <input type="checkbox" :value="item" v-model="selectedItems" @change="updateFilter">
            {{ item }}
        </div>
        </div>
    </div>
</template>

<script>
export default {
  props: {
    label: String,
    items: Array,
  },
  data() {
    return {
      selectedItems: []
    };
  },
  methods: {
    updateFilter() {
      this.$emit('update:filter', this.selectedItems);
    }
  }
};
</script>

<style scoped>
.checkbox-list {
  max-height: 150px;
  overflow-y: auto;
}
</style>
