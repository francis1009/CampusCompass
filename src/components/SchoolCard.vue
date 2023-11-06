<template>
    <div>
    <!-- card -->
    <div class="card" style="width: 15rem; height: 23em; margin-left: 20px 20px;">
      <img :src="schoolImageUrl" class="card-img-top" alt="School Image" style="height:13rem">
      <div class="card-body">
        <h5 class="card-title">{{ schoolName }}</h5>
        <p class="card-text">{{ schoolAddress }}</p>
        <button @click="openDialog" class="btn">View more</button>
      </div>
    </div>

    <!-- dialog -->
    <dialog ref="moreInfo" class="shadow-lg p-3 mb-5 bg-body rounded">
      <form class="flex-fill d-flex flex-column" method="dialog">
        <p class="flex-fill">{{ schoolName }}</p>
        <iframe :src=map_source height="260" width="260" scrolling="no" frameborder="0" allowfullscreen="allowfullscreen" style="width: 260px; height: 260px;"></iframe>
        <menu class="mt-auto d-flex justify-content-center">
          <button @click="closeDialog" class="btn btn-secondary">Close</button>
          <button @click="sendtoindivpage" class="btn btn-secondary">Link to School Page</button>
        </menu>
      </form>
    </dialog>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    props: {
      school: {
        type: Number,
        required: true,
      } 
    },
    data() {
        return {
            schoolName: '',
            schoolAddress: '',
            schoolImageUrl: '',
            one_map: '',
            school_postal_code: '',
        };
    },
    created() {
        this.fetchSchoolDetails();
    },
    methods: {
        fetchSchoolDetails() {
          console.error("benis");
            axios.get(`http://localhost:5000/details/${this.school}`)
                .then(response => {
                    this.schoolName = response.data.School_Name;
                    this.schoolAddress = response.data.School_Address;
                    var school_postal_code = response.data.School_Postal_Code.slice(1,7);
                    this.schoolImageUrl = response.data.School_Image_Source || this.schoolImageUrl;
                    this.map_source = `https://www.onemap.gov.sg/amm/amm.html?mapStyle=Night&zoomLevel=14&marker=postalcode:${school_postal_code}!colour:red&popupWidth=200`
                    
                })
                .catch(error => {
                    console.error(error);
                });
        },
        openDialog() {
            this.$refs.moreInfo.showModal();
        },
        closeDialog() {
            this.$refs.moreInfo.close();
        },
        sendtoindivpage() {
          this.$router.push('/indivschool/' + this.school);
        }
    },
};
</script>

<style scoped>
dialog {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50%;
    height: 90%;
    border: none;
    border-radius: 5px;
}

.btn {
  background-color: #50ad82;
  color: white;
}
</style>