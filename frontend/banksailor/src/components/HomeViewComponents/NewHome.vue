<template>
  <div class="container1">
    <h1>The World's Best Financial Site</h1>
    <div class="boxes">
      <div class="carousel1">
        <NewHomeCarousel />
      </div>
      <div class="sidebox">
        <div class="box1">
          <img src="/src/assets/currency-icon.png" alt="" class="icon" />
          여기는 아마 환율계산기?
        </div>
        <div class="box2">
          <img src="/src/assets/map-icon.png" alt="" class="icon" />
          여기는 아마 지도..?
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import NewHomeCarousel from "./NewHomeCarousel.vue";
</script>

<style scoped>
h1 {
  margin-bottom: 50px;
  color: rgb(28, 54, 89);
}
.container1 {
  width: 100%;
  height: 91vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.boxes {
  /* background-color: pink; */
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  column-gap: 15px;
  width: 80%;
  height: 60%;
}

.carousel1 {
  background-color: lavender;
  flex: 2;
  height: 100%;
  overflow: hidden;
}

.sidebox {
  display: flex;
  flex-direction: column;
  flex: 1;
  height: 100%;
  row-gap: 15px;
}
.box1,
.box2 {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.box1 {
  background-color: rgb(7, 152, 242);
}

.box2 {
  flex: 1;
  background-color: rgb(242, 200, 121);
}
.boxes div {
  border-radius: 10px;
  transition: 0.3s all;
}

.box1:hover {
  background-color: rgb(0, 132, 222);
  transform: scale(1.02);
  color: white;
  cursor: pointer;
}

.box2:hover {
  color: white;
  transform: scale(1.02);
  background-color: rgb(222, 180, 101);
  cursor: pointer;
}

.icon {
  width: 45%;
  /* height: 50%; */
  transition: 0.3s all;
}
</style>
