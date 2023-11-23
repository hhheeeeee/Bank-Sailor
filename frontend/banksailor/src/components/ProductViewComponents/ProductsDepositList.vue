<template>
  <div class="index-bar">
    <div class="box1">공시 제출월</div>
    <div class="box2">금융회사명</div>
    <div class="box3">상품명</div>
    <div class="box4">
      <div class="rate">6개월</div>
      <div class="sortbutton">
        <div class="sortup" @click="selectSortValue(6, false, $event)">up</div>
        <div class="sortdown" @click="selectSortValue(6, true, $event)">
          down
        </div>
      </div>
    </div>
    <div class="box5">
      <div class="rate">12개월</div>
      <div class="sortbutton">
        <div class="sortup" @click="selectSortValue(12, false, $event)">up</div>
        <div class="sortdown" @click="selectSortValue(12, true, $event)">
          down
        </div>
      </div>
    </div>
    <div class="box6">
      <div class="rate">24개월</div>
      <div class="sortbutton">
        <div class="sortup" @click="selectSortValue(24, false, $event)">up</div>
        <div class="sortdown" @click="selectSortValue(24, true, $event)">
          down
        </div>
      </div>
    </div>
    <div class="box7">
      <div class="rate">36개월</div>
      <div class="sortbutton">
        <div class="sortup" @click="selectSortValue(36, false, $event)">up</div>
        <div class="sortdown" @click="selectSortValue(36, true, $event)">
          down
        </div>
      </div>
    </div>
  </div>
  <div class="itemlist">
    <div v-if="isReverse">
      <ProductsDepositItem
        v-for="product in sortedReverseProducts"
        :key="product.id"
        :product="product"
      />
    </div>
    <div v-else>
      <ProductsDepositItem
        v-for="product in sortedProducts"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import upicon from "@/components/ProductViewComponents/upicon.vue";
import downicon from "@/components/ProductViewComponents/downicon.vue";
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import ProductsDepositItem from "@/components/ProductViewComponents/ProductsDepositItem.vue";

const store = useCounterStore();

onMounted(() => {
  store.getDeposits();
});

const props = defineProps({
  selectedBank: String,
});

// 정렬기준 담길 변수
const sortValue = ref(null);
const isReverse = ref(null);

// 버튼으로 부터 정렬 기준 받아오기
const selectSortValue = (param1, param2, event) => {
  sortValue.value = param1;
  isReverse.value = param2;
};

// 오름차순 정렬
const sortedProducts = computed(() => {
  // 여기에서 정렬 기준을 선택하고 정렬한 후 반환합니다.
  // sortValue 값에 따라 정렬 여부를 결정합니다.
  if (sortValue.value) {
    const sortingKey = `rate_${sortValue.value}`;
    if (props.selectedBank === "전체") {
      return store.deposits.sort((a, b) => {
        if (a[sortingKey] === null) return 1;
        if (b[sortingKey] === null) return -1;
        return a[sortingKey] - b[sortingKey];
      });
    } else {
      return props.selectedBank
        ? store.deposits
            .filter((product) => product.kor_co_nm === props.selectedBank)
            .sort((a, b) => {
              // null 값을 뒤로 보내기 위한 처리
              if (a[sortingKey] === null) return 1;
              if (b[sortingKey] === null) return -1;
              return a[sortingKey] - b[sortingKey];
            })
        : store.deposits.sort((a, b) => {
            // null 값을 뒤로 보내기 위한 처리
            if (a[sortingKey] === null) return 1;
            if (b[sortingKey] === null) return -1;
            return a[sortingKey] - b[sortingKey];
          });
    }
  } else {
    if (props.selectedBank === "전체") {
      return store.deposits;
    } else {
      return props.selectedBank
        ? store.deposits.filter(
            (product) => product.kor_co_nm === props.selectedBank
          )
        : store.deposits;
    }
  }
});

// 내림차순 정렬
const sortedReverseProducts = computed(() => {
  // 여기에서 정렬 기준을 선택하고 정렬한 후 반환합니다.
  // sortValue 값에 따라 정렬 여부를 결정합니다.
  if (sortValue.value) {
    const sortingKey = `rate_${sortValue.value}`;
    if (props.selectedBank === "전체") {
      return store.deposits.sort((a, b) => {
        if (a[sortingKey] === null) return 1;
        if (b[sortingKey] === null) return -1;
        return b[sortingKey] - a[sortingKey]; // 역순으로 수정
      }); // 역순으로 수정
    } else {
      return props.selectedBank
        ? store.deposits
            .filter((product) => product.kor_co_nm === props.selectedBank)
            .sort((a, b) => {
              // null 값을 뒤로 보내기 위한 처리
              if (a[sortingKey] === null) return 1;
              if (b[sortingKey] === null) return -1;
              return b[sortingKey] - a[sortingKey]; // 역순으로 수정
            })
        : store.deposits.sort((a, b) => {
            // null 값을 뒤로 보내기 위한 처리
            if (a[sortingKey] === null) return 1;
            if (b[sortingKey] === null) return -1;
            return b[sortingKey] - a[sortingKey]; // 역순으로 수정
          });
    }
  } else {
    if (props.selectedBank === "전체") {
      return store.deposits;
    } else {
      return props.selectedBank
        ? store.deposits.filter(
            (product) => product.kor_co_nm === props.selectedBank
          )
        : store.deposits;
    }
  }
});
</script>

<style scoped>
.index-bar {
  width: 100%;
  height: 50px;
  background-color: rgb(225, 225, 225);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box1 {
  width: 10%;
  text-align: center;
  font-size: small;
}

.box2 {
  width: 18%;
  text-align: center;
  font-size: small;
}

.box3 {
  width: 32%;
  text-align: center;
  font-size: small;
}

.box4,
.box5,
.box6,
.box7 {
  width: 10%;
  text-align: center;
  font-size: small;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.sortbutton {
  width: 40%;
  background-color: transparent;
  display: flex;
  flex-direction: column;
}

.rate {
  display: flex;
  align-items: center;
}

.itemlist {
  background-color: white;
}
</style>
