import {
  createRouter,
  createWebHistory
} from 'vue-router'
import {useAuthStore} from "@/stores/auth";
import {computed} from "vue";
import {useAuthClientService} from "@/shared/api/Auth/Auth.service";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../pages/LoginPage.vue'),
    },
    {
      path: '',
      name: 'root',
      component: () => import('../layouts/UserLayout.vue'),
      children: [
        {
          path: 'list',
          name: 'Список пользователей',
          component: () => import('../pages/@users/UsersListPage.vue')
        },
        {
          path: 'statistics',
          name: 'Статистика',
          component: () => import('../pages/@users/UsersStatisticsPage.vue')
        },
        {
          path: 'company',
          name: 'Компании',
          component: () => import('../pages/@users/UsersCompanyPage.vue')
        },
        {
          path: 'api-clients',
          name: 'Клиенты API',
          component: () => import('../pages/@users/UsersApiPage.vue')
        },
        {
          path: 'settings',
          name: 'Настройки',
          component: () => import('../pages/@users/UsersSettingsPage.vue')
        },
      ],
    },
  ]
})

router.beforeEach(async (to, from, next) => {
  const store = useAuthStore();
  const AuthService = useAuthClientService(store);
  await AuthService.restoreAuth();

  if ((to.name === 'login' || to.name === 'root') && store.isAuthenticated) {
    next({name: 'Список пользователей'})
  }
  if (to.name !== 'login' && !store.isAuthenticated) {
      next({name: 'login'})
  } else next()
})

export default router
