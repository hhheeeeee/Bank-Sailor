<template>
  <div class="containerbody">
    <img
      v-for="i in images"
      :key="i"
      class="coin"
      :style="{ top: i.top + 'px', left: i.left + 'px' }"
      src="@/assets/flags/coin.png"
    />
    <h1 class="title">메인페이지 주요멘트</h1>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const images = ref([]);

onMounted(() => {
  for (let i = 0; i < 20; i++) {
    images.value.push({
      top: Math.random() * window.innerHeight,
      left: Math.random() * window.innerWidth,
    });
  }
});
</script>

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
  position: relative;
}

.coin {
  position: absolute;
  width: 50px;
  height: 50px;
  animation: bounce 1s infinite;
}

@keyframes bounce {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

.title {
  font-size: 6rem;
  color: #1c5f82;
  -webkit-text-stroke-width: 2px;
  -webkit-text-stroke-color: white;
  font-weight: 900;
  margin-bottom: 35px;
  text-shadow: -2px 0px white, 0px 2px white, 2px 0px white, 0px -2px white;
  z-index: 1;
}
</style>
