<template>
  <div class="container1">
    <div class="exchangearea">
      <div class="inputbox">
        <input type="number" class="priceinput" v-model="price" />
        <select class="select" @change="selectedCountry1">
          <option value="null" disabled selected hidden>통화</option>
          <option disabled value="">Please select one</option>
          <template v-for="item in CountriesList" :key="item.id">
            <option>{{ item.cur_unit }}</option>
          </template>
        </select>
      </div>
      <Arrow />
      <div class="inputbox">
        <div class="exchangeresult">
          <div>{{ exchangeresult }}</div>
          <div>₩</div>
        </div>
        <!-- <select class="select" @change="selectedCountry2">
          <option value="null" disabled selected hidden>통화</option>
          <option disabled value="">Please select one</option>
          <template v-for="item in CountriesList" :key="item.id">
            <option v-if="item.cur_unit != fromCountry">
              {{ item.cur_unit }}
            </option>
          </template>
        </select> -->
      </div>
    </div>
    <p>* 엔화/인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
    <button @click="getExchangeResult" class="search-btn">환율 추적</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Swal from "sweetalert2";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import Arrow from "@/components/ExchangeViewComponents/Arrow.vue";
const store = useCounterStore();
const exchangeresult = ref("");
const fromCountry = ref(null);
const toCountry = "KRW";
const price = ref(null);
var st_date = new Date()
  .toISOString()
  .substr(0, 10)
  .replace("T", " ")
  .replace("-", "")
  .replace("-", "");
const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener("mouseenter", Swal.stopTimer);
    toast.addEventListener("mouseleave", Swal.resumeTimer);
  },
});

const getExchangeResult = function () {
  if (price.value == null) {
    Toast.fire({
      icon: "warning",
      title: "금액를 입력해주세요",
    });
    return;
  }
  if (fromCountry.value == null) {
    Toast.fire({
      icon: "warning",
      title: "변환할 통화를 선택해주세요",
    });
    return;
  }

  // if (toCountry.value == null) {
  //   Toast.fire({
  //     icon: "warning",
  //     title: "변환할 통화를 선택해주세요",
  //   });
  //   return;
  // }
  axios({
    method: "get",
    url: `${store.API_URL}/exchange/${fromCountry.value}/${toCountry}/${price.value}/${st_date}`,
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

const selectedCountry1 = (event) => {
  fromCountry.value = event.target.value;
};

const selectedCountry2 = (event) => {
  toCountry.value = event.target.value;
};

const CountriesList = [
  { id: 0, cur_unit: "AED" },
  { id: 1, cur_unit: "ATS" },
  { id: 2, cur_unit: "AUD" },
  { id: 3, cur_unit: "BEF" },
  { id: 4, cur_unit: "BHD" },
  { id: 5, cur_unit: "CAD" },
  { id: 6, cur_unit: "CHF" },
  { id: 7, cur_unit: "CNH" },
  { id: 8, cur_unit: "DEM" },
  { id: 9, cur_unit: "DKK" },
  { id: 10, cur_unit: "ESP(100)" },
  { id: 11, cur_unit: "EUR" },
  { id: 12, cur_unit: "FIM" },
  { id: 13, cur_unit: "FRF" },
  { id: 14, cur_unit: "GBP" },
  { id: 15, cur_unit: "HKD" },
  { id: 16, cur_unit: "IDR(100)" },
  { id: 17, cur_unit: "ITL(100)" },
  { id: 18, cur_unit: "JPY(100)" },
  { id: 19, cur_unit: "KRW" },
  { id: 20, cur_unit: "KWD" },
  { id: 21, cur_unit: "MYR" },
  { id: 22, cur_unit: "NLG" },
  { id: 23, cur_unit: "NOK" },
  { id: 24, cur_unit: "NZD" },
  { id: 25, cur_unit: "SAR" },
  { id: 26, cur_unit: "SEK" },
  { id: 27, cur_unit: "SGD" },
  { id: 28, cur_unit: "THB" },
  { id: 29, cur_unit: "USD" },
  { id: 30, cur_unit: "XOF" },
];
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
  display: flex;
  justify-content: space-between;
}

.selectcountry {
  font-size: 120%;
  margin: 0px 10px;
}

.priceinput {
  background-color: transparent;
  border: none;
  width: 70%;
}

.priceinput:focus {
  border-color: blue;
  outline: none;
}

.exchangeicon {
  font-size: 5rem;
  margin: 0px 15px;
}

.exchangeresult {
  width: 70%;
}

p {
  align-self: flex-start;
  width: 100%;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.search-btn {
  margin-top: 10px;
  border: none;
  width: 100px;
  height: 50px;
  border-radius: 5px;
  background-color: rgb(7, 152, 242);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-btn:hover {
  background-color: rgb(17, 132, 222);
  font-weight: 700;
  color: white;
}

.select {
  width: 70px;
  font-size: 20px;
  border: none;
  background-color: transparent;
}
</style>
