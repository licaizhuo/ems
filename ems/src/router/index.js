import Vue from 'vue'
import Router from 'vue-router'
import login from "../components/login";
import register from "../components/register";
import emplist from "../components/emplist";
import addEmp from "../components/addEmp";
import updateEmp from "../components/updateEmp";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/emp',
      name: 'emplist',
      component: emplist
    },
    {
      path: '/add',
      name: 'addemp',
      component: addEmp
    },
    {
      path: '/update',
      name: 'updateemp',
      component: updateEmp
    },
    {
      path: '/update/:id/:index',
      name: 'updateemp',
      component: updateEmp
    },
    {
      path: '/*',
      name: 'login',
      component: login
    },
  ]
})
