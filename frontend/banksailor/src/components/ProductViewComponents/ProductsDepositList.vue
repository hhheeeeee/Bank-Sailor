<template>
  <div class="index-bar">
    <div class="box1">공시 제출월</div>
    <div class="box2">금융회사명</div>
    <div class="box3">상품명</div>
    <div class="box4">6개월</div>
    <div class="box5">12개월</div>
    <div class="box6">24개월</div>
    <div class="box7">36개월</div>
  </div>
  <div v-if="selectedBank">
    <div v-for="product in filteredProducts" :key="product.id">
      <div v-if="product.kor_co_nm === selectedBank">
        <ProductsDepositItem :product="product"/>
      </div>
    </div>
  </div>
  <div v-else>
    <ProductsDepositItem v-for="product in store.deposits" :key="product.id" :product="product"/>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProductsDepositItem from '@/components/ProductViewComponents/ProductsDepositItem.vue'

const store = useCounterStore()

onMounted(() => {
  store.getDeposits()
})

const props = defineProps({
  selectedBank: String
})

const filteredProducts = computed(() => {
  return props.selectedBank ? store.deposits.filter((product) => product.kor_co_nm === props.selectedBank) : store.deposits
})

</script>

<style scoped>
  .index-bar {
    width: 100%;
    height: 50px;
    background-color: whitesmoke;
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