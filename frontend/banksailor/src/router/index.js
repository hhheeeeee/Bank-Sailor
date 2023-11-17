import { createRouter, createWebHistory } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import HomeView from "../views/HomeView.vue";
import ProductsView from "../views/ProductsView.vue";
import MapView from "../views/MapView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import ArticleView from "../views/ArticleView.vue";
import ArticleCreateView from "@/views/ArticleCreateView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import ProductsDepositView from "@/views/ProductsDepositView.vue";
import ProductsSavingView from "@/views/ProductsSavingView.vue";
import ProductsDepositDetailView from "@/views/ProductsDepositDetailView.vue";
import ProductsSavingDetailView from "@/views/ProductsSavingDetailView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";

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
      ],
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
    {
      path: "/deposit/:id",
      name: "depositdetail",
      component: ProductsDepositDetailView,
    },
    {
      path: "/saving/:id",
      name: "savingdetail",
      component: ProductsSavingDetailView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
  ],
});

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "ArticleView" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  }
  if ((to.name === "SignUpView" || to.name === "LogInView") && store.isLogin) {
    window.alert("이미 로그인 했습니다.");
    return { name: "ArticleView" };
  }
});

export default router;
