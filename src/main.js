import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Importing Bootstrap 5 CSS
import 'bootstrap/dist/css/bootstrap.min.css'

// Optionally, import Bootstrap 5 JS if needed
import 'bootstrap/dist/js/bootstrap.js'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faTable, faSquarePollVertical, faHeart, faAngleDoubleLeft } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faTable, faSquarePollVertical, faHeart, faAngleDoubleLeft)

const app = createApp(App)

app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
