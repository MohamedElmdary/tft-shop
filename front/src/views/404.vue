<template>
  <v-col class="container">
    <div class="mb-15">
      <v-row justify="center" align="center">
        <span class="font-weight-bold mr-2 bitcoin">4</span>
        <img src="@/assets/bitcoin.svg" width="200" />
        <span class="font-weight-bold ml-2 bitcoin">4</span>
      </v-row>

      <v-row justify="center">
        <v-btn color="indigo" @click="$router.push('/')" x-large>
          Go To Shop
        </v-btn>
      </v-row>
    </div>
  </v-col>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  name: "PageNotFound",
})
export default class PageNotFound extends Vue {}
</script>

<style scoped="scss">
.container {
  height: calc(100vh - 64px);
  align-items: center;
  justify-content: center;
  display: flex;
}

.bitcoin {
  color: #faa300;
  font-size: 250px;
}
</style>
