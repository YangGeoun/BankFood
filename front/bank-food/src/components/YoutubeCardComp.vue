<template>
  <div class="card" :class="youtubeAnimate" style="margin-left: 50px;margin-top: 50px;  border: 0px; border-radius: 30px;"
  @mouseover="youtubeAnimate=['animate__animated','animate__pulse', 'animate__infinite']"
  @mouseleave="youtubeAnimate = []"
  >
    <a :href="`https://www.youtube.com/watch?v=${youtube.video_id}`" target="_blank" style="text-decoration: none; color: black;">
      <img :src="youtube.image_url" class="card-img-top" alt="..." style=" border-radius: 10px;">
      <div class="card-body">
        <p class="card-text" style="height: 100px; font-weight: bold;">{{ youtube.title }}</p>
      </div>
    </a>
</div>
</template>

<script setup>
import { ref } from 'vue';
const youtubeAnimate = ref([])

  defineProps({
    youtube:Object
  })

</script>

<style scoped>

</style>