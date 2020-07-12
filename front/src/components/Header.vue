<template>
    <div>
        <v-app-bar
          app
          dark
          color="grey darken-3"  
          class="d-none d-md-block" 
        >
            <div class=" CONTAINER container " >
                <div class="row"> 
                    <div class="col-8 pt-5 ">
                        <div class="my-2 d-inline-block mr-5 pt-0 pb-2">
                            <router-link style="text-decoration: none" to="/">
                                <v-btn class="px-0  " color="grey darken-3"  depressed large>Главная</v-btn>
                            </router-link>
                        </div>

                        <div class="d-inline-block mr-sm-5 ml-sm-5">
                            <router-link style="text-decoration: none" to="/about">
                                <v-btn class="px-0  " color="grey darken-3"  depressed large>О Приложении</v-btn>
                            </router-link>
                        </div>

                        <div class="my-2 d-inline-block ml-5">
                            <router-link style="text-decoration: none" to="/contacts">
                                <v-btn class="px-0  " color="grey darken-3"  depressed  large>Контакты</v-btn>
                            </router-link>
                        </div>

                        <div  v-if="this.$store.state.user.token != null" @click="LogOut()" class="my-2 d-inline-block ml-5">
                            <v-btn class="d-inline-block  "
                              icon
                              depressed
                              fab
                            >
                                <v-icon>mdi-exit-to-app</v-icon>
                            </v-btn>
                        </div>
                    </div>


                    <div class="col-4 text-right pl-0 pr-0">

                        <router-link
                          v-if="this.$store.state.user.token == null"
                          style="text-decoration: none" to="/login"
                        >
                            <v-btn class="mt-4 " color="grey darken-3"  depressed  large>
                                Вход
                            </v-btn>
                        </router-link>
            

                        <v-list-item
                          v-if="this.$store.state.user.token != null"
                          two-line class=" mt-1 pr-3 pl-0"
                        >
                            <v-list-item-content>
                                <v-list-item-title>{{this.$store.state.user.name}}</v-list-item-title>
                                <v-list-item-subtitle>{{this.$store.state.user.email}}</v-list-item-subtitle>
                            </v-list-item-content>

                            <v-list-item-avatar>
                                <v-avatar color="white text-center">
                                    <span class="black--text headline  ">{{this.$store.state.user.name[0]}}</span>
                                </v-avatar>
                            </v-list-item-avatar>
                        </v-list-item>
                    </div>
                </div> 
            </div>     
        </v-app-bar>


        <v-app-bar
          app
          dark
          color="grey darken-3" 
          absolute  
          class=" d-block d-md-none"
        >
            <v-toolbar color="grey darken-3" class="px-5 ">
                <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
                <v-toolbar-title class="pl-0" style="font-size:16px">Калькулятор зарплаты</v-toolbar-title>
                <v-spacer></v-spacer>
            </v-toolbar>
        </v-app-bar>

        <v-navigation-drawer
          v-model="drawer"
          absolute
          temporary
        >
            <v-list-item two-line class=" mt-1 pr-5  pl-4">
                <v-list-item-avatar>
                    <v-avatar color="rgb(0,252,252)">
                        <span class="black--text headline  ">{{this.$store.state.user.name[0]}}</span>
                    </v-avatar>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title>{{this.$store.state.user.name}}</v-list-item-title>
                    <v-list-item-subtitle>{{this.$store.state.user.email}}</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list >
                <v-list-item @click="change('/')" link>
                    <v-list-item-icon>
                        <v-icon >mdi-calculator-variant</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>Главная</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item    @click="change('/about')" link> 
                    <v-list-item-action>   
                        <v-icon >mdi-information-outline</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>    
                        <v-list-item-title>О приложении</v-list-item-title> 
                    </v-list-item-content>     
                </v-list-item>


                <v-list-item @click="change('/contacts')" link> 
                    <v-list-item-action>   
                        <v-icon >mdi-account-group</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>    
                        <v-list-item-title>Контакты</v-list-item-title> 
                    </v-list-item-content>     
                </v-list-item>

                <v-divider ></v-divider>
            
                <v-list-item v-if="this.$store.state.user.token != null" @click="LogOut()" link> 
                    <v-list-item-action>   
                        <v-icon >mdi-exit-run</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>    
                        <v-list-item-title>Выйти</v-list-item-title> 
                    </v-list-item-content>     
                </v-list-item>

                <v-list-item v-if="this.$store.state.user.token == null" @click="change('/login')" link> 
                    <v-list-item-action>   
                        <v-icon >mdi-login-variant</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>    
                        <v-list-item-title>Вход</v-list-item-title> 
                    </v-list-item-content>     
                </v-list-item>

                <v-list-item v-if="this.$store.state.user.token == null" @click="change('/register')" link> 
                    <v-list-item-action>   
                        <v-icon >mdi-account-plus</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>    
                        <v-list-item-title>Регистрация</v-list-item-title> 
                    </v-list-item-content>     
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>


export default {
  data(){
      return{
         drawer: false,
      }
    },
      methods:{
        change(str){
              this.$router.push(str)
          },
        
        LogOut(){
          this.$store.dispatch('LogOut')
        }
    }

}
</script>
