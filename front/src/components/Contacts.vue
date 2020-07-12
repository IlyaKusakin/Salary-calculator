<template>
    <v-content>
        <div class="container CONTAINER  " >
            <div class="row">
                <div class="col-12 " style="position:relative">
                    <v-list-item class="px-0" > 
                        <v-list-item-action class="mr-3">   
                            <v-icon class="d-none d-md-block"  large >mdi-account-group</v-icon>
                            <v-icon class="d-block d-md-none"   >mdi-account-group</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>    
                            <v-list-item-title><span class="pt-1 d-inline-block" id="yral" ><b>Состав команды "Дубки-Уралмаш"</b></span></v-list-item-title>
                        </v-list-item-content>     
                    </v-list-item>
                </div>

                <div class="row px-2 d-none d-md-block" >
                    <div v-for="(developer,i) in developers" :key="i" class="col-12 mb-5 " style="position:relative;padding-left:180px">
                        <v-avatar size="150"  style="position:absolute;left:15px" >
                            <img :src="require('../assets/'+developer.avatar)">
                        </v-avatar>
                        <span class="pt-3 d-block font-weight-medium" style="font-size:30px">{{developer.name}}</span>
                        <span class="pt-1 d-block font-weight-regular" style="font-size:20px">{{developer.role}}</span>
                        <v-list-item class="px-0" > 
                            <v-list-item-action class="mr-3 mt-4">   
                                <v-icon   > mdi-email</v-icon>
                            </v-list-item-action>
                            <v-list-item-content> 
                                <v-list-item-title><span class="pt-1 d-block font-weight-regular" style="font-size:19px">{{developer.mail}}</span></v-list-item-title>   
                            </v-list-item-content>     
                        </v-list-item>
                        <v-divider class="mt-3"></v-divider>  
                    </div>
                </div>

                <div class="row px-2 d-block d-md-none" >
                    <div v-for="(developer,i) in developers" :key="i" class="col-12 mb-5 " style="position:relative;padding-left:125px">
                        <v-avatar size="100"  style="position:absolute;left:15px" >
                            <img :src="require('../assets/'+developer.avatar)">
                        </v-avatar>
                        <span class="pt-0 d-block font-weight-medium" style="font-size:19px">{{developer.name}}</span>
                        <span class="pt-0 d-block font-weight-regular" style="font-size:14px">{{developer.role}}</span>
                        <v-list-item class="px-0" > 
                            <v-list-item-action class="mr-0 mt-0">   
                                <v-icon small  > mdi-email</v-icon>
                            </v-list-item-action>
                            <v-list-item-content class="pt-0"> 
                                <v-list-item-title><span class="pt-0 d-block font-weight-regular" style="font-size:14px">{{developer.mail}}</span></v-list-item-title>
                            </v-list-item-content>     
                        </v-list-item>
                        <v-divider class="mt-0 mt-sm-1"></v-divider>  
                    </div>
                </div>   
            </div>
        </div>
    </v-content>
</template>


<script>
  export default {
    data: () => ({
      developers: [
        {
          avatar: 'Kysakin.jpg',
          name: 'Кусакин Илья',
          role: "Тим-менеджмент, анализ данных, разработка ML-модели",
          mail:"kusakin_ilya@icloud.com"
        },
        {
          avatar: 'Kydrin.jpg',
          name: 'Кудринский Алексей',
          role: "Дата-инжиниринг, разработка ML-модели",
          mail:"a.kudrinsky@mail.ru"
        },
        {
          avatar: 'Cvetozyb.jpg',
          name: 'Цвелодуб Влад',
          role: "Разработка концепции приложения, дизайн графического интерфейса",
          mail:"somevlad@mail.com"
        },
        {
          avatar: 'Alex.jpg',
          name: 'Немашкало Александр',
          role: "Front-end и back-end разработка, дизайн графического интерфейса  ",
          mail:"n.a.vi_talevich@mail.ru"
        }, 
      ],
    }),
  
  }
</script>