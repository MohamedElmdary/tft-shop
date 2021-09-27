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
        disabled
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
import axios from "@/plugins/axios";

@Component({
  name: "TradeForm",
})
export default class TradeForm extends Vue {
  form = {
    amount: 0,
    address: "Loading...",
    message: "",
  };

  tft = 0;
  qrcode = "";

  private _fetchData() {
    axios
      .get("/address")
      .then(({ data }) => (this.form.address = data.address))
      .catch(() => setTimeout(() => this._fetchData(), 5000));
  }

  created() {
    this._fetchData();
  }

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
    return address.trim() === "Loading..." || amount <= 0;
  }
}
</script>
