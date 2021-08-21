<template>
  <div class="container text-center">
    <h1 class="mt-5 mb-5">Diabetes Diagnosting App</h1>
    <div class="card mb-5">
      
      <div class="card-body">
        <h4>You are {{ results.result }}</h4>
        <p>Probability: {{ results.probability }} %</p>
      </div>

    </div>

    <form id="cform">
      <div class="form-row">
      <div class="form-group col-md-4">
        <label for="exampleInputEmail1">Pregnancies</label>
        <input type="text" class="form-control" id="p" ref="p">
      </div>

      <div class="form-group col-md-4">
        <label for="exampleInputEmail1">Glucose</label>
        <input type="text" class="form-control" id="g" ref="g">
      </div>

      <div class="form-group col-md-4">
        <label for="exampleInputEmail1">Blood Pressure</label>
        <input type="text" class="form-control" id="bp" ref="bp">
      </div>
      </div>

      <div class="form-row">
      <div class="form-group col-md-4">
        <label for="exampleInputEmail1">Skin Thickness</label>
        <input type="text" class="form-control" id="st" ref="st">
      </div>

      <div class="form-group col-md-4">
        <label for="exampleInputEmail1">Insulin</label>
        <input type="text" class="form-control" id="i" ref="i">
      </div>

      <div class="form-group col-md-4">
        <label for="exampleInputEmail1">BMI</label>
        <input type="text" class="form-control" id="bmi" ref="bmi">
      </div>
      </div>

      <div class="form-row">
      <div class="form-group col-md-6">
        <label for="exampleInputEmail1">Diabetes Pedigree Function</label>
        <input type="text" class="form-control" id="dpf" ref="dpf" >
      </div>

      <div class="form-group col-md-6">
        <label for="exampleInputEmail1">Age</label>
        <input type="text" class="form-control" id="a" ref="a" >
      </div>
      </div>

      <button @click="getResults" type="submit" class="btn btn-primary">Check Result</button>
     </form>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      results: {}
    };
  },
  methods: {
    getResults: function(e) {
      e.preventDefault();
      
      this.diagnose(this.$refs.p.value, 
      this.$refs.g.value, this.$refs.bp.value, this.$refs.st.value, 
      this.$refs.i.value, this.$refs.bmi.value, this.$refs.dpf.value,
      this.$refs.a.value
      );
    },
    diagnose(p, g, bp, st, i, bmi, dpf, a) {
      const path = `http://localhost:5000/api/${p}/${g}/${bp}/${st}/${i}/${bmi}/${dpf}/${a}`;
      axios.get(path)
        .then((res) => {
          this.results = res.data.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {

  },
};
</script>
