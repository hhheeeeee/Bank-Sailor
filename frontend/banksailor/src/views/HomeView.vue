<template>
  <div class="containerbody">
    <HomeViewUpperpage />
    <HomeViewlowerpage />
  </div>
</template>

<script setup>
import HomeViewUpperpage from "@/components/HomeViewComponents/HomeViewUpperpage.vue";
import HomeViewlowerpage from "@/components/HomeViewComponents/HomeViewlowerpage.vue";
import { ref, onMounted, onUnmounted } from "vue";
let lastScrollY = 0;

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});

function handleScroll() {
  const currentScrollY = window.pageYOffset;

  if (currentScrollY > lastScrollY && currentScrollY > 50) {
    // 스크롤이 아래로 움직였고 100px 이상 움직였을 때
    window.scrollTo({ top: document.body.scrollHeight, behavior: "auto" }); // 페이지 맨 밑으로 이동
  } else if (currentScrollY < lastScrollY && lastScrollY > 50) {
    // 스크롤이 위로 움직였고 100px 이상 움직였을 때
    window.scrollTo({ top: 0, behavior: "auto" }); // 페이지 맨 위로 이동
  }

  lastScrollY = currentScrollY;
}
</script>

<style lang="scss" scoped>
.containerbody {
  width: 100%;
}
</style>
