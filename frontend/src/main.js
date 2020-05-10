import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import 'jquery';
import Vue from 'vue';
import VueClipboard from 'vue-clipboard2';
import App from './App.vue';
import store from './store/index';
import router from './router';

Vue.use(VueClipboard);
Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount('#app');
