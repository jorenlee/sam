<script setup>
//endpoint
const { data: products } = await useFetch("http://127.0.0.1:8000/api/hello/retrieve-products");
console.log(products);
</script>

<template>
  <div>
    <ol>
      <li v-for="(p, i) in products.product" :key="i" style="">
       <!-- <a :href="`/${p.id}`"> -->
         <!-- {{ p.brand }}
        <div style="color: red" v-for="(img, i) in p.images" :key="i">
          <img :src="img" />
        </div> -->
        
       <!-- </a> -->
   
       {{p.productName}}<br>
         {{p.category}}
      </li>
    </ol>
<!-- 
    {{products.brand}}
     <img :src="products.thumb" /> -->
  </div>
</template>