<!-- eslint-disable max-len -->
<template>
  <div class="pt-5">
    <div id="promotionsModal" class="modal fade">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Restaurant Promotions</h2>
              <div class="row">
                <div class="col-lg-12 col-md-12 mb-4" v-for="promotion in promotions"
                  v-bind:key="String(promotion[0])">
                    <div class="card h-100">
                      <div class="card-body">
                        <h4 class="card-title mb-0 text-truncate">
                          {{promotion[6]}}
                        </h4>
                        <h6 class="text-muted">
                          {{promotion[8]}} {{promotion[8] > 1 ? 'days' : 'day'}} left
                        </h6>
                        <p class="card-text">{{promotion[7]}}</p>
                        <h5>
                          Discount: {{formatDiscount(promotion[2], promotion[3])}} OFF
                        </h5>
                        <h5 v-if="promotion[4] > 0">Minimum spend: ${{promotion[4]}}</h5>
                        <h5 v-if="promotion[5] > 0">
                          Discount Cap: {{promotion[6]}}
                        </h5>
                        <div class="input-group mt-3">
                          <input type="text" class="form-control" aria-label="Promotion Code" aria-describedby="basic-addon2" v-bind:value="promotion[1]" readonly>
                          <div class="input-group-append">
                            <button class="btn btn-outline-primary" type="button"
                            v-clipboard:copy="promotion[1]">
                              Copy to clipboard
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div id="cartModal" class="modal fade">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Cart</h2>
              <div class="form-row mb-2">
                <div class="col-md-2 font-weight-bold">Quantity</div>
                <div class="col-md-2 px-3 font-weight-bold">Price</div>
                <div class="col-md-6 px-3 font-weight-bold">Item Name</div>
                <div class="col-md-2 font-weight-bold"></div>
              </div>
              <div class="dropdown-divider"></div>
              <div class="form-row mt-2" v-for="(foodItem, index) in this.$store.state.cart"
              v-bind:key="foodItem.id">
                <div class="col-md-2">
                  <select class="form-control" v-model="foodItem.qty" @change="$store.commit('updateFoodItem')">
                    <option v-bind:key="x" v-bind:value="x" v-for="x in getRange(1, foodItem.orderlimit - foodItem.currentorders)">
                      {{x}}
                    </option>
                  </select>
                </div>
                <div class="col-md-2 px-3 pt-1 text-truncate">
                  ${{formatPrice(foodItem.price * foodItem.qty)}}
                </div>
                <div class="col-md-6 px-3 pt-1 text-truncate">{{foodItem.name}}</div>
                <div class="col-md-2">
                  <input type="button" class="btn btn-outline-danger float-right" value="Remove"
                  v-on:click="selectRemove(index)">
                </div>
              </div>
              <div class="dropdown-divider"></div>
              <div class="form-row mt-2">
                <div class="col-md-6">
                  <label for="colFormLabel" class="col-auto col-form-label">Promotion code</label>
                  <div class="input-group">
                    <input type="text" class="form-control" placeholder="Paste promotion code here." aria-label="Promotion code" aria-describedby="basic-addon2" v-model="promoCode">
                    <div class="input-group-append">
                      <button class="btn btn-outline-primary" v-on:click="selectApply()"
                      type="button">
                        Apply
                      </button>
                    </div>
                  </div>
                </div>
                <div class="col-md-6" v-if="$store.state.user.points">
                  <label for="colFormLabel" class="col-auto col-form-label">Redeem points</label>
                  <select class="form-control" v-model="$store.state.redeemPoint">
                    <option v-bind:key="x" v-bind:value="x"
                    v-for="x in getRange(0, Math.min($store.state.user.points, $store.state.restaurant.fee * 100))">
                      {{x}}
                    </option>
                  </select>
                </div>
                <small id="passwordHelpBlock" class="form-text text-danger pl-3" v-if="promoHint">
                  {{promoHint}}
                </small>
              </div>
              <div class="dropdown-divider"></div>
              <div class="form-row mt-2">
                <div class="col-md-12 font-weight-bold">
                  Delivery fee: ${{formatPrice(this.$store.state.restaurant.fee)}}
                </div>
              </div>
              <div class="form-row mt-2" v-if="$store.state.discount">
                <div class="col-md-12 font-weight-bold">
                  Discount: - ${{formatPrice(this.$store.state.discount)}}
                </div>
              </div>
              <div class="form-row mt-2" v-if="$store.state.redeemPoint">
                <div class="col-md-12 font-weight-bold">
                  Points Discount: - ${{formatPrice(this.$store.state.redeemPoint * 0.01)}}
                </div>
              </div>
              <div class="form-row mt-2">
                <div class="col-md-12 font-weight-bold">
                  Total price: ${{formatPrice(getTotalPrice() + this.$store.state.restaurant.fee - this.$store.state.discount - (this.$store.state.redeemPoint * 0.01))}}
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" data-dismiss="modal"
              v-on:click="selectCheckout()">Checkout</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div id="reviewsModal" class="modal fade">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Reviews</h2>
              <table class="table">
                <thead>
                  <tr class="row">
                    <th class="col-md-3">Date/Time</th>
                    <th class="col-md-2">Rating</th>
                    <th class="col-md-7">Description</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(review, index) in reviews" v-bind:key="index" class="row">
                    <td class="col-md-3">{{review[0]}}</td>
                    <td class="col-md-2">{{review[1]}}/5</td>
                    <td class="col-md-7 text-truncate">{{review[2]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <div class="navbar-brand">FastFoods</div>
        <button class="navbar-toggler" type="button" data-toggle="collapse"
        data-target="#navbarResponsive" aria-controls="navbarResponsive"
        aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link" v-on:click="selectRestaurants()">Restaurants</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" v-on:click="selectReviews()">Reviews</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" v-on:click="selectPromotions()">Promotions</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" v-on:click="showCartDialog()">Cart</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" v-on:click="selectSignOut()">Sign Out</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- Page Content -->
    <div class="container pt-2">
      <div class="row">
        <!-- NavBar -->
        <div class="col-lg-3">
            <h2 class="my-4">{{this.$store.state.restaurant.name}}</h2>
            <a data-toggle="modal" data-target="#cartModal" ref="cartToggle"></a>
            <a data-toggle="modal" data-target="#promotionsModal" ref="promotionsToggle"></a>
            <a data-toggle="modal" data-target="#reviewsModal" ref="reviewsToggle"></a>
            <div class="input-group mb-3">
              <input type="text" class="form-control" aria-label="Text input with dropdown button"
              placeholder="E.g. McDonalds" v-model="query">
              <div class="input-group-append">
                <button class="btn btn-primary" type="button" v-on:click="search(query)">
                  Search
                </button>
              </div>
            </div>
            <div class="list-group">
              <a class="list-group-item" v-on:click="filter('All')">All</a>
              <a class="list-group-item" v-for="type in types" :key="String(type[0])"
              v-on:click="filter(type[0])">
                {{type[0]}}
              </a>
            </div>
        </div>
        <!-- FoodItem List -->
        <div class="col-lg-9">
          <div class="row mt-4">
            <div class="col-md-6 mb-4" v-for="foodItem in foodItems"
            v-bind:key="Number(foodItem[0])">
              <div class="card h-100">
                <img class="card-img-top" src="http://placehold.it/700x400" alt />
                <div class="card-body">
                    <h4 class="card-title mb-0 text-truncate">
                      {{foodItem[2]}}
                    </h4>
                    <h6 class="text-muted">{{foodItem[6]}}</h6>
                    <p class="card-text">{{foodItem[3]}}</p>
                    <h5>Price: ${{formatPrice(foodItem[1])}}</h5>
                </div>
                <div class="card-footer">
                  <input type="button" value="Add to cart" v-on:click="selectAddToCart(foodItem)"
                  class="form-control btn btn-primary btn-lg">
                </div>
              </div>
          </div>
          </div>
          <!-- /.row -->
        </div>
        <!-- /.col-lg-9 -->
      </div>
      <!-- /.row -->
    </div>
    <!-- /.container -->

    <!-- Footer -->
    <Footer/>
  </div>
</template>

<script>
/* eslint-disable no-restricted-syntax */
// @ is an alias to /src
import axios from 'axios';
import Footer from '@/components/Footer.vue';

const apiBase = process.env.VUE_APP_DB_API_BASE;
const apiGetTypes = `${apiBase}/api/v1/fooditems/gettype`;
const apiGetList = `${apiBase}/api/v1/fooditems/getlist`;
const apiGetFilter = `${apiBase}/api/v1/fooditems/getfilter`;
const apiGetSearch = `${apiBase}/api/v1/fooditems/getsearch`;
const apiGetPromotions = `${apiBase}/api/v1/restaurantpromotions/getlist`;
const apiGetAppPromotion = `${apiBase}/api/v1/apppromotions/getentry`;
const apiGetRestPromotion = `${apiBase}/api/v1/restaurantpromotions/getentry`;
const apiGetReviews = `${apiBase}/api/v1/reviews/getlist`;

export default {
  name: 'Menu',
  components: {
    Footer,
  },
  created() {
  },
  mounted() {
    if (!this.$store.state.hasRestaurant) {
      this.$router.push('restaurant');
    }
    axios
      .get(apiGetTypes, {
        params: {
          id: this.$store.state.restaurant.id,
        },
      }).then((response) => {
        this.types = response.data;
        return axios.get(apiGetList, {
          params: {
            id: this.$store.state.restaurant.id,
          },
        });
      }).then((response) => {
        this.foodItems = response.data;
      }).catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  data() {
    return {
      dummy: '',
      types: '',
      foodItems: '',
      query: '',
      promotions: '',
      promoCode: '',
      promoHint: '',
      reviews: '',
    };
  },
  methods: {
    showCartDialog() {
      this.$refs.cartToggle.click();
    },
    getRange(start, stop) {
      return new Array(stop + 1 - start).fill(start).map((n, i) => n + i);
    },
    getTotalPrice() {
      let total = 0;
      for (const item of this.$store.state.cart) {
        total += item.price * item.qty;
      }
      return total;
    },
    formatPrice(value) {
      return value.toFixed(2).toString();
    },
    formatDiscount(type, value) {
      if (type === 'percent') {
        return `${value}%`;
      }
      return `$${value}`;
    },
    applyAppPromo(promo) {
      const type = 2;
      const value = 3;
      const min = 4;
      const max = 5;
      if (promo[type] === 'percent' && this.getTotalPrice() >= promo[min]) {
        const discount = this.$store.state.restaurant.fee * promo[value];
        if (promo[max] > 0) {
          this.$store.commit('updateDiscount', Math.min(discount, promo[max]));
        } else {
          this.$store.commit('updateDiscount', discount);
        }
      } else if (promo[type] === 'flat') {
        this.$store.commit('updateDiscount', promo[value]);
      }
    },
    applyRestPromo(data) {
      const promo = 0;
      const type = 2;
      const value = 3;
      const min = 4;
      const max = 5;
      const items = 1;
      const id = 0;
      const qty = 1;
      const cList = this.$store.state.cart;
      let discount = 0;
      let cItem;
      let pItem;
      if (data[promo][type] === 'percent' && this.getTotalPrice() >= data[promo][min]) {
        /* eslint-disable no-restricted-syntax */
        for (cItem of cList) {
          for (pItem of data[items]) {
            if (cItem.id === pItem[id]) {
              discount += cItem.price * Math.floor(cItem.qty / pItem[qty]) * data[promo][value];
              break;
            }
          }
        }
        if (data[promo][max] > 0) {
          this.$store.commit('updateDiscount', Math.min(discount, data[promo][max]));
        } else {
          this.$store.commit('updateDiscount', discount);
        }
      } else if (data[promo][type] === 'flat') {
        for (cItem of cList) {
          for (pItem of data[items]) {
            if (cItem === pItem[id]) {
              discount += Math.floor(cItem.qty / pItem[qty]) * data[promo][value];
              break;
            }
          }
        }
        if (data[promo][max] > 0) {
          this.$store.commit('updateDiscount', Math.min(discount, data[promo][max]));
        } else {
          this.$store.commit('updateDiscount', discount);
        }
      }
    },
    search(query) {
      if (query === '') { return; }
      axios
        .get(apiGetSearch, {
          params: {
            search: query,
            id: this.$store.state.restaurant.id,
          },
        }).then((response) => {
          this.foodItems = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      this.title = 'Search';
    },
    filter(type) {
      if (type === 'All') {
        axios
          .get(apiGetList, {
            params: {
              id: this.$store.state.restaurant.id,
            },
          })
          .then((response) => {
            this.foodItems = response.data;
          }).catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          });
      } else {
        axios
          .get(apiGetFilter, {
            params: {
              category: type,
              id: this.$store.state.restaurant.id,
            },
          }).then((response) => {
            this.foodItems = response.data;
          }).catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          });
      }
    },
    selectPromotions() {
      axios
        .get(apiGetPromotions, {
          params: {
            id: this.$store.state.restaurant.id,
          },
        }).then((response) => {
          this.promotions = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$refs.promotionsToggle.click();
    },
    selectRestaurants() {
      this.$router.push('restaurant');
      this.$store.commit('emptyCart');
    },
    selectReviews() {
      axios
        .get(apiGetReviews, {
          params: {
            id: this.$store.state.restaurant.id,
          },
        }).then((response) => {
          this.reviews = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      this.$refs.reviewsToggle.click();
    },
    selectSignOut() {
      this.$store.commit('reset');
      this.$router.push('login');
    },
    selectAddToCart(foodItem) {
      for (let i = 0; i < this.$store.state.cart.length; i += 1) {
        if (this.$store.state.cart[i].id === foodItem[0]) {
          this.showCartDialog();
          return;
        }
      }
      this.$store.commit('addFoodItem', {
        id: foodItem[0],
        price: foodItem[1],
        name: foodItem[2],
        description: foodItem[3],
        orderlimit: foodItem[4],
        currentorders: foodItem[5],
        category: foodItem[6],
        qty: 1,
      });
      this.showCartDialog();
    },
    selectRemove(arrayIndex) {
      this.$store.commit('deleteFoodItem', arrayIndex);
    },
    selectApply() {
      if (this.promoCode.charAt(0) === 'A') {
        axios
          .get(apiGetAppPromotion, {
            params: {
              id: this.$store.state.user.id,
              code: this.promoCode,
            },
          }).then((response) => {
            if ((typeof response.data) === 'string') {
              this.promoHint = response.data;
            } else {
              this.promoHint = '';
              this.applyAppPromo(response.data);
            }
          }).catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      } else if (this.promoCode.charAt(0) === 'R') {
        axios
          .get(apiGetRestPromotion, {
            params: {
              id: this.$store.state.restaurant.id,
              code: this.promoCode,
            },
          }).then((response) => {
            if ((typeof response.data) === 'string') {
              this.promoHint = response.data;
            } else {
              this.promoHint = '';
              this.applyRestPromo(response.data);
            }
          }).catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
    selectCheckout() {
      this.$router.push('checkout');
    },
  },
};
</script>

<style scoped>
a:hover {
  cursor: pointer;
}

.dropdown-item, .list-group-item {
    cursor: pointer;
}

.card {
  cursor: default;
}

.list-group-item:hover {
  background-color: #f8f9fa;
}

.table {
    table-layout: fixed;
}
</style>
