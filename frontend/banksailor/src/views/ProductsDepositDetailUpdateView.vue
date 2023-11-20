<template>
  <div>
    <a href="#" @click.prevent="goBack">뒤로가기</a>
    <h1>금리 수정</h1>
    <hr>
    <p>현재 금리: {{ rate }}</p>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()



const goBack = () => {
  router.push({ name: 'depositdetail', params: { id: route.params.id } } )
}
</script>

<style scoped>

</style>