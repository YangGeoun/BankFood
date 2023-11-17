<template>
  <div>
    
      <div style="width: 1500px; display: inline-block;" class="animate__animated animate__fadeIn " id="CarouselDiv">
        
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
      <div class="balloon" style="position: absolute; width:250px; height: 200px;top: 180px; left: 1585px;">
        <p style="font-weight: bold; font-size: 20px;">캐릭터를 누르면 금융 문제가 나옵니다.</p>
      </div>
      <img src="@/assets/QUESTION.png" style=" width: 250px; position: absolute; top:400px; left: 1600px;" alt="">
    <!-- 01 데일리(튜브) -->

    <div >
      <h2 style="font-weight: bold; padding-left: 50px;">01.데일리TUBE</h2>
      <div style="margin-top: 50px;"
      @mouseover="youtubeTime=3000"
      @mouseleave="youtubeTime=1"
      >
        <Carousel :autoplay="youtubeTime" :items-to-show="5" :wrap-around="true" :transition="2000">
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
    <div style="margin-top: 50px; margin-bottom: 100px;">
      <h2 style="font-weight: bold; padding-left: 80px; margin-bottom: 50px;">02.데일리NEWS</h2>
      <div style="margin: auto;  border: 1px; background-color: white; border-radius: 30px; width: 1500px; height: 800px;" id="newsDiv"
      class="animate__animated animate__delay-1s animate__slow"
      :class="fadeIn"
      @mouseover="newsTime=3000"
      @mouseleave="newsTime=1"
      >
      
      </div>
    </div >
    

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


const items=ref([1,2,3,4])
const stores = useCounterStore()
const fadeIn = ref({
  animate__fadeInRight : false
})
onMounted(()=>{
  const newsDiv = document.querySelector('#newsDiv')

  stores.getYoutube()
  const observer = new IntersectionObserver((now)=>{
  fadeIn.value.animate__fadeInRight = true
})
observer.observe(newsDiv)
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

