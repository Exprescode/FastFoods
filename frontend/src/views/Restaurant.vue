<!-- eslint-disable max-len -->
<template>
  <div class="pt-5">
    <div id="promotionsModal" class="modal fade">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>App Promotions</h2>
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
                            Discount: {{formatDiscount(promotion[2], promotion[3])}}
                            OFF Delivery Fee
                          </h5>
                          <h5 v-if="promotion[4] > 0">Minimum spend: ${{promotion[4]}}</h5>
                          <h5 v-if="promotion[5] > 0">
                            Discount Cap: {{promotion[6]}}
                          </h5>
                          <div class="input-group mt-3">
                          <input type="text" class="form-control" aria-label="Promotion Code"
                          aria-describedby="basic-addon2" v-bind:value="promotion[1]" readonly>
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
    <div id="ordersModal" class="modal fade">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Orders</h2>
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Order Date/Time</th>
                    <th scope="col">Status</th>
                    <th scope="col">Status Date/Time</th>
                    <th scope="col"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(order, index) in orders" v-bind:key="index">
                    <th scope="row">{{index + 1}}</th>
                    <td>{{order[2]}}</td>
                    <td>{{formatStatus(order[3])}}</td>
                    <td>{{order[4]}}</td>
                    <td v-if="order[3] == 'completed' && order[1] == null">
                      <input type="button" class="btn btn-outline-success float-right" value="Write a review" v-on:click="selectReview(order[0])">
                    </td>
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
    <div id="reviewModal" class="modal fade">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Review</h2>
              <h4>How would you rate {{review.restaurantName}}?</h4>
              <form class="mt-3">
                <div class="form-group row">
                  <label for="selectRating" class="col-sm-2 col-form-label">Rating</label>
                  <div class="col-auto">
                    <select class="form-control" id="selectRating" v-model="review.rating">
                      <option v-bind:key="x" v-bind:value="x" v-for="x in getRange(1, 5)">
                        {{x}}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="form-group row">
                  <label for="inputDescription" class="col-sm-2 col-form-label">Description</label>
                  <div class="col-sm-10">
                    <input type="text" class="form-control" id="inputDescription" placeholder="Write your review here." v-model="review.description">
                  </div>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" data-dismiss="modal"
              v-on:click="selectPublish()">Publish</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div id="reviewMsgModal" class="modal fade">
      <div class="modal-dialog modal-md">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Info</h2>
              {{review.msg}}
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
              <a class="nav-link" v-on:click="selectLocation()">Location</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" v-on:click="selectPromotions()">Promotions</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" v-on:click="selectOrders()">Orders</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
              data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Account
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" v-on:click="selectProfile()">Profile</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" v-on:click="selectSignOut()">Sign Out</a>
              </div>
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
            <h2 class="my-4">Restaurants</h2>
            <a data-toggle="modal" data-target="#promotionsModal" ref="promotionsToggle"></a>
            <a data-toggle="modal" data-target="#ordersModal" ref="ordersToggle"></a>
            <a data-toggle="modal" data-target="#reviewModal" ref="reviewToggle"></a>
            <a data-toggle="modal" data-target="#reviewMsgModal" ref="reviewMsgToggle"></a>
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
        <!-- Restaurant List -->
        <div class="col-lg-9 list">
          <div class="row mt-4">
            <div class="col-lg-4 col-md-6 mb-4" v-for="restaurant in restaurants"
            v-bind:key="String(restaurant[0])">
              <div class="card h-100">
                  <img class="card-img-top" src="http://placehold.it/700x400" alt />
                  <div class="card-body">
                      <h4 class="card-title mb-0 text-truncate">
                        {{restaurant[1]}}
                      </h4>
                      <h6 class="text-muted">{{restaurant[3]}}</h6>
                      <h5>Fee: ${{formatPrice(restaurant[4])}}</h5>
                  </div>
                  <div class="card-footer">
                  <input type="button" value="Menu" v-on:click="selectRestaurant(restaurant)"
                  class="form-control btn btn-primary">
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
// @ is an alias to /src
import axios from 'axios';
import Footer from '@/components/Footer.vue';

