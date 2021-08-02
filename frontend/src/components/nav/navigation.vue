<template>
    <div class="nav">
        <h1 class="main_icon">
            {{ main_title }}<p>Check if an E-Code is <span class="bold">Halal</span>, <span class="bold">Haram</span> or 
            <span class="bold getInfo">
                Mushbooh <span class="tooltiptext">This means "not confirmed", due to insufficent information.</span>
            </span></p>
        </h1>
        

        <div class="links">
            <ul>
                <li><router-link to="">Contact</router-link></li>
                <li><router-link to="" >About</router-link></li>
                <li><router-link to="/" style="text-decoration: none">Home</router-link></li>
            </ul>
        </div>


    </div>
</template>


<script>
// import something from '../assets/find_icon.png'

export default {
    data(){
        return{
            main_title : this.$store.state.main_title
        }
    }
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;600&display=swap');


.nav{
    margin-top: 2rem;
}

.find_icon{
    width: 2rem;    
    padding: 0px 5px;
}   
.main_icon{
    font-family: 'Source Sans Pro', sans-serif;
    float: left;
    margin-left: 10rem;
    color: #4C4C6D;
    font-size: 3rem;
}
.main_icon p{
    font-size: 1rem;
    background: rgba(76, 76, 109, 0.7);
    padding: 0 10px;
    color: white;
}
.tooltiptext {
  visibility: hidden;
  width: auto;
  background-color: rgba(0, 0, 0, 0.7);
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 10px;
  /* Position the tooltip */
  position: absolute;
  transform: translate(-8rem, -2rem);
  font-size : 0.8rem
}
.getInfo{
    cursor: pointer;
    text-decoration: underline;
}

.getInfo:hover .tooltiptext{
  visibility: visible;
}


.links{
    margin-right: 15%;
    padding-top: 0.5rem;
}

.links ul{
  list-style-type: none;
  overflow: hidden;
}
.links ul li{
    float: right;

}
.links ul li a{
    display: block;
    padding: 0 1rem;
    text-decoration:line-through;
    color: #4C4C6D;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 1.3rem;
    font-weight: 600;
    margin-top: 20pxs;
}
.links ul li a:hover{
    color: black;
}


.green{
    color: green;
}
.red{
    color: #c0392b;
}
.yellow{
    color: #FFE194;
}
.bold{
    font-weight:900;
}
    
@media (max-width : 800px){
    .main_icon{
        margin-left: 3rem;
    }
}
@media (max-width : 400px){
    .main_icon{
        margin-left: 1rem;
    }
}

</style>

