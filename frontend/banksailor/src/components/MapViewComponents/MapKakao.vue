<!-- MapKakao -->
<template>
  <div id="map"></div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const { latitude, longitude } = defineProps({
  latitude: {
    type: Number,
    required: true,
  },
  longitude: {
    type: Number,
    required: true,
  },
});

const map = ref(null);

const loadScript = () => {
  const script = document.createElement("script");
  // 해당 앱키의 값은 추후 변경해야할것(현재 테스트용으로 개인키 입력)
  script.src =
    "//dapi.kakao.com/v2/maps/sdk.js?appkey=20803f06415d76c0c3c3351c83047dee&autoload=false";
  script.onload = () => window.kakao.maps.load(loadMap);

  document.head.appendChild(script);
};

const loadMap = () => {
  const container = document.getElementById("map");
  const options = {
    //좌표값 설정
    center: new window.kakao.maps.LatLng(latitude, longitude),
    level: 4,
  };
  map.value = new window.kakao.maps.Map(container, options);

  loadMaker();
};

const loadMaker = () => {
  const markerPosition = new window.kakao.maps.LatLng(latitude, longitude);
  const marker = new window.kakao.maps.Marker({
    position: markerPosition,
  });
  try {
    marker.setMap(map.value);
  } catch (err) {
    throw new Error(`마커 실패${err}`);
  }
};

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    loadMap();
  } else {
    loadScript();
  }
});
</script>

<style>
#map {
  width: 500px;
  height: 500px;
}
</style>
