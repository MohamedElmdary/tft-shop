import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Shop from "@/views/Shop.vue";
import PageNotFound from "@/views/404.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Shop",
    component: Shop,
  },
  {
    path: "*",
    name: "PageNotFound",
    component: PageNotFound,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
