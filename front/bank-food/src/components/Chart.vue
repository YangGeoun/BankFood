<template>
  <div style="margin: 20px;">
    <canvas id="myChart"></canvas>
  </div>
</template>

<script setup lang="ts">
import Chart from 'chart.js/auto';
import { ref,onMounted } from 'vue';
const props = defineProps({
  name:Array,
  data1:Array,
  data2:Array
})



  const data = {
    labels: props.name,
    datasets: [
      {
      label: '저축 금리',
      backgroundColor: 'rgb(74, 136, 219, 0.5)',
      borderColor: 'rgb(74, 136, 219)',
      data: props.data2,
      tension: 0.3,
      fill: true,
      },
      {
      label: '최고 우대 금리',
      backgroundColor: 'rgb(137, 178, 233, 0.5)',
      borderColor: 'rgb(137, 178, 233)',
      data: props.data1,
      tension: 0.3,
      fill: true
      },
      
  ]
  };


  const config = {
    type: 'line',
    data: data,
    options: {
      scales: {
        y : {
          beginAtZero: true,
          max:6
        }
      }
    }
  };


  onMounted(()=>{
    const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );

  })

</script>

<style scoped>

</style>