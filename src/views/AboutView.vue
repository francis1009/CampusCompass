<!--<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>-->
<template>
  <div>
    <draggable :list="items" :itemKey="customKey">
      <template v-slot:item="{element}">
        <div>
          {{ element }}
        </div>
      </template>
    </draggable>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  data() {
    return {
      items: ["Item 1", "Item 2", "Item 3"],
    };
  },
  methods: {
    customKey(item) {
      return item.id; // Specify a unique identifier for each item
    },
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
