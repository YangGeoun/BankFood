<template>
  <div class="animate__animated animate__fadeIn">
    
    <div class="d-flex justify-content-center " style="margin-top: 10px;
    
    ">
      <img src="@/assets/MYARTICLE.png" alt="" style="height: 200px; width: 200px;">
      <!-- <a href="https://www.flaticon.com/free-icons/article" title="article icons">Article icons created by Vectorslab - Flaticon</a> -->
    </div>
    <hr>
    <h4 style="margin-left: 30px; margin-top: 20px;
    font-weight: 550; color: darkslategray;
    ">My Articles</h4>
    <div class="d-flex justify-content-center" style="margin-top: 20px;;">
      <table class="type09 " style="border: 1px solid skyblue;
      box-shadow: 0 0 5px darkblue;      
      " v-if="article.length>0"
      >
        <thead>
          <tr>
            <th scope="cols">타이틀</th>
            <th scope="cols">내용</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in articleList">
            <th scope="row">{{item.title}}</th>
            <td>{{item.content}}</td>
          </tr>
        </tbody>
    </table>
  </div>
    <div class="d-flex justify-content-center" style="margin: 10px">
      <img src="@/assets/PREV.png" alt="" style="width: 30px; cursor: pointer;"
      @click="()=>{prevPage()
    
      
      }"
      >
      <span style="border-radius: 50%; border: 2px solid; width: 30px; text-align: center; font-weight: bold;
      margin-left: 8px; margin-right: 8px;
      ">{{ nowPage }}</span>
      <img src="@/assets/NEXT.png" alt="" style="width: 30px; cursor: pointer;" 
      @click="()=>{nextPage()
      
      

      }"

      >
    </div>
  </div>
  
</template>z

<script setup>
import { storeToRefs } from 'pinia';
import { ref, computed, onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import axios from 'axios';
const store = useCounterStore()
console.log(store.userInfo)
const flipAnimate = ref({
  "animate__bounce" : true,
  "animate__animated" : true,
})
const articlesPerPage = 7;

const article = ref([

])
const nowPage = ref(1)
const endPage = Math.ceil(article.value.length/articlesPerPage)

const nextPage = function(){
  if(nowPage.value<endPage){
    nowPage.value+=1
  }
}
const prevPage = function(){
  if (nowPage.value>1){
    nowPage.value-=1
  }
}
const startPoint = computed(()=>{
  return (nowPage.value-1)*articlesPerPage
})
const endPoint = computed(()=>{
  const temp = (nowPage.value*7)
  if(temp>=article.value.length){
    return article.value.length
  }
  else{
    return temp
  }
})
const articleList = computed(()=>{
  return article.value.slice(startPoint.value,endPoint.value)
})

onMounted(()=>{
  axios({
    method : 'get',
    url : 'http://127.0.0.1:8000/accounts/userarticles/',
    headers : {
      Authorization : `Token ${store.token}`
    }
  })
  .then(res=>{
    article.value = res.data
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