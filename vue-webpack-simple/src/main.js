import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import App from './App.vue'
import registerRouter from './router'

var app = Vue.extend({})

Vue.use(VueRouter)
Vue.use(VueResource)

Vue.http.options.root = 'http://192.168.0.33:7001/gds'

// Vue.http.interceptors.push({
//     response(response){
//         if(response.data.stat===1){
//             return response.data.result;
//         }else {
//             throw {'name': 'Response Error', 'msg': `stat error ${response.data.stat}`}
//         }
//     }
// })

var router = new VueRouter({
    linkActiveClass: 'active'
})

registerRouter(router)

router.start(app, 'body')