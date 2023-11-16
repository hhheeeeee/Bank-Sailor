<template>
  <div class="inputarea">
    <form>
      <div class="form-group">
        <label for="exampleInputEmail1">광역시 / 도</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          placeholder="광역시 / 도"
        />

        <label for="exampleInputEmail1">시 / 군 / 구</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          placeholder="시 / 군 / 구"
        />

        <label for="exampleInputEmail1">은행명</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          placeholder="은행명"
        />
      </div>

      <button type="submit" class="btn btn-primary" @submit.prevent="searchMap">
        검색
      </button>
    </form>
    <!-- <form>
            <p class="label">광역시 / 도</p>
            <input type="text" />
            <p class="label">시 / 군 / 구</p>
            <input type="text" />
            <p class="label">은행명</p>
            <input type="text" />
            <input type="submit" value="검색" />
          </form> -->
  </div>
</template>

<script setup>
import { ref } from "vue";

const province = ref(null);
const city = ref(null);
const bankName = ref(null);
</script>

<style scoped>
.inputarea {
  width: 35%;
  background-color: pink;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  padding: 30px 0px;
}

.label {
  color: #1c5f82;
  font-weight: 700;
  font-size: 1.5rem;
}

input {
  margin-bottom: 10px;
}
</style>
