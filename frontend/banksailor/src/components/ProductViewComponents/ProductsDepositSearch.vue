<template>
  <div class="content">
    <h4>정기예금</h4>
    <p>은행</p>
    <select v-model="selectedBank">
      <option disabled value="">원하시는 은행을 선택하세요</option>
      <option>전체</option>
      <option v-for="bank in bankList" :key="bank">{{ bank }}</option>
    </select>
    <br />
    <br />
    <button class="searchbutton" @click="buttonClick">검색</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const selectedBank = ref("");

const props = defineProps({
  bankList: Array,
});

const router = useRouter();

const emit = defineEmits(["sendSelectedBank"]);
const buttonClick = () => {
  emit("sendSelectedBank", selectedBank.value);
  router.push({ name: "deposit" });
};
</script>

<style scoped>
.content {
  width: 100%;
  height: 10%;
  border-left: 5px solid hsl(216, 100%, 26%);
  padding: 10px 10px;
  background-color: rgb(189, 217, 252);
  /* margin: 10px 10px; */
}

.searchbutton {
  margin-left: 30px;
  border: none;
  border-radius: 5px;
  background-color: rgb(7, 152, 242);
  color: white;
  cursor: pointer;
}

.searchbutton:hover {
  background-color: rgb(17, 132, 222);
  font-weight: 700;
  color: white;
}

select {
  width: 100%;
}

p {
  margin: 0;
  margin-top: 20px;
}
</style>
