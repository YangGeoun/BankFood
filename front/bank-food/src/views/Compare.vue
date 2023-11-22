<template>
  <div :style="maxWidth" class="mt-3 px-5 py-3 mx-auto" style="background-color: white; border-radius: 10px;">
    <h2 class="fw-bold">예적금상품금리비교</h2>
    <div class="row text-center">
      <hr style="margin-bottom: 0;">
      <div class="col-6" @click="toggleDeposit" :class="{'bg':isDeposit}" style="padding-top: 15px;">
        <h4 class=" fw-bold mb-3">예금금리</h4>
      </div>
      <div class="col-6" @click="toggleDeposit" :class="{'bg':!isDeposit}" style="padding-top: 15px;">
        <h4 class=" fw-bold">적금금리</h4>
      </div>
      
      <hr>
      <div class="col-12 text-start mb-1" @click="allCheck">
        <input type="checkbox" id="all" value="true" :checked="is_all" >
        <label for="all">전체</label>
      </div>
      <div class="col-2 text-start mb-1" v-for="bank in banks">
        <input type="checkbox" :id="bank" :value="bank" v-model="checked" >
        <label :for="bank">{{bank}}</label>
      </div>
      <hr class="mt-1">
      <ul class="d-flex justify-content-around">
        <li class="ms-3">
          <form>
            이자 계산방식
            <label><input type="radio" name="term" value="0" class="ms-2" checked v-model="type"> 전체 </label>
            <label><input type="radio" name="term" value="1" class="ms-2" v-model="type"> 단리 </label>
            <label><input type="radio" name="term" value="2" class="ms-2" v-model="type"> 복리 </label>
          </form>
        </li>
        <li class="">
          <form>
            저축 기간
            <label><input type="radio" name="term" value="0" checked class="ms-2" v-model="term"> 전체 </label>
            <label><input type="radio" name="term" value="6" class="ms-2" v-model="term"> 6 개월 </label>
            <label><input type="radio" name="term" value="12" class="ms-2" v-model="term"> 12 개월</label>
            <label><input type="radio" name="term" value="24" class="ms-2" v-model="term"> 24 개월</label>
            <label><input type="radio" name="term" value="36" class="ms-2" v-model="term"> 36 개월</label>
          </form>
        </li>
      </ul>
      <hr>
    </div>
    <div class="d-flex justify-content-center">
      <button class="btn btn-info fw-bold" style="width: 100px; color: white;" @click="search"> 검 색 </button>
    </div>
  

    
  </div>
  <div :style="maxWidth" class="px-5 py-3 mx-auto" style="background-color: white; margin-top: 20px; border-radius: 10px;">
  <table class="table table-hover">
    <thead>
      <tr>
        <th>공시 제출월</th>
        <th>금융회사명</th>
        <th>금융상품명</th>
        <th>6개월</th>
        <th>12개월</th>
        <th>24개월</th>
        <th>26개월</th>
      </tr>  
    </thead>
    <tbody>
      <DepositItem 
      v-for="(deposit, index) in deposits"
      :key="deposit"
      :deposit=deposit
      :index=index
      />
    </tbody>
  </table>
  </div>
</template>

<script setup>

import axios from 'axios';
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '../stores/counter';
import DepositItem from '../components/DepositItem.vue';

const store = useCounterStore()

const banks = [
  "경남은행", "광주은행", "국민은행", "농협은행주식회사", "대구은행", "부산은행", "수협은행",
  "신한은행", "우리은행", "전북은행", "제주은행", "주식회사카카오뱅크", "주식회사케이뱅크", 
  "중소기업은행", "토스뱅크주식회사", "하나은행", "한국산업은행", "한국스탠다드차타드은행" 
]

const checked = ref([])
const type = ref(0)
const term = ref(0)
const deposits = ref([])



let is_all = computed(() => {
  return (checked.value.length==banks.length)
})

const isDeposit = ref(true)

const toggleDeposit = function () {
  if (isDeposit.value) {
    isDeposit.value = false
  } else {
    isDeposit.value = true
  }
}

const allCheck = function () {
  if (is_all === true) {
    checked.value = []
    is_all = false
  }
  else {
    checked.value = banks
    is_all = true
  }
}

const maxWidth = ref({
  width : `${(screen.availWidth/12)*10}px`
})
onMounted(()=>{
  axios({
    method:'get',
    url: `${store.ServerURL}finances/deposit/`,
  })
  .then((res) => {
    console.log(res)
    deposits.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
})

const search = function () {
  if (isDeposit) {
    axios({
      method:'get',
      url: `${store.ServerURL}finances/searchdeposit/${banks.map((el)=> checked.value.includes(el)? '1' : '0').join('')}/${type.value}/${term.value}/`,
    })
    .then((res) => {
      console.log(res)
      deposits.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  } 
  else{
    axios({
      method:'get',
      url: `${store.ServerURL}finances/searchsaving/${banks.map((el)=> checked.value.includes(el)? '1' : '0').join('')}/${type.value}/${term.value}/`,
    })
    .then((res) => {
      console.log(res)
      deposits.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
}
</script>

<style scoped>
  .bg {
    background-color: #80EAFF;
    color: white;
  }
</style>