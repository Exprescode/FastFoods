<!-- eslint-disable max-len -->
<template>
  <div>
    <div id="errorModal" class="modal fade">
      <div class="modal-dialog modal-sm">
        <div class="modal-content">
          <form>
            <div class="modal-body">
              <h2>Error</h2>
              {{errorMsg}}
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
          <h1 class="my-4">FastFoods</h1>
        </div>
        <form class="px-4 mb-4">
          <div class="form-group">
            <label for="inputAddress" class="fadeIn second">Delivery address</label>
            <div class="input-group" id="inputAddress">
              <input type="text" class="form-control fadeIn second"
                placeholder="Block 123 ABC Street 12 #12-123 Singapore 123456"
                aria-label="Text input with dropdown button" v-model="location.address">
                <div class="input-group-append">
                  <button type="button" data-toggle="dropdown" aria-haspopup="true"
                  aria-expanded="false"
                  class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split
                  fadeIn second">
                    <span class="sr-only">Toggle Dropdown</span>
                  </button>
                  <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" v-on:click="selectRecent(address[0], address[1])" v-for="address in addresses" v-bind:key="String(address[0])">
                      {{address[0]}}
                    </a>
                  </div>
                </div>
            </div>
          </div>
          <div class="form-group fadeIn third">
            <label for="inputRegion">Area</label>
            <select class="custom-select" id="inputRegion" v-model="location.area">
              <option class="entry" v-bind:value="area[0]" v-for="area in areas" v-bind:key="String(area[0])">
                {{area[0]}}
              </option>
            </select>
          </div>
          <div class="form-group fadeIn fourth">
            <input type="button" class="form-control btn btn-primary" value="ENTER"
            v-on:click="redirectRestaurant()">
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const apiGetAddresses = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getrecentaddr`;
const apiGetAreas = `${process.env.VUE_APP_DB_API_BASE}/api/v1/areas/getareas`;

export default {
  name: 'Login',
  mounted() {
    this.$store.commit('setLocation');
    if (!this.$store.state.hasUser) {
      this.$router.push('login');
    }
    axios
      .get(apiGetAddresses, {
        params: {
          id: this.$store.state.user.id,
        },
      })
      .then((response) => {
        this.addresses = response.data;
        return axios.get(apiGetAreas);
      }).then((response) => {
        this.areas = response.data;
      }).catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
  },
  data() {
    return {
      location: {
        address: '',
        area: '',
      },
      addresses: '',
      areas: '',
      errorMsg: 'This is a bug!',
    };
  },
  methods: {
    redirectRestaurant() {
      if (this.location.address === '') {
        this.errorMsg = 'Deliery address cannot be empty!';
        this.showErrorMsg();
        return;
      }
      if (this.location.area === '') {
        this.errorMsg = 'Area cannot be empty!';
        this.showErrorMsg();
        return;
      }
      this.$store.commit('addLocation', this.location);
      this.$router.push('restaurant');
    },
    showErrorMsg() {
      this.$refs.errorToggle.click();
    },
    selectRecent(address, area) {
      this.location.address = address;
      this.location.area = area;
      this.redirectRestaurant();
    },
  },
};
</script>

<style scoped>

/* STRUCTURE */

h1 {
  text-align: center;
}

div:hover {
  cursor: default;
}

select:hover, a:hover {
  cursor: pointer;
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
