<template>
  <div class="calculatorbody">
    <CurrencyInput />
  </div>
</template>
<script setup>
import CurrencyInput from "@/components/ExchangeViewComponents/CurrencyInput.vue";
</script>
<style lang="scss" scoped>
.calculatorbody {
  width: 80%;
  height: 40%;
  margin-top: 30px;
  margin-bottom: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: white;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
}
</style>
