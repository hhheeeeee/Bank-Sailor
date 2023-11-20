<template>
  <div class="container1">
    <h1>---프로필페이지----</h1>
    <div class="sidebar">
      <RouterLink :to="{ name: 'editinfo' }" class="link"
        >기본정보수정</RouterLink
      >
      <RouterLink :to="{ name: 'editprofile' }" class="link"
        >포트폴리오수정</RouterLink
      >
      <RouterLink :to="{ name: 'recommend' }" class="link">추천받기</RouterLink>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.container1 {
  width: 100vw;
  height: 91vh;
  background-color: rgb(214, 232, 255);
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.sidebar {
  position: absolute;
  top: 20%;
  left: 2%;
  width: 15%;
  background-color: rgb(126, 206, 252);
  border-radius: 30px;
  display: flex;
  flex-direction: column;
}

a {
  text-decoration: none;
  color: rgb(28, 54, 89);
  font-weight: 700;
  margin: 13px auto;
}
</style>
