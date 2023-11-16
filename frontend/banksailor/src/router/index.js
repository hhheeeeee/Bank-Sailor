import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductsView from "../views/ProductsView.vue";
import MapView from "../views/MapView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import ArticleView from "../views/ArticleView.vue";
import ArticleCreateView from "@/views/ArticleCreateView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
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
      children: [
        {
          path: "/deposit",
          name: "deposit",
          component: ProductsDepositView,
        },
        {
          path: "/saving",
          name: "saving",
          component: ProductsSavingView,
        },
      ]
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
      path: "/create",
      name: "ArticleCreateView",
      component: ArticleCreateView,
    },
    {
      path: "/article/:id",
      name: "ArticleDetailView",
      component: ArticleDetailView,
    },
  ],
});

export default router;
