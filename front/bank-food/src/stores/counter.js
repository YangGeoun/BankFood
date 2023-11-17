import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {

  // Django Server URL for axios
  const ServerURL ='http://127.0.0.1:8000/'

  //youtube 관리
  const youtube = ref([])
  //youtube DB 업데이트
  const getDjangoYoutube = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/getyoutube/`
    })
  }
  //youtube 리스트 DB에서 가져오기
  const getYoutube = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/youtube/`

    })
    .then(res=>{
      youtube.value = res.data
    })
    .catch(err=>{
      console.log(err)
    })
  }

  //news관리
  const news = ref([])
  const getDjangoNews = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/getnews/`
    })
  }
  const getNews = function(){
    axios({
      methid:'get',
      url:`${ServerURL}daily/news/`
    })
    .then(res=>{
      news.value = res.data
      console.log(news.value)
    })
  }


  return {ServerURL, youtube, news, getDjangoYoutube, getYoutube, getDjangoNews, getNews }
})
