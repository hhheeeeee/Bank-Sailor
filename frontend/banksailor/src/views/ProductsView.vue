<template>
  <main>
    <header>
      <h1>예적금 금리 비교</h1>
      <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>  |
      <RouterLink :to="{ name: 'saving' }">적금</RouterLink>
      <hr>
    </header>
    <div class="body">
      <aside>
        사이드바 들어갈 곳
      </aside>
      <article>
      <RouterView />
      </article>
    </div>
   
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
  header {
    text-align: center;
  }

  main {
    width: 1200px;
    margin: 0 auto;
  }
  
  .body {
    display: flex;
  }

  aside {
    width: 200px;
  }

  article {
    width: 1000px;
  }
</style>
