<template>
  <div class="container1">

    <h1>포트폴리오 수정</h1>

    <div>
      <label for="ID">ID : </label>
      <input type="text" v-model="userInfo.username">
    </div>
    
    <form v-if="portfolio.length > 0 && portfolio.some(item => item.user === userInfo.id)" @submit.prevent="editPortfolio(portfolio.find(item => item.user === userInfo.id).id)">
      수정폼
      {{ portfolio }}
      <div>
        <label for="ID">비밀번호 : </label>
        <input type="text">
      </div>
      <div>
        저축성향 : 
        <div>
          <input type="radio" id="economy" name="saving_style" value="economy" v-model="saving_style">
          <label for="economy">알뜰형</label>
        </div>
        <div>
          <input type="radio" id="challenge" name="saving_style" value="challenge" v-model="saving_style">
          <label for="challenge">도전형</label>
        </div>
        <div>
          <input type="radio" id="ecnonomy" name="saving_style" value="diligent" v-model="saving_style">
          <label for="diligent">성실형</label>
        </div>
      </div>
      <div>
        <label for="favorite_bank">최애은행 : </label>
          <select v-model="favorite_bank">
            <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
          </select>
        </div>
      <input type="submit" value="저장하기">
    </form>

    <form v-else @submit.prevent="createPortfolio">
      크리에이트 폼
      <div>
        <label for="ID">비밀번호 : </label>
        <input type="text">
      </div>
      <div>
        저축성향 : 
        <div>
          <input type="radio" id="economy" name="saving_style" value="economy" v-model="saving_style">
          <label for="economy">알뜰형</label>
        </div>
        <div>
          <input type="radio" id="challenge" name="saving_style" value="challenge" v-model="saving_style">
          <label for="challenge">도전형</label>
        </div>
        <div>
          <input type="radio" id="ecnonomy" name="saving_style" value="diligent" v-model="saving_style">
          <label for="diligent">성실형</label>
        </div>
      </div>
      <div>
        <label for="favorite_bank">최애은행 : </label>
          <select v-model="favorite_bank">
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
const portfolio = ref([])
const saving_style = ref('')
const favorite_bank = ref('')
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

// console.log(store.token)
// console.log('포폴', portfolio)
// console.log('userInfo', userInfo)

const getPortfolio = function () {
      axios({
        method: "get",
        url: `${store.API_URL}/accounts/find/input_portfolioData/`,
      })
        .then((res) => {
          portfolio.value = res.data;
          console.log(portfolio)
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
          user: userInfo.id,
          saving_style: saving_style.value,
          favorite_bank: favorite_bank.value,
        },
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        .then((res) => {
          console.log(res.data);
          alert('정상적으로 저장되었습니다!')
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const editPortfolio = function (portfolioId) {
      axios({
        method: "put",
        url: `${store.API_URL}/accounts/find/get_portfolioData/${portfolioId}`,
        data: {
          user: userInfo.id,
          saving_style: saving_style.value,
          favorite_bank: favorite_bank.value,
        },
        headers: {
          Authorization: `Token ${store.token}`
        }
      })
        .then((res) => {
          console.log(res.data);
          alert('수정 완료')
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
