<template>
  <div>
    <h1>예금상품 상세정보</h1>
    <a href="#" @click="goDeposit">정기예금</a>  |
    <a href="#" @click="goSaving">적금</a>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const router = useRouter()

const goDeposit = () => {
  router.push({ name: 'deposit' })
}

const goSaving = () => {
  router.push({ name: 'saving' })
}




</script>

<style scoped>

</style>