<template>
      <tbody>
      <!-- <tr v-for="article in store.articles" :key="article.id"> -->
        <td>{{ article.id}}</td>
        <td>{{ article.category }}</td>
        <td>
          <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
            <p>{{ article.title }}</p>
          </RouterLink>
        </td>
        <td><!-- <p>{{ article.users }}</p> --></td>
        <td>{{ article.created_at }}</td>
      <!-- </tr> -->
    </tbody>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router'
  
  const store = useCounterStore()
  defineProps({
    article: Object
  })
  
  </script>
  
  <style>
  .table {   
    text-align: center;
  }
  </style>