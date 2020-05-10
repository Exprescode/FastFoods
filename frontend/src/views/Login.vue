<template>
  <div>
    <div id="errorModal" class="modal fade">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Error</h2>
              Invalid credentials!
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="wrapper fadeInDown">
      <div id="formContent">
        <div class="fadeIn first">
          <a data-toggle="modal" data-target="#errorModal" ref="errorToggle"></a>
          <a data-toggle="modal" data-target="#dialogModal" ref="dialogToggle"></a>
          <h1 class="my-4">FastFoods</h1>
        </div>

        <!-- Login Form -->
        <form class="px-4 mb-4">
          <div class="form-group">
            <label for="inputEmail">Email</label>
            <input type="email" class="form-control fadeIn second" id="inputEmail"
            placeholder="sample@example.com" v-model="form.email">
          </div>
          <div class="form-group">
            <label for="inputPassword">Password</label>
            <input type="password" class="form-control  fadeIn third" id="inputPassword"
            placeholder="••••••" v-model="form.password">
          </div>
          <div class="form-group">
            <input type="button" class="form-control btn btn-primary fadeIn fourth" value="LOG IN"
            v-on:click="executeLogIn()">
          </div>
        </form>

        <!-- Remind Passowrd -->
        <div id="formFooter">
          Don't have an account? <a class="underlineHover" v-on:click="redirectSignUp()">Sign up</a>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const apiGetCustomer = `${process.env.VUE_APP_DB_API_BASE}/api/v1/customers/getcustomer`;

export default {
  name: 'LogIn',
  mounted() {
    if (this.$store.state.user && this.$store.state.user.type === 'customer') {
      this.$router.push('location');
    }
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
      },
      userInfo: '',
    };
  },
  methods: {
    redirectSignUp() {
      this.$router.push('signup');
    },
    redirectLocation() {
      this.$router.push('location');
    },
    showErrorMsg() {
      this.$refs.errorToggle.click();
    },
    executeLogIn() {
      axios
        .post(apiGetCustomer, this.form)
        .then((response) => {
          this.userInfo = response.data;
          if (this.userInfo === 'fail') {
            this.showErrorMsg();
          } else {
            this.$store.commit('addUser', {
              id: response.data[0],
              email: response.data[1],
              name: response.data[2],
              phone: response.data[3],
              card: response.data[4],
              points: response.data[5],
              type: 'customer',
            });
            this.redirectLocation();
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

/* BASIC */
a {
  color: #92badd;
  display:inline-block;
  text-decoration: none;
  font-weight: 400;
}

a:hover {
  cursor: pointer;
}

div:hover {
  cursor: default;
}

h1 {
  text-align: center;
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
  width: 40%;
  max-width: 325px;
  min-width: 100px;
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
</style>
