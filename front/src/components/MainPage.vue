<template>
    <v-content>
        <v-list disabled class="pt-5 d-none d-md-block">
            <v-list-item-group   >
                <v-list-item>
                    <div class="container CONTAINER  " >
                        <div class="row">
                            <div class="col-12 " style="position:relative">
                                <img src='../assets/icon3.png' style="position:absolute;left:12px" width="46px" />
                                <span class="pt-3 d-block" style="margin-left:60px;font-size:30px"><b>Нейросетевой калькулятор зарплаты</b></span>
                            </div>
                        </div>
                    </div>
                </v-list-item>
            </v-list-item-group>
        </v-list>

        <div  style="background-color:rgb(66,66,66)"  >
            <Form></Form>
        </div>
<!-- style="pointer-events:none" -->
        <v-list v-if="this.$store.state.inquiries.length>0" disabled   class="pt-5 ">
            <div class="container CONTAINER pb-0 pt-md-5 "  >
                <span class="pt-md-3 d-block " id="title" >
                    <b>Результаты ваших подсчетов:</b>
                </span>
            </div>
            <v-list-item-group>
                <div  v-for="(item, i) in this.$store.state.inquiries.slice((this.page-1)*5,this.page*5)"
                  :key="i" 
                >
                    <v-list-item class=" position:relative px-0 py-0"  >
                        <div class="container CONTAINER py-0 " >
                            <v-list-item-content class="py-0"> 
                                <div class="row " style="position:relative" >
                                    <div class="col-md-9 col-12 p-0">
                                    
                                        <p class="font-weight-bold titleWork" >{{item.title}}</p>
                                        <span class="d-block mb-1 font-weight-regular textWork" ><b>Компания: </b>{{item.company ==""?'не указана':item.company}}</span>

                                        <span class="d-block mb-1 font-weight-regular textWork" ><b>Требуемый опыт: </b> {{GetExp(item.exp)}}</span> 

                                        <span class="d-block mb-1 font-weight-regular textWork" ><b>График работы: </b> {{item.worktime}}</span> 

                                        <span class="d-block mb-1 font-weight-regular textWork" ><b>Тип занятости: </b>{{item.employment}}</span> 
                                        
                                        <span class="d-block mb-1 font-weight-regular textWork" >
                                            <b>Ключевые навыки: </b> {{item.skills==""?'нет навыков':item.skills}}
                                        </span> 
                                
                                        <span v-if="item.text != ''" class="d-block font-weight-regular textWork" >
                                            <b>Описание: </b> {{item.text}}
                                        </span> 
                                        <br>
                                        
                                        <a @click.stop="Delete(item.id)" style="pointer-events:auto" class="d-block-inline  ">удалить</a> 
                                    </div>
                                    
                                    <div class="col-md-3 text-right pt-2 py-0">
                                        <span  class="listCost ">{{item.result}} руб.</span>
                                    </div>
                                </div>
                            </v-list-item-content>
                        </div>
                    </v-list-item>
                    <div class="container CONTAINER py-3 m-0 ">
                        <v-divider></v-divider>
                    </div>
                </div>        
            </v-list-item-group>
        </v-list>


        <v-list v-if="this.$store.state.inquiries.length>0" class="pt-5 pb-5">
            <div class="text-center">
                <v-pagination
                  color="grey darken-3"
                  v-model="page"
                  :length="Math.floor(this.$store.state.inquiries.length/5 == parseInt(this.$store.state.inquiries.length/5)?
                      this.$store.state.inquiries.length/5: this.$store.state.inquiries.length/5 +1)"
                  total-visible="7"
                ></v-pagination>
            </div>
        </v-list>


        <v-list disabled >
            <v-list-item-group   >   
            </v-list-item-group>
        </v-list>
        
    </v-content>
</template>


<script>

  import swal from 'sweetalert'
  import Form from '../components/Form.vue'
  
  export default {
      components:{
          Form
      },
      data(){
          return{    
              page: 1,
          }
      },
      methods:{
          GetExp(exp){
                if(exp==0) return 'без опыта работы'
                if(exp==1) return exp +' год'
                if(exp==11) return 'больше 10 лет'
                if(exp>4) return exp +' лет'
                return exp +' года'

          },
        Delete(id){
            swal({
                  title: "Вы точно хотите удалить данную запись?",
                  text: "После удаления ее нельзя будет никак возобновить!",
                  icon: "warning",
                  buttons: true,
                  dangerMode: true,
                
            }).then((willDelete) => {
                if (willDelete) {
                  this.$store.dispatch('DeleteInquiry',id)
                    swal("Запись была успешно удалена", {
                        icon: "success",
                        button: "Ок",
                    });
                } else {
                      swal("Ваша запись сохранена");
                }
            });
        },

      
      }  
  }
</script>
