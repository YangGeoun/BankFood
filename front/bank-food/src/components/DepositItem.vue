<template>
  <tr @click="goDetail">
    <td>{{ deposit.dcls_month }}</td>
    <td>{{ deposit.kor_co_nm }}</td>
    <td>{{ deposit.fin_prdt_nm }}</td>
    <td v-for="opt in opts">{{ opt }}</td>
  </tr>
</template>


<script setup>
import { ref } from 'vue'
import { RouterLink,useRouter } from 'vue-router'

const router = useRouter()
// console.log(router)
const goDetail = function(){
  router.push({name:'depositdetailView',params:{id:props.deposit.id}})
}

const props = defineProps({
  deposit:Object
})

const opts = ref(['-','-','-','-'])
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
}

</script>

<style scoped> 

</style>