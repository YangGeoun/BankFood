
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VTooltip from 'v-tooltip'

import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(VTooltip)
app.use(createPinia())
app.use(router)

app.mount('#app')
