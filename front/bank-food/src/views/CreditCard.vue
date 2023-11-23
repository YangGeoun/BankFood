<template>
  <div :style="maxWidth" class="mt-3 px-5 py-3 mx-auto" style="background-color: white; border-radius: 10px;">
    <h2 class="fw-bold">카드 추천</h2>
    <div class="row text-center">
      <hr>
      <h3 class="fw-bold mb-2">혜택</h3>
      <div class="col-2 text-start mb-1" v-for="bank in benefits">
        <input type="checkbox" :id="bank" :value="bank" v-model="checked" >
        <label :for="bank" style="margin-left: 5px;">{{bank}}</label>
      </div>
      <hr style="margin-top: 25px;">
    </div>
    <div class="d-flex justify-content-center">
      <button class="btn btn-info fw-bold mx-2" style="width: 100px; color: white; margin-top: 10px;" @click="reset"> 모두 보기</button>
      <button class="btn btn-info fw-bold mx-2" style="width: 100px; color: white; margin-top: 10px;" @click="search"> 검 색 </button>
      <button class="btn btn-info fw-bold mx-2" style="width: 100px; color: white; margin-top: 10px;" @click="()=>{isSearch=true}"> 추천 받기 </button>
    </div>
    <div style="margin-top: 30px;">
      <p class="fs-5" style="text-align: center;" v-if="isSearch">{{ questions[0] }}  <span class="btn btn-primary mx-1" @click="()=>{ansers[0]=1}">그렇다</span><span class="btn btn-success mx-1" @click="()=>{ansers[0]=0}">보통이다</span><span class="btn btn-danger mx-1" @click="()=>{ansers[0]=2}">그렇지않다</span></p>
      <p class="fs-5" style="text-align: center;" v-if="ansers[0]!=3">{{ questions[1] }}  <span class="btn btn-primary mx-1" @click="()=>{ansers[1]=1}">그렇다</span><span class="btn btn-success mx-1" @click="()=>{ansers[1]=0}">보통이다</span><span class="btn btn-danger mx-1" @click="()=>{ansers[1]=2}">그렇지않다</span></p>
      <p class="fs-5" style="text-align: center;" v-if="ansers[1]!=3">{{ questions[2] }}  <span class="btn btn-primary mx-1" @click="()=>{ansers[2]=1}">그렇다</span><span class="btn btn-success mx-1" @click="()=>{ansers[2]=0}">보통이다</span><span class="btn btn-danger mx-1" @click="()=>{ansers[2]=2}">그렇지않다</span></p>
      <p class="fs-5" style="text-align: center;" v-if="ansers[2]!=3">{{ questions[3] }}  <span class="btn btn-primary mx-1" @click="()=>{ansers[3]=1}">그렇다</span><span class="btn btn-success mx-1" @click="()=>{ansers[3]=0}">보통이다</span><span class="btn btn-danger mx-1" @click="()=>{ansers[3]=2}">그렇지않다</span></p>
      <p class="fs-5" style="text-align: center;" v-if="ansers[3]!=3">{{ questions[4] }}  <span class="btn btn-primary mx-1" @click="()=>{ansers[4]=1}">그렇다</span><span class="btn btn-success mx-1" @click="()=>{ansers[4]=0}">보통이다</span><span class="btn btn-danger mx-1" @click="()=>{ansers[4]=2}">그렇지않다</span></p>
      <button class="btn btn-info fw-bold" v-if="ansers[4]!=3" style="margin-left: 45%; width: 100px; color: white; margin-top: 10px;" @click="gosearch"> 제 출 </button>
    </div>
  

    
  </div>
  <div :style="maxWidth" class="px-5 py-3 mx-auto" style="background-color: white; border-radius: 10px;">
  
  </div>
  <div :style="maxWidth" class="px-5 py-3 mx-auto" style="background-color: white; margin-top: 20px; border-radius: 10px;">
    <div class="row row-cols-md-5 g-4" >
      <div class="card mx-4" data-masonry='{"percentPosition": true }' v-for="card in cards" >
        <div class="product-title">
          <div class="product-img-div">
            <img :src="card.img_url" class="product-img" style="object-fit: contain" alt="...">
          </div>
        </div>
        
        <div class="card-body">
          <h5 class="card-title fw-bold">{{ card.name }}</h5>
          <template v-for="benefit in benefits" >
            <span class="card-text" v-if="card[benefits_dic[benefit]]"> {{ benefit }} / </span>
          </template>
        </div>
        <a :href='url+card.naver_card_id'><button class="btn" style="background-color: lightgreen; width: 100%; margin-bottom: 10px;">자세히</button></a>
      </div>
    </div>
    <h1 style="text-align: center; color: gray; margin-top:30px" v-if="cards.length==0"> 검색 결과가 없습니다. </h1>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue'
