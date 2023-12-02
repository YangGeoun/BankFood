<template>
  <div class="animate__animated animate__fadeIn">
    
    <div class="d-flex justify-content-center " style="margin-top: 10px;
    
    ">
      <img src="@/assets/MYBANK.png" alt="" style="height: 200px; width: 200px;">
      <!-- <a href="https://www.flaticon.com/free-icons/internet-banking" title="internet banking icons">Internet banking icons created by Ida Desi Mariana - Flaticon</a> -->
    </div>
    <hr>
    <div class="d-flex flex-row justify-content-between" style="width: 100%;">
    <h4 style="margin-left: 30px; margin-top: 20px;
    font-weight: 550; color: darkslategray;
    ">My Bank</h4>
  </div>
<!-- <a href="https://www.flaticon.com/free-icons/plus" title="plus icons">Plus icons created by Freepik - Flaticon</a> -->
    <div class="d-flex justify-content-center" style="margin-top: 20px;;">
      <table class="type09 " style="border: 1px solid skyblue; 
      box-shadow: 0 0 5px darkblue;" v-if="store.userBank.length>0"
      >
        <thead>
          <tr>
            <th scope="cols">은행</th>
            <th scope="cols">상품명</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in articleList">
            <th scope="row">{{item.kor_co_nm}}</th>
            <td style="font-weight: bold;">{{item.fin_prdt_nm}}</td>
          </tr>
        </tbody>
    </table>
  </div>
    <div class="d-flex justify-content-center" style="margin: 10px">
      <img src="@/assets/PREV.png" alt="" style="width: 30px; cursor: pointer;"
      @click="()=>{prevPage()
      
      }"
      >
      <span style="border-radius: 50%; border: 2px solid; width: 30px; text-align: center; font-weight: bold;
      margin-left: 8px; margin-right: 8px;
      ">{{ nowPage }}</span>
      <img src="@/assets/NEXT.png" alt="" style="width: 30px; cursor: pointer;" 
      @click="()=>{nextPage()
      

      }"

      >
    </div>
    <hr>
    <div>
      <Chart 
      :data1="chartdata1"
      :data2="chartdata2"
      :name="chartname"
      v-if="isShow"
      />
    </div>
  </div>
  
</template>

<script setup>
import axios from 'axios';
import Chart from './Chart.vue';
import { ref, computed, onMounted } from 'vue';
import {useCounterStore} from '@/stores/counter';

const store = useCounterStore()
const flipAnimate = ref({
  "animate__bounce" : true,
  "animate__animated" : true,
})
const articlesPerPage = 7;
const article = ref([])
const nowPage = ref(1)
const chartname = ref([])
const chartdata1 = ref([])
const chartdata2 = ref([])
const isShow = ref(false)
let sum1 = 0
let sum2 = 0

setTimeout(() => {
  isShow.value = true
}, 50);


const endPage = computed(()=>{
  return Math.ceil(article.value.length/articlesPerPage)
})
const timeFunc = function(){
  flipAnimate.value.animate__bounce = false
  flipAnimate.value.animate__animated = false

  setTimeout(()=>{
      flipAnimate.value.animate__bounce = true
      flipAnimate.value.animate__animated = true
      },10)
}
const nextPage = function(){
  if(nowPage.value<endPage.value){
    nowPage.value+=1
  }
}
const prevPage = function(){
  if (nowPage.value>1){
    nowPage.value-=1
  }
}
const startPoint = computed(()=>{
  return (nowPage.value-1)*articlesPerPage
})
const endPoint = computed(()=>{
  const temp = (nowPage.value*7)
  if(temp>=article.value.length){
    return article.value.length
  }
  else{
    return temp
  }
})
const articleList = computed(()=>{
  return article.value.slice(startPoint.value,endPoint.value)
})

onMounted(()=>{
  axios({
    url: 'http://127.0.0.1:8000/accounts/userproducts/',
    method : 'get',
    headers : {
      Authorization : `Token ${store.token}`
    }
  })
  .then(res =>{
    console.log(res)
    store.userBank = res.data
    article.value = store.userBank
    for (const product of res.data)
      if ('depositoption_set' in product) {
        chartname.value.push(product.fin_prdt_nm)
        sum1 = 0
        sum2 = 0
        for (const opt of product.depositoption_set) {
          sum1 += opt.intr_rate2
          sum2 += opt.intr_rate
        }
        chartdata1.value.push(sum1/product.depositoption_set.length)
        chartdata2.value.push(sum2/product.depositoption_set.length)
      } else {
        chartname.value.push(product.fin_prdt_nm)
        sum1 = 0
        sum2 = 0
        for (const opt of product.savingoption_set) {
          sum1 += opt.intr_rate2
          sum2 += opt.intr_rate
        }
        chartdata1.value.push(sum1/product.savingoption_set.length)
        chartdata2.value.push(sum2/product.savingoption_set.length)
      }
      chartname.value.push('평균')
      sum1 = 0
      chartdata1.value.forEach((el)=>{
        sum1 += el
      })
      chartdata1.value.push(sum1/chartdata1.value.length)
      sum1 = 0
      chartdata2.value.forEach((el)=>{
        sum1 += el
      })
      chartdata2.value.push(sum1/chartdata2.value.length)
  })
  .catch(err =>{
    console.log(err)
  })

})

</script>

<style scoped>
table.type09 {
  border-collapse: collapse;
  text-align: left;
  line-height: 1.15;

}
table.type09 thead th {
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  color: #369;
  border-bottom: 3px solid #036;
}
table.type09 tbody th {
  width: 150px;
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
  background: #f3f6f7;
}
table.type09 td {
  width: 350px;
  padding: 10px;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
}

</style>