import { createStore } from 'vuex'

const store = createStore({
    state(){
        return{
            main_title : 'E-Code Finder',
            e_code : '',
            userResult : null,
            redColor : null,
            greenColor : null,
            yellowColor : null,
            showResponseComp : null,
            showNotFound : null
        }
    },
    mutations : {
        UserResult(state, payload){
            state.userResult = null
            state.userResult = payload
        },
    },
    getters : {
        showData(state){
            return state.userResult;
        }
    }

})

export default store