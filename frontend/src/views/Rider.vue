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
    <div id="schedulePartModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Schedule</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Start date</label>
                    <input type="text" class="form-control" placeholder="DD-MM-YY" v-model="editSchedule['sdate']" v-bind:disabled="editSchedule['edate']">
                  </div>
                  <div class="form-group col-md-6" v-if="editSchedule['edate']">
                    <label>End date</label>
                    <input type="text" class="form-control" placeholder="DD-MM-YY" v-model="editSchedule['edate']" disabled>
                  </div>
                </div>
              </form>
              <table class="table table-striped">
                <tbody>
                  <tr>
                    <td></td>
                    <td v-for="(num1, index) in getRange(1,7)" v-bind:key="index" class="text-center">Day {{num1}}</td>
                  </tr>
                  <tr v-for="(num2, index) in getRange(10,21)" v-bind:key="index">
                    <td>{{num2}}:00 to {{num2+1}}:00</td>
                    <td class="text-center" v-for="(num3, index) in getRange(1,7)" v-bind:key="index">
                      <input type="checkbox" v-model="editSchedule[(num3*100 + num2).toString()]" true-value="yes" false-value="no" v-bind:disabled="editSchedule['edate']">
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectPartScheduleAdd()"  v-if="!editSchedule['edate']">Add</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectScheduleDelete()"  v-if="editSchedule['edate']">Delete</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
      </div>
    </div>
    <div id="scheduleFullModal" class="modal fade" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-md" role="document">
        <div class="modal-content">
            <div class="modal-header">
              <h4 class="modal-title">Schedule</h4>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="form-row">
                  <div class="form-group col-md-6">
                    <label>Start date</label>
                    <input type="text" class="form-control" placeholder="DD-MM-YY" v-model="editSchedule['sdate']" v-bind:disabled="editSchedule['edate']">
                  </div>
                  <div class="form-group col-md-6" v-if="editSchedule['edate']">
                    <label>End date</label>
                    <input type="text" class="form-control" placeholder="DD-MM-YY" v-model="editSchedule['edate']" disabled>
                  </div>
                </div>
                <div class="form-group row" v-for="(num, index) in getRange(1,7)" v-bind:key="index">
                  <label class="col-sm-4 col-form-label">Day {{num}}, {{num+7}}, {{num+14}}, {{num+21}}</label>
                  <div class="col-sm-8 pl-0">
                    <select class="form-control" v-model="editSchedule[num]"  v-bind:disabled="editSchedule['edate']">
                      <option v-for="(num2, index) in getRange(1,4)" v-bind:key="index" v-bind:value="num2">Shift {{num2}}: {{9 + num2}}:00 - {{13 + num2}}:00 and {{14 + num2}}:00 - {{18 + num2}}:00</option>
                    </select>
                  </div>
                </div>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-success" data-dismiss="modal" v-on:click="selectFullScheduleAdd()" v-if="!editSchedule['edate']">Add</button>
              <button type="button" class="btn btn-danger" data-dismiss="modal" v-on:click="selectScheduleDelete()" v-if="editSchedule['edate']">Delete</button>
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
            <h2 class="my-4">{{this.$store.state.user.name}}</h2>
            <a data-toggle="modal" data-target="#msgModal" ref="msgToggle"></a>
            <a data-toggle="modal" data-target="#schedulePartModal" ref="schedulePartToggle"></a>
            <a data-toggle="modal" data-target="#scheduleFullModal" ref="scheduleFullToggle"></a>
            <div class="list-group">
              <a class="list-group-item" v-on:click="selectNavAssginment()">Assignment</a>
              <a class="list-group-item" v-on:click="selectNavSchedule()">Schedule</a>
              <a class="list-group-item" v-on:click="selectNavSalary()">Salary</a>
            </div>
        </div>
        <!-- Restaurant List -->
        <div class="col-lg-9 list">
          <div class="row mt-4">
            <div class="col-sm-12" v-if="view=='assign'">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Get new assignment" v-if="!assignmentDetail || assignmentDetail[4]=='completed'" v-on:click="selectAssignmentNew()">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Arrive at restaurant" v-if="assignmentDetail[4]=='torest'" v-on:click="selectAssignmentRest()">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Collected order" v-if="assignmentDetail[4]=='atrest'" v-on:click="selectAssignmentCust()">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Complete" v-if="assignmentDetail[4]=='tocust'" v-on:click="selectAssignmentCompleted()">
            </div>
            <form class="col-sm-12" v-if="view=='assign'">
              <div class="form-group">
                <label>Restaurant Name</label>
                <input type="text" class="form-control" v-bind:value="assignmentDetail[1]" disabled>
              </div>
              <div class="form-group">
                <label>Restaurant Address</label>
                <input type="text" class="form-control" v-bind:value="assignmentDetail[2]" disabled>
              </div>
              <div class="form-group">
                <label>Delivery Address</label>
                <input type="text" class="form-control" v-bind:value="assignmentDetail[3]" disabled>
              </div>
              <div class="form-row">
                <div class="form-group col-md-3">
                  <label>Status</label>
                  <input type="text" class="form-control" v-bind:value="formatStatus(assignmentDetail[4])" disabled>
                </div>
                <div class="form-group col-md-3">
                  <label>Status Date/Time</label>
                  <input type="text" class="form-control" v-bind:value="assignmentDetail[5]" disabled>
                </div>
                <div class="form-group col-md-3">
                  <label>Payment Method</label>
                  <input type="text" class="form-control" v-bind:value="formatPayment(assignmentDetail[6])" disabled>
                </div>
                <div class="form-group col-md-3">
                  <label>Price</label>
                  <input type="text" class="form-control" v-bind:value="formatPrice(assignmentDetail[7])" disabled>
                </div>
              </div>
            </form>
            <div class="table-responsive" v-if="view=='assign'">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th scope="col">Quantity</th>
                    <th scope="col">Name</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in assginmentItems"
                  v-bind:key="index">
                    <td>{{item[1]}}</td>
                    <td>{{item[0]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="col-sm-12" v-if="view=='schedule'">
              <input type="button" class="btn btn-outline-primary float-right mb-4" value="Add new schedule" v-on:click="selectScheduleNew()">
            </div>
            <div class="table-responsive" v-if="view=='schedule'">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Start Date</th>
                    <th scope="col">End Date</th>
                    <th scope="col">Total Hours</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="entry" v-for="(schedule, index) in schedules"
                  v-bind:key="index" v-on:click="selectScheduleEntry(schedule)">
                    <td>{{schedule[1]}}</td>
                    <td>{{schedule[2]}}</td>
                    <td>{{schedule[3]}}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="table-responsive" v-if="view=='salary'">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th scope="col">Start Date</th>
                    <th scope="col">End Date</th>
                    <th scope="col">No. Hours</th>
                    <th scope="col">No. Orders</th>
                    <th scope="col">Total Salary</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(salary, index) in salaries"
                  v-bind:key="index">
                    <td>{{salary[0]}}</td>
                    <td>{{salary[1]}}</td>
                    <td>{{salary[2]}}</td>
                    <td>{{salary[3]}}</td>
                    <td>{{salary[4]}}</td>
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

const apiUpdatePassword = `${process.env.VUE_APP_DB_API_BASE}/api/v1/riders/updatepassword`;
const apiGetSchedule = `${process.env.VUE_APP_DB_API_BASE}/api/v1/schedule/getlist`;
const apiAddPartSchedule = `${process.env.VUE_APP_DB_API_BASE}/api/v1/schedule/addparttime`;
const apiAddFullSchedule = `${process.env.VUE_APP_DB_API_BASE}/api/v1/schedule/addfulltime`;
const apiDeleteSchedule = `${process.env.VUE_APP_DB_API_BASE}/api/v1/schedule/delete`;
const apiGetIntervalsPart = `${process.env.VUE_APP_DB_API_BASE}/api/v1/intervals/getlistpart`;
const apiGetIntervalsFull = `${process.env.VUE_APP_DB_API_BASE}/api/v1/intervals/getlistfull`;
const apiGetLatestAssignment = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/getlistrider`;
const apiUpdateAssignmentToRest = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/statustorest`;
const apiUpdateAssignmentAtRest = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/statusatrest`;
const apiUpdateAssignmentToCust = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/statustocust`;
const apiUpdateAssignmentCompleted = `${process.env.VUE_APP_DB_API_BASE}/api/v1/orders/statuscompleted`;
const apiGetSalaries = `${process.env.VUE_APP_DB_API_BASE}/api/v1/schedule/getsalaries`;

export default {
  name: 'RestaurantAdmin',
  components: {
    Footer,
  },
  mounted() {
    if (!this.$store.state.user || this.$store.state.user.type !== 'rider') {
      this.$router.push('stafflogin');
    }
    this.selectNavAssginment();
  },
  data() {
    return {
      view: '',
      schedules: '',
      editSchedule: {},
      assignmentDetail: '',
      assginmentItems: '',
      salaries: '',
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
    selectNavAssginment() {
      axios
        .get(apiGetLatestAssignment, {
          params: {
            id: this.$store.state.user.id,
          },
        }).then((response) => {
          /* eslint-disable prefer-destructuring */
          if (response.data === 'fail') {
            this.assignment = [];
          } else {
            this.assignmentDetail = response.data[0];
            this.assginmentItems = response.data[1];
          }
          this.view = 'assign';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectAssignmentNew() {
      axios
        .post(apiUpdateAssignmentToRest, {
          id: this.$store.state.user.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.selectNavAssginment();
            return;
          }
          if (response.data !== 'Unknown error!') {
            this.dialog.title = 'Info';
            this.dialog.msg = response.data;
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavAssginment();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectAssignmentRest() {
      axios
        .post(apiUpdateAssignmentAtRest, {
          id: this.assignmentDetail[0],
        })
        .then((response) => {
          if (response.data !== 'pass') {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
            this.$refs.msgToggle.click();
          }
          this.selectNavAssginment();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectAssignmentCust() {
      axios
        .post(apiUpdateAssignmentToCust, {
          id: this.assignmentDetail[0],
        })
        .then((response) => {
          if (response.data !== 'pass') {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
            this.$refs.msgToggle.click();
          }
          this.selectNavAssginment();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectAssignmentCompleted() {
      axios
        .post(apiUpdateAssignmentCompleted, {
          id: this.assignmentDetail[0],
        })
        .then((response) => {
          if (response.data !== 'pass') {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
            this.$refs.msgToggle.click();
          }
          this.selectNavAssginment();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectNavSchedule() {
      axios
        .get(apiGetSchedule, {
          params: {
            id: this.$store.state.user.id,
          },
        }).then((response) => {
          this.schedules = response.data;
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.view = 'schedule';
    },
    selectScheduleNew() {
      this.editSchedule = {};
      if (this.$store.state.user.employmentType === 'part') {
        this.$refs.schedulePartToggle.click();
      } else {
        this.$refs.scheduleFullToggle.click();
      }
    },
    selectScheduleEntry(schedule) {
      this.editSchedule = {};
      if (this.$store.state.user.employmentType === 'part') {
        axios
          .get(apiGetIntervalsPart, {
            params: {
              id: schedule[0],
            },
          }).then((response) => {
            this.editSchedule = response.data;
            /* eslint-disable prefer-destructuring */
            this.editSchedule.id = schedule[0];
            this.editSchedule.sdate = schedule[1];
            this.editSchedule.edate = schedule[2];
            this.$refs.schedulePartToggle.click();
          }).catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      } else {
        axios
          .get(apiGetIntervalsFull, {
            params: {
              id: schedule[0],
            },
          }).then((response) => {
            this.editSchedule = response.data;
            /* eslint-disable prefer-destructuring */
            this.editSchedule.id = schedule[0];
            this.editSchedule.sdate = schedule[1];
            this.editSchedule.edate = schedule[2];
            this.$refs.scheduleFullToggle.click();
          }).catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      }
    },
    selectPartScheduleAdd() {
      const newSchedule = [];
      /* eslint-disable no-restricted-syntax */
      for (const key in this.editSchedule) {
        if (this.editSchedule[key] === 'yes') {
          newSchedule.push(parseInt(key, 10));
        }
      }
      axios
        .post(apiAddPartSchedule, {
          id: this.$store.state.user.id,
          sdate: this.editSchedule.sdate,
          slots: newSchedule,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Schedule added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.selectNavSchedule();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectFullScheduleAdd() {
      const startDate = this.editSchedule.sdate;
      delete this.editSchedule.sdate;
      axios
        .post(apiAddFullSchedule, {
          id: this.$store.state.user.id,
          sdate: startDate,
          slots: this.editSchedule,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Schedule added successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = response.data;
          }
          this.$refs.msgToggle.click();
          this.selectNavSchedule();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectScheduleDelete() {
      axios
        .post(apiDeleteSchedule, {
          id: this.editSchedule.id,
        })
        .then((response) => {
          if (response.data === 'pass') {
            this.dialog.title = 'Success';
            this.dialog.msg = 'Schedule deleted successfully.';
          } else {
            this.dialog.title = 'Error';
            this.dialog.msg = 'System error! Try again later.';
          }
          this.$refs.msgToggle.click();
          this.selectNavSchedule();
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    selectNavSalary() {
      axios
        .get(apiGetSalaries, {
          params: {
            id: this.$store.state.user.id,
          },
        }).then((response) => {
          this.salaries = response.data;
          this.view = 'salary';
        }).catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectChangePassword() {
      axios
        .post(apiUpdatePassword, {
          id: this.$store.state.user.id,
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
