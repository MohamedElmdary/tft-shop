<template>
  <v-app-bar app color="indigo darken-2" dark>
    <div class="d-flex align-center">
      <v-img
        alt="Vuetify Logo"
        class="shrink mr-2"
        contain
        src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF4AAABYCAYAAAB8i0BzAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAUVJREFUeNrs3DFKw1AcwOFEegBHR4+gNMdQFLxAj1AnR+PoZG8gHkCo1APkAJXmCB0dewN9kSIZHBzM/xX7/eAReBkCXx4EkkfKInU0fa4L/XVNGu377Grz08lyC//BabDmadylG9D2Jw+4DN5lGqu0uCfg8/TYxwcf20PCPwQfX4c+BZ+nC/B5OgGfMfDgwQs8eIEHL/DgBR68wIPf+0bbY4NCkiRJkrSTlZEXO1vcH6fDZN/RX89v6lHwNTv4W+u9qL0kyxR48OAFHrzAgxd48AIPXuDBg0cAHrzAgxf4f1H0x+7uj3QNdkmSJEnSr/vaH79cvtUo4qqq8ff+eHvWY7M/PlfgwYMXePACD17gwQs8eIEHDx5BeBvweZqDz9MT+PhmVTVuwMfWJvRrD9f4lX7an/D/+GF76R6mCX2NYkf6FGAAboUr2ns0aCgAAAAASUVORK5CYII="
        transition="scale-transition"
        width="30"
      />
      <span class="font-weight-bold text-h5">
        TFT Shop
      </span>
    </div>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  name: "Navbar",
})
export default class Navbar extends Vue {}
</script>
