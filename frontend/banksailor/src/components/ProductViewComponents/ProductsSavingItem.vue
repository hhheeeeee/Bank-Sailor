<template>
  <div class="record">
    <div class="box1">{{ product.dcls_month }}</div>
    <div class="box2">{{ product.kor_co_nm }}</div>
    <div class="box3">{{ product.fin_prdt_nm }}</div>
    <div class="box4">{{ product.rate_6 }}</div>
    <div class="box5">{{ product.rate_12 }}</div>
    <div class="box6">{{ product.rate_24 }}</div>
    <div class="box7">{{ product.rate_36 }}</div>
  </div>
</template>

<script setup>

defineProps({
  product: Object
})

</script>

<style scoped>
  .record {
    width: 1000px;
    height: 50px;
    border: 1px solid lightgray;
    border-bottom: 0px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .box1 {
    width: 10%;
    text-align: center;
    font-size: small;
  }

  .box2 {
    width: 18%;
    text-align: center;
    font-size: small; 
  }

  .box3 {
    width: 32%;
    text-align: center;
    font-size: small; 
  }

  .box4 {
    width: 10%;
    text-align: center;
    font-size: small; 
  }

  .box5 {
    width: 10%;
    text-align: center;
    font-size: small; 
  }

  .box6 {
    width: 10%;
    text-align: center;
    font-size: small; 
  }

  .box7 {
    width: 10%;
    text-align: center;
    font-size: small; 
  }
</style>