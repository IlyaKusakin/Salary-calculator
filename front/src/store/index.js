import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist';
import axios from 'axios'
import router from '../router'
import swal from 'sweetalert'


Vue.use(Vuex)

const vuexLocalStorage = new VuexPersist({
    key: 'vuex', 
    storage: window.localStorage, 
})

// var port ="http://84.201.133.212/apipy/"
 var port ="http://127.0.0.1:8000/api/"

export default new Vuex.Store({
    state: {
        statusDay:false,

        user :{
            id:null,
            token:null,
            name: "Гость",
            email:"somemail@mail.ru"
        },

        inquiries:[],
    },

    mutations: {
        setStatusDay(state,newStatus){
            state.statusDay =newStatus
        },
        setUser(state,newTab){
            state.user = newTab;
        },
        setInquiries(state,newTab){
            state.inquiries = newTab;
        },
    },

    actions: {
        async GetInquiries(){
            var config ={   headers:{Authorization :"Token "+ this.state.user.token}}
            await axios.get(port + 'inquiry/all/',config).then(response =>{
                console.log(response.data)
                this.commit('setInquiries',response.data.reverse())
            }).catch(function(e){console.log(e)});
        },


        async DeleteInquiry(state,id){
            if(this.state.user.token!=null){
                var config ={   headers:{Authorization :"Token "+ this.state.user.token}}
                await axios.delete(port + 'inquiry/detail/'+ id + '/',config).then(() =>{
                    this.dispatch('GetInquiries')
                }).catch(function(e){console.log(e)}); 
            }
            else{
                var i
                for(i = 0;this.state.inquiries[i].id !=id;i++){
                    continue
                }
                var list = this.state.inquiries.slice()
                console.log(i)
                list.splice(i, 1)
                this.commit('setInquiries',list)
                console.log(this.state.inquiries)
            }
        },


        async AddInquiry(state, form){
            let data = {
                'title' : form.title,
                'company':form.company,
                'employment':form.employment,
                'worktime':form.worktime,
                'exp':form.exp,
                'skills':form.skills.join(', '),
                'text': form.text
            }
            if(this.state.user.token==null){
                await axios.post(port +'inquiry/create/',data).then((response) =>{
                    var list = this.state.inquiries.slice()
                    var obj = {};
                    list.length>0 ? obj["id"]=list[0].id +1 : obj["id"] = 0
                    obj["title"]=data.title
                    obj["text"]=data.text
                    obj["user"]=null
                    obj["company"]=data.company
                    obj["employment"] = data.employment
                    obj["worktime"]=data.worktime
                    obj["exp"] = data.exp
                    obj["skills"] = data.skills
                    obj["result"]=response.data.result
                    list.unshift(obj)
                    this.commit('setInquiries',list) 
                    console.log(this.state.inquiries)
                }).catch(function(e){alert("Чо-то случилось");console.log(e)});
            }
            else{
                var config ={   headers:{Authorization :"Token "+ this.state.user.token}}
                await axios.post(port +'inquiry/create-auth/',data,config).then(() =>{
                    this.dispatch('GetInquiries')
                }).catch(function(e){alert("Что-то произошло");console.log(e)});  
            }
        },


        async SignUp(state,form){
            const data={
                'email':form.email,
                'username': form.name,
                'password': form.password};
            await axios.post(port + 'user/create/',data).then(() =>{
                this.dispatch('LogIn',form)
            }).catch(function(e){
                swal({
                    icon: 'error',
                    title: 'Ошибка',
                    text: 'Это имя уже занято либо вы ввели некорректный email',
                })
            console.log(e)});
        },


        async LogIn(state,form){
            const data={
                'username': form.name,
                'password': form.password};
            await axios.post(port + 'login/',data).then(response =>{
                this.commit('setUser',{id:response.data.id_user , name:response.data.username, token: response.data.token, email: response.data.email})
                router.push("/")
                this.dispatch('GetInquiries')
            }).catch(function(e){
              swal("Ошибка", "Некорректные данные", "error");
              console.log(e)
            });
        },


        async LogOut(){
            this.commit('setUser',{id:null , name:"Гость", token: null, email: "somemail@mail.ru"})  
            var list =[]
            this.commit('setInquiries',list) 
        },    
    },

    plugins: [vuexLocalStorage.plugin]
})
   

