<script setup>
const route = useRoute()
const { data: products } = await useFetch('http://127.0.0.1:8000/api/hello/retrieve-products/1');

console.log(products);
</script>

<template>
 <div>
  <h1>
   Detail Page
  </h1>
   {{products.productName}}
      {{products.category}}
   <!-- <img :src="products.thumbnail" /> -->
 </div>
</template>