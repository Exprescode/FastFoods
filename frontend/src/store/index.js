import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersist from 'vuex-persist';

Vue.use(Vuex);

const vuexPersist = new VuexPersist({
  key: 'fastfoods',
  storage: window.sessionStorage,
});

export default new Vuex.Store({
  state: {
    hasUser: false,
    user: null,
    hasLocation: false,
    location: null,
    hasRestaurant: false,
    restaurant: null,
    hasCart: false,
    cart: [],
    discount: 0,
    redeemPoint: 0,
  },
  mutations: {
    reset(state) {
      state.hasUser = false;
      state.user = null;
      state.hasLocation = false;
      state.location = null;
      state.hasRestaurant = false;
      state.restaurant = null;
      state.cart = [];
      state.discount = 0;
      state.redeemPoint = 0;
    },
    setLocation(state) {
      state.hasLocation = false;
      state.location = null;
      state.hasRestaurant = false;
      state.restaurant = null;
      state.cart = [];
      state.discount = 0;
      state.redeemPoint = 0;
    },
    setRestaurant(state) {
      state.hasRestaurant = false;
      state.restaurant = null;
      state.cart = [];
      state.discount = 0;
      state.redeemPoint = 0;
    },
    addUser(state, user) {
      state.user = user;
      state.hasUser = true;
    },
    updateUser(state, updates) {
      state.user.email = updates.email;
      state.user.name = updates.name;
      state.user.phone = updates.phone;
      state.user.card = updates.card;
    },
    addLocation(state, location) {
      state.location = location;
      state.hasLocation = true;
    },
    addRestaurant(state, restaurant) {
      state.hasRestaurant = true;
      state.restaurant = restaurant;
    },
    addFoodItem(state, foodItem) {
      state.cart.push(foodItem);
      state.discount = 0;
    },
    deleteFoodItem(state, arrayIndex) {
      state.cart.splice(arrayIndex, 1);
      state.discount = 0;
    },
    updateFoodItem(state) {
      state.discount = 0;
    },
    emptyCart(state) {
      state.cart = [];
    },
    updateDiscount(state, value) {
      state.discount = value;
    },
    resetDiscount(state) {
      state.discount = 0;
    },
    resetRedeemPoint(state) {
      state.discount = 0;
    },
  },
  plugins: [vuexPersist.plugin],
});
