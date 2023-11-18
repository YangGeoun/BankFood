<template>
  <nav class="navbar bg-body-tertiary " style="height: 100px; min-width: 1500px; padding-top: 0px;">
      <div class="container-fluid " style="font-weight: bold">
        <img src="@/assets/ICON.gif" alt="" style="height: 100px; margin-left: 5%; padding-bottom: 20px;">
            <div class="nav-item dropdown">
              <a class="nav-link dropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"
              style="font-size: 20px; width:200px"
              >
                예금/적금 조회하기
              </a>
              <ul class="dropdown-menu" id="deposit_list" style="margin-top: 10px;">
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </div>

            <div class="nav-item dropdown">
              <a class="nav-link " href="#" role="button" aria-expanded="false"
              style="font-size: 20px; margin-left: 10%; width:130px"
              @click="calcOpenModal"
              >
                환율 계산기
              </a>
              
            </div>

            <div class="nav-item dropdown">
              <a class="nav-link dropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"
              style="font-size: 20px; margin-left: 10%; width: 180px; margin-bottom: 0;"
              >
                내 근처 은행
              </a>
              <ul class="dropdown-menu" style="margin-top: 10px;">
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </div>

            <div class="nav-item dropdown">
              <a class="nav-link " href="#" role="button" aria-expanded="false"
              style="font-size: 20px; margin-left: 10%; width: 100px;"
              >
                소통창구
              </a>
              <!-- <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul> -->
            </div>

          <!-- </ul> -->
          <form class="d-flex" role="search" style="margin-right: 50px;">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        <!-- </div> -->
      </div>


      <!-- animate__heartBeat animate__infinite -->
      
        
          <a href=""  class="floating animate__animated d-flex flex-column align-items-center"  :style="userWidth" style="text-decoration: none; " :class="userFlag"
          @mouseover="function(){ 
            userFlag=['animate__heartBeat', 'animate__infinite']
            myPage.noneDisplay = false
            myPage.goDisplay = true
            }"
          @mouseleave="function(){ 
            userFlag=[]
            myPage.noneDisplay = true
            myPage.goDisplay = false
          
          }"
          >
          <img src="@/assets/USER.png" style="width: 100%;" alt="">
          <div :class="myPage" style="color: black; font-weight: bold; width: 100px;">마이페이지</div>
          </a>
  
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
      
  </nav>
  <RouterView/>
</template>

<script setup>
import { ref } from 'vue';
import { RouterView } from 'vue-router';

document.body.style.minWidth = document.body.clientWidth
const userWidth = ref({
  left : `${(document.body.clientWidth/16)*13}px`
})
const userFlag = ref([])
const myPage = ref({
  noneDisplay : true,
  goDisplay : false,
})

const calcOpenModal = function(){
  const calcModal = document.getElementById("calc-modal");
  calcModal.style.display = "block";
}
const calcCloseModal = function(){
  const calcModal = document.getElementById("calc-modal");
  calcModal.style.display = "none";
}

</script>

<style scoped>


</style>

<style>

/* 전역 색깔 설정 */
body{
  background-color: #f1f3f8;

}

.floating {
  position: fixed; 

   
  top: 85%; 
  
  text-align:center;
  width: 50px;
  z-index: 999;
}
.noneDisplay {
  display: none;
  
}
.goDisplay{
  
}

/* 모달 */
#calc-modal {
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
        .calc-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 700px;
        border-radius: 15px;
        }
        .close-calc-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-calc-modal:hover,
        .close-calc-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }
        #calc-input1:focus{
            outline: none;
            border: 1px solid greenyellow;
            box-shadow: 0 0 10px greenyellow;
        }
        #calc-input2:focus{
            outline: none;
            border: 1px solid greenyellow;
            box-shadow: 0 0 10px greenyellow;
        }

</style>