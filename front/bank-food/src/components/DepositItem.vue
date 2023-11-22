<template>
  <tr @click="goDetail" style="cursor: pointer;">
    <td :class="{'gray':index%2==0}">{{ deposit.dcls_month }}</td>
    <td :class="{'gray':index%2==0}">{{ deposit.kor_co_nm }}</td>
    <td :class="{'gray':index%2==0}">{{ deposit.fin_prdt_nm }}</td>
    <td :class="{'gray':index%2==0}" v-for="opt in opts">{{ opt }}</td>
  </tr>
  <tr v-if="showDetail">
    <td colspan="7">
      <div class="px-5 py-3" style="background-color: #f1f3f8; border-radius: 5px;">
        <p v-if="isDeposit">저축 금리 유형명 : {{deposit.depositoption_set[0].intr_rate_type_nm}}</p>
        <p v-else>저축 금리 유형명 : {{deposit.savingoption_set[0].intr_rate_type_nm}}</p>
        <p v-else>저축 금리 유형명 : {{deposit.savingoption_set[0].intr_rate_type_nm}}</p>
        <p>최대 한도 : {{ deposit.max_limit }}</p>
        <p>가입 방법 : {{ deposit.join_way }}</p>
        <p>가입 제한 : {{ deposit.join_deny }}</p>
        <p>우대 조건 : {{ deposit.spcl_cnd }}</p>
        <p>기타 유의사항 : {{ deposit.etc_note }}</p>
        <button class="btn btn-info fw-bold" style="width: 100px; color: white;" @click="join"> 상품 가입 </button>
      </div>
    </td>
    
  </tr>
</template>


<script setup>
import { ref } from 'vue'
import { RouterLink,useRouter } from 'vue-router'
import { useCounterStore } from '../stores/counter';
import axios from 'axios';
import Swal from 'sweetalert2';

const store = useCounterStore()
const router = useRouter()
const showDetail = ref(false)
// console.log(router)
const goDetail = function(){
  if (showDetail.value) {
    showDetail.value = false
  } else {
    showDetail.value =true
  }
}

const props = defineProps({
  deposit:Object,
  index:Number,
  isDeposit:Boolean
})

const join = function () {
  Swal.fire({
  title: "Are you sure?",
  text: "해당 상품에 가입하시겠습니까?",
  icon: "warning",
  showCancelButton: true,
  confirmButtonColor: "#3085d6",
  cancelButtonColor: "#d33",
  confirmButtonText: "Yes !!"
}).then((result) => {
  if (result.isConfirmed) {
    axios({
    url : `${store.ServerURL}finances/deposit/join/`,
    data : {
      'fin_prdt_nm':props.deposit.fin_prdt_nm,
    },
    method : 'POST',
    headers : {
      Authorization:`Token ${store.token}`
    }
  })
  .then ((res)=>{
    Swal.fire({
          icon: "success",
          title: `해당 상품에 가입 완료했습니다..`,
          showConfirmButton: false,
          timer: 1500
          });
  })
  .catch ((err)=>{
    console.log(err)
  })
  }
});

}

const opts = ref(['-','-','-','-'])
if (props.isDeposit){
for ( const opt of props.deposit.depositoption_set) {
  if (opt.save_trm == 6) {
    opts.value[0] = opt.intr_rate2
  }
  if (opt.save_trm == 12) {
    opts.value[1] = opt.intr_rate2
  }
  if (opt.save_trm == 24) {
    opts.value[2] = opt.intr_rate2
  }
  if (opt.save_trm == 36) {
    opts.value[3] = opt.intr_rate2
  }
}} else {
  for ( const opt of props.deposit.savingoption_set) {
  if (opt.save_trm == 6) {
    opts.value[0] = opt.intr_rate2
  }
  if (opt.save_trm == 12) {
    opts.value[1] = opt.intr_rate2
  }
  if (opt.save_trm == 24) {
    opts.value[2] = opt.intr_rate2
  }
  if (opt.save_trm == 36) {
    opts.value[3] = opt.intr_rate2
  }
}
}
</script>

<style scoped> 
  .gray {
    background-color: rgb(245, 245, 245);
  }
</style>