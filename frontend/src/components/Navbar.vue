<template>
    <div class="col-lg-3">
        <h2 class="my-4">{{title}}</h2>
        <div class="input-group mb-3">
        <input type="text" class="form-control" aria-label="Text input with dropdown button"
        placeholder="E.g. Laksa" v-model="query">
        <div class="input-group-append">
            <button class="btn btn-outline-secondary dropdown-toggle" type="button"
            data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Search</button>
            <div class="dropdown-menu">
                <a class="dropdown-item" @click="search(query, 'Food')">Food</a>
                <a class="dropdown-item" @click="search(query, 'Restaurant')">Restaurant</a>
                <!-- <div role="separator" class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Separated link</a> -->
            </div>
        </div>
        </div>
        <div class="list-group">
          <div class="list-group-item" v-for="category in categories" :key='category'
          v-on:click="filter(category[0])">
            {{category[0]}}
          </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Navbar',
  created() {
    axios
      .get(`${process.env.VUE_APP_DB_API_BASE}api/v1/fooditem/getcategory`)
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  data() {
    return {
      dummy: '',
      title: 'Home',
      categories: '',
    };
  },
  methods: {
    search(query, type) {
      this.dummy = query;
      this.dummy = type;
    },
    filter(category) {
      this.dummy = category;
    },
  },
};
</script>

<style>
.dropdown-item{
    cursor: pointer;
}
</style>
