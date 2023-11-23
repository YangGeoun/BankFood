<template>
    <tr  :id="`open-detail-modal${idx}`">
        <td>{{ article.author_name }}</td>
        <td>{{ article.title }}</td>
        <td>{{ createdat }}</td>
        <td>{{ updatedat }}</td>

                    <!-- 모달창 -->
            <div :id="`detail-modal${idx}`"
            style="position: fixed; z-index: 1; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0, 0, 0, 0.4); display: none;">
                <div :class="`detail-modal-content${idx}`"
                style="background-color: #fefefe; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 650px;
                overflow: scroll; height: 600px;
                ">
                    <div class="d-flex justify-content-between">
                        <h2 style="margin:0px; margin-bottom: 20px; margin-left: 15px; font-weight: bold;">{{article.author_name}}님의 글</h2>
                        <span :id="`close-detail-modal${idx}`" style="font-size: 30px; cursor: pointer; margin-right: 30px; float: right; font-size: 28px; font-weight: bold;
                        ">X</span>
                    </div>
                    <div>
                        <label for="detail-input1"
                        style="font-weight: bold; font-size: 20px; margin-right: 10px;"
                        >제목 :</label>
                        <input type="text" :id="`detail-input1${idx}`" style="border-radius: 15px; width: 500px; height: 30px; font-size: 20px;  text-align:center; 
                        margin-top: 5px; " v-model="tempInput1" disabled>
                    </div>
                    <div class="d-flex ">
                        <div for="detail-input2"
                        style="font-weight: bold; font-size: 20px; margin-top: 20px; display: block; margin-right: 10px; width: 52.28px;"
                        >내용 :</div>
                        <textarea type="text"  :id="`detail-input2${idx}`" style="
                        border-radius: 15px; width: 500px; height: 300px; font-size: 20px; border: 2px solid; margin-top: 20px; text-align: center
                        " v-model="tempInput2" disabled></textarea>
                    </div>
                    <div class="d-flex justify-content-between" >
                    <div>
                    <img  :id="`edit${idx}`" src="@/assets/EDIT2.png" alt="" style="width: 30px; z-index: 999999; cursor: pointer;"
                    
                    >
                    <button :id="`confirmEdit${idx}`" style="display: none; width: 500px; border-radius: 15px; background-color: whitesmoke; margin-top: 10px;
                    ">수정완료</button>
                        <!-- <a href="https://www.flaticon.com/free-icons/edit" title="edit icons">Edit icons created by Pixel perfect - Flaticon</a> -->
                    </div>
                        <div>
                    <img src="@/assets/DELETE.png" style="width: 30px;height: 33px;margin-top: 1px;  cursor: pointer;"
                    @click="deleteArticle"
                    >
                        <!-- <a href="https://www.flaticon.com/free-icons/uninstall" title="uninstall icons">Uninstall icons created by Tanah Basah - Flaticon</a> -->
                    </div>
                </div>
                    <div  style="border: 1px solid whitesmoke; border-radius: 15px; margin-top: 5px; box-shadow: 1px 1px 1px whitesmoke;">                        
                        <div class="d-flex align-items-center " style="margin-top: 10px;">
                        <div 
                        style="font-weight: bold; font-size: 20px; display: block; width: 53px; margin-right: 10px;"
                        >댓글 :</div> 
                        <input type="text" id="Comment" style=" width: 400px; height: 30px; font-size: 15px; text-align:center; 
                        margin-top: 5px; " v-model="commentWrite">
                        <button style="border-radius: 15px; margin-left: 20px; width: 80px; background-color: white; font-weight: bold;"
                        @click="write"
                        >작성</button>
                        </div>
                    </div>
                    <div v-for="comment in commentList" style="border: 1px solid whitesmoke; border-radius: 15px; margin-top: 5px; box-shadow: 1px 1px 1px whitesmoke;">

                        <div class="d-flex align-items-center " style="margin-top: 10px; ">
                            <div 
                            style=" display: block; margin-right: 10px; font-weight: bold; font-size: 20px;"
                            >{{ comment.author_name }} : </div>
                            <input type="text" id="Comment" style=" width: 400px; height: 30px; font-size: 15px; text-align:center; 
                            margin-top: 5px; " :value="comment.content" disabled>
                            <img src="@/assets/DELETE.png" style="width: 30px; height: 33px; margin-left: 30px; cursor: pointer;" alt=""
                            @click="deleteComment(comment.id,comment.author)"
                            >
                            </div>
                    </div>
                    </div>
                    
            </div>
                    <!-- 모달창 끝 -->
    </tr>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import Swal from 'sweetalert2';


const store = useCounterStore()
const props = defineProps(['article','idx'])
const createdat = ref(props.article.created_at.slice(0,10))
const updatedat = ref(props.article.updated_at.slice(0,10))

