<template>
  <div>
    <h1 class="title">게시판</h1>
    
    <p></p>
    <hr>

    <form @submit.prevent="createArticle">
      <div>
        카테고리
        <select v-model="selectedCategory">
          <option v-for="category in categoryList" :key="category.id" :value="category.value">
            {{ category.value }}
          </option>
        </select>
      </div>
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="저장">
    </form>
    <button @click="moveToList()">목록</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)
const category = ref(null)
const categoryList = [
  {
    id: 1,
    value: '잡담',
  },
  {
    id: 2,
    value: '리뷰',
  }
]

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/articles/`,
    data: {
      title: title.value,
      content: content.value,
      // category: category.value,
      category: '잡담',
    },
    headers: {
        Authorization: `Token ${store.token}`
      }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'article' })
    })
    .catch((err) => {
      console.log(err)
    })
}

const moveToList = () => {
  router.push({name: 'article'})
}



</script>

<style>

</style>
