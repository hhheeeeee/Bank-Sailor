<template>
  <div class="container1">
    <h1 @click="check">기본 정보 수정</h1>
    <!-- <p>{{ store.userInfo }}</p> -->
    <p>회원번호? : {{ store.userInfo.id }}</p>
    <p>username : {{ store.userInfo.username }}</p>
    <p>email : {{ store.userInfo.email ? store.userInfo.email : "X" }}</p>
    <p>salary : {{ store.userInfo.salary ? store.userInfo.salary : "d" }}</p>
    <p>money : {{ store.userInfo.money }}</p>
    <p>가입한거 : {{ store.userInfo.financial_products }}</p>

    <!-- <p>가입한 상품 금리...이거 어케함?ㅜ: {{ result.financial_products }}</p> -->
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, watchEffect, ref } from "vue";
const store = useCounterStore();
const userinfo = ref("");

watchEffect(() => {
  // if (store.userInfo === null) {
  store.getUserInfo();
});
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
