<template>
  <v-container>
    <h1 class="text-center">
      Trade BitCoins for TFTCoins
    </h1>

    <v-divider class="mt-4 mb-4" />

    <v-row>
      <v-col :cols="4">1</v-col>
      <v-col :cols="8">2</v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  name: "Shop",
})
export default class Shop extends Vue {}
</script>
