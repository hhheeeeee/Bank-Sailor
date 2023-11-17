<template>
  <div class="main">
    <aside>
      <ProductsDepositSearch :bank-list="bankList" @sendSelectedBank="handleSelectedBank" />
    </aside>
    <article>
      <ProductsDepositList :selected-bank="selectedBank" />
    </article>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ProductsDepositList from '../components/ProductViewComponents/ProductsDepositList.vue';
import ProductsDepositSearch from '../components/ProductViewComponents/ProductsDepositSearch.vue';

const bankList = ref([])
const selectedBank = ref('')
const store = useCounterStore()

// 은행명 리스트 생성하기
const getBankList = () => {
  for (let prdt of store.deposits) {
    const bankName = prdt.kor_co_nm

    // 은행명 중복 검사
    if (!bankList.value.includes(bankName)) {
      bankList.value.push(bankName);
    }
  }
}

watchEffect(() => {
  getBankList()
})

const handleSelectedBank = (bankname) => {
  selectedBank.value = bankname
}

</script>

<style scoped>
 .main {
  display: flex;
  margin: 0;
 }

  aside {
    width: 250px;
  }

  article {
    width: 950px;
  }
</style>