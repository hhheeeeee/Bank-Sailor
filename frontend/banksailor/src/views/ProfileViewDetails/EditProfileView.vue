<template>
  <div class="container1">

    <h1>포트폴리오 수정</h1>

    <form @submit.prevent="createPortfolio">
    <div>
      <label for="ID">ID : </label>
      <!-- <input type="text" v-model="userInfo.user"> -->
    </div>

    <div>
      <label for="password">비밀번호 : </label>
      <input type="text" v-model="password">
    </div>

    <div>
      저축성향 : 

      <div>
        <input v-if="portfolio" type="radio" id="economy" name="saving_style" value="economy" v-model="portfolio.saving_style"/>
        
        <input v-else type="radio" id="economy" name="saving_style" value="economy" v-model="savingstyle"/>
          <label for="savingstyle">알뜰형</label>
      </div>
      <div>
        <input v-if="portfolio" type="radio" id="challenge" name="saving_style" value="challenge" v-model="portfolio.saving_style"/>

        <input v-else type="radio" id="challenge" name="saving_style" value="challenge" v-model="savingstyle"/>
        <label for="savingstyle">도전형</label>
      </div>
      <div>
        <input v-if="portfolio" type="radio" id="diligent" name="saving_style" value="diligent" v-model="portfolio.saving_style"/>

        <input v-else type="radio" id="diligent" name="saving_style" value="diligent" v-model="savingstyle"/>
        <label for="savingstyle">성실형</label>
      </div>
    </div>

    <div>
        <label for="favorite_bank">최애은행 : </label>
        <select v-if="portfolio" v-model="portfolio.favorite_bank">
          <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
        </select>
        <select v-else v-model="favoritebank">
          <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
        </select>
      </div>
    
    <input type="submit" value="저장하기">

    </form>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()
const userInfo = store.userInfo
const portfolio = ref(null)
const savingstyle = ref('')
const favoritebank = ref('')
const banks = [
  "KEB하나은행",
  "SC제일은행",
  "국민은행",
  "신한은행",
  "외환은행",
  "우리은행",
  "한국시티은행",
  "지방은행",
  "경남은행",
  "광주은행",
  "대구은행",
  "부산은행",
  "전북은행",
  "제주은행",
  "특수은행",
  "기업은행",
  "농협",
  "수협",
  "한국산업은행",
  "한국수출입은행",
];

onMounted(() => {
  getPortfolio()
})

console.log(store.token)
console.log('포폴', portfolio)
console.log('userInfo', store.getUserInfo)

const getPortfolio = function () {
      axios({
        method: "get",
        url: `${store.API_URL}/accounts/find/input_portfolioData/`,
      })
        .then((res) => {
          console.log('포폴겟: ', res.data)
          portfolio.value = res.data;

        })
        .catch((err) => {
          console.log(err);
        });
    };

    const createPortfolio = function () {
      axios({
        method: "post",
        url: `${store.API_URL}/accounts/find/input_portfolioData/`,
        data: {
          saving_style: savingstyle.value,
          favorite_bank: favoritebank.value,
        },
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    };

</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
