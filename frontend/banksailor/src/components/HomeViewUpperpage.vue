<template>
  <div class="containerbody">
    <h1 class="title">메인페이지 주요멘트</h1>
  </div>
</template>

<script setup></script>

<style scoped>
.containerbody {
  width: 100%;
  height: 100vh;
  background-image: url("@/assets/backgroundimg.png");
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  font-size: 6rem;
  color: #1c5f82;
  /* font-size: 10rem; */
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
  margin-bottom: 35px;
  text-shadow: -2px 0px white, 0px 2px white, 2px 0px white, 0px -2px white;
}
</style>
