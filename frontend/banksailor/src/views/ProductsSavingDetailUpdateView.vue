<template>
  <div>
    <a href="#" @click.prevent="goBack">뒤로가기</a>
    <h1>금리 수정</h1>
    <hr>
    <p>현재 금리: {{ this.$route.query.rateValue ? this.$route.query.rateValue : '없음' }}</p>
    <form @submit.prevent="updateRate">
      <label for="newRate">수정 금리: </label>
      <input type="number" step="0.0001" id="newRate" v-model="newRate">
      <input type="submit" value="수정">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'
import { useCounterStore } from "@/stores/counter";


const router = useRouter()
const route = useRoute()
const store = useCounterStore()

const newRate = ref(null)

const sendMail = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/products/email/`,
    params: {
      prdtCode: route.params.id,
      oldRate: route.query.rateValue,
      newRate: newRate.value,
      period: route.params.rate
    }
  })
    .then((response) => {
      console.log(response)
    })
    .catch((error) => {
      console.log(error)
    })
}

const updateRate = () => {
  axios({
    method: "put",
    url: `${store.API_URL}/products/saving/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      rate: newRate.value,
      rateType: route.params.rate
    }
  })
    .then((response) => {
      alert('금리가 수정되었습니다.');
      store.getSavings()
      sendMail()
      router.push({ name: 'savingdetail', params: { id: route.params.id }})
    })
    .catch((error) => {
      console.log(error);
    });
};



const goBack = () => {
  router.push({ name: 'savingdetail', params: { id: route.params.id } } )
}  
</script>

<style scoped>

</style>