import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }
  // 
  const deposits = ref([])
  const savings = ref([])
  
  const API_URL = 'http://127.0.0.1:8000'

  const getDeposits = () => {
    axios({
      method: 'get',
      url: `${API_URL}/products/deposit/`
    })
      .then((response) => {
        deposits.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }


  const getSavings = () => {
    axios({
      method: 'get',
      url: `${API_URL}/products/saving/`
    })
      .then((response) => {
        savings.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { count, doubleCount, increment, deposits, getDeposits, savings, getSavings }
})
