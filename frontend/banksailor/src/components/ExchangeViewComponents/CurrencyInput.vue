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
      <div class="exchangeicon">⇄</div>
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
    <button @click="getExchangeResult">환율 추적</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import CurrencyInput from "@/components/ExchangeViewComponents/CurrencyInput.vue";
import axios from "axios";
import currencyInputDropdown from "@/components/ExchangeViewComponents/currencyInputDropdown.vue";
import { useCounterStore } from "@/stores/counter";

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
  width: 100%;
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
  height: 130px;
  border: 1px solid #0d2a3b;
  border-radius: 30px;
  background-color: #eaf6f9;
  font-size: 35px;
  padding-left: 10px;
  display: flex;
  align-items: center;
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

button {
  border: none;
  outline: none;
  width: 15%;
  height: 55px;
  border-radius: 50px;
  background-color: #1c5f82;
  color: white;
  font-size: 150%;
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
