<template>
    <v-app id="inspire" >
        <v-content >
            <v-container
                class="fill-height"
                fluid
            >
                <v-row
                    align="center"
                    justify="center"
                >
                    <v-col
                        cols="12"
                        sm="8"
                        md="5"
                        lg="4"
                        xl="3"
                    >
                        <v-card class="elevation-12">
                            <v-toolbar
                               color="grey darken-3"
                                dark
                                flat
                            >
                             <v-toolbar-title style="color:rgb(0,252,252)" class="pl-md-0 pl-5 " > <b>Регистрация</b></v-toolbar-title>
                              <v-spacer></v-spacer>
                              <router-link  to="/"  style="font-size:15px;text-decoration: none;color:rgb(0,252,252">
                             <v-btn
                                icon
                                color="rgb(0,252,252)"
                                fab
                                >
                                   <v-icon>mdi-exit-to-app</v-icon>
                                </v-btn>
                                </router-link>
                            </v-toolbar>

                            <v-card-text>
                                <v-form
                                    ref="form"
                                    v-model="valid"
                                    lazy-validation
                                >
                                    <v-text-field
                                        v-model="name"
                                        :counter="20"
                                        :rules="nameRules"
                                        label="Уникальное имя"
                                        required
                                    ></v-text-field>

                                    <v-text-field
                                        v-model="email"
                                        :rules="emailRules"
                                        label="E-mail"
                                        required
                                    ></v-text-field>

                                    <v-text-field
                                        :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                                        :rules="passwordRules"
                                        :type="show ? 'text' : 'password'"
                                        name="input-10-2"
                                        label="Пароль"
                                        hint="Минимум 8 символов"
                                        v-model="password"
                                        required
                                        class="input-group--focused"
                                        @click:append="show = !show"
                                    ></v-text-field>

                                    <div class="text-right w-100">
                                        <v-btn 
                                            :disabled="!valid"
                                            color="rgb(0,252,252)"
                                            class="mr-4 align-self-end  "
                                            @click="validate"
                                        >
                                        <b style="color:rgb(66,66,66)">Подтвердить</b>
                                        </v-btn>
                                    </div>
                                </v-form>
                            <v-spacer></v-spacer>
                            <div class="text-center mt-2 w-100">
                                <router-link to="/login" class="px-5" style="font-size:15px">Войти</router-link>
                            </div>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-content>
  </v-app>
</template>

<script>

  export default {
      props: {
          source: String,
      },
      data: () => ({
          show:false,
          valid: false,
          name: '',
          password: '',
          passwordRules: [
              v => !!v || 'Обязательное поле',
              v => (v.length >= 8) || 'Минимум 8 символов',
          ],
          nameRules: [
              v => !!v || 'Обязательное поле',
              v => (v && v.length <= 20) || 'Имя не может быть длинее 20 символов',
          ],
          email: '',
          emailRules: [
              v => !!v || 'Обязательное поле',
              v => /.+@.+\..+/.test(v) || 'E-mail должен быть корректным',
          ],
        }),

        methods: {
            validate () {
                if(this.password){
                    let data = {
                        name : this.name,
                        password: this.password,
                        email : this.email
                    }
                    this.$store.dispatch("SignUp",data)
                }
                this.$refs.form.validate()
            }, 
        },
    }
</script>