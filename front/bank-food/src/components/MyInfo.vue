<template>
  <div>
    
    <div class="d-flex justify-content-center " style="margin-top: 30px;">
      <img src="@/assets/MAN.png" alt="" v-if="!store.userInfo.gender" style="height: 200px; width: 200px;">
      <img src="@/assets/WOMAN.png" alt="" v-if="store.userInfo.gender" style="height: 200px; width: 200px;">
    </div>
    <hr>
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
              <input type="text" id="username" :value="store.userInfo.username"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
            </div>

            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="nickname" style="margin-left: 10px;">이름 : </label>
              <div>
              <input type="text" id="nickname" :value="store.userInfo.nickname"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
            </div>

            <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="age" style="margin-left: 10px;">나이 : </label>
              <div>
              <input type="text" id="age" :value="store.userInfo.age"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
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
              <input type="text" id="E-MAIL" :value="store.userInfo.email"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
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
              <input type="text" id="SALARY" :value="store.userInfo.salary"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
          </div>

          <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="money" style="margin-left: 10px;">자산 : </label>
              <div>
              <input type="text" id="money" :value="store.userInfo.money"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
              <!-- <a href="https://www.flaticon.com/free-icons/pencil" title="pencil icons">Pencil icons created by riajulislam - Flaticon</a> -->
              </div>
              
          </div>
          <div class="d-flex justify-content-between align-items-center"
            style="margin-top: 10px;"
            > 
              <label for="address" style="margin-left: 10px;">주소지 :  </label>
              <div>
              <input type="text" id="address" :value="store.userInfo.address"
              style="margin-right: 10px;"
              >
              <img src="@/assets/EDIT.png" alt="" style="width: 20px; height: 20px; cursor: pointer; margin-right: 10px;">
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
import { ref } from 'vue';
const store = useCounterStore()
const metAt = ref('')
for(let i = 0; i<10; i++){
  metAt.value += store.userInfo.date_joined[i]
}
const arrowflag = ref(true)
</script>

<style scoped>

</style>