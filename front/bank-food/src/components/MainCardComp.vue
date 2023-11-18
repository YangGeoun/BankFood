<template>
  <div class="card animate__animated" :class="[background, animate]" style="border-radius: 30px; width: 18rem; height: 500px; margin-top: 50px; box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);" 
  @mouseover="function(){
    animate = ['animate__pulse', 'animate__infinite']
  }"
  @mouseleave="function(){
    animate = []
  }"
  @click="clickEvent"
  >
    <div class="card-body">
      <p style="font-size: 30px; height: 90px; color: white; margin-top:30%; font-weight:bold; text-shadow: 2px 2px 2px gray;">{{ name }}</p>
      <img :src="URL" style="margin-top:100px; width:150px;" alt="">
    </div>
  <div id="calc-modal">
        <div class="calc-modal-content">
          <div class="d-flex justify-content-between">
            <h4 style="margin:0px; font-weight: bold;">환율 계산기</h4>
            <div>
              <h4 id="close-calc-modal" style=" cursor: pointer; font-weight: bold;"
              @click="calcCloseModal"  
              >X
              </h4>
          </div>
          </div>
          <hr>
          <div class="d-flex justify-content-center" style="width: 500px; margin-left: 30px;">
            <div>
              <input type="number" id="calc-input1" style="border-radius: 15px; width: 500px; height: 30px; font-size: 20px; text-align: center;">
              <input type="number" id="calc-input2" style="border-radius: 15px; width: 500px; height: 30px; font-size: 20px; margin-top: 20px; text-align: center;">
            </div>
              <img src="@/assets/CALC.png" style="width: 70px;  cursor: pointer;" alt="">
          </div>
        
        </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';

const props = defineProps(['item'])
const name = ref('')
const background = ref('')
const URL = ref('')
const animate = ref([])
const clickEvent = function(){
  if(props.item==2){ 
    const calcModal = document.getElementById("calc-modal");
    calcModal.style.display = "block";
    }
  }
const calcCloseModal = function(){
  const calcModal = document.getElementById("calc-modal");
  calcModal.style.display = "none";
}
onMounted(()=>{
  if(props.item == 1){
    name.value='예금/적금 조회 한번에 하기'
    background.value='bg-primary'
    URL.value='src/assets/MONEY.png'
  }
  else if(props.item==2){
    name.value='현재 환율 check!'
    background.value='bg-warning'
    URL.value='src/assets/CALCULATOR.png'

  }
  else if(props.item==3){
    name.value='근처 은행 찾기'
    background.value='bg-success'
    URL.value='src/assets/MAP.png'

  }
  else{
    name.value='유저들과의 소통'
    background.value='bg-danger-subtle'
    URL.value='src/assets/ARTICLE.png'

  }


}

)


</script>

<style scoped>

</style>