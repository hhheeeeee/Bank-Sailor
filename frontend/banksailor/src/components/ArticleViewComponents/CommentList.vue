<template>
  <div class="comment-box">

    <!-- <p>총 {{ article.value.comment_count }}건의 댓글이 있습니다</p> -->
    <div>
      <form @submit.prevent="createComment">
        <label for="comments_content">댓글 달기 : </label>
        <textarea
        type="text"
        id="comments_content"
        v-model.trim="comments_content"
        ></textarea>
        <input type="submit" label="댓글쓰기" />
      </form>
    </div>

    <div v-for="comment in comments" :key="comment.id">
      <li v-if="article && comment.article.title === article.title">
        {{ comment.content }}
        {{ comment.updated_at.slice(0, 10) }}
        
        <div v-show="comment && userInfo.id === comment.user">
          <button @click="deleteComment(comment.id)">댓삭</button>
        </div>
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
const comments = ref([])
const userInfo = store.userInfo
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

const createComment = function () {
  const content = ref("");
  axios({
    method: "post",
    url: `${store.API_URL}/articles/articles/${route.params.id}/comments/`,
    data: {
      user: userInfo.id,
      content: comments_content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
  .then((res) => {
    // 여기서 comments 배열에 새 댓글을 추
    // res.data는 서버로부터 받은 새 댓글 데이터를 포함.
    comments.value.push(res.data);

    // 댓글 입력 필드를 비운다
    comments_content.value = '';
  })
  .catch((err) => {
    console.log(err);
  });
};

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
