<template>
  <div>
    
      <div :style="carouselWidth"  style=" display:inline-block;" class="animate__animated animate__fadeIn " id="CarouselDiv">
        <Carousel :autoplay="3000" :items-to-show="3" :snap-align="'center'" :wrap-around="true"
        >
          <Slide v-for="(item,idx) in items" :key="item" style="margin-bottom: 20px;"
          :currentSlide="2"
          >
            <MainCard
            :item="item"
            />
          </Slide>
          <template #addons>
            <Pagination style="margin-top:30px"/>
          </template>
        </Carousel>
        
      </div>
      <div class="balloon d-flex align-items-center" :style="balloonWidth" style="position: absolute; top: 150px; ">
        <p style="font-weight: bold; font-size: 23px; text-align: center;">캐릭터를 누르면 금융 문제가　 나옵니다.</p>
      </div>
      <img src="@/assets/QUESTION.png" :style="pigIconWidth" style=" position: absolute; top:450px;" alt="">
    <!-- 01 데일리(튜브) -->

    <div >
      <h2 style="font-weight: bold; padding-left: 50px;">01. 데일리TUBE</h2>
      <div
      @mouseover="youtubeTime=3000"
      @mouseleave="youtubeTime=1"
      id="youtubeDiv"
      >
        <Carousel :autoplay="youtubeTime" :items-to-show="5" :wrap-around="true" :transition="2000" :style="dailyWidth">
        <Slide v-for="youtube in stores.youtube" :key="youtube" style="margin-bottom: 20px;">
          <YoutubeCard
          :youtube="youtube"

          />
        </Slide>
        <template #addons>
          <!-- <Pagination style="margin-top:30px"/> -->
        </template>
      </Carousel>
      </div>
    </div>


    <!-- 02 데일리(뉴스) -->
    <div style="margin-top: 20px;">
      <h2 style="font-weight: bold; padding-left: 50px;" >02. 데일리NEWS</h2>
      <div style=""
      @mouseover="newsTime=3000"
      @mouseleave="newsTime=1"
      id="newsDiv"
      :class="fadeIn2"
      >
        <Carousel :autoplay="newsTime" :items-to-show="5" :wrap-around="true" :transition="2000" :style="dailyWidth">
        <Slide v-for="news in stores.news" :key="news" style="margin-bottom: 20px;"

        >
          <NewsPage
          :news="news"
          />
        </Slide>
        <template #addons>
          <!-- <Pagination style="margin-top:30px"/> -->
        </template>
      </Carousel>
      </div>
    </div>  
    <!-- 03 주식차트 -->
    <div class="d-flex">
      <div style="width: 600px; height: 600px; border-radius: 15px;
    box-shadow: 0px 0px 1px black; background-color: white;  margin-left: 200px; margin-top: 50px; margin-bottom: 50px;"
    id="chartDiv"
    :class="fadeIn3"
    >
    <br>
      <div class="d-flex align-items-center" >
        <h3 style="font-weight: 550; color: rgb(68, 67, 67);  margin-left: 50px; filter: drop-shadow(0px 0px 1px rgb(128, 127, 127));">03. 오늘의 주식
        </h3>
        <img src="@/assets/CHART.png" alt="" style="width: 50px; margin-left: 10px; filter: drop-shadow(1px 1px 3px black); margin-bottom: 30px;" >
      </div>
      <div class="d-flex flex-column" >
        <div class="d-flex flex-row">
          <div style="width: 200px; height: 200px; border-radius: 15px;
          box-shadow: 0px 0px 1px black; background-color: white; margin: auto;"
          class="cardItem"
          id="open-chart1-modal"
          >
          <p style="margin-left: 10px; margin-top: 10px; font-weight: bold; font-size: 20px; margin-bottom: 5px;">{{ stockIdx[0]?.name }}</p>
          <hr style="margin: 3px; color: red;">
          <p style="margin-left: 10px; font-weight: bold; margin-bottom: 5px;" >{{ stockIdx[0]?.now_price}}</p>
          <div :style="stockColor[0]">
            <span style="margin-bottom: 0px; margin-left: 10px;">{{ stockIdx[0]?.price_raise }}</span>
            <span style="margin-left: 10px;">{{  stockIdx[0]?.price_raise_percent }}</span>
          </div>
            <img :src="stockIdx[0]?.chart_url" alt="">
          </div>

          <div style="width: 200px; height: 200px; border-radius: 15px;
          box-shadow: 0px 0px 1px black; background-color: white; margin: auto;"
          class="cardItem"
          id="open-chart2-modal"
          >
          
          <p style="margin-left: 10px; margin-top: 10px; font-weight: bold; font-size: 20px; margin-bottom: 5px;">{{ stockIdx[1]?.name }}</p>
          <hr style="margin: 3px; color: red;">
          <p style="margin-left: 10px; font-weight: bold; margin-bottom: 5px;" >{{ stockIdx[1]?.now_price}}</p>
          <div :style="stockColor[1]">
            <span style="margin-bottom: 0px; margin-left: 10px;">{{ stockIdx[1]?.price_raise }}</span>
            <span style="margin-left: 10px;">{{  stockIdx[1]?.price_raise_percent }}</span>
          </div>
            <img :src="stockIdx[1]?.chart_url" alt="">
          </div>

        </div>
        <div class="d-flex flex-row" style="margin-top: 50px;">
          <div style="width: 200px; height: 200px; border-radius: 15px;
          box-shadow: 0px 0px 1px black; background-color: white; margin: auto;"
          class="cardItem"
          id="open-chart3-modal"
          >
        
          <p style="margin-left: 10px; margin-top: 10px; font-weight: bold; font-size: 20px; margin-bottom: 5px;">{{ stockIdx[2]?.name }}</p>
          <hr style="margin: 3px; color: red;">
          <p style="margin-left: 10px; font-weight: bold; margin-bottom: 5px;" >{{ stockIdx[2]?.now_price}}</p>
          <div :style="stockColor[2]">
            <span style="margin-bottom: 0px; margin-left: 10px;">{{ stockIdx[2]?.price_raise }}</span>
            <span style="margin-left: 10px;">{{  stockIdx[2]?.price_raise_percent }}</span>
          </div>
            <img :src="stockIdx[2]?.chart_url" alt="">
        
        </div>
          <div style="width: 200px; height: 200px; border-radius: 15px;
          box-shadow: 0px 0px 1px black; background-color: white; margin: auto;"
          class="cardItem"
          id="open-chart4-modal"
          >
          <p style="margin-left: 10px; margin-top: 10px; font-weight: bold; font-size: 20px; margin-bottom: 5px;">{{ stockIdx[3]?.name }}</p>
          <hr style="margin: 3px; color: red;">
          <p style="margin-left: 10px; font-weight: bold; margin-bottom: 5px;" >{{ stockIdx[3]?.now_price}}</p>
          <div :style="stockColor[3]">
            <span style="margin-bottom: 0px; margin-left: 10px;">{{ stockIdx[3]?.price_raise }}</span>
            <span style="margin-left: 10px;">{{  stockIdx[3]?.price_raise_percent }}</span>
          </div>
            <img :src="stockIdx[3]?.chart_url" alt="">


        </div>
        </div>
      </div>
    </div>
    
    
  <!-- 모달창 -->
      <div id="chart1-modal">
        <div class="chart1-modal-content">
            <div class="d-flex justify-content-between ">
                <h2 style="margin:0px; margin-bottom: 20px; margin-left: 15px; font-weight: bold; margin-top: 7px;">코스피</h2>
                <span id="close-chart1-modal" style="font-size: 30px; cursor: pointer; margin-right: 30px;">X</span>
            </div>
            <hr style="margin-top: 0px;">
            <div class="d-flex align-items-center">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급등주 </h3> 
              <img src="@/assets/CHARTUP.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type09 " style="border: 1px solid lightcoral; 
              box-shadow: 0 0 5px crimson; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in (0,5)">
                  <td style="font-weight: bold;">{{ Kospi[idx-1]?.name }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx-1]?.type }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx-1]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx-1]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx-1]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>

          <div class="d-flex align-items-center" style="margin-top: 20px;">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급락주 </h3> 
              <img src="@/assets/CHARTDOWN.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type10 " style="border: 1px solid skyblue; 
              box-shadow: 0 0 5px darkblue; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in 5">
                  <td style="font-weight: bold;">{{ Kospi[idx+4]?.name }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx+4]?.type }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx+4]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx+4]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ Kospi[idx+4]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>

          </div>
      </div>
      <div id="chart2-modal">
        <div class="chart2-modal-content">
            <div class="d-flex justify-content-between">
                <h2 style="margin:0px; margin-bottom: 20px; margin-left: 15px; font-weight: bold; margin-top: 7px;">코스닥</h2>
                <span id="close-chart2-modal" style="font-size: 30px; cursor: pointer; margin-right: 30px;">X</span>
            </div>
            <hr style="margin-top: 0px;">
            <div class="d-flex align-items-center">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급등주 </h3> 
              <img src="@/assets/CHARTUP.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type09 " style="border: 1px solid lightcoral; 
              box-shadow: 0 0 5px crimson; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in (0,5)">
                  <td style="font-weight: bold;">{{ Kosdaq[idx-1]?.name }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx-1]?.type }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx-1]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx-1]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx-1]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>

          <div class="d-flex align-items-center" style="margin-top: 20px;">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급락주 </h3> 
              <img src="@/assets/CHARTDOWN.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type10 " style="border: 1px solid skyblue; 
              box-shadow: 0 0 5px darkblue; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in 5">
                  <td style="font-weight: bold;">{{ Kosdaq[idx+4]?.name }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx+4]?.type }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx+4]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx+4]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ Kosdaq[idx+4]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>

          </div>
      </div>
      <div id="chart3-modal">
        <div class="chart3-modal-content">
            <div class="d-flex justify-content-between">
                <h2 style="margin:0px; margin-bottom: 20px; margin-left: 15px; font-weight: bold; margin-top: 7px;">나스닥</h2>
                <span id="close-chart3-modal" style="font-size: 30px; cursor: pointer; margin-right: 30px;">X</span>
            </div>
            <hr style="margin-top: 0px;">
            <div class="d-flex align-items-center">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급등주 </h3> 
              <img src="@/assets/CHARTUP.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type09 " style="border: 1px solid lightcoral; 
              box-shadow: 0 0 5px crimson; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in (0,5)">
                  <td style="font-weight: bold;">{{ Nasdaq[idx-1]?.name }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx-1]?.type }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx-1]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx-1]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx-1]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>

          <div class="d-flex align-items-center" style="margin-top: 20px;">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급락주 </h3> 
              <img src="@/assets/CHARTDOWN.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type10 " style="border: 1px solid skyblue; 
              box-shadow: 0 0 5px darkblue; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in 5">
                  <td style="font-weight: bold;">{{ Nasdaq[idx+4]?.name }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx+4]?.type }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx+4]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx+4]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ Nasdaq[idx+4]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>
          </div>
      </div>
      <div id="chart4-modal">
        <div class="chart4-modal-content">
            <div class="d-flex justify-content-between">
                <h2 style="margin:0px; margin-bottom: 20px; margin-left: 15px; font-weight: bold; margin-top: 7px;">S&P-500</h2>
                <span id="close-chart4-modal" style="font-size: 30px; cursor: pointer; margin-right: 30px;">X</span>
            </div>
            <hr style="margin-top: 0px;">
            <div class="d-flex align-items-center">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급등주 </h3> 
              <img src="@/assets/CHARTUP.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type09 " style="border: 1px solid lightcoral; 
              box-shadow: 0 0 5px crimson; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in (0,5)">
                  <td style="font-weight: bold;">{{ SP[idx-1]?.name }}</td>
                  <td style="font-weight: bold;">{{ SP[idx-1]?.type }}</td>
                  <td style="font-weight: bold;">{{ SP[idx-1]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ SP[idx-1]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ SP[idx-1]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>

          <div class="d-flex align-items-center" style="margin-top: 20px;">
              <h3 style="font-weight: bold; margin-bottom: 0px; "> 급락주 </h3> 
              <img src="@/assets/CHARTDOWN.png" style="width: 40px; margin-left: 10px;" alt="">
            </div>
            <table class="type10 " style="border: 1px solid skyblue; 
              box-shadow: 0 0 5px darkblue; margin-top: 10px;" 
            >
              <thead>
                <tr>
                  <th scope="cols">종목</th>
                  <th scope="cols">타입</th>
                  <th scope="cols">시가</th>
                  <th scope="cols">등락</th>
                  <th scope="cols">등락률</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idx in 5">
                  <td style="font-weight: bold;">{{ SP[idx+4]?.name }}</td>
                  <td style="font-weight: bold;">{{ SP[idx+4]?.type }}</td>
                  <td style="font-weight: bold;">{{ SP[idx+4]?.now_price }}</td>
                  <td style="font-weight: bold;">{{ SP[idx+4]?.price_raise }}</td>
                  <td style="font-weight: bold;">{{ SP[idx+4]?.price_raise_percent }}</td>
                </tr>
              </tbody>
          </table>
          </div>
      </div>
    <!-- 모달창 끝 -->
      <Quiz 
      style="margin-top: 50px;"
      />
    </div>

    </div>
</template>

<script setup>
import { Carousel, Pagination, Slide } from "vue3-carousel";
import { onMounted, ref, resolveDirective } from 'vue';
import "vue3-carousel/dist/carousel.css";
import MainCard from '@/components/MainCardComp.vue'
import axios from 'axios'
import {useCounterStore} from '@/stores/counter'
import YoutubeCard from '@/components/YoutubeCardComp.vue'
import NewsPage from "@/components/NewsPage.vue";
import Quiz from "@/components/quiz.vue"

const stock = ref([])
const stockIdx = ref([])
const Kospi = ref([])
const Kosdaq = ref([])
const Nasdaq = ref([])
const SP = ref([])
const redColor = ref({
  color : 'red'
})
const blueColor = ref({
  color : 'blue'
})

const items=ref([1,2,3,4])
const stores = useCounterStore()
const carouselWidth = ref({
  width : `${(screen.availWidth/12)*10}px`
})
const pigIconWidth = ref({
  width : `${(screen.availWidth/14)*2}px`,
  left : `${(screen.availWidth/12)*(10)}px`
})
const balloonWidth = ref({
  width : `${(screen.availWidth/14)*2}px`,
  height : `${(screen.availWidth/12)*1.6}px`,
  left : `${(screen.availWidth/12)*(10)}px`
})
const fadeIn1 = ref({
  animate__fadeIn : false,
  animate__animated : true,
  'animate__delay-1s' : true,
  animate__slow : true,

})

const dailyWidth = ref({
  width: `${screen.availWidth}px`
})



const fadeIn2 = ref({
  animate__fadeIn : false,
  animate__animated : true,
  'animate__delay-1s' : true,
  animate__slow : true,
})
const fadeIn3 = ref({
  animate__fadeIn : false,
  animate__animated : true,
  'animate__delay-2s' : true,
  animate__slow : true,
})
onMounted(()=>{
  const newsDiv = document.querySelector('#newsDiv')
  const youtubeDiv = document.querySelector('#youtubeDiv')
  const chartDiv = document.querySelector('#chartDiv')
  // stores.getDjangoYoutube()
  // stores.getDjangoNews()
  // stores.getDjangoExchange()
  stores.getExchange()
  stores.getYoutube()
  stores.getNews()
  const observer1 = new IntersectionObserver((now)=>{
  fadeIn1.value.animate__fadeIn = true
})
observer1.observe(youtubeDiv)

  const observer2 = new IntersectionObserver((now)=>{
  fadeIn2.value.animate__fadeIn = true
})
observer2.observe(newsDiv)

  const observer3 = new IntersectionObserver((now)=>{
    fadeIn3.value.animate__fadeIn = true
  })
  observer3.observe(chartDiv)
    // 모달
    const chart1Modal = document.getElementById("chart1-modal");
    const openchart1ModalBtn = document.getElementById("open-chart1-modal");
    const closechart1ModalBtn = document.getElementById("close-chart1-modal");
    // 모달창 열기
    openchart1ModalBtn.addEventListener("click", () => {
      chart1Modal.style.display = "block";
    });
    // 모달창 닫기
    closechart1ModalBtn.addEventListener("click", () => {
      chart1Modal.style.display = "none";
    });
    // 모달
    const chart2Modal = document.getElementById("chart2-modal");
    const openchart2ModalBtn = document.getElementById("open-chart2-modal");
    const closechart2ModalBtn = document.getElementById("close-chart2-modal");
    // 모달창 열기
    openchart2ModalBtn.addEventListener("click", () => {
      chart2Modal.style.display = "block";
    });
    // 모달창 닫기
    closechart2ModalBtn.addEventListener("click", () => {
      chart2Modal.style.display = "none";
    });
    // 모달
    const chart3Modal = document.getElementById("chart3-modal");
    const openchart3ModalBtn = document.getElementById("open-chart3-modal");
    const closechart3ModalBtn = document.getElementById("close-chart3-modal");
    // 모달창 열기
    openchart3ModalBtn.addEventListener("click", () => {
      chart3Modal.style.display = "block";
    });
    // 모달창 닫기
    closechart3ModalBtn.addEventListener("click", () => {
      chart3Modal.style.display = "none";
    });
    // 모달
    const chart4Modal = document.getElementById("chart4-modal");
    const openchart4ModalBtn = document.getElementById("open-chart4-modal");
    const closechart4ModalBtn = document.getElementById("close-chart4-modal");
    // 모달창 열기
    openchart4ModalBtn.addEventListener("click", () => {
      chart4Modal.style.display = "block";
    });
    // 모달창 닫기
    closechart4ModalBtn.addEventListener("click", () => {
      chart4Modal.style.display = "none";
    });
}) 
const youtubeTime = ref(1)
const newsTime = ref(1)
const stockColor = ref([])

axios({
  method: 'get',
  url : 'http://127.0.0.1:8000/daily/index/',
})
.then(res=>{
  stockIdx.value = res.data
  for(let i=0; i<4; i++){
  if(res.data[i].price_raise[0] == '+')
    {  stockColor.value.push(redColor.value)}
  else{
    stockColor.value.push(blueColor.value)
  }
}
})
axios({
  method: 'get',
  url : 'http://127.0.0.1:8000/daily/stock/',
})
.then(res=>{
  stock.value = res.data
  for(let i = 0; i<10; i++){
    Kospi.value.push(stock.value[i])
  }
  for(let i =10; i<20; i++){
    Kosdaq.value.push(stock.value[i])
  }
  for(let i=20; i<30; i++){
    Nasdaq.value.push(stock.value[i])
  }
  for(let i =30; i<40; i++){
    SP.value.push(stock.value[i])
  }
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
  color: rgb(153, 51, 51);
  border-bottom: 3px solid rgb(153, 51, 51);
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

table.type10 {
  border-collapse: collapse;
  text-align: left;
  line-height: 1.15;

}
table.type10 thead th {
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  color: #369;
  border-bottom: 3px solid #036;
}
table.type10 tbody th {
  width: 150px;
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
  background: #f3f6f7;
}
table.type10 td {
  width: 350px;
  padding: 10px;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
}



.blue{
  color: blue;
}
.balloon {
    display: inline-block;
    position: relative;
    background: #ccc;
    height: 70px;
    width: 120px;
    margin: 0 auto 10px;
    border-radius: 50%;
    padding:50px
}
.balloon:before {
    content: '';
    position: absolute;
    background: #ccc;
    height: 20px;
    width: 20px;
    border-radius: 10px;
    bottom: -20px;
    left: 70px;
}
.balloon:after {
    content: '';
    position: absolute;
    background: #ccc;
    height: 10px;
    width: 10px;
    border-radius: 5px;
    bottom: -30px;
    left: 90px;
}


@keyframes cursorOn {
      25% {
        transform: rotate(2deg) scale(1.01);
    }
    50% {
        transform: rotate(0deg) scale(1);
    }
    75% {
        transform: rotate(-2deg) scale(1.01);
    }
    }
    .cardItem:hover{
      opacity: 0.9;
      animation: cursorOn 0.8s linear 1;
      filter: drop-shadow(5px 5px 1px rgb(116, 114, 114));
      cursor: pointer;
    }

    #chart1-modal {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
        display: none;
        }
        .chart1-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 650px;
        border-radius: 15px;
        }
        .close-chart1-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-chart1-modal:hover,
        .close-chart1-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }
        #chart2-modal {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
        display: none;
        }
        .chart2-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 650px;
        border-radius: 15px;
        }
        .close-chart2-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-chart2-modal:hover,
        .close-chart2-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }

        #chart3-modal {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
        display: none;
        }
        .chart3-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 650px;
        border-radius: 15px;
        }
        .close-chart3-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-chart3-modal:hover,
        .close-chart3-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }

        #chart4-modal {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
        display: none;
        }
        .chart4-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 650px;
        border-radius: 15px;
        }
        .close-chart4-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-chart4-modal:hover,
        .close-chart4-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }



</style>


