<template>
  <div>
    <h1 class="title">게시판</h1>
    
    <p>검색창 자리 게시판이랑 가로길이 똑같이</p>
    <input type="text" v-model="searchQuery" placeholder="검색어를 입력하세요" />
    
    <div>
      <select v-model="search_key">
        <option value="all">전체</option>
        <option value="category">분류</option>
        <option value="title">제목</option>
        <option value="contents">내용</option>
        <option value="user">작성자</option>
      </select>
      &nbsp;
      <input type="text" v-model="search_value" @keyup.enter="fnPage()">
      &nbsp;
      <button @click="fnPage()">검색</button>
    </div>

    <hr>
    
    <ArticleList />

    <RouterLink :to="{ name: 'ArticleCreateView' }">
      <button>새글쓰기</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
  store.getComments()
})
</script>

<style scoped>
.title {
  text-align: center;
  font-size: 5rem;
  color: #1c5f82;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
  margin: 35px;
  text-shadow: -2px 0px white, 0px 2px white, 2px 0px white, 0px -2px white;
}

button {
  border: 1px solid #1c5f82;
  border-radius: 30px;
  padding-bottom: 4px;
  width: 80px;
  height: 35px;
  color: white;
  background-color: #1c5f82;
}
</style>
