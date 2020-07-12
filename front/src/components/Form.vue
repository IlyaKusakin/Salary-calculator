<template>
<<<<<<< HEAD
            <v-form ref="form"    
              v-model="valid"
              lazy-validation 
              >
                <div class="container CONTAINER " >
                    <div class="row" style="position:relative">
                        <div class="col-12 pt-5 pb-0 " >
                    
                            <v-text-field class="mb-4"
                              dark
                              v-model="title"
                              :rules="titleRules"
                              label="Название вакансии"
                              required
                            ></v-text-field>

                            <v-text-field 
                              dark
                              v-model="company"
                              label="Название компании"
                              required
                            ></v-text-field>

                            <div class="row mt-3">
                                <div class="col-md-6 py-0  col-12">
                                     <v-select
                                        dark
                                        v-model="employment"
                                        :items="employments"
                                        label="Тип занятости"
                                      ></v-select>
                                </div>
                                <div class="col-md-6 py-0 col-12">
                                  <v-select
                                    dark
                                    v-model="worktime"
                                    :items="worktimes"
                                    label="График работы"
                                  ></v-select>
                                </div>
                            </div>
                           
                            <v-slider
                              class="mt-5 pt-1"
                                dark
                                v-model="exp" 
                                label="Опыт работы"
                                step="1"
                               
                                ticks
                                min="0"
                                max="11"
                                color="white"
                              >
                              <template v-slot:thumb-label="{ value }"  >
                                <span style="color:black">  {{  value == 11 ? '> 10': value }}</span>
                              </template> 
                            </v-slider>

                            
                            <v-combobox
                                class="mb-5"
                                dark
                                v-model="skills"
                                :filter="filter"
                                :hide-no-data="!search"
                                :items="items"
                                :search-input.sync="search"
                                hide-selected
                                label="Ключевые навыки"
                                multiple
                                small-chips
                              > 
                                <template v-slot:selection="{ attrs, item, parent, selected }">
                                  <v-chip
                                    v-if="item === Object(item)"
                                    v-bind="attrs"
                                    :color="`grey darken-1`"
                                    :input-value="selected"
                                    label
                                    small
                                  >
                                    <span class="pr-2">
                                      {{ item.text }}
                                    </span>
                                    <v-icon
                                      small
                                      @click="parent.selectItem(item)"
                                    >mdi-close</v-icon>
                                  </v-chip>
                                </template>

                                <template v-slot:item="{ item }" >
                                  <v-chip
                                    :color="`grey darken-1`"
                                    dark
                                    label
                                    small
                                  >
                                    {{ item.text }}
                                  </v-chip>
                                </template>
                              </v-combobox>

                            <div style="position:relative">
                                <v-btn 
                                  color="secondary" 
                                  @click="FileInput()"  
                                  style="position:absolute;top:-25px;right:0px;border-radius: 10px  ;"  
                                  x-small dark
                                >
                                    <input type="file" id="fileInput" @change="ReadFiles($event)" class="btn d-none btn-info mb-1 btn-sm"/>
                                    загрузить текст
                                </v-btn> 

                                <v-textarea
                                dark
                                outlined
                                v-model="text"
                                name="input-7-4"
                                label="Подробное описание вакансии"
                                required
                              ></v-textarea>
                          </div>

                          <div class=" mb-5 " style="position:relative">

                            <v-btn
                                    color="grey darken-1 " 
                                    id="mybtn"  
                                    :disabled="!valid"  
                                    @click="validate" 
                                    dark 
                                    x-large
                                    :loading="loading"
                                    >Рассчитать <br> зарплату
                                  </v-btn>
                            
                              <span style="position:absolute;right:0;" id="cost" > <b>{{this.result==null ? "":this.result + ' руб.' }}</b></span>
                          </div>

=======
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

        <div  style="background-color:rgb(66,66,66)" class="mb-1" >

            <v-form ref="form" >
                <div class="container CONTAINER " >
                    <div class="row">
                        <div class="col-md-8 col-12 pt-5 pb-0 pb-md-2  " style="position:relative">
                    
                            <v-text-field
                            v-model="title"
                            style=" border-radius: 15px 15px 0 0;"
                            class="pt-5"
                            light
                            required
                            background-color="white"
                            label="Название вакансии"
                            filled
                            ></v-text-field>
    
                            <v-btn 
                              color="secondary" 
                              @click="FileInput()"  
                              style="position:absolute;top:100px;right:12px;border-radius: 15px 0 0 15px ;"  
                              x-small dark
                            >
                                <input type="file" id="fileInput" @change="ReadFiles($event)" class="btn d-none btn-info mb-1 btn-sm"/>
                                загрузить текстовый файл
                            </v-btn> 
            
  
                            <v-textarea
                              light
                              v-model="text"
                              filled
                              solo
                              required
                              style=" border-radius: 0 0 15px 15px "
                              height="250px"
                              background-color="white"
                              name="input-7-4"
                              label="Подробное описание вакансии"
                            ></v-textarea>
                        </div>

                        <div style="position:relative" class="col-md-4 d-inline-block d-md-block pt-md-5 pt-0 pl-md-5 ">
                            <div style="height:50px" class=" my-md-2 pt-md-3 pl-md-5">
                                <v-btn
                                  color="grey darken-1 mb-1" 
                                  id="mybtn"  
                                  :disabled="!valid"  
                                  @click="validate" 
                                  dark 
                                  x-large
                                  :loading="loading"
                                  >Рассчитать <br> зарплату
                                </v-btn>
                            </div>
                            <span class="d-md-block  mt-md-5 pt-md-4 pl-md-5" id="cost"> <b>{{this.result==null ? "":this.result + ' руб.' }}</b></span>
