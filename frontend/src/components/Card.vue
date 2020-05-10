<template>
    <div class="col-lg-4 col-md-6 mb-4">
        <div class="card h-100">
            <a href="#">
                <img class="card-img-top" src="http://placehold.it/700x400" alt />
            </a>
            <div class="card-body">
                <h4 class="card-title mb-0"><a href="#" class="text-dark">Item Six</a></h4>
                <h6><a href="#" class="text-muted">@Restaurant</a></h6>
                <h5>$24.99</h5>
                <p class="card-text">Lorem ipsum dolor sit amet</p>
            </div>
            <div class="card-footer">
                  <div class="form-row">
                    <div class="form-group col-md-6 pl-0 mb-0">
                      <select class="form-control">
                        <option v-for="x in getRange(1,1000)" v-bind:key="x">
                          {{x}}
                        </option>
                      </select>
                    </div>
                    <div class="form-group col-md-6 pr-0 mb-0">
                      <input type="button" class="form-control btn btn-primary" value="Add to cart">
                    </div>
                  </div>
                </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Card',
};
</script>
