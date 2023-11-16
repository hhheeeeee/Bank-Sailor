<template>
  <div class="containerbody1">
    <h1 class="maptitle">내 근처 은행 찾기</h1>
    <div class="mapcontents">
      <Mapinput />
    </div>
  </div>
</template>

<script setup>
import Mapinput from "@/components/MapViewComponents/Mapinput.vue";
</script>

<style scoped>
.containerbody1 {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(
      rgba(255, 255, 255, 0.4),
      rgba(255, 255, 255, 0.4)
    ),
    url("@/assets/backgroundimg.png");

  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.maptitle {
  font-weight: 900;
  font-size: 3.5rem;
  text-shadow: 2px 2px 2px grey;
  text-align: center;
  margin-bottom: 30px;
}

.mapcontents {
  display: flex;
  width: 80%;
  height: 60vh;
  border: 3px solid #1c5f82;
  background-color: #f6ddb4;
  justify-content: space-evenly;
  align-items: center;
  padding: 20px 20px;
  border-radius: 30px;
}
</style>
