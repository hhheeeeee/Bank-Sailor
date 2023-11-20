<template>
  <div class="containerbody">
    <h1 class="calculatortitle">환율 계산기</h1>
    <Currency />
  </div>
</template>

<script setup>
import Currency from "@/components/ExchangeViewComponents/Currency.vue";
</script>

<style scoped>
.containerbody {
  width: 100%;
  height: 91vh;
  background-color: rgb(214, 232, 255);
  /* background-image: linear-gradient(
      rgba(255, 255, 255, 0.4),
      rgba(255, 255, 255, 0.4)
    ),
    url("@/assets/backgroundimg.png"); */

  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.calculatortitle {
  background-color: rgb(214, 232, 255);
  color: rgb(28, 54, 89);
  font-weight: 700;
  font-size: 40px;
  margin-bottom: 50px;
}
</style>
