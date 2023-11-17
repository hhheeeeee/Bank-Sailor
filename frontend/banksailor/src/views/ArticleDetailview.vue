<template>
  <div>
    <h1 class="title">게시판</h1>
    
    <hr>

    <div>
      <div v-if="article" >
        
        <div class="header" v-if="currentState">
          <p>{{ article.category }}</p> / <p>{{ article.title }}</p>
          <p>작성자 : {{ article.user }}</p>
          <p>작성일 : {{ article.created_at.substring(0, 10) }}</p>
          <div class="main">
            <p>{{ article.content }}</p>
          </div>
        </div>
        
        <div class="header" v-else>
          <form @submit.prevent="editArticle">
            <div>
              카테고리: <select v-model="article.category">
                <option v-for="category in categoryList" :key="category.id" :value="article.category">
                  {{ category.value }}
                </option>
              </select>
            </div>

            <div>
              <label for="title">제목:</label>
              <input type="text" v-model="article.title">
            </div>

            <div>
              <label for="content">내용:</label>
              <textarea type="text" v-model="article.content"></textarea>
            </div>
            <button v-show="!currentState">완료</button>
            <button @click="$router.go(0)">취소</button>
          </form>
        </div>
        </div>
      </div>

    
    <div>
      <button v-show="currentState" @click="onClickEvent()">수정</button>
      <button @click="deleteArticle()">삭제</button>
      <button @click="moveToList()">목록</button>
    </div>
  </div>
  
  <div class="comment-box">
    <!-- <p>총 {{ article.value.comment_count }}건의 댓글이 있습니다</p> -->
    <form @submit.prevent="createComment">
      <label for="comments_content">댓글 달기 : </label>
      <textarea type="text" id="comments_content" v-model.trim="comments_content"></textarea>
      <input type="submit" label="댓글쓰기">
    </form>

    <CommentList :article="article"/>
  </div>

</template>


<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'
import CommentList from '@/components/ArticleViewComponents/CommentList.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const title = ref(null)
const content = ref(null)
const category = ref(null)
const currentState = ref(true)
const comments_content = ref(null)
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

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const moveToList = () => {
  router.push({name: 'article'})
}

const onClickEvent = () => {
  currentState.value = !currentState.value
}

const editArticle = function () {
  currentState.value = !currentState.value
    axios({
      method: 'put',
      url: `${store.API_URL}/articles/articles/${route.params.id}/`,
      data: {
        title: article.value.title,
        content: article.value.content,
        category: article.value.category,
      },
    })
      .then((res) => {
        console.log(res.data)
        currentState.value = true
      }).catch((error) => {
        console.log(error)
      })
  }

  const deleteArticle = function (request, article_pk) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/articles/articles/${route.params.id}/`,
    })
      .then((res) => {
        console.log('삭제완')
        alert('삭제 시 복구되지 않습니다.')
        router.push({ name: 'article' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createComment = function () {
    const content = ref('')
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/articles/${route.params.id}/comments/`,
      data: {
          content: comments_content.value,
        },
      })  
      .then((res) => {
        console.log(res)
        console.log('된다고해!!!!!!!!!')
        router.go(0)
      })
      .catch((err) => {
        console.log(err)
      })
    }

</script>

<style>
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

.header {
  margin: 20px;
  font-size: 1.2rem;
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
}

.header p {
  display: inline;
  margin-right: 10px;
}

.main {
  margin: 20px;
  font-size: 1rem;
  line-height: 1.6;
}

.comment-box {
  margin: 20px;
}

textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  resize: vertical;
}

input[type='submit'] {
  padding: 8px 16px;
  background-color: #1c5f82;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

input[type='submit']:hover {
  background-color: #144362;
}

button {
  border: 1px solid #1c5f82;
  border-radius: 30px;
  padding-bottom: 4px;
  width: 80px;
  height: 35px;
}
</style>
