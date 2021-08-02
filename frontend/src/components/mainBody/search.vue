<template>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<center>
    
    <div class="container">
        <input @keyup.enter="getUserData" class="search_bar" type="text" v-model="userInput" name="E-Codes">
        <label for="search_bar"><button  @click="getUserData"><i class="fa fa-search"></i></button></label>
        <p>E-Code <span style="color : #16a085">e.g: E100</span></p>

        <div v-if="notFound" class="error">
            <h1>Sorry ! The data with ecode <span style="color : #4C4C6D"> [{{ e_code }}] </span> not available right now, please try different ecode.</h1>
        </div>

    </div>
</center>


  <router-view v-if="showComp" ></router-view>

</template>


<script>
import axios from 'axios'

export default {
    data(){
        return{
            userInput : '',
        }
    },
    methods : {
        getUserData(){
            this.$store.state.showNotFound = false
            this.$store.state.e_code = this.userInput

            axios.post('https://zainulabideen.pythonanywhere.com/getFromUser', {
                'ecode' : this.$store.state.e_code,
            })
            .then((res)=>{
                if (res){
                axios.get('https://zainulabideen.pythonanywhere.com/getData')
                .then((resp)=>{
                    if (resp.data['error'] === 'Error') {
                        this.$store.state.showResponseComp = false
                        this.$store.state.showNotFound = true
                    }else{

                    this.$store.commit('UserResult', resp.data)
                    this.$store.state.showResponseComp = true
                    this.$store.state.showNotFound = false
                    if (this.$store.state.userResult[1] === 'HALAL') {
                        this.$store.state.redColor = false,
                        this.$store.state.greenColor = true,
                        this.$store.state.yellowColor = false
                    }else if (this.$store.state.userResult[1] === 'HARAM') {
                        this.$store.state.redColor = true,
                        this.$store.state.greenColor = false,
                        this.$store.state.yellowColor = false
                    }else if (this.$store.state.userResult[1] === 'MUSHBOOH') {
                        this.$store.state.redColor = false,
                        this.$store.state.greenColor = false,
                        this.$store.state.yellowColor = true
                    }


                    this.$router.push('/search/' + this.$store.state.e_code)
                    }

                    })
                    
                }
            })
            .catch((err)=>{
                console.log(err)
            })
            
        },

    },
    computed : {
        showComp(){
            return this.$store.state.showResponseComp
        },
        notFound(){
            return this.$store.state.showNotFound
        },
        e_code(){
            return this.$store.state.e_code
        },
    }
}
</script>



<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;600&display=swap');



.container{
    margin-top: 6rem;
}

.error{ 
    color: #e74c3c;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 0.8rem;
    position: relative;
    text-align: center;
    position: relative;
    top: 10vh;
}

.search_bar, .search_bar:focus {
    width: 15rem;
    /* height: 4vh; */
    font-size: 1.5rem;
    border-radius: 5px 0 0 5px;
    border: 1px solid  rgba(76, 76, 109, 0.7);
    padding: 10px 10px;
    color: #4C4C6D;
    font-family: 'Source Sans Pro', sans-serif;
    font-weight: bold;
}
button{
    background: white;
    font-size: 1.5rem;
    border: 2px solid  rgba(76, 76, 109, 0.7);
    border-radius: 0px 5px 5px 0px;
    padding: 10px 8px;
    margin-left: 10px;
    cursor: pointer;
}

button i{
    color: rgba(76, 76, 109, 1);
}

.container p {
    font-family: 'Source Sans Pro', sans-serif;
}
@media (max-width: 500px){
    .container{
        margin-top: 2rem;
    }
}
@media (min-width: 500px) and (max-width: 670px){
    .container{
        margin-top: 2rem;
    }
}

@media (max-width: 460px){
    .container{
        margin-top: 4rem;
    }
}
@media (max-width: 364px){
    .container{
        margin-top: 6rem;
    }
}

/* @media (max-height : 700){
    .container{
        margin-top: 4rem;
    }
} */

</style>