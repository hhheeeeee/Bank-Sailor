<template>
  <div>
    <a href="#" @click="goDeposit">정기예금</a>  |
    <a href="#" @click="goSaving">적금</a>
    <h1>적금상품 상세정보</h1>
    <hr>
  </div>
  <div v-if="product">
    <p>공시 제출월: {{ product.dcls_month }}</p>
    <p>금융회사명: {{ product.kor_co_nm }}</p>
    <p>상품명: {{ product.fin_prdt_nm }}</p>
    <p>가입제한: {{ product.join_deny }}</p>
    <p>가입대상: {{ product.join_member }}</p>
    <p>가입방법: {{ product.join_way }}</p>
    <p>우대 조건: {{ product.spcl_cnd }}</p>
    <p>기타 유의사항: {{ product.etc_note }}</p>
    <p>최고한도: {{ product.max_limit }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const router = useRouter()
const route = useRoute()

const product = ref(null)

const goDeposit = () => {
  router.push({ name: 'deposit' })
}

const goSaving = () => {
  router.push({ name: 'saving' })
}

const store = useCounterStore()

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/products/saving/${route.params.id}/`
  })
  .then((response) => {
    product.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
})



</script>

<style scoped>

</style>