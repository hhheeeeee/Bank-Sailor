<template>
  <div class="container1">
    추천~!
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const router = useRouter();
const userInfo = store.userInfo;
const portfolio = ref([]);

onMounted(() => {
  getPortfolio();
});

const getPortfolio = function () {
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/find/input_portfolioData/`,
  })
    .then((res) => {
      portfolio.value = res.data;
      console.log(portfolio);
    })
    .catch((err) => {
      console.log(err);
    });
};
const recommend = function (portfolioId) {
  axios({
    method: "post",
    url: `${store.API_URL}/accounts/find/get_portfolioData/${portfolioId}`,
    data: {
      user: userInfo.id,
      saving_style: saving_style.value,
      favorite_bank: favorite_bank.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      Toast.fire({
        icon: "success",
        title: "수정 완료!",
      });
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