import { useCounterStore } from '../stores/counter';
import DepositItem from '../components/DepositItem.vue';

const store = useCounterStore()

const isSearch = ref(false)
const benefits_dic = {
    '주유': 'fuel',
    '쇼핑' : 'shoping',
    '대형마트' : 'supermarket',
    '편의점': 'convenience_store',
    '외식' : 'eat_out',
    '카페/베이커리' : 'cafe/bakery',
    '영화' : 'movie',
    '대중교통' : 'public_transport',
    '관리비' : 'maintenance',
    '통신' : 'communication',
    '교육' : 'education',
    '육아' : 'parenting',
    '문화' : 'culture',
    '레저' : 'leisure',
    '항공마일리지' : 'airline_mileage',
    '프리미엄' : 'premium',
    '하이패스' : 'hi-pass',
    '오토' : 'auto',
    '의료' : 'medical',
    '뷰티' : 'beauty',
    '포인트/캐시백' : 'points/cashback',
    '간편결제' : 'easy_payment',
    '렌탈' : 'rental',
    '반려동물' : 'pet',
}

const benefits = [
  '주유','쇼핑','대형마트','편의점','외식','카페/베이커리','영화','대중교통','관리비','통신','교육','육아',
  '문화','레저','항공마일리지','프리미엄' ,'하이패스' ,'오토','의료','뷰티','포인트/캐시백' ,'간편결제','렌탈'
]

const questions = ref([
  '나는 카페에 자주가는 편이다.',
  '나는 편의점보다 대형마트에 자주 간다.',
  '나는 간편결제를 자주 사용한다.',
  '나는 자차가 있고 자주 타는 편이다.',
  '나는 다른 사람들에 비해 병원에 자주 가는 편이다.',
])

const checked = ref([])
const ansers = ref([3,3,3,3,3])
const cards = ref([])

const url = 'https://card-search.naver.com/item?cardAdId='

let is_all = computed(() => {
  return (checked.value.length==benefits.length)
})

const gosearch = function () {
  axios({
    method:'get',
    url: `${store.ServerURL}finances/cardrecommend/`,
    params : {
      'cafe':ansers.value[0],
      'supermaket':ansers.value[1],
      'simple_payment':ansers.value[2],
      'car':ansers.value[3],
      'medical':ansers.value[4],
    }
  })
  .then((res) => {
    console.log(res)
    cards.value = res.data
    ansers.value = [3,3,3,3,3]
    isSearch.value = false
  })
  .catch((err) => {
    console.log(err)
  })
}

const maxWidth = ref({
  width : `${(screen.availWidth/12)*10}px`
})
onMounted(()=>{
  axios({
    method:'get',
    url: `${store.ServerURL}finances/card/`,
  })
  .then((res) => {
    console.log(res)
    cards.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
})

const search = function () {
  axios({
    method:'get',
    url: `${store.ServerURL}finances/cardsearch/${benefits.map((el)=> checked.value.includes(el)? '1' : '0').join('')}/`,
  })
  .then((res) => {
    console.log(res)
    cards.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}

const reset = function () {
  axios({
    method:'get',
    url: `${store.ServerURL}finances/card/`,
  })
  .then((res) => {
    console.log(res)
    cards.value = res.data
    checked.value = []
  })
  .catch((err) => {
    console.log(err)
  })
}

</script>

<style scoped>
  .bg {
    background-color: #80EAFF;
    color: white;
  }
  .product-title {
    text-align:center;
    display:table;
    height:250px;
    padding-top: 5px;
}

.product-img-div {
    display:table-cell;
    vertical-align:middle;
}

.product-img {
    max-width:180px;
    max-height:180px;
}
</style>