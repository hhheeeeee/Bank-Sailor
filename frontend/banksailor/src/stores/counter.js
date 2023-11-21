import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import axios from "axios";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const router = useRouter();
    const articles = ref([]);
    const comments = ref([]);
    const userInfo = ref([]);
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    const signUp = function (payload) {
      console.log(payload);
      const {
        username,
        password1,
        password2,
        email,
        nickname,
        age,
        money,
        salary,
      } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          email,
          nickname,
          age,
          money,
          salary,
          // financial_products
        },
      })
        .then((res) => {
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => {
          console.log("??????????");
          console.log(err.json);
        });
    };

    const logIn = function (payload) {
      const { username, password } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log(res.data);
          token.value = res.data.key;
          getUserInfo();
          router.push({ name: "home" });
        })
        .catch((err) => {
          window.alert("아이디 혹은 비밀번호가 일치하지 않습니다.");
          console.log(err);
        });
    };

    const logOut = function () {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          token.value = null;
          router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/articles/articles/`,
        // headers: {
        //   Authorization: `Token ${token}`,
        // },
      })
        .then((res) => {
          console.log(res);
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };
    //
    const deposits = ref([]);
    const savings = ref([]);

    const getDeposits = () => {
      axios({
        method: "get",
        url: `${API_URL}/products/deposit/`,
      })
        .then((response) => {
          deposits.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const createArticle = function () {
      axios({
        method: "post",
        url: `${API_URL}/articles/articles/`,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getComments = function () {
      axios({
        method: "get",
        url: `${API_URL}/articles/comments/`,
      })
        .then((res) => {
          comments.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const createComments = function () {
      axios({
        method: "post",
        url: `${API_URL}/articles/articles/<int:article_pk>/comments/`,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getSavings = () => {
      axios({
        method: "get",
        url: `${API_URL}/products/saving/`,
      })
        .then((response) => {
          savings.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getUserInfo = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          userInfo.value = res.data;
          return res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      articles,
      API_URL,
      getArticles,
      createArticle,
      createComments,
      getComments,
      deposits,
      getDeposits,
      savings,
      getSavings,
      logIn,
      logOut,
      signUp,
      isLogin,
      token,
      getUserInfo,
      userInfo,
    };
  },
  { persist: true }
);
