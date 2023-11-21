<template>
  <Form
    @submit.prevent="signUp"
    :validation-schema="schema"
    v-slot="{ errors }"
  >
    <h1>가입 폼</h1>
    <form @submit.prevent="signUp">
      <p>유저네임</p>
      <Field name="username" v-model="username" />
      <span class="warning">{{ errors.username }}</span>
      <button @click="checkId">중복확인버튼</button>
      <p v-show="isChecked == 2" style="color: red">중복된 아이디 입니다.</p>
      <p v-show="isChecked == 1" style="color: green">
        사용 가능한 아이디 입니다.
      </p>

      <p>이메일</p>
      <Field name="email" v-model="email" />
      <span class="warning">{{ errors.email }}</span>
      <p>비번</p>
      <Field name="password1" type="password" v-model="password1" />
      <span class="warning">{{ errors.password1 }}</span>
      <p>비번확인</p>
      <Field name="password2" type="password" v-model="password2" />
      <span class="warning">{{ errors.password2 }}</span>
      <p>닉넴</p>

      <Field name="nickname" v-model="nickname" />
      <span class="warning">{{ errors.nickname }}</span>
      <p>나이</p>

      <Field name="age" type="number" v-model="age" />
      <span class="warning">{{ errors.age }}</span>
      <p>money</p>
      <Field name="money" type="number" v-model="money" />
      <span class="warning">{{ errors.money }}</span>
      <p>salary</p>

      <Field name="salary" type="number" v-model="salary" />
      <span class="warning">{{ errors.salary }}</span>
      <button
        :disabled="!isFormValid"
        type="submit"
        value="가입하기"
        class="submit"
      >
        제ㅐ출
      </button>
    </form>
  </Form>
</template>

<script setup>
import { Form, Field, defineRule } from "vee-validate";
import { useCounterStore } from "@/stores/counter";
import { ref, computed } from "vue";
import axios from "axios";

defineRule("confirmed", (value, [target]) => {
  if (value == target) {
    return true;
  }
  return "비밀번호가 일치하지 않습니다.";
});

defineRule("different", (value, [target]) => {
  if (value !== target) {
    return true;
  }
  return "위험성이 높은 패스워드입니다. 다른 값을 입력해주세요.";
});

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
  username: "required",
  email: "required|validEmail",
  password1: "required|min:6|different:@username",
  password2: "required|confirmed:@password1",
  nickname: "required",
  age: "required|validAge",
  money: "required|validPositiveNumber",
  salary: "required|validPositiveNumber",
};

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const nickname = ref(null);
const age = ref(null);
const money = ref(null);
const salary = ref(null);
const isChecked = ref(null);

const checkId = function () {
  // 아이디 값이 존재하면 axios 요청
  if (username.value) {
    axios({
      // 조회니까 get
      method: "get",
      //  중복확인 하는 URL로
      url: `${store.API_URL}/accounts/find/duplicateID/`,
      // get 이여서 params? 사용
      params: {
        username: username.value,
      },
      // 요청 성공시
    })
      .then((res) => {
        console.log(res);
        // isChecked 로 p 태그 조작
        if (isChecked.value) {
          // res.data == 1인 경우 아이디가 존재하지않는 경우이므로 사용 문구
          if (res.data == 1) {
            if (isChecked.value == 2) {
              isChecked.value = 1;
            }
          }
          // res.data == 2인 경우 아이디가 존재하기 떄문에 사용불가 문구
          else if (res.data == 2) {
            if (isChecked.value == 1) {
              isChecked.value = 2;
            }
          }
        } else {
          isChecked.value = res.data;
        }
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    isChecked.value = null;
    alert("아이디를 입력해주세요");
  }
};

const isFormValid = computed(() => {
  return (
    username.value &&
    password1.value &&
    password2.value &&
    email.value &&
    nickname.value &&
    age.value &&
    money.value &&
    salary.value &&
    isChecked.value === 1
  );
});

const signUp = function () {
  if (isFormValid.value) {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      email: email.value,
      nickname: nickname.value,
      age: age.value,
      money: money.value,
      salary: salary.value,
    };
    console.log(payload);
    store.signUp(payload);
  }
};
</script>

<style scoped>
.warning {
  color: red;
}
</style>
