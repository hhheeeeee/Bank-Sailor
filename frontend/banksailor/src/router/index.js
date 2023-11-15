import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductsView from "../views/ProductsView.vue";
import MapView from "../views/MapView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import ArticleView from "../views/ArticleView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/products",
      name: "products",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //   component: () => import("../views/AboutView.vue"),
      component: ProductsView,
    },
    {
      path: "/map",
      name: "map",
      component: MapView,
    },
    {
      path: "/exchange",
      name: "exchange",
      component: ExchangeView,
    },
    {
      path: "/article",
      name: "article",
      component: ArticleView,
    },
  ],
});

export default router;
