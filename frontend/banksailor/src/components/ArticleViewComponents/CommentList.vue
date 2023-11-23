<template>
  <div class="comment-box">

    <div class="input-comment"> <!-- 댓글입력창 -->
      <form @submit.prevent="createComment" class="input-bar">
        <textarea
        type="text"
        id="comments_content"
        v-model.trim="comments_content"
        placeholder="댓글을 입력해주세요"
        ></textarea>
        <input type="submit" label="댓글쓰기" value="작성!"/>
      </form>
    </div>

    <div v-for="comment in comments" :key="comment.id"> <!-- 댓글목록창 -->
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

<style scoped>
.input-comment {
  width: 100%;
}
.input-bar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}
.input-bar textarea,
.input-bar button {
  padding: 8px;
  margin: 0 5px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
}
.input-bar input[type="submit"] {
  height: auto;
  padding: 8px;
  /* margin: 0 5px; */
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
  background-color: rgb(0, 53, 133);
  color: white;
  border: none;
  cursor: pointer;
}
.input-bar button:hover {
  background-color: rgb(131, 133, 0);
}

</style>