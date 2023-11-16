<template>
  <div>
    <div class="btn-group">
      <button
        class="btn dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        {{ selected || "" }}
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" @click="selectItem('AED')">AED</a></li>
        <li><a class="dropdown-item" @click="selectItem('ATS')">ATS</a></li>
        <li><a class="dropdown-item" @click="selectItem('AUD')">AUD</a></li>
        <li><a class="dropdown-item" @click="selectItem('BEF')">BEF</a></li>
        <li><a class="dropdown-item" @click="selectItem('BHD')">BHD</a></li>
        <li><a class="dropdown-item" @click="selectItem('CAD')">CAD</a></li>
        <li><a class="dropdown-item" @click="selectItem('CHF')">CHF</a></li>
        <li><a class="dropdown-item" @click="selectItem('CNH')">CNH</a></li>
        <li><a class="dropdown-item" @click="selectItem('DEM')">DEM</a></li>
        <li><a class="dropdown-item" @click="selectItem('DKK')">DKK</a></li>
        <li><a class="dropdown-item" @click="selectItem('ESP')">ESP</a></li>
        <li><a class="dropdown-item" @click="selectItem('EUR')">EUR</a></li>
        <li><a class="dropdown-item" @click="selectItem('FIM')">FIM</a></li>
        <li><a class="dropdown-item" @click="selectItem('FRF')">FRF</a></li>
        <li><a class="dropdown-item" @click="selectItem('GBP')">GBP</a></li>
        <li><a class="dropdown-item" @click="selectItem('HKD')">HKD</a></li>
        <li><a class="dropdown-item" @click="selectItem('IDR')">IDR</a></li>
        <li><a class="dropdown-item" @click="selectItem('ITL')">ITL</a></li>
        <li><a class="dropdown-item" @click="selectItem('JPY')">JPY</a></li>
        <li><a class="dropdown-item" @click="selectItem('KRW')">KRW</a></li>
        <li><a class="dropdown-item" @click="selectItem('KWD')">KWD</a></li>
        <li><a class="dropdown-item" @click="selectItem('MYR')">MYR</a></li>
        <li><a class="dropdown-item" @click="selectItem('NLG')">NLG</a></li>
        <li><a class="dropdown-item" @click="selectItem('NZD')">NZD</a></li>
        <li><a class="dropdown-item" @click="selectItem('SAR')">SAR</a></li>
        <li><a class="dropdown-item" @click="selectItem('SEK')">SEK</a></li>
        <li><a class="dropdown-item" @click="selectItem('SGD')">SGD</a></li>
        <li><a class="dropdown-item" @click="selectItem('THB')">THB</a></li>
        <li><a class="dropdown-item" @click="selectItem('USD')">USD</a></li>
        <li><a class="dropdown-item" @click="selectItem('XOF')">XOF</a></li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const selected = ref("");

const selectItem = (item) => {
  selected.value = item;
};
</script>

<style scoped>
.btn-group {
  position: relative;
}

.dropdown-menu {
  max-height: 200px; /* 원하는 높이로 설정 */
  overflow-y: auto;
}
</style>
