<!-- eslint-disable max-len -->
<template>
  <div class="pt-5">
    <div id="pwdModal" class="modal fade"  tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Change Password</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group">
                  <label for="inputOldPassword">Current Password</label>
                  <input type="password" class="form-control" id="inputOldPassword" placeholder="Enter current password here." v-model="password.old">
                </div>
                <div class="form-group">
                  <label for="inputNewPassword">New Password</label>
                  <input type="password" class="form-control" id="inputNewPassword" placeholder="Enter new password here."  v-model="password.new">
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectChangePassword()">Change</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="msgModal" class="modal fade"  tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">{{dialog.title}}</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <p>{{this.dialog.msg}}</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="favModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Favourites</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th scope="col">Ranking</th>
                    <th scope="col">Name</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(entry, index) in orderSummaryFavorite"
                  v-bind:key="index">
                    <td>{{index + 1}}</td>
                    <td>{{entry[0]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="menuModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">{{editFoodItem[0] ? 'Edit Menu' : 'New Menu'}}</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label for="inputPrice">Price</label>
                    <input type="text" class="form-control" id="inputPrice" v-model="editFoodItem[1]">
                  </div>
                  <div class="form-group col-md-6">
                    <label for="inputLimit">Limit</label>
                    <input type="text" class="form-control" id="inputLimit" v-model="editFoodItem[4]">
                  </div>
                </div>
                <div class="form-group">
                  <label for="inputName">Name</label>
                  <input type="text" class="form-control" id="inputName" v-model="editFoodItem[2]">
                </div>
                <div class="form-group">
                  <label for="inputDescription">Description</label>
                  <input type="text" class="form-control" id="inputDescription" v-model="editFoodItem[3]">
                </div>
                <div class="form-group">
                  <label for="inputCategory">Category</label>
                  <input type="text" class="form-control" id="inputCategory" v-model="editFoodItem[6]">
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectMenuAdd()" v-if="!editFoodItem[0]">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectMenuUpdate()" v-if="editFoodItem[0]">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectMenuDelete()" v-if="editFoodItem[0]">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
            </div>
        </div>
      </div>
    </div>
    <div id="promotionsModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">{{editPromo[0] ? 'Edit Promotion' : 'New Promotion'}}</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label for="inputStartDate">Start date</label>
                    <input type="text" class="form-control" id="inputStartDate" v-model="editPromo[9]">
                  </div>
                  <div class="form-group col-md-6">
                    <label for="inputEndDate">End date</label>
                    <input type="text" class="form-control" id="inputEndDate" v-model="editPromo[10]">
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label for="selectType">Discount type</label>
                    <select class="custom-select" v-model="editPromo[2]">
                      <option value="percent">Percent</option>
                      <option value="flat">Fixed</option>
                    </select>
                  </div>
                  <div class="form-group col-md-6">
                    <label for="inputValue">Discount value</label>
                    <input type="text" class="form-control" id="inputValue" v-model="editPromo[3]">
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label for="inputMin">Discount min order</label>
                    <input type="text" class="form-control" id="inputMin" v-model="editPromo[4]">
                  </div>
                  <div class="form-group col-md-6">
                    <label for="inputMax">Discount max value</label>
                    <input type="text" class="form-control" id="inputMax" v-model="editPromo[5]">
                  </div>
                </div>
                <div class="form-group">
                  <label for="inputName2">Name</label>
                  <input type="text" class="form-control" id="inputName2" v-model="editPromo[6]">
                </div>
                <div class="form-group">
                  <label for="inputDescription2">Description</label>
                  <input type="text" class="form-control" id="inputDescription2" v-model="editPromo[7]">
                </div>
                <div class="form-group">
                  <label>Promotion Items</label>
                  <div class="input-group mt-1" v-for="(item, index) in foodItems" v-bind:key="index">
                    <input type="text" class="form-control col-2" v-model="editPromoQty[item[0]]">
                    <div class="input-group-append col-10 px-0">
                      <span class="input-group-text col text-truncate">{{item[2]}}</span>
                    </div>
                  </div>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectPromoAdd()" v-if="!editPromo[0]">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectPromoUpdate()" v-if="editPromo[0]">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectPromoDelete()" v-if="editPromo[0]">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
            </div>
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
              <a class="nav-link" data-toggle="modal" data-target="#pwdModal">Change Password</a>
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
        <div class="col-lg-3 mb-4">
            <h2 class="my-4">Restaurants</h2>
            <a data-toggle="modal" data-target="#msgModal" ref="msgToggle"></a>
            <a data-toggle="modal" data-target="#favModal" ref="favToggle"></a>
            <a data-toggle="modal" data-target="#menuModal" ref="menuToggle"></a>
            <a data-toggle="modal" data-target="#promotionsModal" ref="promotionsToggle"></a>
            <div class="list-group">
              <a class="list-group-item" v-on:click="selectNavOrders()">Orders</a>
              <a class="list-group-item" v-on:click="selectNavOrderSummary()">Order Summary</a>
              <a class="list-group-item" v-on:click="selectNavMenu()">Menu</a>
              <a class="list-group-item" v-on:click="selectNavPromotions()">Promotions</a>
              <a class="list-group-item" v-on:click="selectNavPromotionSummary()">Promotion Summary</a>
            </div>
        </div>
        <!-- Restaurant List -->
        <div class="col-lg-9 list">
          <div class="row mt-4">
            <div class="table-responsive">
              <table class="table table-hover" v-if="view=='ordersummary'">
                <thead>
                  <tr>
                    <th scope="col">Year</th>
                    <th scope="col">Month</th>
                    <th scope="col">No. Orders</th>
                    <th scope="col">Total Cost</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(entry, index) in orderSummary" v-bind:key="index" v-on:click="selectNavOrderSummaryEntry(entry[1],entry[0])">
                    <td>{{entry[0]}}</td>
                    <td>{{formatMonth(entry[1])}}</td>
                    <td>{{entry[2]}}</td>
                    <td>${{formatPrice(entry[3])}}</td>
                  </tr>
                </tbody>
              </table>
              <table class="table table-striped" v-if="view=='promotionsummary'">
                <thead>
                  <tr>
                    <th scope="col">Promotion Name</th>
                    <th scope="col">No. Day(s)</th>
                    <th scope="col">Orders per Day</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(entry, index) in promotionSummary"
                  v-bind:key="index">
                    <td>{{entry[0]}}</td>
                    <td>{{entry[1]}}</td>
                    <td>{{entry[2]}}</td>
                  </tr>
                </tbody>
              </table>
              <table class="table table-striped" v-if="view=='orders'">
                <thead>
                  <tr>
                    <th scope="col">Order ID</th>
                    <th scope="col">Date/Time</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Item</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in orderItems"
                  v-bind:key="index">
                    <td>{{item[0]}}</td>
                    <td>{{item[1]}}</td>
                    <td>{{item[2]}}</td>
                    <td>{{item[3]}}</td>
                  </tr>
                </tbody>
              </table>
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Add new item" v-if="view=='menu'" v-on:click="selectMenuNew()">
              <table class="table table-hover" v-if="view=='menu'">
                <thead>
                  <tr>
                    <th scope="col">Price</th>
                    <th scope="col">Name</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(item, index) in foodItems"
                  v-bind:key="index" v-on:click="selectMenuEntry(item)">
                    <td >${{formatPrice(item[1])}}</td>
                    <td>{{item[2]}}</td>
                  </tr>
                </tbody>
              </table>
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Add new promotion" v-if="view=='promotions'" v-on:click="selectPromoNew()">
              <table class="table table-hover" v-if="view=='promotions'">
                <thead>
                  <tr>
                    <th scope="col">Start Date/Time</th>
                    <th scope="col">End Date/Time</th>
                    <th scope="col">Name</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(promo, index) in promotions"
                  v-bind:key="index" v-on:click="selectPromoEntry(promo)">
                    <td>{{promo[9]}}</td>
                    <td>{{promo[10]}}</td>
                    <td>{{promo[6]}}</td>
                  </tr>
                </tbody>
              </table>
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

const apiUpdatePassword = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantstaff/updatepassword`;
const apiOrderSummary = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getrestaurantsummary`;
const apiOrderSummaryFavorite = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getrestaurantsummaryfavorite`;
const apiPromotionSummary = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantpromotions/getrestaurantsummary`;
const apiGetOrders = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getrestaurantlist`;
const apiGetFoodItems = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fooditems/getlist`;
const apiAddFoodItem = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fooditems/additem`;
const apiUpdateFoodItem = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fooditems/updateitem`;
const apiDeleteFoodItem = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fooditems/deleteitem`;
const apiGetPromotions = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantpromotions/getlist`;
const apiGetPromoItems = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantpromotionitems/getlist`;
const apiAddPromotion = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantpromotions/addpromo`;
const apiUpdatePromotion = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantpromotions/updatepromo`;
const apiDeletetPromotion = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantpromotions/deletepromo`;

export default {
  name: 'RestaurantAdmin',
  components: {
    Footer,
  },
  mounted() {
    if (!this.$store.state.user || this.$store.state.user.type !== 'restaurant') {
      this.$router.push('stafflogin');
    }
    this.selectNavOrders();
  },
  data() {
    return {
      view: 'orders',
      orderSummary: '',
      orderSummaryFavorite: {},
      promotionSummary: '',
      orderItems: '',
      foodItems: '',
      editFoodItem: '',
      promotions: '',
      editPromo: '',
      editPromoQty: {},
      dialog: {
        title: '',
        msg: '',
      },
      password: {
        old: '',
        new: '',
      },
    };
  },
  methods: {
    formatPrice(value) {
      if (typeof value === 'string') {
        /* eslint-disable no-param-reassign */
        value = parseFloat(value);
      }
      return value.toFixed(2).toString();
    },
    formatMonth(intMonth) {
      const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      return months[intMonth - 1] || '';
    },
    populateFoodItems() {
      axios
        .get(apiGetFoodItems, {
          params: {
            id: this.$store.state.user.restaurantId,
          },
        }).then((response) => {
          this.foodItems = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectNavOrderSummary() {
      axios
        .get(apiOrderSummary, {
          params: {
            id: this.$store.state.user.restaurantId,
          },
        }).then((response) => {
          this.orderSummary = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.view = 'ordersummary';
    },
    selectNavOrderSummaryEntry(mth, yr) {
      axios
        .get(apiOrderSummaryFavorite, {
          params: {
            id: this.$store.state.user.restaurantId,
            month: mth,
            year: yr,
          },
        }).then((response) => {
          this.orderSummaryFavorite = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$refs.favToggle.click();
    },
    selectNavPromotionSummary() {
      axios
        .get(apiPromotionSummary, {
          params: {
            id: this.$store.state.user.restaurantId,
          },
        }).then((response) => {
          this.promotionSummary = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.view = 'promotionsummary';
    },
    selectNavOrders() {
      axios
        .get(apiGetOrders, {
          params: {
            id: this.$store.state.user.restaurantId,
          },
        }).then((response) => {
          this.orderItems = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.view = 'orders';
    },
    selectNavMenu() {
      this.populateFoodItems();
      this.view = 'menu';
    },
    selectNavPromotions() {
      axios
        .get(apiGetPromotions, {
          params: {
            id: this.$store.state.user.restaurantId,
          },
        }).then((response) => {
          this.promotions = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.view = 'promotions';
    },
    selectMenuNew() {
      this.editFoodItem = new Array(7);
      this.$refs.menuToggle.click();
    },
    selectMenuAdd() {
      axios
        .post(apiAddFoodItem, {
          id: this.$store.state.user.restaurantId,
          price: this.editFoodItem[1],
          limit: this.editFoodItem[4],
          name: this.editFoodItem[2],
          description: this.editFoodItem[3],
          category: this.editFoodItem[6],
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Item added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input! Item not added.';
          }
          this.$refs.msgToggle.click();
          this.selectNavMenu();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectMenuEntry(foodItem) {
      this.editFoodItem = foodItem;
      this.$refs.menuToggle.click();
    },
    selectMenuUpdate() {
      axios
        .post(apiUpdateFoodItem, {
          id: this.editFoodItem[0],
          price: this.editFoodItem[1],
          limit: this.editFoodItem[4],
          name: this.editFoodItem[2],
          description: this.editFoodItem[3],
          category: this.editFoodItem[6],
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Item updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input! Update not successful.';
          }
          this.$refs.msgToggle.click();
          this.selectNavMenu();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectMenuDelete() {
      axios
        .post(apiDeleteFoodItem, {
          id: this.editFoodItem[0],
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Item deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavMenu();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectPromoNew() {
      this.editPromo = [];
      this.editPromoQty = {};
      this.populateFoodItems();
      this.$refs.promotionsToggle.click();
    },
    selectPromoAdd() {
      axios
        .post(apiAddPromotion, {
          id: this.$store.state.user.restaurantId,
          type: this.editPromo[2],
          value: this.editPromo[3],
          min: this.editPromo[4],
          max: this.editPromo[5],
          name: this.editPromo[6],
          description: this.editPromo[7],
          start: this.editPromo[9],
          end: this.editPromo[10],
          items: this.editPromoQty,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Promotion added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input! Promotion not added.';
          }
          this.$refs.msgToggle.click();
          this.selectNavPromotions();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectPromoEntry(promo) {
      this.editPromo = promo;
      this.editPromoQty = {};
      axios
        .get(apiGetPromoItems, {
          params: {
            id: promo[0],
          },
        }).then((response) => {
          /* eslint-disable no-restricted-syntax, prefer-destructuring */
          for (const item of response.data) {
            this.editPromoQty[item[0]] = item[1];
          }
          return this.populateFoodItems();
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.$refs.promotionsToggle.click();
    },
    selectPromoUpdate() {
      axios
        .post(apiUpdatePromotion, {
          id: this.editPromo[0],
          type: this.editPromo[2],
          value: this.editPromo[3],
          min: this.editPromo[4],
          max: this.editPromo[5],
          name: this.editPromo[6],
          description: this.editPromo[7],
          start: this.editPromo[9],
          end: this.editPromo[10],
          items: this.editPromoQty,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Promotion updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input! Update not successful.';
          }
          this.$refs.msgToggle.click();
          this.selectNavPromotions();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectPromoDelete() {
      axios
        .post(apiDeletetPromotion, {
          id: this.editPromo[0],
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Promotion deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavPromotions();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectChangePassword() {
      axios
        .post(apiUpdatePassword, {
          uid: this.$store.state.user.id,
          opwd: this.password.old,
          npwd: this.password.new,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Password changed successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.password.old = '';
          this.password.new = '';
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectSignOut() {
      this.$store.commit('reset');
      this.$router.push('stafflogin');
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

tr.entry:hover {
  cursor: pointer;
}
</style>
