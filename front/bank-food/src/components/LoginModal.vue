<template>
  <div>
    <button style="width: 100px; border-radius: 0px 15px 15px 0px;   font-weight: bold;" id="open-LOGIN-modal">LOGIN</button>
    <div id="LOGIN-modal">
        <div class="LOGIN-modal-content" >
          <div class="d-flex justify-content-between ">
            <h2 style="margin:0px; font-weight: bold; color: white; 
            text-shadow: -3px 0 black, 0 1px black, 1px 0 black, 0 -2px black; 
            "
            class="align-self-center"
            >LOGIN</h2>
            <span id="close-LOGIN-modal" style="font-size: 30px; cursor: pointer; margin-right: 40px;
          
            ">X</span>
          </div>  
          <hr>
          <div class="d-flex justify-content-around">
            <div style="display: inline-block; width: 510px;">
                <div class="d-flex justify-content-between" style="margin-top: 20px;">
                  <label for="id" style="font-weight: 30px; font-size: 25px;">ID :　</label>
                  <input type="text" id="id" style="border-radius: 15px; width: 300px; height: 30px; font-size: 20px; text-align: center;" v-model="username">
                </div>
                <div class="d-flex justify-content-between" style="margin-top: 20px;">
                <label for="password" style="font-weight: 30px; font-size: 25px;">password :　</label>
                <input type="password" id="password" style="border-radius: 15px; width: 300px; height: 30px; font-size: 20px; text-align: center;" v-model="password">
              </div>
              <br>
              <Button class="btn" style="border-radius: 50px; width: 500px; border: 2px solid lightgreen; font-weight: bold;"
              @click = login(username,password)
              >LOGIN</Button>
            </div>
            <div style="display: inline-block;  ">
              <img src="@/assets/LOGIN.gif" alt="" style="width: 200px; height: 200px;">
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '../stores/counter';
import axios from 'axios';

const username = ref('')
const password = ref('')
const store = useCounterStore()
const message = ref('')

  const login = function(username,password){
    axios({
      method : 'post',
      url : `http://127.0.0.1:8000/accounts/login/`,
      data : {
        username,
        password,
      }
    })
    .then(res=>{
      store.token = res.data.key
      const LOGINModal = document.getElementById("LOGIN-modal")
      LOGINModal.style.display = "none"
      axios({
        method: 'get',
        url : `http://127.0.0.1:8000/accounts/userinfo/`,
        headers : {
          Authorization : `Token ${res.data.key}`
        }
      })
      .then(userInfo =>{
        store.userInfo =  
        console.log(store.userInfo)
      })
    })
    .catch(err => {
      console.log(err)
    })
  }


onMounted(()=>{
  const LOGINModal = document.getElementById("LOGIN-modal");
  const openLOGINModalBtn = document.getElementById("open-LOGIN-modal");
  const closeLOGINModalBtn = document.getElementById("close-LOGIN-modal");
  // 모달창 열기
  openLOGINModalBtn.addEventListener("click", () => {
    LOGINModal.style.display = "block";
  });
  // 모달창 닫기
  closeLOGINModalBtn.addEventListener("click", () => {
    LOGINModal.style.display = "none";
  });
})

</script>

<style scoped>
#LOGIN-modal {
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
        .LOGIN-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 900px;
        height: 320px; 
        border-radius: 15px;
        }
        .close-LOGIN-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-LOGIN-modal:hover,
        .close-LOGIN-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }
        input:focus{
            outline: none;
            border: 1px solid lightgreen;
            box-shadow: 0 0 10px lightgreen;
        }
        input:hover{
          outline: none;
            border: 1px solid lightgreen;
            box-shadow: 0 0 10px lightgreen;
        }
        Button:hover{
          outline: none;
          
            border: 1px solid lightgreen;
            border-left: 0px;
            box-shadow: 0 0 10px lightgreen;
        }
</style>