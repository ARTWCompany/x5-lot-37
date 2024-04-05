import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from './plugins/axios'
import { createPinia } from 'pinia'

// region Vuetify
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import "@/assets/styles/global.scss"
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
// endregion

const vuetify = createVuetify({
  components,
  directives,
})

const pinia = createPinia()

import PortalVue from 'portal-vue'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

createApp(App)
  .use(router)
  .use(axios, {
    baseUrl: '/'
  })
  .use(PortalVue)
  .use(vuetify)
  .use(pinia)
  .mount('#app')
