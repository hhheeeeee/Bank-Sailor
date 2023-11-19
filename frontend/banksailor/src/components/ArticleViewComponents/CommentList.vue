<template>
  <div>
    <!-- <p>총 {{ article.value.comment_count }}건의 댓글이 있습니다</p> -->
    <div v-show="!store.isLogin">
      <p>로그인 시 댓글 작성이 가능합니다</p>
    </div>
    <form v-show="store.isLogin" @submit.prevent="createComment">
      <label for="comments_content">댓글 달기 : </label>
      <textarea type="text" id="comments_content" v-model.trim="comments_content"></textarea>
      <input type="submit" label="댓글쓰기">
    </form>

    <div v-for="comment in comments" :key="comment.id">
      <li>
        {{ comment.content }}
        {{ comment.updated_at.substring(0, 10) }}
        <button @click="deleteComment(comment.id)">댓삭</button>

      </li>
    </div>

  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'


const createComment = function () {
    const content = ref('')
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/articles/${route.params.id}/comments/`,
      data: {
          content: comments_content.value,
        },
      headers: {
          Authorization: `Token ${store.token}`,
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


const store = useCounterStore()
  defineProps({
    article: Object,
  })
const route = useRoute()
const router = useRouter()
const comments = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/comments/`
  })
    .then((res) => {
      // console.log(res.data)
      comments.value = res.data
      // console.log(comments)
    })
    .catch((err) => {
      console.log(err)
    })
})

const deleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/comments/${commentId}/`,
  })
    .then((res) => {
      // console.log('삭제완')
      alert('댓글이 삭제됩니다.')
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>
