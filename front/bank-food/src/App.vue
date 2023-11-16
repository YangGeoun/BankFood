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
              <a class="nav-link dropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"
              style="font-size: 20px; margin-left: 10%; width:130px">
                환율 계산기
              </a>
              <ul class="dropdown-menu" style="margin-top: 10px;">
                <li><a class="dropdown-item" href="#" >Something else here</a></li>
              </ul>
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
      
        
          <a href=""  class="floating animate__animated d-flex flex-column align-items-center"  style="text-decoration: none; " :class="userFlag"
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
        
      
  </nav>
  <RouterView/>
</template>

<script setup>
import { ref } from 'vue';
import { RouterView } from 'vue-router';



const userFlag = ref([])
const myPage = ref({
  noneDisplay : true,
  goDisplay : false,
})


</script>

<style lang="scss" scoped>

</style>

<style>

/* 전역 색깔 설정 */
body{
  background-color: #f1f3f8;
  min-width: 1500px;
}

.floating {
  position: fixed; 

  right: 47%; 
  top: 85%; 
  margin-right: -720px;
  text-align:center;
  width: 50px;
}
.noneDisplay {
  display: none;
  
}
.goDisplay{
  
}
</style>