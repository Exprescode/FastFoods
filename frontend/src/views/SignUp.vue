<template>
  <div>
    <div id="errorModal" class="modal fade">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Error</h2>
              {{msg}}
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
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
              Your account has been created!
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary"
              v-on:click="redirectLogIn()" data-dismiss="modal">
                Confirm
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="wrapper fadeInDown">
      <div id="formContent">
        <!-- Tabs Titles -->

        <!-- Icon -->
        <div class="fadeIn first">
          <a data-toggle="modal" data-target="#errorModal" ref="errorToggle"></a>
          <a data-toggle="modal" data-target="#redirectModal" ref="redirectToggle"></a>
          <h1 class="my-4">FastFoods</h1>
        </div>

        <!-- Login Form -->
        <form class="px-4 mb-4">
          <div class="form-group fadeIn second">
            <label for="inputEmail">Email</label>
            <input type="email" class="form-control" id="inputEmail"
            placeholder="sample@example.com" v-model="form.email">
          </div>
          <div class="form-group fadeIn third">
            <label for="inputPassword">Password</label>
            <input type="password" class="form-control" id="inputPassword"
            placeholder="••••••" v-model="form.password">
          </div>
          <div class="form-group fadeIn fourth">
            <label for="inputName">Name</label>
            <input type="text" class="form-control" id="inputName"
            placeholder="Sample" v-model="form.name">
          </div>
          <div class="form-group fadeIn fifth">
            <label for="inputPhoneNumber">Phone number</label>
            <input type="text" class="form-control" id="inputPhoneNumber"
            placeholder="12345678" v-model="form.phone">
          </div>
          <div class="form-group fadeIn sixth">
            <label for="inputCreditCardNumber">Credit card number</label>
            <input type="text" class="form-control" id="inputCreditCardNumber"
            placeholder="1234123412341234" v-model="form.card">
          </div>
          <div class="form-group fadeIn seventh">
            <input type="button" class="form-control btn btn-outline-primary btn-sm"
            value="SIGN UP" v-on:click="executeSignUp()"/>
          </div>
        </form>
        <!-- Remind Passowrd -->
        <div id="formFooter">
          Have an account? <a class="underlineHover" v-on:click="redirectLogIn()">Log in</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const apiAddCustomer = `${process.env.VUE_APP_DB_API_BASE}/api/v1/customers/addcustomer`;

export default {
  name: 'SignUp',
  data() {
    return {
      form: {
        email: '',
        password: '',
        name: '',
        phone: '',
        card: '',
      },
      msg: 'This is a bug!',
    };
  },
  methods: {
    redirectLogIn() {
      this.$router.push('login');
    },
    showErrorMsg() {
      this.$refs.errorToggle.click();
    },
    showRedirectMsg() {
      this.$refs.redirectToggle.click();
    },
    executeSignUp() {
      axios
        .post(apiAddCustomer, this.form)
        .then((response) => {
          this.msg = response.data;
          if (this.msg === 'pass') {
            this.showRedirectMsg();
          } else {
            this.showErrorMsg();
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
a {
  color: #92badd;
  display:inline-block;
  text-decoration: none;
  font-weight: 400;
}

h1 {
  text-align: center;
}

div:hover {
  cursor: default;
}

.wrapper {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}

#formContent {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #fff;
  padding: 30px;
  width: 50%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
}

#formFooter {
  background-color: #f6f6f6;
  border-top: 1px solid #dce8f1;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}

/* ANIMATIONS */

/* Simple CSS3 Fade-in-down Animation */
.fadeInDown {
  -webkit-animation-name: fadeInDown;
  animation-name: fadeInDown;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@-webkit-keyframes fadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

@keyframes fadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

/* Simple CSS3 Fade-in Animation */
@-webkit-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@-moz-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }

.fadeIn {
  opacity:0;
  -webkit-animation:fadeIn ease-in 1;
  -moz-animation:fadeIn ease-in 1;
  animation:fadeIn ease-in 1;

  -webkit-animation-fill-mode:forwards;
  -moz-animation-fill-mode:forwards;
  animation-fill-mode:forwards;

  -webkit-animation-duration:1s;
  -moz-animation-duration:1s;
  animation-duration:1s;
}

.fadeIn.first {
  -webkit-animation-delay: 0.1s;
  -moz-animation-delay: 0.1s;
  animation-delay: 0.1s;
}

.fadeIn.second {
  -webkit-animation-delay: 0.2s;
  -moz-animation-delay: 0.2s;
  animation-delay: 0.2s;
}

.fadeIn.third {
  -webkit-animation-delay: 0.3s;
  -moz-animation-delay: 0.3s;
  animation-delay: 0.3s;
}

.fadeIn.fourth {
  -webkit-animation-delay: 0.48s;
  -moz-animation-delay: 0.4s;
  animation-delay: 0.4s;
}

.fadeIn.fifth {
  -webkit-animation-delay: 0.5s;
  -moz-animation-delay: 0.5s;
  animation-delay: 0.5s;
}

.fadeIn.sixth {
  -webkit-animation-delay: 0.6s;
  -moz-animation-delay: 0.6s;
  animation-delay: 0.6s;
}

.fadeIn.seventh {
  -webkit-animation-delay: 0.7s;
  -moz-animation-delay: 0.7s;
  animation-delay: 0.7s;
}

/* Simple CSS3 Fade-in Animation */
.underlineHover:after {
  display: block;
  left: 0;
  bottom: -10px;
  width: 0;
  height: 2px;
  background-color: #56baed;
  content: "";
  transition: width 0.2s;
}

.underlineHover:hover {
  color: #0d0d0d;
  cursor: pointer;
}

.underlineHover:hover:after{
  width: 100%;
}
</style>
