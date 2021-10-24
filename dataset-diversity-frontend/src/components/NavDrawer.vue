<template>
  <v-navigation-drawer app clipped permanent>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
          Dataset Name
        </v-list-item-title>
        <v-list-item-subtitle>
          subtext
        </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list
        dense
        nav
    >
      <v-list-item
          v-for="item in items"
          :key="item.title"
          link
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-spacer></v-spacer>
    <v-list>
      <v-list-item>
        Test
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data () {
    return {
      items: [
        { title: 'Dataset 1', icon: 'mdi-file-document-outline' },
        { title: 'Dataset 2', icon: 'mdi-file-document-outline' },
        { title: 'Dataset 3', icon: 'mdi-file-document-outline' },
      ],
      right: null,
    }
  },
}
</script>
