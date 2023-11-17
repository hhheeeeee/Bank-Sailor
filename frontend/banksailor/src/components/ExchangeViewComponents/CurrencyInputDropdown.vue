<template>
  <div>
    <div class="btn-group" @click="ToKorea">
      <button
        class="btn dropdown-toggle dropdownbutton"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        {{ selected || "" }}
      </button>
      <ul class="dropdown-menu" v-show="isshow">
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
        <li>
          <a class="dropdown-item" @click="selectItem('IDR(100)')">IDR</a>
        </li>
        <li>
          <a class="dropdown-item" @click="selectItem('ITL(100)')">ITL</a>
        </li>
        <li>
          <a class="dropdown-item" @click="selectItem('JPY(100)')">JPY</a>
        </li>
        <!-- 만약에 처음에 원화를 선택했으면 다른거 다 선택 가능해야됨 -->
        <li v-show="korea">
          <a class="dropdown-item" @click="selectItem('KRW')">KRW</a>
        </li>
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
import { processSlotOutlet } from "@vue/compiler-core";
import { ref, computed } from "vue";
const isshow = ref("true");
const korea = ref("true");
const props = defineProps({ firstinput: String, order: String });

const emit = defineEmits(["selectCountry"]);

const selected = ref("");

const allowAll = computed(() => {
  return props.firstinput === "KRW" || props.firstinput.length === 0;
});

const selectItem = (item) => {
  selected.value = item;
  emit("selectCountry", selected.value);
};

const ToKorea = () => {
  if (props.order == "second") {
    if (props.firstinput === "KRW") {
      korea.value = false;
    } else if (props.firstinput.length > 0) {
      selected.value = "KRW";
      emit("selectCountry", selected.value);
      isshow.value = false;
    }
  }
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

.dropdownbutton {
  font-size: 100%;
}
</style>
