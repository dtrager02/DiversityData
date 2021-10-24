<template>
  <v-item-group>
    <v-container>
      <v-row>
        <v-col
            v-for="n in 12"
            :key="n"
            cols="12"
            md="4"
        >
          <v-item>
            <DatasetItem title="test" subtitle="Test sub" description="description"></DatasetItem>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script>
import DatasetItem from "../components/DatasetItem";
export default {
  name: "Explore",
  components: {DatasetItem}
}
</script>
