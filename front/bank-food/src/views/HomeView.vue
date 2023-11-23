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
    

    

  </div>
</template>

<script setup>
import { Carousel, Pagination, Slide } from "vue3-carousel";
import { onMounted, ref } from 'vue';
import "vue3-carousel/dist/carousel.css";
import MainCard from '@/components/MainCardComp.vue'
import axios from 'axios'
import {useCounterStore} from '@/stores/counter'
import YoutubeCard from '@/components/YoutubeCardComp.vue'
import NewsPage from "@/components/NewsPage.vue";

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
onMounted(()=>{
  const newsDiv = document.querySelector('#newsDiv')
  const youtubeDiv = document.querySelector('#youtubeDiv')
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
}) 
const youtubeTime = ref(1)
const newsTime = ref(1)




</script>

<style scoped>
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



</style>


