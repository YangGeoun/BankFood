import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const quest = ref('구미')
  const mapType = ref(1)
  // Django Server URL for axios
  const ServerURL ='http://127.0.0.1:8000/'
  const changeQuest = function(value){
    quest.value = value
  }
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
    })
  }

  const exchange = ref([])
  const getDjangoExchange = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/getexchange`
    })
  }
  const getExchange = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/exchange`
    })
    .then(res=>{
      exchange.value = res.data
      console.log(exchange.value)
    })
  }

  return {ServerURL, youtube, news, quest, mapType,exchange,getDjangoExchange,getExchange ,getDjangoYoutube, getYoutube, getDjangoNews, getNews, changeQuest }
},{persist : true})
