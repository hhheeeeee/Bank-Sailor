
<template>
  <div>
    <!-- <p>총 {{ article.comment_count }}건의 댓글이 있습니다</p> -->
    <form>
      <textarea name="" id="" cols="30" rows="5"></textarea>
      <input type="submit">
    </form>
    
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
// const article = article
const comments = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/comments/`
    // url: `${store.API_URL}/articles/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      comments.value = res.data
      console.log(comments)
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
      console.log('삭제완')
      alert('댓글이 삭제됩니다.')
      router.go(0)
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>
