<template>
    <v-app id="inspire">
        
      <Header />

      <router-view></router-view>
      
      <Footer/>

    </v-app>
</template>

<script>

  import Header from '../components/Header'
  import Footer from '../components/Footer'
  
  export default {
      components:{
        Header,
        Footer
      },
  }
</script>
<style >

</style>








