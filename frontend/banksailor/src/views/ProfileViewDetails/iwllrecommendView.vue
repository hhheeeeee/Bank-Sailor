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
const userInfo = store.userInfo;

onMounted(() => {
  recommend();
  get_portfolioData();
});

const get_portfolioData = function (portfolioId) {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/get_portfolioData/${portfolioId}`,
  }).then((res) => {
      console.log(res.data);
    })
    .catch((error) => {
      console.log(error);
    });
}

const recommend = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/products/iwillrecommendyou/`,
    data: {
      age: userInfo.age,
      salary: userInfo.salary,
      money: userInfo.money,
      saving_style: '알뜰형',
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
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


get_portfolioData