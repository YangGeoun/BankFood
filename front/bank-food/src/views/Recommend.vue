<template>
  <div style="height: 3000px;">
  <div :style="maxWidth" class="mt-3 px-5 py-3 mx-auto" style="background-color: white; border-radius: 10px;" >
    <div class="row" style="margin-top: 25px;">


      <div class="col-2" >
        <h2 style="font-weight: bold;">내 정보</h2>
        <table class="type09 " style="width: 100%; margin-top: 20px; border: 1px solid skyblue; 
          box-shadow: 0 0 5px darkblue;" v-if="recommends?.length>0"
          >
            <tbody>
              <tr>
                <th scope="row">나이</th>
                <td style="font-weight: bold;">{{store.userInfo.age}}</td>
              </tr>
              <tr>
                <th scope="row">월급</th>
                <td style="font-weight: bold;">{{store.userInfo.salary}}</td>
              </tr>
              <tr>
                <th scope="row">나이</th>
                <td style="font-weight: bold;">{{store.userInfo.money}}</td>
              </tr>
            </tbody>
        </table>
        <button  class="btn mt-2" style="width: 100%; height: 100px; font-weight: bold; font-size: 25px; border: 1px solid skyblue; box-shadow: 0 0 5px darkblue;"
          @click.prevent="()=>{router.push({name:'compare'})}" >예금 적금 상품 <br> 가입하러가기</button>
      </div>
      <div class="col-5">
        <h2 style="font-weight: bold;">내가 가입한 상품</h2>
        <div class="d-flex justify-content-center" style="margin-top: 20px;">
          <table class="type09 " style="width: 100%; border: 1px solid skyblue; 
            box-shadow: 0 0 5px darkblue;" v-if="store.userBank.length>0"
            >
              <thead>
                <tr>
                  <th scope="cols">은행</th>
                  <th scope="cols">상품명</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in myBank">
                  <th scope="row">{{item.kor_co_nm}}</th>
                  <td style="font-weight: bold;">{{item.fin_prdt_nm}}</td>
                </tr>
              </tbody>
          </table>
        </div>
        <button class="btn mt-2" style="width: 100%; font-weight: bold; color: black; 
        box-shadow: 3px 1px 5px darkblue; font-size: 20px;
        " @click.prevent="showChart1">내 상품 그래프 보기</button>
      </div>


      <div class="col-5">
        <h2 style="font-weight: bold;">나와 비슷한 사람들이 가입한 상품</h2>
        <div class="d-flex justify-content-center" style="margin-top: 20px;">
          <table class="type09 " style="width: 100%; border: 1px solid skyblue; 
            box-shadow: 0 0 5px darkblue;" v-if="recommends?.length>0"
            >
              <thead>
                <tr>
                  <th scope="cols">은행</th>
                  <th scope="cols">상품명</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in recommends">
                  <th scope="row">{{item.kor_co_nm}}</th>
                  <td style="font-weight: bold;">{{item.fin_prdt_nm}}</td>
                </tr>
              </tbody>
          </table>
        </div>
        <button class="btn mt-2" style="width: 100%;font-weight: bold; font-size: 20px; border: 1px solid skyblue; box-shadow: 0 0 5px darkblue;"
          @click.prevent="showChart2">추천 상품 그래프 보기</button>
      </div>



    </div>
    <div >
      
      <Chart 
      v-if="isShow1"
      :name="chartname1"
      :data1="chartdata1"
      :data2="chartdata2"
      />

      <Chart 
      v-if="isShow2"
      :name="chartname2"
      :data1="chartdata3"
      :data2="chartdata4"
      />
    </div>
  </div>
  </div>
</template>

