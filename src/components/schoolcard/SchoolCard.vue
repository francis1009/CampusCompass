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
    <dialog ref="moreInfo" class="dialog-wrapper shadow-lg p-3 mb-5 bg-body rounded">
      <div class="dialog">
        <div class="dialog-content">
          <h3 class="school-name">{{ schoolName }}</h3>
          <div class=" d-flex school-details">
            <div class="school-logo">
              <img :src="schoolImageUrl" alt="School Image" style="max-width: 12rem; max-height:12rem; margin-right:50px">
            </div>
            <div class="school-info">
              <div>
                <label>Region:</label>
                {{ schoolRegion }}
              </div>
              <div>
                <label>Address:</label>
                {{ schoolAddress }}
              </div>
              <div>
                <label>Nature:</label>
                {{ schoolNature }}
              </div>
              <div>
                <label>Type:</label>
                {{ schoolType }}
              </div>
              <div>
                <label>Website:</label>
                {{ schoolwebsite }}
              </div>
            </div>
          </div>
        </div>
        <iframe :src="map_source" height="260" width="260" scrolling="no" frameborder="0" 
          allowfullscreen="allowfullscreen" style="width: 260px; height: 260px; margin-top:20px"></iframe>
        <menu class="mt-auto d-flex justify-content-center">
          <button @click="closeDialog" class="btn btn-secondary" style="margin-right:50px">Close</button>
          <button @click="sendtoindivpage" class="btn btn-secondary">Link to School Page</button>
        </menu>
      </div>
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
            schoolRegion: '',
            schoolMode: '',
            schoolNature: '',
            schoolType: '',
            schoolwebsite: '',
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
            axios.get(`http://localhost:5000/details/${this.school}`)
                .then(response => {
                    this.schoolName = response.data.School_Name;
                    this.schoolAddress = response.data.School_Address;
                    this.schoolRegion = response.data.School_Region;
                    this.schoolMode = response.data.School_Mode;
                    this.schoolNature = response.data.School_Nature;
                    this.schoolType = response.data.School_Type;
                    this.schoolwebsite = response.data.School_Website;
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
.dialog-wrapper {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50%;
  height: 90%;
  border: none;
  border-radius: 5px;
}
.dialog {
    width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.school-details{
  height:200px;
}
.school-name{
  text-align:center;
  margin-bottom:20px;
}
.btn {
  background-color: #50ad82;
  color: white;
}
</style>