<template>
  <div class="container1">
    <h1 class="title">게시판</h1>
    <hr />
    <form @submit.prevent="createArticle" class="customform">
      <div class="form-group">
        <label class="form-label" for="category">카테고리</label>
        <select v-model="selectedCategory" id="category">
          <option
            v-for="category in categoryList"
            :key="category.id"
            :value="category.value"
          >
            {{ category.value }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label" for="title">제목:</label>
        <input
          type="text"
          v-model.trim="title"
          id="title"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label class="form-label" for="content">내용:</label>
        <textarea
          v-model.trim="content"
          id="content"
          class="form-control form-control-textarea"
        ></textarea>
      </div>
      <input type="submit" value="저장" class="form-submit" />
    </form>
    <button class="btn" @click="moveToList()">목록</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const store = useCounterStore();
const router = useRouter();

const title = ref(null);
const content = ref(null);
const category = ref(null);
const categoryList = [
  {
    id: 1,
    value: "잡담",
  },
  {
    id: 2,
    value: "리뷰",
  },
];

const createArticle = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/articles/articles/`,
    data: {
      title: title.value,
      content: content.value,
      // category: category.value,
      category: "잡담",
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: "article" });
    })
    .catch((err) => {
      console.log(err);
    });
};

const moveToList = () => {
  router.push({ name: "article" });
};
</script>

<style scoped>
.container1 {
  width: 100%;
  margin: 0;
  padding: 0;
  background-color: #ffffff;
}

.title {
  margin: 0;
  width: 100%;
  padding: 20px;
  text-align: center;
  color: #1c5f82;
  background-color: #4db7e5;
}

.customform {
  max-width: 900px;
  height: 60vh;
  margin: 20px auto;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 10px;
}

.form-group {
  margin-bottom: 10px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  color: #1c5f82;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #cccccc;
  border-radius: 5px;
}

.form-control-textarea {
  height: 300px;
}

.form-submit {
  padding: 10px 20px;
  color: #ffffff;
  background-color: #1c5f82;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.form-submit:hover {
  background-color: #4db7e5;
}

.btn {
  display: block;
  width: 100px;
  margin: 20px auto;
  padding: 10px;
  color: #ffffff;
  background-color: #1c5f82;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn:hover {
  background-color: #4db7e5;
}
</style>
