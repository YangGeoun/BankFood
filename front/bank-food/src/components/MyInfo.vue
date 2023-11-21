<template>
  <div>
    <div class="d-flex justify-content-center " style="margin-top: 30px;">
      <img src="@/assets/MAN.png" alt="" v-if="!store.userInfo.gender" style="height: 200px; width: 200px;">
      <img src="@/assets/WOMAN.png" alt="" v-if="store.userInfo.gender" style="height: 200px; width: 200px;">
    </div>
    <div class="d-flex flex-column" >
        <br>
        <hr>
    </div>
    
  </div>
</template>

<script setup>
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()

</script>

<style scoped>

</style>