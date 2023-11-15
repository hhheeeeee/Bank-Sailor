<template>
  <div class="calculatorbody">
    <div class="exchangearea">
      <div class="inputbox">
        <input type="number" />
        <img :src="fromContryflagimgurl" alt="" class="flagimg" />
        <div class="selectcountry">⌵</div>
      </div>
      <div class="exchangeicon">⇄</div>
      <div class="inputbox">
        <div class="exchangeresult">{{ exchangeresult.value }}</div>
        <img :src="toContryflagimgurl" alt="" class="flagimg" />
        <div class="selectcountry">⌵</div>
      </div>
    </div>
    <p>* 엔화/인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    <button @click="getExchangeResult">환율 추적</button>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
const store = useCounterStore();

const fromCountry = "USD";
const toCountry = "KRW";
const price = 1;
const exchangeresult = ref("null");

const fromContryflagimgurl = `/src/assets/flags/${fromCountry}.png`;
const toContryflagimgurl = `/src/assets/flags/${toCountry}.png`;

const getExchangeResult = function () {
  axios({
    method: "get",
    url: `${store.API_URL}/exchange/${fromCountry}/${toCountry}/${price}`,
  })
    .then((res) => {
      console.log(res.data);
      // exchangeresult.value = res.exchangeresult;
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style lang="scss" scoped>
.calculatorbody {
  background-color: white;
  width: 80%;
  height: 50%;
  margin-top: 30px;
  border: 4px solid #0d2a3b;
  border-radius: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.exchangearea {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

.inputbox {
  outline: none;
  width: 37%;
  height: 120px;
  border: 1px solid #0d2a3b;
  border-radius: 30px;
  background-color: #eaf6f9;
  font-size: 35px;
  padding-left: 10px;
  display: flex;
  align-items: center;
}

button {
  border: none;
  outline: none;
  width: 15%;
  height: 10%;
  border-radius: 50px;
  background-color: #1c5f82;
  color: white;
  font-size: 150%;
}

input {
  background-color: transparent;
  border: none;
  width: 70%;
}

.exchangeicon {
  font-size: 5rem;
  margin: 0px 15px;
}

.exchangeresult {
  width: 70%;
}

.flagimg {
  width: 100px;
  height: 100px;
  object-fit: fill;
}

.selectcountry {
  font-size: 120%;
  margin: 0px 10px;
}

p {
  align-self: flex-start;
  margin-left: 80px;
  margin-bottom: 30px;
}
</style>
