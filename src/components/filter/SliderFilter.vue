<template>
  <div>
    <label for="psle-slider">PSLE Score: {{ value }}</label>
    <input
      id="psle-slider"
      type="range"
      min="4"
      max="32"
      class="form-range"
      @input="updateValue($event.target.valueAsNumber)"
    />
  </div>
</template>

<script>
export default {
  props: {
    value: Number,
  },
  methods: {
    updateValue(newValue) {
      this.$emit('update:slider', newValue);
    },
  },
};
</script>