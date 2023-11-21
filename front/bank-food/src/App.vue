<template>
  <nav class="navbar bg-body-tertiary " style="height: 100px; padding-top: 0px;" :style="navWidth">
      <div class="container-fluid " style="font-weight: bold">
        <img src="@/assets/ICON.gif" alt="" style="height: 100px; margin-left: 5%; padding-bottom: 20px; cursor: pointer;"
        @click="router.push({name:'home'})"
        >
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
              @click="router.push({name:'map'})"
              >
                내 근처 은행
              </a>
              
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
            <div style="margin-right: 50px;" class="d-flex">
              <SIgnUpModal  style="border-right: 0px;" v-if="!store.token"/>
              <LoginModal style="border-left: 0px;" v-if="!store.token"/>
              <button id="MyPage" style="width: 100px; border-radius: 15px 0px 0px 15px; border-right: 0px;   font-weight: bold;" v-if="store.token"
              @click="router.push({name:'mypage'})"
              >My Page</button>
              <button id="LogOut" style="width: 100px; border-radius: 0px 15px 15px 0px;    font-weight: bold;" v-if="store.token"
              @click="logout()"
              >LOGOUT</button>
              
            </div>
        <!-- </div> -->
      </div>


      <!-- animate__heartBeat animate__infinite -->
      
        
          <p href=""  class="floating animate__animated d-flex flex-column align-items-center"  :style="userWidth" style="text-decoration: none; " :class="userFlag"
          @mouseover="function(){ 

            myPage.noneDisplay = false
            myPage.goDisplay = true
            userDropDown()
            }"
          @mouseleave="function(){ 
            userFlag=[]
            myPage.noneDisplay = true
            myPage.goDisplay = false
            userDropDownFalse()
          }"
          
          >
          <div style="display: none; width: 50px;"  id="userDrop" >
            </div>
            <img src="@/assets/USER.png" style="width: 100%;" alt=""
            >
            
          </p>
  
      <div id="calc-modal" style="z-index: 99999;">
        <div class="calc-modal-content">
          <div class="d-flex justify-content-between">
            <h4 style="margin:0px; margin-left: 30px; font-weight: bold;">환율 계산기</h4>
            <div>
              <h4 id="close-calc-modal" style=" cursor: pointer; font-weight: bold;"
              @click="calcCloseModal"  
              >X
              </h4>
          </div>
          </div>
          <hr style="margin:3px">
          <div style="line-height: 60%;">
            <br>

          </div>
          <div class="d-flex align-items-center" style="width: 500px; margin-left: 30px;">
            <div>
              <div class="d-flex">
                <input type="number" step="0.01" v-model="country_1"   id="calc-input1" style="border-radius: 5px 0px 0px 5px; width: 400px; height: 30px; font-size: 20px; text-align: center;"
                @focus="flag1 = true; flag2=false;"
                >
                <select class="form-select" v-model="value_1" aria-label="Default select example" style="width: 150px; height: 30px; font-size: 11px; font-weight: bold; border-radius: 0px 5px 5px 0px; border: 2px black; border-style: solid solid solid hidden; display: inline-block;">
                  <option style="text-align: center;" v-for="change in store.exchange" :value="change.deal_bas_r"
                  :id="change.cur_unit"
                  >
                    <span>{{change.cur_nm}}</span>
                  </option>
                </select>
              </div>
              <div class="d-flex" style="margin-top: 20px;">
                <input type="number" step="0.01" id="calc-input2"  v-model="country_2"  style="border-radius: 5px 0px 0px 5px; width: 400px; height: 30px; font-size: 20px;  text-align: center;"
                @focus="flag2 = true; flag1 = false;"
                >
                <select class="form-select" v-model="value_2" aria-label="Default select example" style="width: 150px; height: 30px; font-size: 11px; font-weight: bold; border-radius: 0px 5px 5px 0px; border: 2px black; border-style: solid solid solid hidden; display: inline-block;">
                  <option style="text-align: center;
                  " v-for="change in store.exchange" :value="change.deal_bas_r">
                    {{change.cur_nm}}
                  </option>

                </select>
              </div>
            </div>
              <img src="@/assets/CALC.png" style="width: 70px; height: 70px; margin-left: 15px; cursor: pointer;" alt=""
              @click="calculator()"
              class="animate__animated animate__infinite"
              :class="{'animate__headShake' : calcFlag}"
              >
          </div>
        
        </div>
      </div>
      
  </nav>
  <RouterView/>
</template>

<script setup>
import { ref } from 'vue';
import { RouterView } from 'vue-router';
import { useRouter } from 'vue-router';
import {useCounterStore} from '@/stores/counter'
import SIgnUpModal from './components/SIgnUpModal.vue';
import LoginModal from './components/LoginModal.vue';
import axios from 'axios';
import MyPage from './views/MyPage.vue';
const logout = function(){
  axios({
    url :`http://127.0.0.1:8000/accounts/logout/`,
    method : 'get',
    headers :{
      Authorization : `Token ${store.token}`
    }
  })
  .then(
    res=>{
    store.token = null
    store.userInfo = {}
  }
  )
  .catch(err=>{
    console.log(err)
    store.token = null
    store.userInfo = {}
  }
    )
}

const store = useCounterStore()
const navWidth = ref({
  width: `${screen.availWidth}px`
})
const router = useRouter()
document.body.style.minWidth = `${screen.availHeight}px`
const userWidth = ref({
  left : `${(screen.availWidth/16)*13}px`,

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


// 환율계산기
const country_1 = ref(null)
const country_2 = ref(null)
const flag1 = ref(false)
const flag2 = ref(false)
const value_1 = ref(null)
const value_2 = ref(null)

const calculator = function(){
  calcFlag.value = true

  if(flag1.value===true){
    const calcInput2 = document.querySelector('#calc-input2')
    country_2.value = parseFloat((parseFloat(country_1.value) * parseFloat(value_1.value.replace(/,/g , ''))) / parseFloat(value_2.value.replace(/,/g , '')))

  }
  else{
    country_1.value = parseFloat((country_2.value * parseFloat(value_2.value.replace(/,/g , ''))) / parseFloat(value_1.value.replace(/,/g , '')))

  }
  setTimeout(()=>{
    calcFlag.value=false
  },1000)

} 
const calcFlag = ref(false)


const userDropDown = function(){
  const userDrop = document.querySelector('#userDrop')
  userDrop.style.display = 'block'
}
const userDropDownFalse = function(){
  const userDrop = document.querySelector('#userDrop')
  userDrop.style.display = 'none'
}


</script>

<style scoped>

#MyPage:focus{
            outline: none;
            border: 1px solid deepskyblue;
            box-shadow: 0 0 10px deepskyblue;
        }
        #MyPage:hover{
          outline: none;
            border: 1px solid deepskyblue;
            box-shadow: 0 0 10px deepskyblue;
        }
        #MyPage:hover{
          outline: none;
          
            border: 1px solid deepskyblue;
            border-left: 0px;
            box-shadow: 0 0 10px deepskyblue;
        }

        #LogOut:focus{
            outline: none;
            border: 1px solid red;
            box-shadow: 0 0 10px red;
        }
        #LogOut:hover{
          outline: none;
            border: 1px solid red;
            box-shadow: 0 0 10px red;
        }
        #LogOut:hover{
          outline: none;
          
            border: 1px solid red;
            border-left: 0px;
            box-shadow: 0 0 10px red;
        }


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
        padding-left: 5px;
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
            
            box-shadow: 0 0 10px greenyellow;
        }
        #calc-input2:focus{
            outline: none;
            
            box-shadow: 0 0 10px greenyellow;
        }



</style>