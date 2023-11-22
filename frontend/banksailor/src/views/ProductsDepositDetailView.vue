<template>
  <div class="main">
    <a href="#" @click="goDeposit">정기예금</a> |
    <a href="#" @click="goSaving">적금</a>
    <h1>예금상품 상세정보</h1>
    <hr />
  </div>
  <div v-if="product" class="info-list">
    <div class="info">
      <div class="info-title">공시 제출월:</div>
      <div class="info-content">{{ product.dcls_month }}</div>
    </div>
    <div class="info">
      <div class="info-title">상품명:</div>
      <div class="info-content">{{ product.kor_co_nm }}</div>
    </div>
    <div class="info">
      <div class="info-title">금융회사명:</div>
      <div class="info-content">{{ product.fin_prdt_nm }}</div>
    </div>
    <div class="info">
      <div class="info-title">가입제한:</div>
      <div class="info-content">{{ product.join_deny }}</div>
    </div>
    <div class="info">
      <div class="info-title">가입대상:</div>
      <div class="info-content">{{ product.join_member }}</div>
    </div>
    <div class="info">
      <div class="info-title">가입방법:</div>
      <div class="info-content">{{ product.join_way }}</div>
    </div>
    <div class="info">
      <div class="info-title">최고한도:</div>
      <div class="info-content">{{ product.max_limit }}</div>
    </div>
    <div class="info">
      <div class="info-title">우대 조건:</div>
      <div class="info-content">{{ product.spcl_cnd }}</div>
    </div>
    <div class="info">
      <div class="info-title">기타 유의사항:</div>
      <div class="info-content">{{ product.etc_note }}</div>
    </div>
    <div class="info">
      <div class="info-title">금리</div>
      <div class="info-content">
        <p v-if="rateInfo.rate_6">
          6개월: {{ rateInfo.rate_6 ? `${rateInfo.rate_6}%` : "없음" }} (최고:
          {{ rateInfo.rate_6_max ? `${rateInfo.rate_6_max}%` : "없음" }})
          <p v-if="calculatedRate6">예상이자: {{ calculatedRate6 }} 원</p>
          <button
            v-if="store.userInfo.is_superuser"
            class="btn btn-warning p-0"
            @click="goUpdate6"
          >
            수정
          </button>
        </p>
        <p v-if="rateInfo.rate_12">
          12개월:
          {{ rateInfo.rate_12 ? `${rateInfo.rate_12}%` : "없음" }} (최고:
          {{ rateInfo.rate_12_max ? `${rateInfo.rate_12_max}%` : "없음" }})
          <p v-if="calculatedRate12">예상이자: {{ calculatedRate12 }} 원</p>
          <button
            v-if="store.userInfo.is_superuser"
            class="btn btn-warning p-0"
            @click="goUpdate12"
          >
            수정
          </button>
        </p>
        <p v-if="rateInfo.rate_24">
          24개월:
          {{ rateInfo.rate_24 ? `${rateInfo.rate_24}%` : "없음" }} (최고:
          {{ rateInfo.rate_24_max ? `${rateInfo.rate_24_max}%` : "없음" }})
          <p v-if="calculatedRate24">예상이자: {{ calculatedRate24 }} 원</p>
          <button
            v-if="store.userInfo.is_superuser"
            class="btn btn-warning p-0"
            @click="goUpdate24"
          >
            수정
          </button>
        </p>
        <p v-if="rateInfo.rate_36">
          36개월:
          {{ rateInfo.rate_36 ? `${rateInfo.rate_36}%` : "없음" }} (최고:
          {{ rateInfo.rate_36_max ? `${rateInfo.rate_36_max}%` : "없음" }})
          <p v-if="calculatedRate36">예상이자: {{ calculatedRate36 }} 원</p>
          <button
            v-if="store.userInfo.is_superuser"
            class="btn btn-warning p-0"
            @click="goUpdate36"
          >
            수정
          </button>
        </p>
      </div>
    </div>
    <hr>
    <div class="info">
      <div class="info-title">이자 계산기:</div>
      <form @submit.prevent="calculate">
        <input type="number" v-model="inputMoney" min="1000000">
        <input type="submit">
      </form>
    </div>
    <hr />
    <button class="btn btn-primary signup" @click="signup">상품가입</button>
  </div>
