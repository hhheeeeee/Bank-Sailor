<template>
  <main class="container1">
    <div class="header">
      <h1 class="title">예적금 금리 비교</h1>
      <div class="selecttype">
        <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>
        <RouterLink :to="{ name: 'saving' }">적금</RouterLink>
      </div>
    </div>
    <RouterView />
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.container1 {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  margin-top: 40px;
}

.selecttype {
  width: 60%;
  display: flex;
  justify-content: center;
  /* margin: 20px 0px; */
}

/* a {
  text-decoration: none;
  color: rgb(28, 54, 89);
  font-weight: 700;
  margin: 13px auto;
} */

.header {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.selecttype {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
}

.selecttype a {
  display: inline-block;
  width: 100px;
  height: 100%;
  text-align: center;
  line-height: 50px;
  background-color: #ccc;
  color: #fff;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.selecttype a.router-link-exact-active {
  background-color: #333;
}
</style>
