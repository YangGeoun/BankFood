<template>
  <div>
  <div class="sub_bg">
    <h2 style="font-weight: bold; text-shadow: 1px 1px 2px black;">소통 게시판 
      <span>여러 상품에 대해 이야기 해보세요</span></h2>
  </div>
  <div :style="maxWidth" class="px-5 py-3 mx-auto" style="background-color: white; margin-top: 20px; border-radius: 10px;">
  <table class="table table-hover">
    <thead>
      <tr>
        <th>작성자</th>
        <th>제목</th>
        <th>내용</th>
        <th>작성일자</th>
        <th>좋아요</th>
      </tr>  
    </thead>
    <tbody>
      
    </tbody>
  </table>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue';

const maxWidth = ref({
  width : `${(screen.availWidth/12)*8}px`
})
</script>

<style scoped>

.sub_bg{
  width: 100%;
  height: 300px;
  background: url('../assets/BACKGROUND.jpg') 0 0% no-repeat;
  background-size: 100%;
  -webkit-animation: animate_background 10s infinite;
  animation: animate_background 10s infinite;
}
.sub_bg h2 {
  color: #fff;
  font-size: 40px;
  text-align: center;
  font-weight: 500;
  padding-top: 100px;
}
.sub_bg h2 span {
  display: block;
  font-size: 20px;
}

@-webkit-keyframes animate_background {
  0% {background-position: 0% 0%}
  50% {background-position: 0% 100%}
  100% {background-position: 0% 0%}

}
@keyframes animate_background{
  0%   {background-position:0% 0%}
  50%  {background-position:0% 100%;}
  100%  {background-position:0% 0%;}		  
}


</style>