<template>
  <div class="exchangearea">
    <div class="inputbox">
      <input type="number" />
      <!-- <img :src="fromContryflagimgurl" alt="" class="flagimg" /> -->
      <currencyInputDropdown
        @selectCountry="getFromCountry"
        :firstinput="fromCountry"
        order="first"
      />
    </div>
    <div class="exchangeicon">⇄</div>
    <div class="inputbox">
      <!-- <div class="exchangeresult">{{ exchangeresult }}</div> -->
      <!-- <img :src="toContryflagimgurl" alt="" class="flagimg" /> -->
      <currencyInputDropdown
        @selectCountry="getToCountry"
        :firstinput="fromCountry"
        order="second"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import currencyInputDropdown from "@/components/ExchangeViewComponents/currencyInputDropdown.vue";
const fromCountry = ref("");
const toCountry = ref("");

const getFromCountry = function (arg) {
  fromCountry.value = arg;
};

const getToCountry = function (arg) {
  console.log(`fromcountry: ${fromCountry.value}`);
  toCountry.value = arg;
};
</script>

<style scoped>
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

input {
  background-color: transparent;
  border: none;
  width: 70%;
}
</style>
