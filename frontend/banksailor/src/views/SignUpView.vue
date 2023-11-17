<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
      <p>유저이름</p>
      <input type="text" v-model.trim="username" />
      <p>비밀번호1</p>
      <input type="password" v-model.trim="password1" />
      <p>비밀번호2</p>
      <input type="password" v-model.trim="password2" />
      <input type="submit" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  console.log(payload)
  store.signUp(payload);
};
</script>

<style></style>
