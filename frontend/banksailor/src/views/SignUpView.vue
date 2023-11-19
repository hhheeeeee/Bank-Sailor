<template>
  <div class="container1">
    <h1>Signup</h1>

    <form @submit.prevent="signUp" class="form">
      <div style="display : flex; justify-content:space-between; align-items : center;">
        <label for="username"> 아이디 </label>
        <input type="text" v-model.trim="username" class="input" id="username" />
        <p @click="checkId" style="border : 1px solid gray; border-radius : .5rem; padding : .5rem 1rem; cursor : pointer;">중복 확인</p>
      </div>
      <p v-show="isChecked == 2" style="color: red;">중복된 아이디 입니다.</p>
      <p v-show="isChecked == 1" style="color: green;">사용 가능한 아이디 입니다.</p>
      
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

      <label for="email">Email</label>
      <input
        type="email"
        v-model.trim="email"
        class="input"
        id="email"
      />

      <label for="nickname">Nickname</label>
      <input
        type="nickname"
        v-model.trim="nickname"
        class="input"
        id="nickname"
      />

      <label for="age">나이</label>
      <input
        type="age"
        v-model.trim="age"
        class="input"
        id="age"
      />

      <label for="money">현재 가진 금액</label>
      <input
        type="money"
        v-model.trim="money"
        class="input"
        id="money"
      />

      <label for="salary">연봉</label>
      <input
        type="salary"
        v-model.trim="salary"
        class="input"
        id="salary"
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
const email = ref(null);
const nickname = ref(null);
const age = ref(null);
const money = ref(null);
const salary = ref(null);
const financial_products = ref(null);
const isChecked = ref(null);

const checkId = function () {
  // 아이디 값이 존재하면 axios 요청
  if (username.value) {
    axios({
      // 조회니까 get
      method: 'get',
      //  중복확인 하는 URL로
        url: `${store.API_URL}/accounts/find/duplicateID/`,
        // get 이여서 params? 사용
        params: {
          username: username.value
        }
        // 요청 성공시
    }).then((res) => {
      console.log(res)
      // isChecked 로 p 태그 조작
      if (isChecked.value) {
        // res.data == 1인 경우 아이디가 존재하지않는 경우이므로 사용 문구
        if (res.data == 1) {
          if (isChecked.value == 2) {
            isChecked.value = 1
          }
        }
        // res.data == 2인 경우 아이디가 존재하기 떄문에 사용불가 문구
        else if (res.data == 2) {
          if (isChecked.value == 1) {
            isChecked.value = 2
          }
        }
      } else {
        isChecked.value = res.data
      }
    }).catch((error) => {
      console.log(error)
    })
  }
  else {
    isChecked.value = null
    alert("아이디를 입력해주세요")
  }
}

const signUp = function () {
  if (
    !username.value ||
    !password1.value ||
    !password2.value ||
    !email.value ||
    !nickname.value ||
    !age.value ||
    !money.value ||
    !salary.value
  ) {
    alert("입력칸을 모두 작성해주세요.");
  }
  if (password1.value.length < 8) {
    alert("비밀번호는 8자 이상이어야 합니다");
  }
  if (password1.value != password2.value) {
    alert("입력한 비밀번호와 비밀번호 확인 입력 문구가 다릅니다");
  }
  if (isChecked.value == 1) {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      email: email.value,
      nickname: nickname.value,
      age: age.value,
      money: money.value,
      salary: salary.value,
      // financial_products: ['싸피금융']
    };
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
