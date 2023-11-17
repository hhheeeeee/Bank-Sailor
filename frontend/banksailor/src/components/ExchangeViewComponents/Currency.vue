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
</style>
