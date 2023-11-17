<template>
  <div class="container1">
    <h1>Signup</h1>
    <form @submit.prevent="signUp" class="form">
      <label for="username"> 아이디 </label>
      <input type="text" v-model.trim="username" class="input" id="username" />
      <label for="password">비밀번호 </label>
      <input
        type="password"
        v-model.trim="password1"
        class="input"
        id="password"
      />
      <label for="password2">비밀번호 확인</label>
      <input
        type="password"
        v-model.trim="password2"
        class="input"
        id="password2"
      />
      <input type="submit" value="가입하기" class="submit" />
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

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  try {
    axios({
      method: 'get',
      url: `${store.API_URL}/accounts/find/duplicateID/`,
      data: {
        username: username
      }
    }) .then((res) => {
      alert('이미 등록된 ID입니다!')
    }) .catch((err) => {
      console.log(err)
    })
  } catch {
    store.signUp(payload)
  }
};

</script>

<style scoped>
.container1 {
  width: 100%;
  height: 100vh;
  background-color: #c3bfbf;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #1c5f82;
}

h1 {
  font-size: 2em;
  color: #1c5f82;
  margin-bottom: 20px;
  font-weight: 800;
}

.form {
  display: flex;
  flex-direction: column;
  width: 40%;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  background-color: #f5f5f5;
}

label {
  margin-bottom: 5px;
}

.input {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #1c5f82;
  border-radius: 5px;
}

.submit {
  padding: 10px;
  background-color: #1c5f82;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit:hover {
  background-color: #4db7e5;
}
</style>
