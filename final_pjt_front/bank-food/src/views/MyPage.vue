<template>
  <div>

    <!-- WARNINGPAGE -->
    <div v-if="!store.token" class="d-flex justify-content-center align-items-center flex-column" :style="warningBody">
      <img src="@/assets/WARNING.png" style="width: 300px; height: 300px;" alt="">
    <h1 style="font-weight: bold;">로그인이 필요한 페이지입니다.</h1>
    <!-- <a href="https://www.flaticon.com/free-icons/warning" title="warning icons">Warning icons created by Pixel perfect - Flaticon</a> -->
    </div>

    <div v-if="store.token" style="margin: auto; margin-top: 30px; margin-bottom: 50px;" :style="pageBody">
      <div class="listBox" style="position: relative;">
        
        <div style="">
            <h2 :style="pageBody">My Page</h2>
            <div class="d-flex flex-row" :style="pageBody">
              <ul>
                <li
                @click="()=>{
                  flag_1= true;
                  flag_2=false;
                  flag_3=false;
                }"
                
                ><span>1</span><p style="font-weight: 600; font-size: 20px;">My Info</p></li>
                <li
                @click="()=>{
                  flag_1= false;
                  flag_2=true;
                  flag_3=false;
                }"
                
                ><span>2</span><p style="font-weight: 600; font-size: 20px;">My Articles</p></li>
                <li
                @click="()=>{
                  flag_1= false;
                  flag_2=false;
                  flag_3=true;
                }"
                
                ><span>3</span><p style="font-weight: 600;  font-size: 20px;">My Bank Info</p></li>
              </ul>
              <div style="background-color: white; height: 620px; width: 950px; margin: 0px; margin-left: 30px; border-radius: 10px;
              overflow: hidden;
              ">
                <div style="background-color:rgb(145, 144, 144) ; width: 1000px; height: 50px; "
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
                <div style="background-color: white;  height: 570px; width: 100%; overflow: scroll;">
                  <MyInfo
                  v-if="flag_1"
                  :userInfo="store.userInfo"
                  />
                  <MyArticles
                  v-if="flag_2"
                  />
                  <MyBankInfo
                  v-if="flag_3"
                  />
              </div>
              </div>
            </div>
          </div>

        </div>
      <div>
        
      </div>
    </div>

  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';
import { onMounted, ref } from 'vue';
import MyInfo from '../components/MyInfo.vue'
import MyArticles from '../components/MyArticles.vue'
import MyBankInfo from '../components/MyBankInfo.vue'
import axios from 'axios';
import Swal from 'sweetalert2';
const store = useCounterStore()
const warningBody = ref({
  height : `${(screen.availHeight/12)*10}px`,
  width : `${screen.availWidth}px`,
})
const pageBody = ref({
  width : `${(screen.availWidth/12)*8}px`,
})

const flag_1 = ref(true)
const flag_2 = ref(false)
const flag_3 = ref(false)





</script>

<style scoped>

.listBox{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  width: 300px;
  

}
.listBox h2 {
  color: black;
  border: 1px solid deepskyblue;
  box-shadow: 0 0 5px deepskyblue;
  background: white;
  padding:  10px 20px;
  font-size: 20px;
  font-weight: 700;
  border-radius: 10px;

}
.listBox ul{
  width: 300px;
  position: relative;
  background-color: #fff;
  margin-bottom: 0px;
  border-bottom: 20px solid white;
  
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}
.listBox ul li{
  list-style: none;
  padding: 10px;
  width: 100%;
  height: 200px;
  background-color: #fff;
  box-shadow: 0 5px 25px rgba(0,0,0,.1);
  transition: transform 0.5s;
}
.listBox ul:hover li{
  opacity: 0.2;
}
.listBox ul li:hover{
  transform: scale(1.1);
  z-index: 100;
  background-color: #25bcff;
  box-shadow: 0 5px 25px rgba(0, 0, 0, .2);
  color : #fff;
  opacity: 1;
}

.listBox ul li span{
  width: 20px;
  height: 20px;
  text-align: center;
  line-height: 20px;
  background-color: #25bcff;
  color: #fff;
  display: inline-block;
  border-radius: 50%;
  margin-right: 20px;
  font-size: 12px;
  font-weight: 600;
  transform: translate(-2px);


}
.listBox ul li:hover span{
  background: #fff;
  color: #25bcff;
}

::-webkit-scrollbar{
    width: 13px;
    background-color: rgba(105, 103, 103, 0.048);
}
::-webkit-scrollbar-thumb {
    border-radius: 15px;
    background-color: lightgrey;
    border : 1px solid black;
  }
::-webkit-scrollbar-track {
    background-color: lightgrey;
}
</style>