<script setup>
  import Chart from '../components/Chart.vue';
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useCounterStore } from '../stores/counter';
  import { useRouter } from 'vue-router';
  
  const router = useRouter()
  const store = useCounterStore()

  const maxWidth = ref({
    width : `${(screen.availWidth/12)*10}px`
  })

  setTimeout(() => {
    isShow1.value = true
  }, 100);

  const isShow1 = ref(false)
  const isShow2 = ref(false)
  const myBank = ref([])
  const chartname1 = ref([])
  const chartname2 = ref([])
  const chartdata1 = ref([])
  const chartdata2 = ref([])
  const chartdata3 = ref([])
  const chartdata4 = ref([])
  const recommends = ref([])
  let sum1 = 0
  let sum2 = 0

  const showChart1 = function () {
    isShow2.value = false
    isShow1.value = true
  }
  const showChart2 = function () {
    isShow1.value = false
    isShow2.value = true
  }

  onMounted(()=>{
    axios({
      url: 'http://127.0.0.1:8000/finances/recommend/',
      method : 'get',
      headers : {
        Authorization : `Token ${store.token}`
      }
    })
    .then(res =>{
      console.log(res)
      recommends.value = res.data
      for (const product2 of res.data) {
        chartname2.value.push(product2.fin_prdt_nm)
        sum1 = 0
        sum2 = 0
        if (product2.depositoption_set){
        for (const opt of product2.depositoption_set) {
          sum1 += opt.intr_rate2
          sum2 += opt.intr_rate
        chartdata3.value.push(sum1/product2.depositoption_set.length)
        chartdata4.value.push(sum2/product2.depositoption_set.length)

        }} else {
          for (const opt of product2.savingoption_set) {
          sum1 += opt.intr_rate2
          sum2 += opt.intr_rate
        chartdata3.value.push(sum1/product2.savingoption_set.length)
        chartdata4.value.push(sum2/product2.savingoption_set.length)
        }}
        
      }
      chartname2.value.push('평균')
      sum1 = 0
      chartdata3.value.forEach((el)=>{
        sum1 += el
      })
      chartdata3.value.push(sum1/chartdata3.value.length)
      sum1 = 0
      chartdata4.value.forEach((el)=>{
        sum1 += el
      })
      chartdata4.value.push(sum1/chartdata4.value.length)
    })
    

    axios({
      url: 'http://127.0.0.1:8000/accounts/userproducts/',
      method : 'get',
      headers : {
        Authorization : `Token ${store.token}`
      }
    })
    .then(res =>{
      console.log(res)
      store.userBank = res.data
      myBank.value = store.userBank
      for (const product of res.data)
        if ('depositoption_set' in product) {
          chartname1.value.push(product.fin_prdt_nm)
          sum1 = 0
          sum2 = 0
          for (const opt of product.depositoption_set) {
            sum1 += opt.intr_rate2
            sum2 += opt.intr_rate
          }
          chartdata1.value.push(sum1/product.depositoption_set.length)
          chartdata2.value.push(sum2/product.depositoption_set.length)
        } else {
          chartname1.value.push(product.fin_prdt_nm)
          sum1 = 0
          sum2 = 0
          for (const opt of product.savingoption_set) {
            sum1 += opt.intr_rate2
            sum2 += opt.intr_rate
          }
          chartdata1.value.push(sum1/product.savingoption_set.length)
          chartdata2.value.push(sum2/product.savingoption_set.length)
        }
        chartname1.value.push('평균')
        sum1 = 0
        chartdata1.value.forEach((el)=>{
          sum1 += el
        })
        chartdata1.value.push(sum1/chartdata1.value.length)
        sum1 = 0
        chartdata2.value.forEach((el)=>{
          sum1 += el
        })
        chartdata2.value.push(sum1/chartdata2.value.length)
    })
    .catch(err =>{
      console.log(err)
    })


  })
</script>

<style scoped>
table.type09 {
  border-collapse: collapse;
  text-align: left;
  line-height: 1.15;

}
table.type09 thead th {
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  color: #369;
  border-bottom: 3px solid #036;
}
table.type09 tbody th {
  width: 150px;
  padding: 10px;
  font-weight: bold;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
  background: #f3f6f7;
}
table.type09 td {
  width: 350px;
  padding: 10px;
  vertical-align: top;
  border-bottom: 1px solid #ccc;
}

</style>