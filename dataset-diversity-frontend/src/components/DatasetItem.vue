<template>
  <v-card
      class="mx-auto"
      max-width="344"
  >
    <v-img
        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
        height="200px"
    ></v-img>

    <v-card-title>
      {{ title }}
      {{show}}
    </v-card-title>

    <v-card-subtitle>
      {{ subtitle }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
          color="orange lighten-2"
          text
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
          icon
          @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          <DemographicBar :demo="demotest"></DemographicBar>
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script lang="ts">
import {Component, Prop, Vue} from "vue-property-decorator";
import DemographicBar from "@/components/DemographicBar.vue";
import {ServerResponse} from "@/assets/ts/ServerResponse";
import DemographicData = ServerResponse.DemographicData;

const DatasetItemProps = Vue.extend({
  props: {
    title: String,
    subtitle: String,
    description: String
  }
})
@Component({
  components: {DemographicBar}
})
export default class DatasetItem extends DatasetItemProps
{
  public demotest = {
    "race": {
      "black": 1213,
      "white": 12493,
      "asian": 313013,
      "hispanic": 3019221
    },
    "gender": {
      "female": 123,
      "male": 301,
      "nonbinary": 3013
    }
  } as DemographicData;
  public show = false;
}
</script>
