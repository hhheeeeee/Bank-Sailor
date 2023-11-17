<template>
  <div>
    <h4>정기예금</h4>
    <p>은행</p>
    <select v-model="selectedBank">
      <option disabled value="">원하시는 은행을 선택하세요</option>
      <option v-for="bank in bankList" :key="bank">{{ bank }}</option>
    </select>
    <br>
    <br>
    <button @click="buttonClick">검색</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const selectedBank = ref('')

const props = defineProps({
  bankList: Array
})

const router = useRouter()

const emit = defineEmits(['sendSelectedBank'])
const buttonClick = () => {
  emit('sendSelectedBank', selectedBank.value)
  router.push({ name: 'deposit' })
}


</script>

<style lang="scss" scoped>
select {
  width: 90%;
}
p {
  margin: 0;
  margin-top: 20px;
}
</style>