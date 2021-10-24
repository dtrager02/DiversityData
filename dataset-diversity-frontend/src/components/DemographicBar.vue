<template>
  <v-container>
    <v-progress-linear v-for="(race, contribute) in this.demo.race"
                       v-bind:key="race"
                       v-bind:style="{ width: (contribute/totalContributor).toFixed(0)*100+'px' }"
                       value="100" height="15" style="display: inline-block"></v-progress-linear>
  </v-container>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";
import {ServerResponse} from "@/assets/ts/ServerResponse";
import DemographicData = ServerResponse.DemographicData;

const DemographicBarProp = Vue.extend({
  props: {
    demo: Object as () => DemographicData
  }
})

@Component
export default class DemographicBar extends DemographicBarProp {
  get totalContributor(): number {
    let total = 0;
    Object.values(this.demo).map(value => total += value);
    return total;
  }
}
</script>
