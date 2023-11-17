<template>
  <div>
    <h1 class="title">게시판</h1>

    <form @submit.prevent="searchArticle" class="search-bar">
      <select v-model="key_for_search">
        <option value="all">전체</option>
        <option value="category">분류</option>
        <option value="title">제목</option>
        <option value="content">내용</option>
        <option value="user">작성자</option>
      </select>
      &nbsp;   <!-- 줄바꿈없이 간격띄우는 인자 -->
      <input type="text" v-model="value_for_search">
      &nbsp;
      <input type="submit" label="검색">
      <!-- <button @click="searchArticle()">검색</button> -->
    </form>

    <hr>

    <div v-if="searchfinish===true">
      <h3>총 {{ filtered_article.length }}건의 검색결과가 있습니다</h3>
      <hr>
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
            <tr v-for="article in filtered_article" :key="article.id">
              <td>{{ article.id }}</td>
              <td>{{ article.category }}</td>
              <td>{{ article.title }}</td>
              <td>{{ article.user }}</td>
              <td>{{ article.created_at.substring(0, 10) }}</td>
            </tr>
          </tbody>
        </table>
        <button @click="(searchfinish = !searchfinish)">목록가기</button>
      </div>

    </div>
    
    <div v-else>
      <ArticleList />

      <RouterLink :to="{ name: 'ArticleCreateView' }">
        <button>새글쓰기</button>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
import ArticleList from '@/components/ArticleViewComponents/ArticleList.vue'

const store = useCounterStore()
const searchfinish = ref(false)
const key_for_search = ref(null)
const value_for_search = ref(null)

onMounted(() => {
  store.getArticles()
  store.getComments()
})

console.log(store.articles)

const filtered_article = computed(() => {
  if (key_for_search.value && value_for_search.value) {
    const key = key_for_search.value
    const value = value_for_search.value
    if (key === 'all') {
      return store.articles.filter(
        (article) =>
        store.articles.category.includes(value) ||
        store.articles.title.includes(value) ||
        store.articles.content.includes(value) ||
        store.articles.user.includes(value)
      )
    } else {
      return store.articles.filter((article) =>
        article[key].includes(value)
      )
    }
  } else {
    return store.articles.value
  }
});

const searchArticle = function () {
  if (value_for_search == '') {
    alert('검색어를 입력해주세용!')
  } else {
    searchfinish.value = !searchfinish.value
  }
}

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

.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.search-bar select,
.search-bar input[type="text"],
.search-bar button {
  padding: 8px;
  margin: 0 5px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
}

.search-bar button {
  background-color: #1c5f82;
  color: white;
  border: none;
  cursor: pointer;
}

.search-bar button:hover {
  background-color: #144362;
}

</style>
