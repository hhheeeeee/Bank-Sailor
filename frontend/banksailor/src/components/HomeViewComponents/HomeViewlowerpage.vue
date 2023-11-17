<template>
  <div class="containerbody">
    <div class="upperbox" :ref="setUpperBoxRef">
      <div class="uppertextarea">
        <h2>금리 비교 알아보실?</h2>
        <button>go!</button>
      </div>
      <div>여기 사진 넣기~</div>
    </div>
    <div class="lowerbox" :ref="setLowerBoxRef">
      <div class="lowertextarea">
        <h2>환전 알아보실?</h2>
        <button>go!</button>
      </div>
      <div>여기 사진 넣기</div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from "vue";
import { debounce } from "lodash";

let upperBox = ref(null);
let lowerBox = ref(null);

const setUpperBoxRef = (el) => {
  upperBox.value = el;
};
const setLowerBoxRef = (el) => {
  lowerBox.value = el;
};

onMounted(() => {
  window.addEventListener("scroll", checkScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", checkScroll);
});

const checkScroll = debounce(() => {
  const windowHeightHalf = window.innerHeight / 2;

  const upperBoxTop = upperBox.value.getBoundingClientRect().y;
  const lowerBoxTop = lowerBox.value.getBoundingClientRect().y;

  if (upperBoxTop <= windowHeightHalf) {
    upperBox.value.style.animationName = "slideFromRight";
  }

  if (lowerBoxTop <= windowHeightHalf) {
    lowerBox.value.style.animationName = "slideFromLeft";
  }
}, 300);
</script>

<style scoped>
@keyframes slideFromRight {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}

@keyframes slideFromLeft {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}

.containerbody {
  width: 100%;
  height: 100vh;
  background-color: #f9dcb4;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
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
  animation: none 1s ease-out;
}

.lowerbox {
  background-color: #4db7e5;
  width: 90%;
  height: 37%;
  border-radius: 0px 40px 40px 0px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  animation: none 1s ease-out;
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
