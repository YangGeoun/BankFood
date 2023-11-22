<template>
  <div class="animate__animated animate__fadeIn">
    
    <div class="d-flex justify-content-center " style="margin-top: 30px;
    height: 100%; margin-top: 0;
    "
    >
      <img src="@/assets/MAN.png" alt="" v-if="!store.userInfo.gender" style="height: 200px; width: 200px;
      margin-top: 15px; margin-bottom: 15px;
      ">
      <img src="@/assets/WOMAN.png" alt="" v-if="store.userInfo.gender" style="height: 200px; width: 200px;
      margin-top: 15px; margin-bottom: 15px;
      ">
    </div>
    <hr style="margin-top: 0;">

    <h4 style="margin-left: 40px; font-weight: 550; color: darkslategray; margin-bottom: 25px;"
      >Basic Information</h4>
    <div class="d-flex flex-column" >
        <div style="border: 1px solid black; font-weight: bold; border-radius: 10px; height: 210px; width: 50%; margin: auto;"
        class="d-flex flex-column"
        >
            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="username" style="margin-left: 10px;">아이디 : </label>
              <div>
              <input type="text" id="username" v-model="id" disabled
              style="margin-right: 10px;"
              >
              <img src="@/assets/LOCK.png" alt="" style="width: 20px; height: 20px; margin-right: 10px;"
              
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
            </div>

            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="nickname" style="margin-left: 10px;">이름 : </label>
              <div>
              <input type="text" id="nickname" v-model="name"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;"
              @click="changeInfo('nickname',name)"
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
            </div>

            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="age" style="margin-left: 10px;">나이 : </label>
              <div>
              <input type="number" id="age" v-model="age"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;"
              @click="changeInfo('age',age)"
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>  
            </div>

            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="date_joined" style="margin-left: 10px;">가입 일자 : </label>
              <div>
              <input type="text" id="date_joined" :value="metAt"
              style="margin-right: 10px;" disabled
              >
              <img src="@/assets/LOCK.png" alt="" style="width: 20px; height: 20px; cursor: auto; margin-right: 10px;">
              <!-- <a href="https://www.flaticon.com/free-icons/lock" title="lock icons">Lock icons created by Pixel perfect - Flaticon</a> -->
              </div>
            </div>

            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="E-MAIL" style="margin-left: 10px;">이메일 : </label>
              <div>
              <input type="text" id="E-MAIL" v-model="email"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;"
              @click="changeInfo('email',email)"
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
            </div>
        </div>
        <hr>
        <div class="d-flex flex-row ">
          <h4 style="margin-left: 40px; font-weight: 550; color: darkslategray">For more details...</h4>
          <img v-if="arrowflag" src="@/assets/DOWNARROW.png" alt="" style="width: 20px; height: 20px; margin-top: 5px; margin-left: 10px; cursor: pointer;"
          @click="arrowflag=!arrowflag"
          >
          <img v-else src="@/assets/UPARROW.png" alt="" style="width: 20px; height: 20px; margin-top: 5px; margin-left: 10px; cursor: pointer;"
          @click="arrowflag=!arrowflag"
          >
          
        </div>
        <div v-if="!arrowflag" style="border: 1px solid black; font-weight: bold; border-radius: 10px; height: 130px; width: 50%; margin: auto;
        margin-top: 15px;
        margin-bottom: 30px;
        "
        class="d-flex flex-column"
        >
          <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="SALARY" style="margin-left: 10px;">월 수입 : </label>
              <div>
              <input type="number" id="SALARY" v-model="salary"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;"
              @click="changeInfo('salary',salary)"
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
          </div>

          <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="money" style="margin-left: 10px;">자산 : </label>
              <div>
              <input type="number" id="money" v-model="money"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;"
              @click="changeInfo('money',money)"
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
          </div>
          <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="address" style="margin-left: 10px;">주소지 :  </label>
              <div>
              <input type="text" id="address" v-model="address"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;"
              @click="changeInfo('address',address)"
              >
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
          </div>

      </div>
      <br>
    </div>
    
  </div>
</template>

<script setup>

import { useCounterStore } from '../stores/counter';
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Swal from 'sweetalert2';


const store = useCounterStore()
const metAt = ref('')
const id = ref(store.userInfo.username)
const name = ref(store.userInfo.nickname)
const age = ref(store.userInfo.age)
const email = ref(store.userInfo.email)
const salary = ref(store.userInfo.salary)
const money = ref(store.userInfo.money)
const address = ref(store.userInfo.address)
for(let i = 0; i<10; i++){
  metAt.value += store.userInfo.date_joined[i]
}
const arrowflag = ref(true)
const changeInfo = function(key, value){
  axios({
    method : 'post',
    url : 'http://127.0.0.1:8000/accounts/userinfo/',
    data : {
      key : key,
      value : value,
      id : store.userInfo.id
    },
    headers : {
      Authorization : `Token ${store.token}`
    }
  })
  .then(userInfo =>{
    axios({
        method: 'get',
        url : `http://127.0.0.1:8000/accounts/userinfo/`,
        headers : {
          Authorization : `Token ${store.token}`
        }
      })
      .then(userInfo =>{
        store.userInfo =  userInfo.data
        Swal.fire({
          icon: "success",
          title: `수정 완료했습니다.`,
          showConfirmButton: false,
          timer: 1500
          });
      })
      })
  .catch(
    err=>{
      console.log(err)
    }

  )
}
</script>

<style scoped>

</style>