<template>
  <div>
    <div style="height: 1000px;">
    </div>
      <div style="width: 1300px; margin:auto" class="animate__animated animate__delay-2s" :class="animateClass" id="CarouselDiv">
      <Carousel :autoplay="3000" :items-to-show="3" :snap-align="'center'" :wrap-around="true" >
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
  </div>
</template>

<script setup>
import { Carousel, Pagination, Slide } from "vue3-carousel";

import { onMounted, ref } from 'vue';
import "vue3-carousel/dist/carousel.css";
import MainCard from '@/components/MainCardComp.vue'

const animateClass = ref({
  'animate__fadeInRight' : false
})

let observer = null
onMounted(()=>{
  const carouselDiv = document.querySelector('#CarouselDiv')
  observer = new IntersectionObserver(function(entries){
  animateClass.value.animate__fadeInRight = true
  // entries.target.classList.add('animate__fadeInRight')
})
observer.observe(carouselDiv)
})




// observer.observe(carouselDiv)
const items=ref([1,2,3,4])

</script>

<style scoped>

</style>

