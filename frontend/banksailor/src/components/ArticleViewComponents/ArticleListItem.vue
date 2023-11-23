<template>
  <tbody class="tbody3">
    <td class="td1">{{ article.id }}</td>
    <td class="td2">{{ article.category }}</td>
    <td class="td3">
      <RouterLink
        :to="{ name: 'ArticleDetailView', params: { id: article.id } }"
      >
        <p>{{ article.title }}</p>
      </RouterLink>
    </td>
    <td class="td4">
      <p>{{ article.username }}</p>
    </td>
    <td class="td5">{{ article.created_at.slice(0,10) }}</td>
  </tbody>
</template>


<script setup>
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";

const store = useCounterStore();
defineProps({
  article: Object,
});
</script>


<style>
.tbody3 {
  border-bottom: 1px solid darkgray;
}
.td1 {
  width: 10%;
  border-collapse: collapse;
  text-align: center;
}
.td2 {
  width: 15%;
  border-collapse: collapse;
  text-align: center;
}
.td3 {
  width: 45%;
  border-collapse: collapse;
  text-align: center;
}
.td4 {
  width: 15%;
  border-collapse: collapse;
  text-align: center;
}
.td5 {
  width: 15%;
  border-collapse: collapse;
  text-align: center;
}
</style>