>>>>>>> a0d2f18c6b2ce3687c6117f748e7934af5a95790
                        </div>
                    </div>
                </div>
            </v-form>
<<<<<<< HEAD
=======
        </div>

        <v-list v-if="this.$store.state.inquiries.length>0"  style="pointer-events:none"  class="pt-5 ">
            <div class="container CONTAINER pb-0 pt-md-5 "  >
                <span class="pt-md-3 d-block " id="title" >
                    <b>Результаты ваших подсчетов:</b>
                </span>
            </div>
            <v-list-item-group>
                <div  v-for="(item, i) in this.$store.state.inquiries.slice((this.page-1)*5,this.page*5)"
                  :key="i" 
                >
                    <v-list-item class="position:relative px-0 py-0">
                        <div class="container CONTAINER py-0 ">
                            <v-list-item-content class="py-0"> 
                                <div class="row " style="position:relative" >
                                    <div class="col-md-8 col-12 p-0">
                                        <div>
                                            <p class="font-weight-bold titleWork" >{{item.title}}</p>
                                        </div>
                                        
                                        <span class="d-block font-weight-regular textWork" >{{item.text}}</span> 
                                        <br>
                                        
                                        <div>
                                            <a @click="Delete(item.id)" style="pointer-events:auto" class="d-block-inline  ">удалить</a>
                                        </div>
                                    </div>
                                    
                                    <div class="col-md-4 text-center py-0">
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
    </v-content>
>>>>>>> a0d2f18c6b2ce3687c6117f748e7934af5a95790
</template>


<script>

  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  var txt

  import swal from 'sweetalert'
  
  export default {
      data(){
          return{
              loading: false,

              title:"",
              company:"",
              employment:"Полная занятость",
              worktime:"Полный день",
              exp:1,
              skills: [{text: 'Исполнительность'}],
              text:"",

              result:null,
              valid:  true ,
              search: null,

              employments:[
                'Полная занятость',
                'Частичная занятость',
                'Стажировка',
                'Проектная работа'
              ],
              worktimes:[
                'Полный день',
                'Гибкий график',
                'Сменный график',
                'Удаленная работа',
                'Вахтовый метод'
              ],
              items: [
                { header: 'Выберите или создайте свой навык' },
                {
                  text: 'Исполнительность'
                },
                {
                  text: 'SQL'
                },
                {
                  text: 'Умение работать в команде'
                },
                {
                  text: 'HTML'
                },
              ],
              titleRules: [
                  v => !!v || 'Это поле обязательное',
              ],
        
          }
      },

      create(){
        this.result=null
      },

      watch: {
          skills (val, prev) {
            if (val.length === prev.length) return
            this.skills = val.map(v => {
                if (typeof v === 'string') {
                  v = {
                    text: v
                  }
                  this.items.push(v)
                }
              return v
            })
      }
      },

      methods:{
          filter (item, queryText, itemText) {
            if (item.header) return false

            const hasValue = val => val != null ? val : ''

            const text = hasValue(itemText)
            const query = hasValue(queryText)

            return text.toString()
              .toLowerCase()
              .indexOf(query.toString().toLowerCase()) > -1
          },

        FileInput(){
            var fileInput = document.getElementById("fileInput");
            fileInput.click();
        },

        async ReadFiles(event){
            var file = event.target.files[0]
            if(file.type =="text/plain"){
                var fr = new FileReader();
                fr.readAsText(file)
                fr.onload = ( function (e) {
                txt = e.currentTarget.result  
                })
                await sleep(100)
                this.text = txt;
            } else{
                swal({
                title: "Ошибка",
                text: "Вы можете загрузить только файл с разширением txt",
                icon: "error",
                button: "Окей",
                });
            }
        },

        async validate () {
            let list =[]
            this.skills.forEach(e => {
              list.push(e.text)
            });
    
            let form = {
                title : this.title,
                company:this.company,
                employment:this.employment,
                worktime:this.worktime,
                exp:this.exp,
                skills:list,
                text: this.text
            }
<<<<<<< HEAD
            if(this.$refs.form.validate())
              {
                this.loading = true
                this.$refs.form.validate()
                console.log(form)
                await sleep(1000)
                await this.$store.dispatch("AddInquiry",form)
                this.loading = false
                this.result = this.$store.state.inquiries[0].result
                this.$refs.form.validate()
              }
        },


=======
            this.loading = true
            await sleep(1000)
            await this.$store.dispatch("AddInquiry",form)
            this.loading = false
            this.result = this.$store.state.inquiries[0].result
            this.$refs.form.validate()
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

        async LogOut(){
            await this.$store.dispatch('LogOut')
        },

        Day(){
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark
        },

        change(){
            this.$store.dispatch("Change",this.$store.state.tab)
        }
>>>>>>> a0d2f18c6b2ce3687c6117f748e7934af5a95790
      }  
  }
</script>

<style>
  .custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>