const idx = props.idx
const commentWrite = ref('')
const commentList = ref([])
const flagEdit = ref('block')
const deleteArticle = function(){
    if(store.userInfo.id != props.article.author){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "글 작성자와 같은 유저가 아닙니다.!",
            });
        return
    }
    Swal.fire({
    title: "정말 삭제하시겠습니까?",
    text: "삭제시 되돌릴 수 없습니다.!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "YES!"
    }).then((result) => {
    if (result.isConfirmed) {
        axios({
            method:'delete',
            url:`http://127.0.0.1:8000/articles/${props.article.id}/`,
            headers:{
                Authorization: `Token ${store.token}`
            }
        }).then(
            res=>{
                Swal.fire({
                    title: "Deleted!",
                    text: "Your file has been deleted.",
                    icon: "success",
                    showConfirmButton: false,
                    }
                    );
                    setTimeout(()=>{
                        location.reload()
                    },1000)
            }
        )
        
    }
    });
}

const deleteComment = function(commentPk,author){
    if(store.userInfo.id != author){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "글 작성자와 같은 유저가 아닙니다.!",
            });
        return
    }
    Swal.fire({
    title: "정말 삭제하시겠습니까?",
    text: "삭제시 되돌릴 수 없습니다.!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "YES!"
    }).then((result) => {
    if (result.isConfirmed) {
    axios({
        method : 'delete',
        url : `http://127.0.0.1:8000/articles/${props.article.id}/comments/${commentPk}`,
        headers : {
            Authorization : `Token ${store.token}`
        }
    })
    .then(res=>{
        axios({
        method: 'get',
        url:`http://127.0.0.1:8000/articles/${props.article.id}/comments/`,
        headers:{
            Authorization : `Token ${store.token}`
        }
    })
    .then(
        res =>{
            commentList.value = res.data
        }
    )
    })
    }
    })
    
}


const write = function(){
    axios({
        method:'post',
        url:`http://127.0.0.1:8000/articles/${props.article.id}/comments/`,
        headers:{
            Authorization : `Token ${store.token}`
        },
        data: {
        content :commentWrite.value
    }
    }).then(
        setTimeout(()=>{
            axios({
            method: 'get',
            url:`http://127.0.0.1:8000/articles/${props.article.id}/comments/`,
            headers:{
                Authorization : `Token ${store.token}`
            }
            })
            .then(
                res =>{
                    commentList.value = res.data
                    console.log(commentList)
                }
            )
        },100)
        
        )
}
const tempInput1 = ref(props.article.title)
const tempInput2 = ref(props.article.content)


onMounted(()=>{
    const confirmEdit = document.getElementById(`confirmEdit${idx}`)
    const editImg = document.getElementById(`edit${idx}`)
    const input1 = document.getElementById(`detail-input1${idx}`)
    const input2 = document.getElementById(`detail-input2${idx}`)

    editImg.addEventListener('click',(event)=>{
        if(store.userInfo.id != props.article.author){
            Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "글 작성자와 같은 유저가 아닙니다.!",
            });
        return
    }
        event.stopPropagation()
        editImg.style.display = 'none'
        confirmEdit.style.display = "block"
        input1.disabled = false
        input2.disabled = false
    })
    confirmEdit.addEventListener('click',(event)=>{
        event.stopPropagation()
        confirmEdit.style.display = 'none'
        editImg.style.display = 'block'
        input1.disabled = true
        input2.disabled = true
        props.article.title = tempInput1.value
        props.article.content = tempInput2.value
        axios({
            method:'put',
            url:`http://127.0.0.1:8000/articles/${props.article.id}/`,
            data:{
                title : tempInput1.value,
                content : tempInput2.value,
            },
            headers : {
                Authorization : `Token ${store.token}`
            }
        })
    })
    // 모달
    const detailModal = document.getElementById(`detail-modal${idx}`);
    const openDetailModalBtn = document.getElementById(`open-detail-modal${idx}`);
    const closeDetailModalBtn = document.getElementById(`close-detail-modal${idx}`);
    // 모달창 닫기
    closeDetailModalBtn.addEventListener("click", (event) => {
    event.stopPropagation()
    confirmEdit.style.display = 'none'
    editImg.style.display = 'block'
    input1.disabled = true
    input2.disabled = true
    detailModal.style.display = "none";
    tempInput1.value = props.article.title
    tempInput2.value = props.article.content
    });
    // 모달창 열기
    openDetailModalBtn.addEventListener("click", (event) => {
    event.stopPropagation()
    detailModal.style.display = "block";
    });
    axios({
        method: 'get',
        url:`http://127.0.0.1:8000/articles/${props.article.id}/comments/`,
        headers:{
            Authorization : `Token ${store.token}`
        }
    })
    .then(
        res =>{
            commentList.value = res.data
        }
    )

})

</script>

<style scoped>
::-webkit-scrollbar{
    width: 13px;
    background-color: rgba(105, 103, 103, 0.048);
}
::-webkit-scrollbar-thumb {
    border-radius: 15px;
    background-color: white;
    border : 1px solid black;
  }
::-webkit-scrollbar-track {
    background-color: white;
}
        /* .close-detail-modal:hover,
        .close-detail-modal:focus {
        color: black;
        text-decoration: none;
        cursor: Pointer;
        } */
        /* #detail-input1:focus{
            outline: none;
            border: 1px solid greenyellow;
            box-shadow: 0 0 10px greenyellow;
        }
        #detail-input2:focus{
            outline: none;
            border: 1px solid greenyellow;
            box-shadow: 0 0 10px greenyellow;
        } */

</style>