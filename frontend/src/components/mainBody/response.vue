<template>
<center>
    <section :class="outerBorderColor" class="container">



        <center>
            <h1 :class="titleBgColor" class="title mushbooh" style="text-align : center">
                <img v-if="halalSign" class="halal-sign" src="../assets/halal.png" alt="Halal Sign">
                <img v-if="haramSign" class="haram-sign" src="../assets/haram_icon.png" alt="">
                {{title}} </h1>
        </center>

        <div :class="btnBgColor" class="ecode_name">
            <p>{{ name }} <span style="font-size: 0.7rem;">[ {{ ecode }} ]</span> </p>
        </div>


        <table class="extras">
            <tbody>
                <tr v-if="extra1" class="extra extra1">
                    <td class="icon">
                            <img class="extra_icon" src="../assets/extra_icon.png" alt="Extra icon">
                    </td>
                    <td class="content">{{ extra1 }}</td>
                </tr>
                <tr v-if="extra2" class="extra extra2">
                    <td class="icon">
                        <center>
                            <img class="extra_icon" src="../assets/extra_icon.png" alt="Extra icon">
                        </center>
                    </td>
                    <td class="content">{{ extra2 }}</td>
                </tr>
                <tr v-if="extra3" class="extra extra3">
                    <td class="icon">
                        <center>
                            <img class="extra_icon" src="../assets/extra_icon.png" alt="Extra icon">
                        </center>
                    </td>
                    <td class="content">{{ extra3 }}</td>
                </tr>
            </tbody>
        </table>


        <section class="ecode_data">
            <div>
                <div :class="innerBorderColor" class="data">
                    <div class="data_icon">
                        <center>
                            <img class="data_icon_1" src="../assets/categary_icon.png" alt="Data icon">
                        </center> 
                    </div>
                    <div class="content_icon left">
                        <p>{{ categary }}</p>
                    </div>
                </div>


                <div :class="innerBorderColor" class="data">
                     <div class="data_icon">
                        <center>
                            <img class="data_icon_1" src="../assets/data_icon.png" alt="Data icon">
                        </center>
                    </div>
                    <div class="content_icon left">
                        <p>{{ info }}</p>
                    </div>
                </div>

                <div :class="innerBorderColor" class="data">
                    <div class="data_icon">
                        <center>
                            <img class="data_icon_1" src="../assets/desc_icon.png" alt="Data icon">
                        </center>                        
                    </div>
                    <div class="content_icon left">
                        <p>{{ comment }}</p>
                    </div>
                </div>

            </div>
        </section>

    </section>
</center>

</template>


<script>
// import { mapGetters } from 'vuex'

export default {
    data(){
        return{
            // redColor : true,
            // greenColor : false,
            // yellowColor : false
        }
    },
    computed : {
        ecode(){
            return this.$store.state.userResult[0]
        },
        title(){
            return this.$store.state.userResult[1]
        },
        name(){
            return this.$store.state.userResult[2]
        },
        extra1(){
            return this.$store.state.userResult[3]
        },
        extra2(){
            return this.$store.state.userResult[4]
        },
        extra3(){
            return this.$store.state.userResult[5]
        },
        categary(){
            return this.$store.state.userResult[6]
        },
        info(){
            return this.$store.state.userResult[7]
        },
        comment(){
            return this.$store.state.userResult[8]
        },
        titleBgColor(){
            return { green_title_bg : this.$store.state.greenColor, red_title_bg : this.$store.state.redColor, yellow_title_bg : this.$store.state.yellowColor }
        },
        btnBgColor(){
            return { green_btn_bg : this.$store.state.greenColor, red_btn_bg : this.$store.state.redColor, yellow_btn_bg : this.$store.state.yellowColor }
        },
        innerBorderColor(){
            return { green_inner_border_color : this.$store.state.greenColor, red_inner_border_color : this.$store.state.redColor, yellow_inner_border_color : this.$store.state.yellowColor }
        },
        outerBorderColor(){
            return { green_outer_border_color : this.$store.state.greenColor, red_outer_border_color : this.$store.state.redColor, yellow_outer_border_color : this.$store.state.yellowColor }
        },
        halalSign(){
            return this.$store.state.greenColor
        },
        haramSign(){
            return this.$store.state.redColor
        },
    }
}
</script>



<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;600&display=swap');


.container{
    border: 2px solid;
    width: 28rem;
    /* position: relative;
    left: 38%; */
    margin-top: 3rem;
    height: auto;
    font-family: 'Source Sans Pro', sans-serif;
    border-radius: 6px;    
}
.title{
    font-size: 3rem;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    width: 18rem;
    margin: 1.5rem 0;
    color: white;
    padding-right: 1rem;
    border-radius: 6px;
}
.mushbooh{
    padding-right: 0;
}

.halal-sign, .haram-sign{
    width: 2.5rem;
    color: white;
    padding-bottom: 3px;
}
.haram-sign{
    padding-bottom: 0px;
}

.extras{
    width: 100%;
}
.extra .icon{
    width: 8%;
    padding: 8px 0;
}

.extra .content{
    width: 92%;
    padding: 8px;
    color: #8b7100;
}
.extra_icon{
    width: 1rem;
    float: right;
}

.ecode_name{
    padding : 10px ;

    font-size: 1.1rem;
    font-family: sans-serif;
}
.ecode_name p, .left p{
    text-align: left;
}

.ecode_data{
    margin-top: 1rem;
    width: 99.7%;
    margin-bottom: 0.8rem;
}


.data_icon{
    width: 10%;    
    padding: 15px;
}
.content_icon{
    width: 90%;    
    padding: 15px;
}
.data {
    display: flex;
    flex-direction: row;
    border-top: 1.5px solid #dff0d8;
}
.data_icon_1{
    width: 1rem;
}


.green_outer_border_color{
    border-color: rgba(92, 184, 92,0.5);
}
.green_inner_border_color{
    border-color: #dff0d8;
}
.green_btn_bg{
    color : green;
    background: #dff0d8;
}
.green_title_bg{
    background: #5cb85c;
}

.red_outer_border_color{
    border-color: rgba(217, 83, 79, 0.5);
}
.red_inner_border_color{
    border-color: rgba(217, 83, 79, 0.3);
}
.red_btn_bg{
    color : #c0392b;
    background: #f2dede;
}
.red_title_bg{
    background: #d9534f;
}


.yellow_outer_border_color{
    border-color: rgba(243, 156, 18,0.5);
}
.yellow_inner_border_color{
    border-color: rgba(243, 156, 18,0.3);
}
.yellow_btn_bg{
    color : #f0932b;
    background: #fdf7d4;
}
.yellow_title_bg{
    background: #f0ad4e;
}

@media  (max-width: 500px) {
    .container{
        width: 20rem;
        margin-top: 1rem;
    }
}

</style>