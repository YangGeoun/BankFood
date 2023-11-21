<template>
  <div :style="maxWidth" class="p-5 mx-auto" style="background-color: white;">
    <h2 class="fw-bold">예금상품금리비교</h2>
    <div class="row text-center">
      <hr>
      <h4 class="col-6 fw-bold mb-3">예금금리</h4>
      <h4 class="col-6 fw-bold">적금금리</h4>
      <hr>
      <div>{{ checked }}</div>
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
            <label><input type="radio" name="term" value="0" class="ms-2"> 전체 </label>
            <label><input type="radio" name="term" value="1" class="ms-2"> 단리 </label>
            <label><input type="radio" name="term" value="2" class="ms-2"> 복리 </label>
          </form>
        </li>
        <li class="">
          <form>
            저축 기간
            <label><input type="radio" name="term" value="0" class="ms-2"> 전체 </label>
            <label><input type="radio" name="term" value="6" class="ms-2"> 6 개월 </label>
            <label><input type="radio" name="term" value="12" class="ms-2"> 12 개월</label>
            <label><input type="radio" name="term" value="24" class="ms-2"> 24 개월</label>
            <label><input type="radio" name="term" value="36" class="ms-2"> 36 개월</label>
          </form>
        </li>
      </ul>
    </div>

  </div>
</template>

<script setup>

import { ref, computed } from 'vue'

const banks = [
  "경남은행", "광주은행", "국민은행", "농협은행주식회사", "대구은행", "부산은행", "수협은행",
  "신한은행", "우리은행", "전북은행", "제주은행", "주식회사카카오뱅크", "주식회사케이뱅크", 
  "중소기업은행", "토스뱅크주식회사", "하나은행", "한국산업은행", "한국스탠다드차타드은행" 
]
const checked = ref(["광주은행", "국민은행", "농협은행주식회사", "대구은행"])

console.log(banks.map((el)=> checked.value.includes(el)? '1' : '0').join(''))
let is_all = computed(() => {
  return (checked.value.length==banks.length)
})

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
  width : `${(screen.availWidth/12)*9}px`
})


</script>

<style scoped>

</style>