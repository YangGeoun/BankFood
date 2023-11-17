import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {

  // Django Server URL for axios
  const ServerURL ='http://127.0.0.1:8000/'
  const youtube = ref([])
  const getDjangoYoutube = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/getyoutube/`
    })
  }
  const getYoutube = function(){
    axios({
      method:'get',
      url:`${ServerURL}daily/youtube/`

    })
    .then(res=>{
      console.log(res.data)
      // console.log(youtube.value)
      youtube.value = res.data
    })
    .catch(err=>{
      console.log(err)
    })

  }
  return {ServerURL, youtube, getDjangoYoutube, getYoutube }
})
