<template>
  <div>
    <div class="d-flex justify-content-center " style="margin-top: 30px;">
      <img src="@/assets/MYARTICLE.png" alt="" style="height: 200px; width: 200px;">
      <!-- <a href="https://www.flaticon.com/free-icons/article" title="article icons">Article icons created by Vectorslab - Flaticon</a> -->
    </div>
    <hr>

    <div v-for="item in displayedArticles" :key="item.title">
      <p>{{ item.title }} - {{ item.content }}</p>
    </div>
    <button @click="prevPage" :disabled="nowPage === 1">prev</button>
    <p>{{ nowPage }}</p>
    <button @click="nextPage" :disabled="nowPage === endPage">next</button>
    
  </div>
  
</template>

<script setup>
import { ref, computed } from 'vue';
const articlesPerPage = 7;
const article = [
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
]
const nowPage = ref(1);
const endPage = computed(() => Math.ceil(article.length / articlesPerPage));

const currentMark = computed(() => (nowPage.value - 1) * articlesPerPage);

const displayedArticles = computed(() =>
  article.slice(currentMark.value, currentMark.value + articlesPerPage)
);

const nextPage = function () {
  if (nowPage.value < endPage.value) {
    nowPage.value += 1;
  }
};

const prevPage = function () {
  if (nowPage.value > 1) {
    nowPage.value -= 1;
  }
};
</script>

<style scoped>

</style>