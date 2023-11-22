<template>
  <div>
  <div class="sub_bg" style="margin-bottom: 80px;">
    <h2 style="font-weight: bold; text-shadow: 1px 1px 2px black; ">소통 게시판 
      <span style="margin-top: 8px;">여러 상품에 대해 이야기 해보세요</span></h2>
  </div>
  <div :style="maxWidth" class="px-5 py-3 mx-auto" style="background-color: white; margin-top: 20px; border-radius: 10px;">
  <img src="@/assets/PLUS.png" alt="" style="width: 30px; height: 30px; margin-left: 95%; cursor: pointer;"
  id="open-post-modal"
  >
  <table class="table table-hover">
    <thead>
      <tr>
        <th style="padding-top: 0px;">작성자</th>
        <th style="padding-top: 0px;">제목</th>
        <th style="padding-top: 0px;">작성일자</th>
        <th style="padding-top: 0px;">수정일자</th>
      </tr>  
    </thead>
    <tbody>
      <ArticleItem v-for="article in articleList" :key="article"
      :article="article"
      />
    </tbody>
  </table>



  <!-- 모달창 -->
  <div id="post-modal">
    <div class="post-modal-content">
        <div class="d-flex justify-content-between">
            <h2 style="margin:0px; margin-bottom: 20px; margin-left: 15px; font-weight: bold;">글 작성</h2>
            <span id="close-post-modal" style="font-size: 30px; cursor: pointer; margin-right: 30px;">X</span>
        </div>
        <div>
            <label for="post-input1"
            style="font-weight: bold; font-size: 20px; margin-right: 10px;"
            >제목 :</label>
            <input type="text" id="post-input1" style="border-radius: 15px; width: 500px; height: 30px; font-size: 20px;    
            margin-top: 5px; " v-model="title">
        </div>
        <div class="d-flex ">
            <div for="post-input2"
            style="font-weight: bold; font-size: 20px; margin-top: 20px; display: block; margin-right: 10px; width: 52.28px;"
            >내용 :</div>
            <textarea type="text" v-model="content" id="post-input2" style="
            border-radius: 15px; width: 500px; height: 300px; font-size: 20px; border: 2px solid; margin-top: 20px
            ;"></textarea>
        </div>
        <button id="close-post-modal-2" style="width: 500px; margin-left: 60px; margin-top: 20px; border-radius: 15px;
            font-weight: bold; background-color: skyblue; box-shadow: 1px 1px 1px skyblue; border: skyblue;
            " @click="writeArticle();"
            >submit</button>
      </div>
    </div>
    <!-- 모달창 끝 -->
    <div class="d-flex" style="margin-left: 388px; margin-top: 20px;">
      <img src="@/assets/PREV.png" alt="" style="width: 30px; cursor: pointer;"
        @click="()=>{prevPage()
        }">
        <span style="border-radius: 50%; border: 2px solid; width: 30px; height: 30px; text-align: center; font-weight: bold;
        margin-left: 8px; margin-right: 8px;
        ">{{ nowPage }}</span>
        <img src="@/assets/NEXT.png" alt="" style="width: 30px; cursor: pointer;" 
        @click="()=>{nextPage()
        }">
      </div>
    </div>
    <br>
    <br>
</div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import ArticleItem from '../components/ArticleItem.vue';
import axios from 'axios';
import { useCounterStore } from '../stores/counter';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useCounterStore()
const title = ref('')
const content = ref('')
const maxWidth = ref({
  width : `${(screen.availWidth/12)*8}px`
})

const writeArticle = function(){
  axios({
    method:'post',
    url:'http://127.0.0.1:8000/articles/',
    data: {
      title: title.value,
      content : content.value
    },
    headers : {
      Authorization : `Token ${store.token}`
    }
  })
  .then(location.reload())
}

const articlesPerPage = 7;
const nowPage = ref(1)
const endPage = computed(()=>{
  return Math.ceil(articles.value.length/articlesPerPage)
})
const nextPage = function(){
  if(nowPage.value<endPage.value){
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
  if(temp>=articles.value.length){
    return articles.value.length
  }
  else{
    return temp
  }
})
const articleList = computed(()=>{
  return articles.value.slice(startPoint.value,endPoint.value)
})
const articles = ref([])
onMounted(()=>{
  axios({
    method: 'get',
    url : 'http://127.0.0.1:8000/articles/',
  })
  .then(res => {
    articles.value = res.data
  })

  // 모달
  const postModal = document.getElementById("post-modal");
  const openPostModalBtn = document.getElementById("open-post-modal");
  const closePostModalBtn = document.getElementById("close-post-modal");
  const closePostModalBtn_2 = document.getElementById("close-post-modal-2");
  // 모달창 열기
  openPostModalBtn.addEventListener("click", () => {
  postModal.style.display = "block";
  });
  // 모달창 닫기
  closePostModalBtn.addEventListener("click", () => {
  postModal.style.display = "none";
  });
  closePostModalBtn_2.addEventListener("click",()=>{
  postModal.style.display = "none";
  })
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


#post-modal {
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.4);
        display: none;
        }
        .post-modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 650px;
        border-radius: 15px;
        }
        .close-post-modal {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        }
        .close-post-modal:hover,
        .close-post-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        }
        /* #post-input1:focus{
            outline: none;
            border: 1px solid greenyellow;
            box-shadow: 0 0 10px greenyellow;
        }
        #post-input2:focus{
            outline: none;
            border: 1px solid greenyellow;
            box-shadow: 0 0 10px greenyellow;
        } */

</style>