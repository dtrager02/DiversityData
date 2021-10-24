<template>
  <v-form
      ref="form"
      lazy-validation
  >
    <v-file-input
        counter
        truncate-length="15"
        placeholder="Select a file"
    ></v-file-input>
    <v-select
        :items="this.fileTypes"
        v-model="this.selected"
        dense>
    </v-select>
    <DemographicForm></DemographicForm>
  </v-form>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";
import DemographicForm from "@/components/DemographicForm.vue";
@Component({
  components: {DemographicForm}
})
export default class AddDataForm extends Vue {
  fileTypes = ['CSV', 'JSON'];
  selected = 'CSV';
}
</script>
