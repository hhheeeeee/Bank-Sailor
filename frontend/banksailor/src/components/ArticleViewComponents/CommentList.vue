<template>
  <div class="comment-box">

    <!-- <p>총 {{ article.value.comment_count }}건의 댓글이 있습니다</p> -->
    <form @submit.prevent="createComment">
      <label for="comments_content">댓글 달기 : </label>
      <textarea type="text" id="comments_content" v-model.trim="comments_content"></textarea>
      <input type="submit" label="댓글쓰기">
    </form>

    <div v-for="comment in comments" :key="comment.id">
      <li v-if="article && comment.article.title === article.title">
        {{ comment.content }}
        {{ comment.updated_at.slice(0, 10) }}
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


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const comments = ref(null)
const comments_content = ref(null)

defineProps({
  article: Object,
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/comments/`
  })
    .then((res) => {
      console.log('댓글', res.data)
      comments.value = res.data
      console.log('댓글', comments)
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
