<template>
  <div class="container1">
    <h1 @click="check">EditInfoView</h1>
    <p>회원번호? : {{ store.userInfo.pk }}</p>
    <p>username : {{ store.userInfo.username }}</p>
    <p>email : {{ store.userInfo.email }}</p>
    <p>salary : {{ result.salary }}</p>
    <p>money : {{ result.money }}</p>
    <p>가입한거 : {{ result.financial_products }}</p>
    <p>가입한거 : {{ result.financial_products }}</p>
    <p>가입한 상품 금리...이거 어케함?ㅜ: {{ result.financial_products }}</p>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, computed, ref } from "vue";
import axios from "axios";
const store = useCounterStore();
const result = ref(null);

onMounted(() => {
  store.getUserInfo();
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("personal info: ", res.data);
      result.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
