<template>
  <v-data-table
      :headers="headers"
      :items="desserts"
      class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
          flat
      >
        <v-toolbar-title>DATA NAME</v-toolbar-title>
        <v-divider
            class="mx-4"
            inset
            vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
            v-model="dialog"
            max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
            >
              Add Data
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Add Data To Dataset 1</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <AddDataForm></AddDataForm>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="blue darken-1"
                  text
              >
                Cancel
              </v-btn>
              <v-btn
                  color="blue darken-1"
                  text
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:no-data>
      <v-btn
          color="primary"
          @click="initialize"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";
import AddDataForm from "@/components/AddDataForm.vue";
@Component({
  components: {AddDataForm}
})
export default class DataView extends Vue
{
  dialog = false;
  headers = [
    {
      text: 'Dessert (100g serving)',
      align: 'start',
      sortable: false,
      value: 'name',
    },
    {text: 'Calories', value: 'calories'},
    {text: 'Fat (g)', value: 'fat'},
    {text: 'Carbs (g)', value: 'carbs'},
    {text: 'Protein (g)', value: 'protein'},];
  desserts = [];

  created() {
    this.initialize()
  }

  initialize() {
    this.desserts = [
      {
        name: 'Frozen Yogurt',
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
      },
      {
        name: 'Ice cream sandwich',
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
      },
      {
        name: 'Eclair',
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
      },
      {
        name: 'Cupcake',
        calories: 305,
        fat: 3.7,
        carbs: 67,
        protein: 4.3,
      },
      {
        name: 'Gingerbread',
        calories: 356,
        fat: 16.0,
        carbs: 49,
        protein: 3.9,
      },
      {
        name: 'Jelly bean',
        calories: 375,
        fat: 0.0,
        carbs: 94,
        protein: 0.0,
      },
      {
        name: 'Lollipop',
        calories: 392,
        fat: 0.2,
        carbs: 98,
        protein: 0,
      },
      {
        name: 'Honeycomb',
        calories: 408,
        fat: 3.2,
        carbs: 87,
        protein: 6.5,
      },
      {
        name: 'Donut',
        calories: 452,
        fat: 25.0,
        carbs: 51,
        protein: 4.9,
      },
      {
        name: 'KitKat',
        calories: 518,
        fat: 26.0,
        carbs: 65,
        protein: 7,
      },
    ]
  }
}
</script>
