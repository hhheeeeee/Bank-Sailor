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
  height: 100vh;
  background-image: linear-gradient(
      rgba(255, 255, 255, 0.4),
      rgba(255, 255, 255, 0.4)
    ),
    url("@/assets/backgroundimg.png");

  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.calculatortitle {
  font-weight: 900;
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px grey;
}
</style>
