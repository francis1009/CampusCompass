<template>
    <div class="d-flex container">
        <CheckboxListFilter label="Areas" :items="areas"  @update:filter="updateAreas" />
        <CheckboxListFilter label="Subjects" :items="subjects"  @update:filter="updateSubjects" />
        <CheckboxListFilter label="CCAs" :items="ccas"  @update:filter="updateCCAs" />
        <CheckboxListFilter label="Special Educations" :items="specialEducations" @update:filter="updateSpecialEducations" />
    </div>
    <div>
        <button @click="applyFilters">Apply Filters</button>
    </div>
</template>

<script>
    import CheckboxListFilter from '../components/filter/CheckboxListFilter.vue'

    export default {
        components: {
            CheckboxListFilter
        },
        data(){
            return{
                areas: ['north', 'south', 'west', 'east'],
                subjects: ['math', 'science', 'english', 'history', 'language'],
                ccas: ['sports', 'arts', 'music', 'technology'],
                specialEducations: ['adhd', 'autism', 'dyalexis'],
                selectedAreas: [],
                selectedSubjects: [],
                selectedCCAs: [],
                selectedSpecialEducations: [],
            }
        },
        methods: {
            updateAreas(value) {
                this.selectedAreas = value;
            },
            updateSubjects(value) {
                this.selectedSubjects = value;
            },
            updateCCAs(value) {
                this.selectedCCAs = value;
            },
            updateSpecialEducations(value) {
                this.selectedSpecialEducations = value;
            },
            applyFilters() {
                // filter logic(?)
                console.log("selected areas: "+this.selectedAreas);
                console.log("selected subjects: "+this.selectedSubjects);
                console.log("selected ccas: "+this.selectedCCAs);
                console.log("selected special educations: "+this.selectedSpecialEducations);
            },
        },
    };
</script>