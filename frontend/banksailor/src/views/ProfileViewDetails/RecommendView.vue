<template>
  <div class="container1">
    <h1>추천~</h1>

    <div v-if="loading">로딩 중...</div>

    <div v-if="!loading && depositList.length > 0">
      <h2>Deposit List</h2>
      <ul>
        <li v-for="deposit in depositList" :key="deposit.id">
          {{ deposit.fin_prdt_nm }}
        </li>
      </ul>
    </div>

    <div v-if="!loading && savingList.length > 0">
      <h2>Saving List</h2>
      <ul>
        <li v-for="saving in savingList" :key="saving.id">
          {{ saving.fin_prdt_nm }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, ref } from "vue";
import axios from "axios";

const store = useCounterStore();
const loading = ref(false);
const depositList = ref([]);
const savingList = ref([]);

onMounted(async () => {
  await getRecommend();
});

const getRecommend = async function () {
  loading.value = true; // 로딩 시작

  try {
    const response = await axios.post(
      `${store.API_URL}/products/recommend/`,
      null,
      {
        headers: {
          Authorization: `Token ${store.token}`,
        },
      }
    );

    depositList.value = response.data.deposits || [];
    savingList.value = response.data.savings || [];
  } catch (error) {
    console.error("Error fetching recommendations:", error);
  } finally {
    loading.value = false; // 로딩 완료
  }
};
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
