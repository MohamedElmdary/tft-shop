<template>
  <div>
    <form>
      <v-text-field
        label="Bit Coin*"
        color="indigo"
        type="number"
        min="0"
        v-model="form.amount"
        @input="updateTFT()"
      >
        <v-img slot="append" src="@/assets/bitcoin.svg" width="20" />
      </v-text-field>

      <v-text-field
        label="TFT*"
        color="indigo"
        type="number"
        min="0"
        disabled
        v-model="tft"
      >
        <v-img slot="append" src="@/assets/tft.png" width="20" />
      </v-text-field>

      <v-text-field
        label="TFT Wallet Address*"
        color="indigo"
        type="text"
        v-model="form.address"
      >
        <v-icon slot="append" color="red">
          mdi-map-marker
        </v-icon>
      </v-text-field>

      <v-textarea label="Message" v-model="form.message"></v-textarea>

      <v-btn color="indigo" @click="generateQrCode" :disabled="isDisabled()">
        Generate QRCode
      </v-btn>
    </form>

    <v-row justify="center" class="mt-10">
      <img :src="qrcode" alt="qrcode" v-if="!isDisabled() && qrcode" />
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import QRCode from "qrcode";

@Component({
  name: "TradeForm",
})
export default class TradeForm extends Vue {
  form = {
    amount: 0,
    address: "",
    message: "",
  };

  tft = 0;
  qrcode = "";

  public updateTFT(): void {
    this.tft = this.form.amount * 0.5;
  }

  public generateQrCode() {
    const { address, amount, message } = this.form;
    QRCode.toDataURL(`bitcoin:${address}?amount=${amount}&message=${message}`)
      .then((url: string) => {
        this.qrcode = url;
      })
      .catch(console.error);
  }

  public isDisabled() {
    const { address, amount } = this.form;
    return address.trim() === "" || amount === 0;
  }
}
</script>
