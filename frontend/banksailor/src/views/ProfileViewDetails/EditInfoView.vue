<template>
  <div class="container1">
    <Form
      @submit.prevent="UpdateInfo"
      :validation-schema="schema"
      v-slot="{ errors }"
      class="FF"
    >
      <form @submit.prevent="signUp" class="customform">
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
        <button type="submit" value="가입하기" class="submit">제ㅐ출</button>
        <p>내가 가입한것들</p>
        <p>deposit :</p>
        <DepositChart />
        <hr />
        <p>saving :</p>
        <SavingChart />
      </form>
    </Form>
  </div>
</template>

<script setup>
import DepositChart from "../../components/ProfileViewComponents/DepositChart.vue";
import SavingChart from "../../components/ProfileViewComponents/SavingChart.vue";
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
const like_deposit = ref(null);
const like_saving = ref(null);

onMounted(() => {
  // username.value = store.userInfo.username;
  email.value = store.userInfo.email;
  nickname.value = store.userInfo.nickname;
  age.value = store.userInfo.age;
  money.value = store.userInfo.money;
  salary.value = store.userInfo.salary;
  like_deposit.value = store.userInfo.like_deposit;
  like_saving.value = store.userInfo.like_saving;
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
    salary: salary.value,
    money: money.value,
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

// const isFormValid = computed(() => {
// return;
// username.value &&
//   email.value &&
//     nickname.value &&
//     age.value &&
//     money.value &&
//     salary.value &&
//     isChecked.value === 1;
// });
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}

.customform {
  width: 100%;
}

.FF {
  width: 600px;
}
</style>
