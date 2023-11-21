<template>
  <!-- <Form
    @submit.prevent="UpdateInfo"
    :validation-schema="schema"
    v-slot="{ errors }"
  >
    <h1>가입 폼</h1>
    <form @submit.prevent="signUp">
      <br />
      <p>닉넴</p>
      <Field name="nickname" v-model="nickname" />
      <span class="warning">{{ errors.nickname }}</span>

      <p>이메일</p>
      <Field name="email" v-model="email" />
      <span class="warning">{{ errors.email }}</span>

      <p>나이</p>
      <Field name="age" type="number" v-model="age" />
      <span class="warning">{{ errors.age }}</span>

      <p>money</p>
      <Field name="money" type="number" v-model="money" />
      <span class="warning">{{ errors.money }}</span>

      <p>salary</p>
      <Field name="salary" type="number" v-model="salary" />
      <span class="warning">{{ errors.salary }}</span>
      <br />
      <p>내가 가입한것들</p>
      <template v-for="item in financial_products" :key="item">
        <p>{{ item }} <button>x</button></p>
      </template>
      <input type="text" v-model="financial_products" /> 

      <button
        :disabled="!isFormValid"
        type="submit"
        value="가입하기"
        class="submit"
      >
        제ㅐ출
      </button>
    </form>
  </Form> -->
  <p>{{ store.userInfo }}</p>
  <p>{{ typeof store.userInfo }}</p>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, watchEffect, ref, computed } from "vue";
import { Form, Field, defineRule } from "vee-validate";
import axios from "axios";
const store = useCounterStore();
// const username = ref("");

const email = ref("");
const nickname = ref("");
const age = ref("");
const money = ref("");
const salary = ref("");
const financial_products = ref([]);
const isChecked = ref(null);
const test = ref(null);

onMounted(() => {
  // username.value = store.userInfo.username;
  email.value = store.userInfo.email;
  nickname.value = store.userInfo.nickname;
  age.value = store.userInfo.age;
  money.value = store.userInfo.money;
  salary.value = store.userInfo.salary;
  financial_products.value = store.userInfo.financial_products;
});

watchEffect(() => {
  store.getUserInfo();
});

const UpdateInfo = function () {
  const payload = {
    // username: username.value,
    email: email.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    financial_products: financial_products.value,
  };
  console.log(payload);
  // store.signUp(payload);
};

defineRule("validEmail", (value) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (regex.test(value)) {
    return true;
  }
  return "올바른 이메일 형식이어야 합니다.";
});

defineRule("validAge", (value) => {
  const age = parseInt(value);
  if (!isNaN(age) && age >= 1 && age <= 130) {
    return true;
  }
  return "1에서 130 사이의 숫자여야 합니다.";
});

defineRule("validPositiveNumber", (value) => {
  const number = parseFloat(value);
  if (!isNaN(number) && number >= 0) {
    return true;
  }
  return "0 이상의 숫자여야 합니다.";
});

const schema = {
  // username: "required",
  email: "required|validEmail",
  nickname: "required",
  age: "required|validAge",
  money: "required|validPositiveNumber",
  salary: "required|validPositiveNumber",
};

const isFormValid = computed(() => {
  return;
  // username.value &&
  email.value &&
    nickname.value &&
    age.value &&
    money.value &&
    salary.value &&
    isChecked.value === 1;
});
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
