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
import axios from 'axios'

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const signUp = async function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  try {
    axios({
      method: 'get',
      urls: `${store.API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  } catch (err) {
    console.log(err)
  }
  store.signUp(payload)
};
</script>

<style></style>
