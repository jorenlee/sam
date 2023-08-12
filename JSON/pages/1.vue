<script setup>
const route = useRoute()
const { data: products } = await useFetch('https://dummyjson.com/products/1');

console.log(products);
</script>

<template>
 <div>
  <h1>
   Detail Page
  </h1>
   {{products.brand}}
   <img :src="products.thumbnail" />
 </div>
</template>