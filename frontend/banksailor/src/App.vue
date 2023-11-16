<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <nav class="navbar bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img
            src="@/assets/banksailor_logo.png"
            alt="Logo"
            width="30"
            height="30"
            class="d-inline-block align-text-top"
          />
        </a>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink :to="{ name: 'products' }">예금 비교</RouterLink>
        <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
        <RouterLink :to="{ name: 'map' }">은행 지도</RouterLink>
        <RouterLink :to="{ name: 'article' }">게시판</RouterLink>

        <!-- 만약 로그인 안된 상태라면 -->
        <button class="login">LOGIN</button>
        <button class="signin">SIGN IN</button>
        <!-- 로그인 상태라면 -->
        <!-- <button class="logout">logout</button> -->
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
a {
  text-decoration: none;
  color: #1c5f82;
}

button {
  border: 1px solid #1c5f82;
  border-radius: 30px;
  padding-bottom: 4px;
  width: 80px;
  height: 35px;
}

.login {
  color: #1c5f82;
}

.signin {
  color: white;
  background-color: #1c5f82;
}

.logout {
  color: white;
  background-color: #1c5f82;
}
</style>
