<template>
  <div class="container1">
    <div class="container1">
    <p>당신과 같은 20대 {{ myPortfolio[0].saving_style }} 유저는 이런 상품을 선택했어요~!</p>

    <div v-for="recommend in recommend_list">
      <div class="line-box">
        <RouterLink
        :to="{ name: 'savingdetail', params: { id: recommend.fin_prdt_cd } }">
          {{ recommend.kor_co_nm }} - {{ recommend.fin_prdt_nm }}
        </RouterLink>
      </div>

    </div>
  </div>  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const userInfo = store.userInfo;
const portfolio = store.portfolio
const portfolioId = portfolio.find((item) => item.user === userInfo.id).id
const myPortfolio = computed(() => {
  return portfolio.filter((item) => item.user === userInfo.id);
});
if (store.userInfo.like_saving.length === 0) {
  const like_saving = '00266451';
} else {
  const like_saving = store.userInfo.like_saving[0];
};

onMounted(() => {
  recommend();
  get_portfolioData();
});

const get_portfolioData = function () {
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
      saving_style: myPortfolio.saving_style,
      like_saving: like_saving.value,
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
