<template>
  <form>
    <v-text-field
      label="Bit Coin"
      color="indigo"
      type="number"
      min="0"
      v-model="form.bitcoins"
      @input="updateTFT()"
    >
      <v-img slot="append" src="@/assets/bitcoin.svg" width="20" />
    </v-text-field>

    <v-text-field
      label="TFT"
      color="indigo"
      type="number"
      min="0"
      disabled
      v-model="form.tft"
    >
      <v-img slot="append" src="@/assets/tft.png" width="20" />
    </v-text-field>

    <v-text-field
      label="TFT Wallet Address"
      color="indigo"
      type="text"
      v-model="form.address"
    >
      <v-icon slot="append" color="red">
        mdi-map-marker
      </v-icon>
    </v-text-field>

    <v-btn color="indigo">
      Swap BitCoins into TFT
    </v-btn>
  </form>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  name: "TradeForm",
})
export default class TradeForm extends Vue {
  form = {
    bitcoins: 0,
    tft: 0,
    address: "",
  };

  public updateTFT(): void {
    this.form.tft = this.form.bitcoins * 1715;
  }
}
</script>
