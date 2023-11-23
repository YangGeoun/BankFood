import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  // 로그인 처리
  const userInfo = ref({})
  const userBank = ref([])
  const token = ref(null)
  const quest = ref('구미')
  const mapType = ref(1)
  const quizes = ref([
    {question: '기업 주식을 갖고 있는 주주들이 회사가 올린 이익의 일부를 나눠 받는 것은?',
    selections:['증자', '감자', '상장', '배당'],
    anser: 4
    },
    {question: '예적금이나 대출 이자를 계산할 때 원금에 대한 이자뿐 아니라 이자에 대한 이자도 함께 계산하는 방식은?',
    selections:['복리', '단리', '고정금리', '변동금리'],
    anser: 1
    },
    {question: '다음 중 나라 살림의 건전성과 지속 가능성을 파악하는 데 활용할 수 있는 지표는?',
    selections:['서비스수지', '경상수지', '이전소득수지', '관리재정수지'],
    anser: 4
    },
    {question: '중앙은행이 통화를 시중에 직접 공급해 신용경색을 해소하고 경기를 부양시키는 통화정책은?',
    selections:['테이퍼링 ', '양적완화', '턴어라운드 ', '리디노미네이션'],
    anser: 2
    },
    {question: '예비 창업자나 초기 기업에 투자하는 것으로, 기업 가치가 올라가고 나서 차익을 회수하는 이 방식은?',
    selections:['대체투자 ', '분산투자', '역외투자 ', '엔젤투자'],
    anser: 4
    },
    {question: '불황기에 ‘작은 사치’를 누릴 수 있는 소비재가 잘 팔리는 현상을 가리키는 말은?',
    selections:['립스틱 효과', '밴드왜건 효과', '피구 효과', '메기 효과'],
    anser: 1
    },
    {question: '재택근무, 자율 출퇴근 등과 같이 개인 여건에 따라 근무시간과 형태를 조절할 수 있는 제도를 통칭하는 말은?',
    selections:['골디락스', '유연근무제', '임금피크제 ', '배당'],
    anser: 2
    },
    {question: '자국 수출을 늘리기 위해 정부가 인위적으로 외환시장에 개입해 자국 통화 가치를 낮추는 국가를 일컫는 말은?',
    selections:['조세피난처', '개발도상국', 'G7', '환율조작국'],
    anser: 4
    },
    {question: '병원에서 환자가 부담한 의료비 중 건강보험이 적용되지 않는 비급여 진료비와 본인부담금을 보상해주는 보험상품은?',
    selections:['실손보험 ', '변액보험', '재보험 ', '종신보험'],
    anser: 4
    },
    {question: '외환 유동성 위기에 대비할 목적으로 국가 간에 체결하는 계약을 가리키는 용어는?',
    selections:['재정거래 ', '차입공매도', '신용융자 ', '통화스와프'],
    anser: 1
    },
  ])
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
    })
  }

  return {userBank, userInfo ,token, ServerURL, youtube, news, quest, quizes, mapType,exchange,getDjangoExchange,getExchange ,getDjangoYoutube, getYoutube, getDjangoNews, getNews, changeQuest,  }
},{persist : true})
