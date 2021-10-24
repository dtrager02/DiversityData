<template>
  <v-container>
    <NavDrawer></NavDrawer>
    <DataView></DataView>
  </v-container>
</template>

<script>
import NavDrawer from "../components/NavDrawer";
import DataView from "./DataView";
export default {
  name: "DatasetView",
  components: {DataView, NavDrawer}
}
</script>
