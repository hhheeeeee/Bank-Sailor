<template>
  <div>
    <h1>예적금 금리 비교</h1>
    <RouterLink :to="{ name: 'deposit' }">정기적금</RouterLink>  |
    <RouterLink :to="{ name: 'saving' }">정기예금</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

</style>
