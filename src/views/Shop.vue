<template>
  <v-container>
    <h1 class="text-center">
      Trade BitCoins for TFTCoins
    </h1>

    <v-divider class="mt-4 mb-4" />

    <v-row>
      <v-col :cols="6">
        <v-row justify="center">
          <v-img src="@/assets/trade.svg" max-width="600px" width="90%" />
        </v-row>
      </v-col>
      <v-col :cols="6">
        <TradeForm />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import TradeForm from "@/components/TradeForm.vue";

@Component({
  name: "Shop",
  components: {
    TradeForm,
  },
})
export default class Shop extends Vue {}
</script>
