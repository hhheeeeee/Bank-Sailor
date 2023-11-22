<template>
  <div class="container-main">
    <!-- <h1>The World's Best Financial Site</h1> -->
    <div class="boxes">
      <div class="carousel1">
        <NewHomeCarousel />
      </div>
      <div class="sidebox">
        <div class="box1">
          <img src="/src/assets/currency-icon.png" alt="" class="icon ms-4" />
          <div class="exchange me-4">
            <img src="/src/assets/arrow.png" alt="" width="60">
            <h3>환율 정보</h3>
          </div>
        </div>
        <div class="box2">
          <img src="/src/assets/map-icon.png" alt="" class="icon ms-4" />
          <div class="map me-4">
            <img src="/src/assets/arrow.png" alt="" width="60">
            <h2>지도</h2>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import NewHomeCarousel from "./NewHomeCarousel.vue";
</script>

<style scoped>
/* h1 {
  margin-bottom: 50px;
  color: rgb(28, 54, 89);
} */

.boxes {
  /* background-color: pink; */
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  column-gap: 20px;
  width: 100%;
  height: 100%;
}

.carousel1 {
  background-color: lavender;
  flex: 2;
  height: 100%;
  overflow: hidden;
  box-shadow: 3px 3px 5px 1px lightgray;
}

.sidebox {
  display: flex;
  flex-direction: column;
  width: 30%;
  height: 100%;
  row-gap: 20px;
}
.box1,
.box2 {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 5px 5px 5px 1px lightgray;
}

.box1 {
  background-color: rgb(7, 152, 242);
}

.box2 {
  flex: 1;
  background-color: rgb(242, 200, 121);
}
.boxes div {
  border-radius: 20px;
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





.container-main {
  width: 100%;
  height: 600px;
  padding: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
}

.exchange {
  display: flex;
  flex-direction: column;
  align-items: end;
  row-gap: 10px;
}

.map {
  display: flex;
  flex-direction: column;
  align-items: end;
  row-gap: 10px;
}

</style>
