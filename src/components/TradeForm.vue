<template>
  <form>
    <v-text-field
      label="Bit Coin"
      color="indigo"
      type="number"
      min="0"
      v-model="form.bitcoins"
      @input="updateTFTCoins()"
    >
      <v-img slot="append" src="@/assets/bitcoin.svg" width="20" />
    </v-text-field>

    <v-text-field
      label="TFT Coin"
      color="indigo"
      type="number"
      min="0"
      disabled
      v-model="form.tftcoins"
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
    tftcoins: 0,
    address: "",
  };

  public updateTFTCoins(): void {
    this.form.tftcoins = this.form.bitcoins * 1715;
  }
}
</script>
