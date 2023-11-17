<template>
  <div class="card" :class="newsAnimate" style="margin-left: 50px; margin-top: 50px; border: 0px; border-radius: 30px;"
  
  @mouseover="newsAnimate = ['animate__animated','animate__pulse', 'animate__infinite']"
  @mouseleave="newsAnimate = []"
  >
    <a href="" target="_blank" style="text-decoration: none; color: black;">
      <img :src="news.image_url" class="card-img-top" alt="..." style=" border-radius: 10px; width: 100%; height: 180px;">
      <div class="card-body">
        <p class="card-text" style="height: 100px; font-weight: bold;">{{ news.title }}</p>
      </div>
    </a>
</div>
</template>

<script setup>
import { ref } from 'vue';

  defineProps({
    news:Object
  })
  const newsAnimate = ref([])

</script>

<style scoped>

</style>