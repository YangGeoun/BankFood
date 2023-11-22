<template>
  <div>
    
    <div class="d-flex justify-content-center " style="margin-top: 10px;">
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
      "
      :class="flipAnimate"
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
      timeFunc()
      
      }"
      >
      <span style="border-radius: 50%; border: 2px solid; width: 30px; text-align: center; font-weight: bold;
      margin-left: 8px; margin-right: 8px;
      ">{{ nowPage }}</span>
      <img src="@/assets/NEXT.png" alt="" style="width: 30px; cursor: pointer;" 
      @click="()=>{nextPage()
      
      timeFunc()

      }"

      >
    </div>
  </div>
  
</template>z

<script setup>
import { ref, computed } from 'vue';

const flipAnimate = ref({
  "animate__bounce" : true,
  "animate__animated" : true,
})
const articlesPerPage = 7;
const article = ref([
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목2', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목5', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
  {title : '제목', content : '내용'},
])
const nowPage = ref(1)
const endPage = Math.ceil(article.value.length/articlesPerPage)
const timeFunc = function(){
  flipAnimate.value.animate__bounce = false
  flipAnimate.value.animate__animated = false

  setTimeout(()=>{
      flipAnimate.value.animate__bounce = true
      flipAnimate.value.animate__animated = true
      },10)
}
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