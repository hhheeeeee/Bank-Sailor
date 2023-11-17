<template>
  <div>
    <table class="table">
    <thead>
        <th>번호</th>
        <th>분류</th>
        <th>제목</th>
        <th>작성자</th>
        <th>작성일</th>
    </thead>
    <tbody>
      <td>-</td>
      <td>공지</td>
      <td>무분별한 도배, 욕설, 비방은 무통보 삭제될 수 있습니다</td>
      <td>항해사</td>
      <td>2000-00-00</td>
    </tbody>
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </table>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleViewComponents/ArticleListItem.vue'

const store = useCounterStore()


// console.log(store.articles)
// console.log(store.comments)
</script>
