import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductsView from "../views/ProductsView.vue";
import MapView from "../views/MapView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import ArticleView from "../views/ArticleView.vue";
import ProductsDepositView from "@/views/ProductsDepositView.vue";
import ProductsSavingView from "@/views/ProductsSavingView.vue";

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
    {
      path: "/products/deposit/",
      name: "deposit",
      component: ProductsDepositView,
    },
    {
      path: "/products/saving/",
      name: "saving",
      component: ProductsSavingView,
    },
  ],
});

export default router;