</template>

<script setup>
import { ref, watch, watchEffect } from "vue";
import { useRouter, useRoute } from "vue-router";
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import Swal from "sweetalert2";

const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener("mouseenter", Swal.stopTimer);
    toast.addEventListener("mouseleave", Swal.resumeTimer);
  },
});

const router = useRouter();
const route = useRoute();

// axios 를 통해 불러온 단일 상품 데이터가 담길 변수
const product = ref(null);

// 정기예금으로 이동
const goDeposit = () => {
  router.push({ name: "deposit" });
};
5;

// 적금으로 이동
const goSaving = () => {
  router.push({ name: "saving" });
};

// store
const store = useCounterStore();

// 금리정보가 담긴 객체
const rateInfo = ref();

// 금리수정으로 이동
const goUpdate6 = () => {
  router.push({
    name: "depositrateupdate",
    params: { id: product.value.fin_prdt_cd, rate: 6 },
    query: { rateValue: rateInfo.value.rate_6 },
  });
};
const goUpdate12 = () => {
  router.push({
    name: "depositrateupdate",
    params: { id: product.value.fin_prdt_cd, rate: 12 },
    query: { rateValue: rateInfo.value.rate_12 },
  });
};
const goUpdate24 = () => {
  router.push({
    name: "depositrateupdate",
    params: { id: product.value.fin_prdt_cd, rate: 24 },
    query: { rateValue: rateInfo.value.rate_24 },
  });
};
const goUpdate36 = () => {
  router.push({
    name: "depositrateupdate",
    params: { id: product.value.fin_prdt_cd, rate: 36 },
    query: { rateValue: rateInfo.value.rate_36 },
  });
};

//
const getRate = () => {
  for (const deposit of store.deposits) {
    if (product.value) {
      if (deposit.fin_prdt_cd === product.value.fin_prdt_cd) {
        rateInfo.value = deposit;
      }
    }
  }
};

// 해당 상품 상세정보 가져오기
onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/products/deposit/${route.params.id}/`,
  })
    .then((response) => {
      product.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
  getRate();
});

// 이자정보 가져오기
watchEffect(() => {
  getRate();
});

// watch(rateInfo, (tmp1, tmp2) => {
//   getRate()
// })

// 상품가입 버튼 누르면 동작
const signup = async () => {
  try {
    await axios({
      method: "post",
      url: `${store.API_URL}/products/deposit/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    });

    await store.getUserInfo(); // 상품 가입 후에 getUserInfo 호출

    Toast.fire({
      icon: "success",
      title: "상품에 가입되었습니다.",
    });
  } catch (error) {
    // Handle the error without logging to the console
    // You can add more specific error handling logic here if needed
    if (error.response && error.response.status === 409) {
      Toast.fire({
        icon: "error",
        title: "이미 가입된 상품입니다.",
      });
    } else {
      // Handle other types of errors or log them if necessary
      // console.error("An error occurred:", error);
    }
  }
};

// 이자 계산기 관련

const inputMoney = ref()
const calculatedRate6 = ref(null)
const calculatedRate12 = ref(null)
const calculatedRate24 = ref(null)
const calculatedRate36 = ref(null)

const calculate = () => {
  calculatedRate6.value = rateInfo.value.rate_6 ? Math.round(inputMoney.value * rateInfo.value.rate_6 / 200) : null
  calculatedRate12.value = rateInfo.value.rate_12 ? Math.round(inputMoney.value * rateInfo.value.rate_12 / 100) : null
  calculatedRate24.value = rateInfo.value.rate_24 ? Math.round(inputMoney.value * rateInfo.value.rate_24 / 100 * 2) : null
  calculatedRate36.value = rateInfo.value.rate_36 ? Math.round(inputMoney.value * rateInfo.value.rate_36 / 100 * 3) : null
}


</script>

<style scoped>
.main {
  width: 80%;
  margin: 0 auto;
}

.datail-info {
  width: 80%;
  margin: 0 auto;
}

.info-list {
  width: 80%;
  margin: 0 auto;
}

.info {
  display: flex;
  margin: 30px 0;
}

.info-title {
  width: 20%;
}
.info-content {
  width: 80%;
}

.signup {
  width: 150px;
  height: 50px;
}
</style>
