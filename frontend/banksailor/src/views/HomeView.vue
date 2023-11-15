<template>
  <div class="containerbody">
    <HomeViewUpperpage />
    <HomeViewlowerpage />
  </div>
</template>

<script setup>
import HomeViewUpperpage from "@/components/HomeViewUpperpage.vue";
import HomeViewlowerpage from "@/components/HomeViewlowerpage.vue";
</script>

<style lang="scss" scoped>
.containerbody {
  width: 100%;
}
</style>
