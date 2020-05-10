import Vue from 'vue';
import VueRouter from 'vue-router';
import LogIn from '../views/LogIn.vue';
import SignUp from '../views/SignUp.vue';
import Profile from '../views/Profile.vue';
import Location from '../views/Location.vue';
import Restaurant from '../views/Restaurant.vue';
import Menu from '../views/Menu.vue';
import Checkout from '../views/Checkout.vue';
import StaffLogin from '../views/StaffLogin.vue';
import RestaurantAdmin from '../views/RestaurantAdmin.vue';
import Rider from '../views/Rider.vue';
import FDS from '../views/Fds.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '*',
    redirect: '/login',
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/location',
    name: 'Location',
    component: Location,
  },
  {
    path: '/restaurant',
    name: 'Restaurant',
    component: Restaurant,
  },
  {
    path: '/menu',
    name: 'Menu',
    component: Menu,
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: Checkout,
  },
  {
    path: '/stafflogin',
    name: 'StaffLogin',
    component: StaffLogin,
  },
  {
    path: '/restaurantadmin',
    name: 'RestaurantAdmin',
    component: RestaurantAdmin,
  },
  {
    path: '/rider',
    name: 'Rider',
    component: Rider,
  },
  {
    path: '/fds',
    name: 'FDS',
    component: FDS,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
