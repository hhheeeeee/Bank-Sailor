<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();

const customlogout = function () {
  window.alert("정말 떠나실건가요..?");
  store.logOut();
};
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
        <RouterLink :to="{ name: 'deposit' }">예금 비교</RouterLink>
        <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
        <RouterLink :to="{ name: 'map' }">은행 지도</RouterLink>
        <RouterLink :to="{ name: 'article' }">게시판</RouterLink>

        <template v-if="store.isLogin">
          <!-- <form @submit.prevent="store.logOut"> -->
          <form @submit.prevent="customlogout">
            <input type="submit" value="Logout" />
          </form>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'LogInView' }" class="login"
            >LogIn</RouterLink
          >
          <RouterLink :to="{ name: 'SignUpView' }" class="signup"
            >SignUp</RouterLink
          >
        </template>
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
  border: 1px solid #1c5f82;
  color: #1c5f82;
  padding: 5px 12px;
  border-radius: 13px;
  font-weight: 700;
}

.signup {
  color: white;
  background-color: #1c5f82;
}

.signup {
  border: 1px solid #1c5f82;
  color: white;
  padding: 5px 12px;
  border-radius: 13px;
}
</style>
