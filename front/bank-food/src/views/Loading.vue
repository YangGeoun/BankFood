<template>
    <div class="back">
    <div class="content">
        <h2
        id="first"
        class="animate__animated animate__slow"
        @click="goHome"
        >BankFood</h2>
        <h2
        id="second"
        class="animate__animated animate__slow"
        @click="goHome"
        >BankFood</h2>
    </div>
</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';
const router = useRouter()
const nav = document.querySelector('nav')

nav.style.display = 'none'
setTimeout(()=>{
    const array1 = document.querySelector('#first')
    const array2 = document.querySelector('#second')
    array1.innerHTML = "WELCOME"
    array2.innerHTML = "WELCOME"
    array1.classList.add('animate__fadeIn')
    array2.classList.add('animate__fadeIn')
    setTimeout(()=>{
    nav.style.display = 'block'
    router.push({name:'home'})  
    },3000)
},10000)



    const goHome = function(){
    const array1 = document.querySelector('#first')
    const array2 = document.querySelector('#second')
    array1.innerHTML = "WELCOME"
    array2.innerHTML = "WELCOME"
    array1.classList.add('animate__fadeIn')
    array2.classList.add('animate__fadeIn')
    setTimeout(()=>{
    nav.style.display = 'block'
    router.push({name:'home'})  
    },3000)}

    

</script>

<style scoped>
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            
        }
        .back{
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background:url(../assets/Loading.jpg);
            background-color: rgba(255, 0, 0, 0.1);
            background-size: cover;
            
        }
        .back::before {
            position: absolute;
            content: "";
            top:0px;
            left:0px;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.25);
        }
        .content{
            position: relative;
        }
        .content h2{
            position: absolute;
            color: #fff;
            transform: translate(-50%,-50%);
            font-size: 8em;
            cursor: pointer;
        }
        .content h2:nth-child(1){
            color: transparent;
            -webkit-text-stroke: 2px #03a9f4;
            cursor: pointer;

        }
        .content h2:nth-child(2){
            color: #03a9f4;
            animation: animate 4s ease-in-out infinite;
            -webkit-text-stroke: 2px #03a9f4;
            cursor: pointer;

        }
        @keyframes animate {
            0%,100%{
                clip-path: polygon(0% 45%, 15% 44%, 32% 50%,
                54% 60%, 70% 61%, 84% 59%, 100% 52%, 100% 100%, 0% 100%);
            }
            50%{
                clip-path: polygon(0% 60%, 16% 65%, 34% 66%,
                51% 62%, 67% 50%, 84% 45%, 100% 46%, 100% 100%, 0% 100%);
            }
        }
        
</style>