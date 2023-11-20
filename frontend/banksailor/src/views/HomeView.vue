<template>
  <div class="containerbody">
    <NewHome />
  </div>
</template>

<script setup>
import { gsap } from "gsap";
import NewHome from "@/components/HomeViewComponents/NewHome.vue";
</script>

<style lang="scss" scoped>
.containerbody {
  width: 100%;
  height: 91vh;
}
</style>
