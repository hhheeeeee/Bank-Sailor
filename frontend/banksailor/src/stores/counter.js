import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])  
  const comments = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/articles/`
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createArticle = function () {
    axios({
      method: 'post',
      url: `${API_URL}/articles/articles/`
    })
      .then((res) => {
        console.log(res.data)
      }).catch((error) => {
        console.log(error)
      })
  }
  
  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/comments/`,
    })
      .then((res) => {
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createComments = function () {
    axios({
      method: 'post',
      url: `${API_URL}/articles/articles/<int:article_pk>/comments/`
    })
      .then((res) => {
        console.log(res.data)
      }).catch((error) => {
        console.log(error)
      })
  }

  return { articles, API_URL, getArticles, createArticle, getComments, }
}, {persist:true})