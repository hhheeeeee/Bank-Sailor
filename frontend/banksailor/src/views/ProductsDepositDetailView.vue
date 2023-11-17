<template>
  <div class="main">
    <a href="#" @click="goDeposit">정기예금</a>  |
    <a href="#" @click="goSaving">적금</a>
    <h1>예금상품 상세정보</h1>
    <hr />
  </div>
  <div v-if="product" class="info-list">
    <div class="info">
      <div class="info-title">공시 제출월:</div>
      <div class="info-content">{{ product.dcls_month }}</div>  
    </div>
    <div class="info">
      <div class="info-title">상품명:</div>
      <div class="info-content">{{ product.kor_co_nm }}</div>  
    </div>
    <div class="info">
      <div class="info-title">금융회사명:</div>
      <div class="info-content">{{ product.fin_prdt_nm }}</div>  
    </div>
    <div class="info">
      <div class="info-title">가입제한:</div>
      <div class="info-content">{{ product.join_deny }}</div>  
    </div>
    <div class="info">
      <div class="info-title">가입대상:</div>
      <div class="info-content">{{ product.join_member }}</div>  
    </div>
    <div class="info">
      <div class="info-title">가입방법:</div>
      <div class="info-content">{{ product.join_way }}</div>  
    </div>
    <div class="info">
      <div class="info-title">최고한도:</div>
      <div class="info-content">{{ product.max_limit }}</div>  
    </div>
    <div class="info">
      <div class="info-title">우대 조건:</div>
      <div class="info-content">{{ product.spcl_cnd }}</div>  
    </div>
    <div class="info">
      <div class="info-title">기타 유의사항:</div>
      <div class="info-content">{{ product.etc_note }}</div>  
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import axios from "axios";

const router = useRouter();
const route = useRoute();

const product = ref(null);

const goDeposit = () => {
  router.push({ name: "deposit" });
};

const goSaving = () => {
  router.push({ name: "saving" });
};

const store = useCounterStore();

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/products/deposit/${route.params.id}/`,
  })
    .then((response) => {
      product.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>

<style scoped>
  .main {
    width: 80%;
    margin: 0 auto;
  }

  .datail-info {
    width: 80%;
    margin: 0 auto;
  }
  
  .info-list {
    width: 80%;
    margin: 0 auto;
  }

  .info {
    display: flex;
    margin: 30px 0;
  }

  .info-title {
    width: 20%;
  }
  .info-content {
    width: 80%;
  }
</style>
