<template>
  <div class="container2">
    <h1 class="title">기본 정보 수정</h1>
    <Form
      @submit.prevent="UpdateInfo"
      @changed="changed"
      :validation-schema="schema"
      v-slot="{ errors }"
      class="FF"
    >
      <form @submit.prevent="UpdateInfo" class="customform">
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
        <button
          type="submit"
          value="가입하기"
          class="submit"
          :disabled="isChanged == true"
        >
          수정하기
        </button>
      </form>
    </Form>
    <div class="chartarea">
      <p>내가 가입한것들</p>
      <div class="chart1">
        <p class="saving">[예금]</p>
        <DepositChart />
      </div>
      <div class="chart1">
        <p class="saving">[적금]</p>
        <SavingChart />
      </div>
    </div>
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

const isChanged = ref(false);

const changed = function () {
  console.log(isChanged.value);
  isChanged.value = true;
};

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

// watchEffect(() => {
//   store.getUserInfo();
// });

const UpdateInfo = function () {
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/find/update/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      // username: username.value,
      email: email.value,
      nickname: nickname.value,
      age: age.value,
      salary: salary.value,
      money: money.value,
    },
  })
    .then((res) => {
      alert("수 정 완 료");
      store.getUserInfo();
      return true
        .then((res) => {
          email.value = store.userInfo.email;
          nickname.value = store.userInfo.nickname;
          age.value = store.userInfo.age;
          money.value = store.userInfo.money;
          salary.value = store.userInfo.salary;
          like_deposit.value = store.userInfo.like_deposit;
          like_saving.value = store.userInfo.like_saving;
        })
        .catch((err) => {
          console.error(err);
        });
    })
    .catch((err) => {
      // console.log("??????????????????????");
      // console.log(err.json);
    });
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
.container2 {
  width: 75%;
  height: auto;
  overflow-x: hidden;
  background-color: white;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container2::-webkit-scrollbar {
  width: 10px; /* 스크롤바의 너비 */
}

.container2::-webkit-scrollbar-thumb {
  height: 20%; /* 스크롤바의 길이 */
  background: #217af4; /* 스크롤바의 색상 */
  border-radius: 10px;
}

.container2::-webkit-scrollbar-track {
  background: rgba(33, 122, 244, 0.1); /*스크롤바 뒷 배경 색상*/
}

.container2::-webkit-scrollbar-thumb {
  height: 50%;
}
.customform {
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.FF {
  width: 100%;
  display: flex;
  justify-content: center;
}

.title {
  font-size: 50px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 30px;
  color: rgb(28, 54, 89);
}

.chartarea {
  width: 90%;
  text-align: center;
}

.saving {
  font-size: 20px;
  font-weight: 800;
  color: rgb(7, 152, 242);
  background-color: rgb(234, 218, 190);
  padding-bottom: 5px;
}

.chart1 {
  border: 3px solid rgb(234, 218, 190);
  margin-bottom: 40px;
}
</style>
