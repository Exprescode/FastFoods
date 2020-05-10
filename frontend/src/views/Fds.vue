<!-- eslint-disable max-len -->
<template>
  <div class="pt-5">
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
    <div id="promoModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Promotion</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Name</label>
                    <input type="text" class="form-control" v-model="editPromo['name']">
                  </div>
                  <div class="form-group col-md-6">
                    <label>Condition</label>
                    <select class="form-control" v-model="editPromo['condition']">
                      <option value='new user'>New User</option>
                      <option value='return user'>Returning User</option>
                    </select>
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Discount type</label>
                    <select class="form-control" v-model="editPromo['type']">
                      <option value='percent'>Percentage</option>
                      <option value='flat'>Fix Value</option>
                    </select>
                  </div>
                  <div class="form-group col-md-6">
                    <label>Discount value</label>
                    <input type="text" class="form-control" placeholder="0.1" v-model="editPromo['value']">
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Minimum order amount ($)</label>
                    <input type="text" class="form-control" placeholder="5.50" v-model="editPromo['minlimit']">
                  </div>
                  <div class="form-group col-md-6">
                    <label>Maximum discount amount ($)</label>
                    <input type="text" class="form-control" placeholder="10.50" v-model="editPromo['maxlimit']">
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Start date</label>
                    <input type="text" class="form-control" placeholder="DD-MM-YY" v-model="editPromo['sdate']">
                  </div>
                  <div class="form-group col-md-6">
                    <label>End date</label>
                    <input type="text" class="form-control" placeholder="DD-MM-YY" v-model="editPromo['edate']">
                  </div>
                </div>
                <div class="form-group">
                  <label>Description</label>
                  <input type="text" class="form-control" v-model="editPromo['descript']">
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectPromotionAdd()" v-if="!editPromo['id']">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectPromotionUpdate()" v-if="editPromo['id']">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectPromotionDelete()" v-if="editPromo['id']">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="restaurantModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Restaurant</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Name</label>
                    <input type="text" class="form-control" v-model="editRestaurant['name']">
                  </div>
                  <div class="form-group col-md-6">
                    <label>Type</label>
                    <input type="text" class="form-control" placeholder="Western" v-model="editRestaurant['type']">
                  </div>
                </div>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Address</label>
                    <input type="text" class="form-control" placeholder="68 Orchard Rd, #B1-07 Singapore 238839" v-model="editRestaurant['address']">
                  </div>
                  <div class="form-group col-md-6">
                    <label>Location</label>
                    <input type="text" class="form-control" placeholder="Plaza Singapura" v-model="editRestaurant['location']">
                  </div>
                </div><div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Area</label>
                    <select class="form-control" v-model="editRestaurant['area']">
                      <option value='North'>North</option>
                      <option value='South'>South</option>
                      <option value='East'>East</option>
                      <option value='West'>West</option>
                      <option value='Central'>Central</option>
                    </select>
                  </div>
                  <div class="form-group col-md-6">
                    <label>Minimum order ($)</label>
                    <input type="text" class="form-control" placeholder="10.50" v-model="editRestaurant['minorder']">
                  </div>
                </div><div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Opening Time</label>
                    <input type="text" class="form-control" placeholder="10:30" v-model="editRestaurant['ohour']">
                  </div>
                  <div class="form-group col-md-6">
                    <label>Closing Time</label>
                    <input type="text" class="form-control" placeholder="22:30" v-model="editRestaurant['chour']">
                  </div>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectRestaurantAdd()" v-if="!editRestaurant['id']">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectRestaurantUpdate()" v-if="editRestaurant['id']">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectRestaurantDelete()" v-if="editRestaurant['id']">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="rstaffModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Restaurant Staff</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group">
                  <label>Name</label>
                  <input type="text" class="form-control" v-model="editrstaff['name']">
                </div>
                <div class="form-group">
                  <label>Email</label>
                  <input type="text" class="form-control" placeholder="sample@example.com" v-model="editrstaff['email']">
                </div>
                <div class="form-group">
                  <label>Password</label>
                  <input type="password" class="form-control" v-model="editrstaff['password']">
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectRStaffAdd()" v-if="!editrstaff['id']">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectRStaffUpdate()" v-if="editrstaff['id']">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectRStaffDelete()" v-if="editrstaff['id']">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="fstaffModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">FDS Manager</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group">
                  <label>Name</label>
                  <input type="text" class="form-control" v-model="editfstaff['name']">
                </div>
                <div class="form-group">
                  <label>Email</label>
                  <input type="text" class="form-control" placeholder="sample@example.com" v-model="editfstaff['email']">
                </div>
                <div class="form-group">
                  <label>Password</label>
                  <input type="password" class="form-control" v-model="editfstaff['password']">
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectFStaffAdd()" v-if="!editfstaff['id']">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectFStaffUpdate()" v-if="editfstaff['id']">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectFStaffDelete()" v-if="editfstaff['id'] && editfstaff['id'] != $store.state.user.id">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="riderModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Rider</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-group">
                  <label>Name</label>
                  <input type="text" class="form-control" v-model="editRider['name']">
                </div>
                <div class="form-group">
                  <label>Email</label>
                  <input type="text" class="form-control" placeholder="sample@example.com" v-model="editRider['email']">
                </div>
                <div class="form-group">
                  <label>Base salary</label>
                  <input type="text" class="form-control" placeholder="1234" v-model="editRider['salary']">
                </div>
                <div class="form-group">
                  <label>Employment type</label>
                  <select class="form-control" v-model="editRider['type']">
                      <option value='part'>Part-time</option>
                      <option value='full'>Full-time</option>
                    </select>
                </div>
                <div class="form-group">
                  <label>Password</label>
                  <input type="password" class="form-control" v-model="editRider['password']">
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectRiderAdd()" v-if="!editRider['id']">Add</button>
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectRiderUpdate()" v-if="editRider['id']">Update</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectRiderDelete()" v-if="editRider['id']">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
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
            <h2 class="my-4">{{this.$store.state.user.name}}</h2>
            <a data-toggle="modal" data-target="#msgModal" ref="msgToggle"></a>
            <a data-toggle="modal" data-target="#promoModal" ref="promoToggle"></a>
            <a data-toggle="modal" data-target="#restaurantModal" ref="restaurantToggle"></a>
            <a data-toggle="modal" data-target="#rstaffModal" ref="rstaffToggle"></a>
            <a data-toggle="modal" data-target="#fstaffModal" ref="fstaffToggle"></a>
            <a data-toggle="modal" data-target="#riderModal" ref="riderToggle"></a>
            <div class="list-group">
              <a class="list-group-item" v-on:click="selectNavSummary()">Summary</a>
              <a class="list-group-item" v-on:click="selectNavPromotions()">Promotions</a>
              <a class="list-group-item" v-on:click="selectNavRestaurants()">Restaurants</a>
              <a class="list-group-item" v-on:click="selectNavRStaff()">Restaurant Staff</a>
              <a class="list-group-item" v-on:click="selectNavFStaff()">FDS Managers</a>
              <a class="list-group-item" v-on:click="selectNavRiders()">Riders</a>
            </div>
        </div>
        <!-- Restaurant List -->
        <div class="col-lg-9 list">
          <div class="row mt-4">
            <div class="table-responsive" v-if="view=='summary'">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th class="text-center" scope="col">Year</th>
                    <th class="text-center" scope="col">Month</th>
                    <th class="text-center" scope="col">No. New Customers</th>
                    <th class="text-center" scope="col">No. Orders</th>
                    <th class="text-center" scope="col">Total Cost</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(entry, index) in summaryInfo" v-bind:key="index">
                    <td class="text-center">{{entry[0]}}</td>
                    <td class="text-center">{{formatMonth(entry[1])}}</td>
                    <td class="text-center">{{entry[2]}}</td>
                    <td class="text-center">{{entry[3]}}</td>
                    <td class="text-center">{{formatPrice(entry[4])}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="col-sm-12" v-if="view=='promotions'">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="New Promotion" v-on:click="selectPromotionNew()">
            </div>
            <div class="table-responsive" v-if="view=='promotions'">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th class="text-center" scope="col">Start Date</th>
                    <th class="text-center" scope="col">End Date</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(promo, index) in promotions" v-bind:key="index" v-on:click="selectPromotionEntry(promo)">
                    <td>{{promo[8]}}</td>
                    <td class="text-center">{{promo[6]}}</td>
                    <td class="text-center">{{promo[7]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="col-sm-12" v-if="view=='restaurant'">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="New Restaurant" v-on:click="selectRestaurantNew()">
            </div>
            <div class="table-responsive" v-if="view=='restaurant'">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th class="text-center" scope="col">No. Staff</th>
                    <th class="text-center" scope="col">No. Items</th>
                    <th class="text-center" scope="col">No. Review</th>
                    <th class="text-center" scope="col">Rating</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(restaurant, index) in restaurants" v-bind:key="index" v-on:click="selectRestaurantEntry(restaurant)">
                    <td>{{restaurant[1]}}</td>
                    <td class="text-center">{{restaurant[9]}}</td>
                    <td class="text-center">{{restaurant[10]}}</td>
                    <td class="text-center">{{restaurant[11]}}</td>
                    <td class="text-center">{{restaurant[12]}}/5</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="col-sm-12" v-if="view=='rstaff'">
              <div class="form-row">
                  <div class="form-group col">
                    <label>Restaurant</label>
                    <select class="form-control" v-model="rstaffrest" @change="getRStaff()">
                      <option v-for="(restaurant, index) in restaurants" v-bind:key="index" v-bind:value="restaurant[0]">
                        {{restaurant[1]}}
                      </option>
                    </select>
                  </div>
                  <div class="form-group col-auto" v-if="rstaffrest">
                    <label>.</label>
                    <input type="button" class="form-control btn btn-outline-primary aglin-bottom" value="New Restaurant Staff" v-on:click="selectRStaffNew()">
                  </div>
                </div>
            </div>
            <div class="table-responsive" v-if="view=='rstaff' && rstaff">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(staff, index) in rstaff" v-bind:key="index" v-on:click="selectRStaffEntry(staff)">
                    <td>{{staff[1]}}</td>
                    <td>{{staff[2]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="col-sm-12" v-if="view=='fstaff'">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="New FDS Manager" v-on:click="selectFStaffNew()">
            </div>
            <div class="table-responsive" v-if="view=='fstaff'">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(staff, index) in fstaff" v-bind:key="index" v-on:click="selectFStaffEntry(staff)">
                    <td>{{staff[1]}}</td>
                    <td>{{staff[2]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="col-sm-12" v-if="view=='riders'">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="New Rider" v-on:click="selectRidersNew()">
            </div>
            <div class="table-responsive" v-if="view=='riders'">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th class="text-center" scope="col">Delivery Time (min)</th>
                    <th class="text-center" scope="col">No. Reviews</th>
                    <th class="text-center" scope="col">Rating</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(rider, index) in riders" v-bind:key="index" v-on:click="selectRiderEntry(rider)">
                    <td>{{rider[1]}}</td>
                    <td class="text-center">{{rider[5]}}</td>
                    <td class="text-center">{{rider[6]}}</td>
                    <td class="text-center">{{rider[7]}}</td>
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

const apiGetSummary = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getfdssummary`;
const apiGetPromotions = `${process.env.VUE_APP_DB_API_BASE}/api/v1/apppromotions/getfdslist`;
const apiAddPromotion = `${process.env.VUE_APP_DB_API_BASE}/api/v1/apppromotions/addpromo`;
const apiUpdatePromotion = `${process.env.VUE_APP_DB_API_BASE}/api/v1/apppromotions/updatepromo`;
const apiDeletePromotion = `${process.env.VUE_APP_DB_API_BASE}/api/v1/apppromotions/deletepromo`;
const apiGetRestaurants = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/getfdslist`;
const apiAddRestaurant = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/addrestaurant`;
const apiUpdateRestaurant = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/updaterestaurant`;
const apiDeleteRestaurant = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/deleterestaurant`;
const apiGetRestaurantNames = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurants/getnamelist`;
const apiGetRStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantstaff/getlist`;
const apiAddRStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantstaff/addstaff`;
const apiUpdateRStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantstaff/updatestaff`;
const apiDeleteRStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/restaurantstaff/deletestaff`;
const apiGetFStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fdsstaff/getlist`;
const apiAddFStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fdsstaff/addstaff`;
const apiUpdateFStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fdsstaff/updatestaff`;
const apiDeleteFStaff = `${process.env.VUE_APP_DB_API_BASE}/api/v1/fdsstaff/deletestaff`;
const apiGetRiders = `${process.env.VUE_APP_DB_API_BASE}/api/v1/riders/getsummary`;
const apiAddRider = `${process.env.VUE_APP_DB_API_BASE}/api/v1/riders/addrider`;
const apiUpdateRider = `${process.env.VUE_APP_DB_API_BASE}/api/v1/riders/updateRider`;
const apiDeleteRider = `${process.env.VUE_APP_DB_API_BASE}/api/v1/riders/deleteRider`;

export default {
  name: 'fds',
  components: {
    Footer,
  },
  mounted() {
    if (!this.$store.state.user || this.$store.state.user.type !== 'fds') {
      this.$router.push('stafflogin');
    }
    this.selectNavSummary();
  },
  data() {
    return {
      view: '',
      summaryInfo: '',
      promotions: '',
      editPromo: '',
      restaurants: '',
      editRestaurant: '',
      rstaffrest: '',
      rstaff: '',
      editrstaff: '',
      fstaff: '',
      editfstaff: '',
      riders: '',
      editRider: '',
      dialog: {
        title: '',
        msg: '',
      },
    };
  },
  methods: {
    getRange(start, stop) {
      return new Array(stop + 1 - start).fill(start).map((n, i) => n + i);
    },
    formatPrice(value) {
      if (typeof value === 'undefined') {
        /* eslint-disable consistent-return */
        return;
      }
      if (typeof value === 'string') {
        /* eslint-disable no-param-reassign */
        value = parseFloat(value);
      }
      return `$${value.toFixed(2).toString()}`;
    },
    formatMonth(intMonth) {
      const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      return months[intMonth - 1] || '';
    },
    formatStatus(status) {
      switch (status) {
        case 'torest':
          return 'On route to restaurant';
        case 'atrest':
          return 'Collecting delivery order';
        case 'tocust':
          return 'On route to destination';
        case 'completed':
          return 'Order delivered';
        default:
          return '';
      }
    },
    formatPayment(method) {
      if (typeof method === 'undefined') {
        /* eslint-disable consistent-return */
        return;
      }
      return method.charAt(0).toUpperCase() + method.slice(1);
    },
    selectNavSummary() {
      axios
        .get(apiGetSummary)
        .then((response) => {
          this.summaryInfo = response.data;
          this.view = 'summary';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectNavPromotions() {
      axios
        .get(apiGetPromotions)
        .then((response) => {
          this.promotions = response.data;
          this.view = 'promotions';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectPromotionNew() {
      this.editPromo = {
        sid: this.$store.state.user.id,
      };
      this.$refs.promoToggle.click();
    },
    selectPromotionAdd() {
      axios
        .post(apiAddPromotion, this.editPromo)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Promotion added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input. Promotion not added.';
          }
          this.$refs.msgToggle.click();
          this.selectNavPromotions();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectPromotionEntry(promo) {
      this.editPromo = {
        id: promo[0],
        type: promo[2],
        value: promo[3],
        minlimit: promo[4],
        maxlimit: promo[5],
        sdate: promo[6],
        edate: promo[7],
        name: promo[8],
        descript: promo[9],
        condition: promo[10],
        sid: this.$store.state.user.id,
      };
      this.$refs.promoToggle.click();
    },
    selectPromotionUpdate() {
      axios
        .post(apiUpdatePromotion, this.editPromo)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Promotion updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input. Update failed.';
          }
          this.$refs.msgToggle.click();
          this.selectNavPromotions();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectPromotionDelete() {
      axios
        .post(apiDeletePromotion, {
          id: this.editPromo.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Promotion deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error. Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavPromotions();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectNavRestaurants() {
      axios
        .get(apiGetRestaurants)
        .then((response) => {
          this.restaurants = response.data;
          this.view = 'restaurant';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectRestaurantNew() {
      this.editRestaurant = {};
      this.$refs.restaurantToggle.click();
    },
    selectRestaurantAdd() {
      axios
        .post(apiAddRestaurant, this.editRestaurant)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Restaurant added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input. Restaurant not added.';
          }
          this.$refs.msgToggle.click();
          this.selectNavRestaurants();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectRestaurantEntry(restaurant) {
      this.editRestaurant = {
        id: restaurant[0],
        name: restaurant[1],
        type: restaurant[2],
        address: restaurant[3],
        location: restaurant[4],
        area: restaurant[5],
        minorder: restaurant[8],
        ohour: restaurant[6],
        chour: restaurant[7],
      };
      this.$refs.restaurantToggle.click();
    },
    selectRestaurantUpdate() {
      axios
        .post(apiUpdateRestaurant, this.editRestaurant)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Restaurant updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'Invalid input. Update failed.';
          }
          this.$refs.msgToggle.click();
          this.selectNavRestaurants();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectRestaurantDelete() {
      axios
        .post(apiDeleteRestaurant, {
          id: this.editRestaurant.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Restaurant deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error. Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavRestaurants();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectNavRStaff() {
      axios
        .get(apiGetRestaurantNames)
        .then((response) => {
          this.restaurants = response.data;
          this.view = 'rstaff';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getRStaff() {
      axios
        .get(apiGetRStaff, {
          params: {
            id: this.rstaffrest,
          },
        })
        .then((response) => {
          this.rstaff = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectRStaffNew() {
      this.editrstaff = {
        rid: this.rstaffrest,
      };
      this.$refs.rstaffToggle.click();
    },
    selectRStaffAdd() {
      axios
        .post(apiAddRStaff, this.editrstaff)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Restaurant staff added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.getRStaff();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectRStaffEntry(staff) {
      this.editrstaff = {
        id: staff[0],
        name: staff[1],
        email: staff[2],
      };
      this.$refs.rstaffToggle.click();
    },
    selectRStaffUpdate() {
      axios
        .post(apiUpdateRStaff, this.editrstaff)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Restaurant staff updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.getRStaff();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectRStaffDelete() {
      axios
        .post(apiDeleteRStaff, {
          id: this.editrstaff.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Restaurant staff deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error. Try again later.';
          }
          this.$refs.msgToggle.click();
          this.getRStaff();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectNavFStaff() {
      axios
        .get(apiGetFStaff)
        .then((response) => {
          this.fstaff = response.data;
          this.view = 'fstaff';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectFStaffNew() {
      this.editfstaff = {};
      this.$refs.fstaffToggle.click();
    },
    selectFStaffAdd() {
      axios
        .post(apiAddFStaff, this.editfstaff)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Manager added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.selectNavFStaff();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectFStaffEntry(staff) {
      this.editfstaff = {
        id: staff[0],
        name: staff[1],
        email: staff[2],
      };
      this.$refs.fstaffToggle.click();
    },
    selectFStaffUpdate() {
      axios
        .post(apiUpdateFStaff, this.editfstaff)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Manager updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.selectNavFStaff();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectFStaffDelete() {
      axios
        .post(apiDeleteFStaff, {
          id: this.editfstaff.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Manager deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error. Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavFStaff();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectNavRiders() {
      axios
        .get(apiGetRiders)
        .then((response) => {
          this.riders = response.data;
          this.view = 'riders';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectRidersNew() {
      this.editRider = {};
      this.$refs.riderToggle.click();
    },
    selectRiderAdd() {
      axios
        .post(apiAddRider, this.editRider)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Rider added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.selectNavRiders();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectRiderEntry(rider) {
      this.editRider = {
        id: rider[0],
        name: rider[1],
        email: rider[2],
        salary: rider[3],
        type: rider[4],
      };
      this.$refs.riderToggle.click();
    },
    selectRiderUpdate() {
      axios
        .post(apiUpdateRider, this.editRider)
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Rider updated successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.selectNavRiders();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectRiderDelete() {
      axios
        .post(apiDeleteRider, {
          id: this.editRider.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Rider deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error. Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavRiders();
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
