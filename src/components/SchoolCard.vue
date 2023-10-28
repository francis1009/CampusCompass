<template>
    <div>
    <!-- card -->
    <div class="card" style="width: 18rem;">
      <img src="https://via.placeholder.com/150" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ school.name }}</h5>
        <p class="card-text">{{ school.info }}</p>
        <button @click="openDialog" class="btn">View more</button>
      </div>
    </div>

    <!-- dialog -->
    <dialog ref="moreInfo" class="shadow-lg p-3 mb-5 bg-body rounded">
      <form class="flex-fill d-flex flex-column" method="dialog">
        <p class="flex-fill">More info</p>
        <menu class="mt-auto d-flex justify-content-center">
          <button @click="closeDialog" class="btn btn-secondary">Close</button>
        </menu>
      </form>
    </dialog>
  </div>
</template>

<script>
export default {
    props: {
      school: {
        type: Object,
        required: true,
        default: () => ({ name: '', info: '', imageUrl: '', }),
      }
    },
    methods: {
        openDialog() {
            this.$refs.moreInfo.showModal();
        },
        closeDialog() {
            this.$refs.moreInfo.close();
        },
    },
};
</script>

<style scoped>
dialog {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 30%;
    height: 50%;
    border: none;
    border-radius: 5px;
}

.btn {
  background-color: #50ad82;
  color: white;
}
</style>