<template>
  <div>
  <button style="width: 100px; border-radius: 15px; font-weight: bold;" id="open-SIGNUP-modal">SIGN UP</button>
  <div id="SIGNUP-modal">
        <div class="SIGNUP-modal-content" >
          <div class="d-flex justify-content-between ">
            <div>
            <h2 style="margin:0px; font-weight: bold; color: white; 
            text-shadow: -3px 0 black, 0 1px black, 1px 0 black, 0 -2px black; 
            "
            class="align-self-center"
            >SIGN UP</h2>
            <p style="margin-bottom: 0; color: red; font-weight: bold;">{{ message }}</p>
          </div>
            <span id="close-SIGNUP-modal" style="font-size: 30px; cursor: pointer; margin-right: 40px;
          
            ">X</span>
          </div>  
          <hr>
          <div class="d-flex ">
            <div style="display: inline-block; width: 510px;">
                <div class="d-flex justify-content-between" style="margin-top: 20px;">
                  <label for="id" style="font-weight: 30px; font-size: 25px;">ID :　</label>
                  <input type="text" id="id" style="border-radius: 15px; width: 300px; height: 30px; font-size: 20px; text-align: center;" v-model="nickname">
                </div>
                <div class="d-flex justify-content-between" style="margin-top: 20px;">
                <label for="password" style="font-weight: 30px; font-size: 25px;">password :　</label>
                <input type="password" id="password" style="border-radius: 15px; width: 300px; height: 30px; font-size: 20px; text-align: center;" v-model="password1">
              </div>
              <div class="d-flex justify-content-between " style="margin-top: 20px;">
                <label for="confirm" style="font-weight: 30px; font-size: 25px;">confirm :　</label>
                <input type="password" id="confirm" style="border-radius: 15px; width: 300px; height: 30px; font-size: 20px; text-align: center;" v-model="password2">
              </div>
              <div class="d-flex justify-content-between" style="margin-top: 20px;">

                <label for="username" style="font-weight: 30px; font-size: 25px;">name :　</label>
                <input type="text" id="username" style="border-radius: 15px; width: 300px; height: 30px; font-size: 20px; text-align: center;" v-model="username">
              </div>
              <div class="d-flex align-items-center justify-content-between" style="margin-top: 20px;">
                <div class="d-flex align-items-center">
                  <label for="genter" style="font-weight: 30px; font-size: 25px ; ">gender:　</label>
                  <select id="gender" style="border-radius: 15px; height: 30px; font-size: 15px; text-align: center; font-weight: bold;" v-model="gender">
                    <option value="0">남자</option>
                    <option value="1">여자</option>
                  </select>
                </div>
                <div style="margin-left: 30px;"  class="d-flex align-items-center">
                  <label for="age" style="font-weight: 30px; font-size: 25px;" ><span style="text-align: center;">age :　</span> </label>
                  <input type="number" id="age"  style="border-radius: 15px; height: 30px; font-size: 20px; text-align: center;"  v-model="age" 
                  @input="ageWarning()"
                  >
                </div>  
              </div>
              <hr>
              <Button class="btn" style="border-radius: 50px; width: 500px; border: 2px solid deepskyblue; font-weight: bold;"
              @click="makeAccount"
              >REGISTER</Button>
            </div>
            <div style="display: inline-block; margin-left: 50px; margin-top: 50px;">
              <img src="@/assets/SIGNUP.gif" alt="" style="width: 300px; height: 300px;">
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, watch } from 'vue';
import axios from 'axios'
import { ref } from 'vue';
const age = ref(0)
const message = ref('')
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const gender = ref(0)
const nickname = ref(null)

const makeAccount = function(){
  console.log(username.value)
          axios({
            url: 'http://127.0.0.1:8000/accounts/signup/',
            method:'post',
            data: {
              username : username.value,
              nickname : nickname.value,
              age : age.value,
              password1 : password1.value,
              password2 : password2.value,
              gender : gender.value,
            }
          })
          .then(
            data => {
              username.value = null
              nickname.value = null
              age.value = 0
              password1.value = null
              password2.value = null
              const SIGNUPModal = document.getElementById("SIGNUP-modal")
              SIGNUPModal.style.display = "none"
              message.value = ''
            }
          )
          .catch(err => {
            const errCode = err.response.data
            for( const code in errCode){
              message.value = errCode[code]
            }
          })
        }



const ageWarning = function(){
      if(age.value>151){
        age.value = 150
        message.value = "나이 제한 150살까지입니다."
      }
      else if(age.value <0){
        age.value = 1
        message.value = "나이 제한 음수는 들어갈 수 없습니다."
      }
      else{
        message.value = ''
      }
    }
  onMounted(()=>{
    const SIGNUPModal = document.getElementById("SIGNUP-modal");
        const openSIGNUPModalBtn = document.getElementById("open-SIGNUP-modal");
        const closeSIGNUPModalBtn = document.getElementById("close-SIGNUP-modal");
        // 모달창 열기
        openSIGNUPModalBtn.addEventListener("click", (target) => {
          target.preventDefault()
        SIGNUPModal.style.display = "block";
        });
        // 모달창 닫기
        closeSIGNUPModalBtn.addEventListener("click", () => {
        SIGNUPModal.style.display = "none";
        });
        
  })
        
</script>

<style scoped>
        #SIGNUP-modal {
        position: fixed;
        z-index: 99999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
        display: none;
        }
        .SIGNUP-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 900px;
        height: 500px;
        border-radius: 15px;
        }
        .close-SIGNUP-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-SIGNUP-modal:hover,
        .close-SIGNUP-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }
        input:focus{
            outline: none;
            border: 1px solid deepskyblue;
            box-shadow: 0 0 10px deepskyblue;
        }
        input:hover{
          outline: none;
            border: 1px solid deepskyblue;
            box-shadow: 0 0 10px deepskyblue;
        }
        Button:hover{
          outline: none;
            border: 1px solid deepskyblue;
            box-shadow: 0 0 10px deepskyblue;
        }
</style>