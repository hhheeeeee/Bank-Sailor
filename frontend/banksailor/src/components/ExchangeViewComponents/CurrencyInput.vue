<template>
  <div class="container1">
    <div class="exchangearea">
      <div class="inputbox">
        <input type="number" class="priceinput" v-model="price" />
        <!-- <img :src="fromContryflagimgurl" alt="" class="flagimg" /> -->
        <currencyInputDropdown
          @selectCountry="getFromCountry"
          :firstinput="fromCountry"
          order="first"
        />
      </div>
      <Arrow />
      <div class="inputbox">
        <!-- <img :src="toContryflagimgurl" alt="" class="flagimg" /> -->
        <div class="exchangeresult">{{ exchangeresult }}</div>
        <currencyInputDropdown
          @selectCountry="getToCountry"
          :firstinput="fromCountry"
          order="second"
        />
      </div>
    </div>
    <p>* 엔화/인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    <button @click="getExchangeResult" class="currencybutton">환율 추적</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import CurrencyInput from "@/components/ExchangeViewComponents/CurrencyInput.vue";
import axios from "axios";
import currencyInputDropdown from "@/components/ExchangeViewComponents/currencyInputDropdown.vue";
import { useCounterStore } from "@/stores/counter";
import Arrow from "@/components/ExchangeViewComponents/Arrow.vue";
const store = useCounterStore();
const exchangeresult = ref("");
const fromCountry = ref(null);
const toCountry = ref(null);
const price = ref(null);

const getFromCountry = function (arg) {
  fromCountry.value = arg;
};

const getToCountry = function (arg) {
  console.log(`fromcountry: ${fromCountry.value}`);
  toCountry.value = arg;
};

// const fromContryflagimgurl = `/src/assets/flags/${fromCountry}.png`;
// const toContryflagimgurl = `/src/assets/flags/${toCountry}.png`;

const getExchangeResult = function () {
  if (price.value == null) {
    window.alert("금액를 입력해주세요");
    return;
  }
  if (fromCountry.value == null) {
    window.alert("현재 통화를 선택해주세요");
    return;
  }

  if (toCountry.value == null) {
    window.alert("변환할 통화를 선택해주세요");
    return;
  }
  axios({
    method: "get",
    url: `${store.API_URL}/exchange/${fromCountry.value}/${toCountry.value}/${price.value}/`,
  })
    .then((res) => {
      console.log(res.data);
      exchangeresult.value = res.data.exchangeresult;
      // console.log(exchangeresult.value);
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.container1 {
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
.exchangearea {
  width: 100%;
  height: 90%;
  display: flex;
  justify-content: space-between;
}

.inputbox {
  outline: none;
  width: 45%;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background-color: rgb(234, 218, 190);
  font-size: 30px;
}

.exchangeresult {
  width: 70%;
}

.selectcountry {
  font-size: 120%;
  margin: 0px 10px;
}

.priceinput {
  background-color: transparent;
  border: none;
  width: 70%;
  margin: 0px 10px;
}

.priceinput:focus {
  border-color: blue;
  outline: none;
}

.currencybutton {
  border: none;
  outline: none;
  width: 15%;
  height: 40px;
  border-radius: 50px;
  background-color: rgb(6, 152, 242);
  color: rgb(28, 55, 89);
  font-size: 150%;
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
  width: 100%;
}

.currencybutton:hover {
  background-color: rgb(28, 55, 89);
  color: white;
  box-shadow: 3px 3px 3px grey;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
