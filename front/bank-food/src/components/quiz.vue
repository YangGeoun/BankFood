<template>
  <div class="d-flex flex-row" :style="pageBody">
    
    <div style="background-color: white; height: 600px; width: 450px; margin: 0px; margin-left: 30px; border-radius: 15px;
    overflow: hidden;
     border: 1px solid lightgray;" >
      <div style="background-color:rgb(145, 144, 144) ; width: 1000px; height: 35px; "
      class="d-flex align-items-center"
      >
      <div style="border-radius: 50%; background-color: yellow; z-index: 999; width: 10px; height: 10px;
      margin-left: 20px;
      "></div>
      <div style="border-radius: 50%; background-color: green; z-index: 999; width: 10px; height: 10px;
      margin-left: 5px;
      "></div>
      <div style="border-radius: 50%; background-color: red; z-index: 999; width: 10px; height: 10px;
      margin-left: 5px;
      "></div>
      </div>
      <div class="p-2" >
        <div class="row row-cols-1 row-cols-md-2 g-4 text-center">
          <div class="col" v-for="(quiz, index) in quizes">
            <div class="card"  style="border-radius: 15px; position: relative;"  @click="showanswer(index)">
                <div v-show="isShow[index]" style="background-color:skyblue; position: absolute; padding: 15px; border: 1px solid lightgray; 
                border-radius: 10px; top:30%; margin-left: 25px;"
                >
                  <p class="fw-bold mb-0" style="color: white;">정답 : {{ quiz.anser }}.{{ quiz.selections[quiz.anser-1] }}</p>
                </div>
                <div class="card-body">
                <div class="fw-bold">
                  <p class="card-title" >문제{{ index + 1 }}</p><hr class="my-1">
                  <p class="card-title">{{ quiz.question }}</p>
                </div>
                <div class="row">
                  <p class="card-text col-6 px-1" 
                  style="margin-bottom: 0;" v-for="(s, index2) in quiz.selections">
                  {{index2+1}}. {{ s }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>






          
        <!-- <div class="col-6" v-for="(quiz, index) in quizes">
            <p class="fs-5">문제{{ index + 1 }}. {{ quiz.question }}</p>
          <div class="row">  
            <p class=" col-6 text-center" v-for="(s, index2) in quiz.selections">{{index2+1}}. {{ s }}</p>
          </div>
        </div> -->
      </div>
      <!-- <div style="background-color: white;  height: 570px; width: 100%; overflow: scroll;">
    </div> -->
    </div>
  </div>
    
</template>

<script setup>
  import { ref } from 'vue';
  import { useCounterStore } from '../stores/counter';
  const store = useCounterStore()
  const num = Math.floor(Math.random() * 7)
  const quizes = store.quizes.slice(num,num+4)

  const isShow = ref([false,false,false,false])
  const showanswer = function (index) {
    isShow.value[index] = true
  }
  
</script>

<style scoped>

</style>