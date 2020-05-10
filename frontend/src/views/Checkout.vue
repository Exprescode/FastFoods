<!-- eslint-disable max-len -->
<template>
  <div class="pt-5">
    <div id="errorModal" class="modal fade">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Error</h2>
              Something is wrong with the system.
              Please try again later.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal" v-on:click="$router.push('restaurant')">
                Close
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div id="redirectModal" class="modal fade" data-backdrop="static" data-keyboard="false">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Success</h2>
              Your order has been placed.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary"
              v-on:click="$router.push('restaurant')" data-dismiss="modal">
                Confirm
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <div class="navbar-brand">
          <a data-toggle="modal" data-target="#errorModal" ref="errorToggle"></a>
          <a data-toggle="modal" data-target="#redirectModal" ref="redirectToggle"></a>
          FastFoods
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse"
        data-target="#navbarResponsive" aria-controls="navbarResponsive"
        aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <!-- <li class="nav-item">
              <a class="nav-link" v-on:click="selectCancel()">Cancel</a>
            </li> -->
          </ul>
        </div>
      </div>
    </nav>
    <!-- Page Content -->
    <div class="container pt-2">
      <div class="row">
        <div class="col-md-8 offset-md-2 py-4">
          <table class="table">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Item</th>
                <th scope="col">Quantity</th>
                <th scope="col">Price</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in this.$store.state.cart"
              v-bind:key="index">
                <th scope="row">{{index + 1}}</th>
                <td>{{item.name}}</td>
                <td>{{item.qty}}</td>
                <td>{{formatPrice(item.price * item.qty)}}</td>
              </tr>
            </tbody>
          </table>
          <div class="dropdown-divider"></div>
          <div class="row mt-2">
            <div class="col">
              <span class="font-weight-bold">Delivery fee:</span> ${{formatPrice(this.$store.state.restaurant.fee)}}
            </div>
          </div>
          <div class="row mt-2" v-if="$store.state.discount">
            <div class="col">
              <span class="font-weight-bold">Discount:</span> - ${{formatPrice(this.$store.state.discount)}}
            </div>
          </div>
          <div class="row mt-2" v-if="$store.state.user.points">
            <div class="col">
              <span class="font-weight-bold">Point discount:</span> - ${{formatPrice(this.$store.state.redeemPoint * 0.01)}}
            </div>
          </div>
          <div class="row mt-2">
            <div class="col font-weight-bold h4">
              Total: ${{formatPrice(getTotalPrice() + this.$store.state.restaurant.fee - this.$store.state.discount - (this.$store.state.redeemPoint * 0.01))}}
            </div>
          </div>
          <div class="dropdown-divider"></div>
          <div class="row mt-2">
            <div class="col">
              <span class="font-weight-bold">Deliver to:</span> {{$store.state.location.address}}
            </div>
          </div>
          <div class="dropdown-divider"></div>
          <div class="row mt-2">
            <div class="col-auto font-weight-bold">
              Select a payment method:
            </div>
            <div class="col">
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="card" v-model="paymentMethod">
                <label class="form-check-label" for="inlineRadio1">
                  Credit card
                </label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="cash" v-model="paymentMethod">
                <label class="form-check-label" for="inlineRadio2">
                  Cash on delivery
                </label>
              </div>
            </div>
          </div>
          <div class="row mt-3" v-if="paymentMethod == 'card'">
            <form class="col">
              <div class="form-group row">
                <label for="colFormLabel" class="col-sm-2 col-form-label">Card number</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control" placeholder="1234123412341234" v-bind:value="$store.state.user.card">
                </div>
              </div>
              <div class="form-group row">
                <label for="colFormLabel" class="col-sm-2 col-form-label">Expiry</label>
                <div class="col-sm-5">
                  <input type="month" class="form-control" placeholder="123">
                </div>
              </div>
              <div class="form-group row">
                <label for="colFormLabel" class="col-sm-2 col-form-label">CVV/CVC</label>
                <div class="col-sm-3">
                  <input type="text" class="form-control" placeholder="123">
                </div>
              </div>
            </form>
          </div>
          <div class="dropdown-divider"></div>
          <div class="row mt-2">
            <div class="col-12 text-right">
              <input class="btn btn-primary mr-1" type="button" value="Confirm" v-on:click="selectConfirm()">
              <input class="btn btn-secondary" type="button" value="Cancel" v-on:click="$router.push('menu')">
            </div>
          </div>
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

const apiBase = process.env.VUE_APP_DB_API_BASE;
const apiAddOrder = `${apiBase}/api/v1/orders/addorder`;

export default {
  name: 'Checkout',
  components: {
    Footer,
  },
  created() {
  },
  mounted() {
  },
  data() {
    return {
      paymentMethod: 'card',
    };
  },
  methods: {
    getTotalPrice() {
      const cartList = this.$store.state.cart;
      let total = 0;
      for (let i = 0; i < cartList.length; i += 1) {
        total += cartList[i].price * cartList[i].qty;
      }
      return total;
    },
    formatPrice(value) {
      return value.toFixed(2).toString();
    },
    showErrorDialog() {
      this.$refs.errorToggle.click();
    },
    showRedirectDialog() {
      this.$refs.redirectToggle.click();
    },
    selectConfirm() {
      axios
        .post(apiAddOrder, {
          restId: this.$store.state.restaurant.id,
          custId: this.$store.state.user.id,
          address: this.$store.state.location.address,
          area: this.$store.state.location.area,
          fee: this.$store.state.restaurant.fee,
          discount: this.$store.state.discount,
          point: this.$store.state.redeemPoint,
          payment: this.paymentMethod,
          cart: this.$store.state.cart,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.showRedirectDialog();
          } else {
            this.showErrorDialog();
          }
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
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
</style>