const apiGetTypes = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/gettype`;
const apiGetRestaurants = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/getlist`;
const apiGetFilter = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/getfilter`;
const apiGetSearch = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/getsearch`;
const apiGetPromotions = `${process.env.VUE_APP_DB_API_BASE}/api/v1/apppromotions/getlist`;
const apiGetOrders = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getlist`;
const apiGetRestaurantName = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getrestaurantname`;
const apiAddReview = `${process.env.VUE_APP_DB_API_BASE}/api/v1/reviews/addreview`;

export default {
  name: 'Restaurant',
  components: {
    Footer,
  },
  created() {
    this.$store.commit('setRestaurant');
    if (!this.$store.state.hasLocation) {
      this.$router.push('location');
    }
    axios
      .get(apiGetTypes)
      .then((response) => {
        this.types = response.data;
        return axios.get(apiGetRestaurants, {
          params: {
            area: this.$store.state.location.area,
          },
        });
      }).then((response) => {
        this.restaurants = response.data;
      }).catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  mounted() {
  },
  data() {
    return {
      dummy: '',
      types: '',
      restaurants: '',
      query: '',
      promotions: '',
      orders: '',
      review: '',
    };
  },
  methods: {
    getRange(start, stop) {
      return new Array(stop + 1 - start).fill(start).map((n, i) => n + i);
    },
    formatPrice(value) {
      return value.toFixed(2).toString();
    },
    formatDiscount(type, value) {
      if (type === 'percent') {
        return `${value * 100}%`;
      }
      return `$${value}`;
    },
    formatStatus(status) {
      switch (status) {
        case 'ordered':
          return 'Processing order';
        case 'torest':
          return 'On route to restaurant';
        case 'atrest':
          return 'Collecting package';
        case 'tocust':
          return 'On route to destination';
        case 'completed':
          return 'Completed';
        default:
          return 'System error';
      }
    },
    search(query) {
      if (query === '') { return; }
      axios
        .get(apiGetSearch, {
          params: {
            search: query,
            area: this.$store.state.location.area,
          },
        }).then((response) => {
          this.restaurants = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      this.title = 'Search';
    },
    filter(type) {
      if (type === 'All') {
        axios
          .get(apiGetRestaurants, {
            params: {
              area: this.$store.state.location.area,
            },
          })
          .then((response) => {
            this.restaurants = response.data;
          }).catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          });
      } else {
        axios
          .get(apiGetFilter, {
            params: {
              category: type,
              area: this.$store.state.location.area,
            },
          }).then((response) => {
            this.restaurants = response.data;
          }).catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          });
      }
    },
    selectRestaurant(restaurant) {
      this.$store.commit('addRestaurant', {
        id: restaurant[0],
        name: restaurant[1],
        type: restaurant[2],
        location: restaurant[3],
        fee: restaurant[4],
      });
      this.$router.push('menu');
    },
    selectLocation() {
      this.$router.push('location');
    },
    selectPromotions() {
      axios
        .get(apiGetPromotions)
        .then((response) => {
          this.promotions = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$refs.promotionsToggle.click();
    },
    selectOrders() {
      axios
        .get(apiGetOrders, {
          params: {
            id: this.$store.state.user.id,
          },
        }).then((response) => {
          this.orders = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$refs.ordersToggle.click();
    },
    selectReview(orderId) {
      const restNameIndex = 0;
      this.$refs.ordersToggle.click();
      this.review = {
        id: orderId,
        restaurantName: '',
        rating: 5,
        description: '',
        msg: '',
      };
      axios
        .get(apiGetRestaurantName, {
          params: {
            id: orderId,
          },
        }).then((response) => {
          this.review.restaurantName = response.data[restNameIndex];
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$refs.reviewToggle.click();
    },
    selectPublish() {
      axios
        .post(apiAddReview, {
          id: this.review.id,
          rating: this.review.rating,
          description: this.review.description,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.review.msg = 'Your review has published successfully.';
          } else {
            this.review.msg = 'An error has occured please try again later.';
          }
          this.$refs.reviewMsgToggle.click();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectProfile() {
      this.$router.push('profile');
    },
    selectSignOut() {
      this.$store.commit('reset');
      this.$router.push('login');
    },
  },
};
</script>

<style scoped>
a:hover {
  cursor: pointer;
}

.dropdown-item, .list-group-item, .list .card-body {
    cursor: pointer;
}

.list-group-item:hover {
  background-color: #f8f9fa;
}
</style>
