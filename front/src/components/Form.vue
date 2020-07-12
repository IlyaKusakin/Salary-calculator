<template>
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

                        </div>
                    </div>
                </div>
            </v-form>
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
                {text: 'Исполнительность'},
                {text: 'Коммуникация'},
                {text: 'Пользование интернетом'},
                { text: 'Способность обучаться'},
                { text: 'Умение вести переписку'},
                { text: 'Умение работать в команде'}
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
            if(this.$refs.form.validate())
              {
                this.loading = true
                this.$refs.form.validate()          
                await this.$store.dispatch("AddInquiry",form)
                await sleep(100)
                this.loading = false
                this.result = this.$store.state.inquiries[0].result
                
              }
        },
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