import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'
import RegisterView from '@/components/RegisterView.vue'
import Menu from '@/components/Menu.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: RegisterView
    },
    {
      path: '/home',
      name: 'home',
      component: Menu,
        children:[
          {
            path:'/dashboard', name:'dashboard', component: RegisterView
          },
          {
            path:'/sucursal', name:'sucursal', component: RegisterView
          },
          {
            path:'/dietas', name:'dietas', component: RegisterView
          },
          {
            path:'/preguntaNutricional', name:'preguntaNutricional', component: RegisterView
          },
          {
            path:'/valoracionNutricional', name:'valoracionNutricional', component: RegisterView
          },
          {
            path:'/ejercicios', name:'ejercicios', component: RegisterView
          },
          {
            path:'/rutinas', name:'rutinas', component: RegisterView
          },
          {
            path:'/programaSaludable', name:'programaSaludable', component: RegisterView
          },
          {
            path:'/rutinasEjercicios', name:'rutinasEjercicios', component: RegisterView
          },
          {
            path:'/detalleProgramas', name:'detalleProgramas', component: RegisterView
          },
          {
            path:'/equipamiento', name:'equipamiento', component: RegisterView
          },
          {
            path:'/prestamos', name:'prestamos', component: RegisterView
          },
          {
            path:'/membresias', name:'membresias', component: RegisterView
          },
          {
            path:'/miembros', name:'miembros', component: RegisterView
          },
          {
            path:'/personas', name:'personas', component: RegisterView
          },
          {
            path:'/areas', name:'areas', component: RegisterView
          },
          {
            path:'/puestos', name:'puestos', component: RegisterView
          },
          {
            path:'/empleados', name:'empleados', component: RegisterView
          },
          {
            path:'/instructores', name:'intructores', component: RegisterView
          },
          {
            path:'/horarios', name:'horarios', component: RegisterView
          },
          {
            path:'/sucursal', name:'sucursal', component: RegisterView
          },
          {
            path:'/instalaciones', name:'instalaciones', component: RegisterView
          },
          {
            path:'/mantenimiento', name:'mantenimiento', component: RegisterView
          },
          
        ]
    },
  ]
})

export default router
