<template>
  <div>
    <div v-for="comment in comments" :key="comment.id">
      <li v-if="article && comment.article.title === article.title">
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


const store = useCounterStore()
  defineProps({
    article: Object
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
