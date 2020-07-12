<template>
    <v-footer
      dark
      padless
      color="grey darken-3"
    >
    
        <div class="container CONTAINER text-center ">
            <v-btn
              class="mx-4 white--text"
              icon
              href="https://xn--80aaap2atgrpcmp.xn--p1ai/#rec200612850"
            >
                <v-icon size="24px">mdi-alpha-t-circle</v-icon>
            </v-btn> 

            <div class="d-inline-block pl-5 ml-1 pt-5 pb-5">
                <v-icon size="24px">mdi-white-balance-sunny</v-icon>
            </div> 

            <div class="d-inline-block mx-1   mb-5" style="position:relative">
                <v-switch 
                  style="position:absolute;top:-17px"
                  v-model="statusDay"
                  @change="Day"
                  color="black"
                  value="true"  
                  hide-details
                ></v-switch>
            </div> 

            <div class="d-inline-block ml-5 pl-5 pr-5 mr-1">
                <v-icon size="24px">mdi-weather-night</v-icon>  
            </div> 

            <v-btn
              class="mx-4 white--text"
              icon
              href="https://github.com/AlexandrNemashkalo/Salary-calculator"
            >
                <v-icon size="24px">mdi-github</v-icon>
            </v-btn> 

            <br>
            <span class="d-inline-block pb-5">
              Приложение было разработано командой "Дубки-Уралмаш" в 2020 году в рамках участия в Хакатоне Труда
            </span>

            <v-divider></v-divider>
            <v-card-text class="white--text">
                {{ new Date().getFullYear() }} — <strong>Хакатон Труда</strong>
            </v-card-text>
        </div>
    </v-footer>
</template>

<script>
  export default {
    data: () => ({
      statusDay:false 
    }),
    
    mounted(){
        this.statusDay = this.$store.state.statusDay

        if(this.statusDay == null||this.statusDay == false)
            this.$vuetify.theme.dark = false
        else
            this.$vuetify.theme.dark = true  
    },
    
    methods:{
        Day(){      
              this.$store.commit('setStatusDay',this.statusDay)
              if(this.statusDay == null)
                  this.$vuetify.theme.dark = false
              else
                  this.$vuetify.theme.dark = true
        },
    }
  }
</script>