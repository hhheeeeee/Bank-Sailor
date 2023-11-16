<template>
  <div class="containerbody">
    <div class="upperbox">
      <div class="uppertextarea">
        <h2>금리 비교 알아보실?</h2>
        <button>go!</button>
      </div>
      <div>여기 사진 넣기~</div>
    </div>
    <div class="lowerbox">
      <div class="lowertextarea">
        <h2>환전 알아보실?</h2>
        <button>go!</button>
      </div>
      <div>여기 사진 넣기</div>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.containerbody {
  width: 100%;
  height: 100vh;
  background-color: #f9dcb4;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  /* align-items: center; */
}

.upperbox {
  background-color: #42a8b4;
  width: 90%;
  height: 37%;
  border-radius: 40px 0px 0px 40px;
  align-self: last baseline;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.lowerbox {
  background-color: #4db7e5;
  width: 90%;
  height: 37%;
  border-radius: 0px 40px 40px 0px;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

button {
  border: 0;
  outline: 0;
  width: 80px;
  height: 35px;
  border-radius: 30px;
  background-color: #1c5f82;
}
</style>
