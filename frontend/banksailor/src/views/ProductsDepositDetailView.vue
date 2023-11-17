<template>
  <div>
    <h1>예금상품 상세정보</h1>
    <a href="#" @click="goDeposit">정기예금</a>  |
    <a href="#" @click="goSaving">적금</a>
  </div>
  <div>
    
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const router = useRouter()
const route = useRoute()

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
    url: `${store.API_URL}/products/deposit/${route.params.id}/`
  })
  .then((response) => {
    console.log(response)
  })
  .catch((error) => {
    console.log(error)
  })
})



</script>

<style scoped>

</style>