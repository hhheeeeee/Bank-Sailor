<template>
  <div class="container1">
    <h1>추천~</h1>

    {{ test }}
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted, watchEffect, ref, computed } from "vue";
import { Form, Field, defineRule } from "vee-validate";
import axios from "axios";
const store = useCounterStore();
const test = ref(null);
onMounted(() => {
  // username.value = store.userInfo.username;
  store.getUserInfo();
});

console.log(store.userInfo);
test.value = store.userInfo;
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
