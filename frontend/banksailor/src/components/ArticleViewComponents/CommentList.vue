<template>
  <div>
    <!-- <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    /> -->
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
const comment = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/comments/`
    // url: `${store.API_URL}/articles/articles/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
      comment.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>
