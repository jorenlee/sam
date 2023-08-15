<script setup>
const { data: products } = await useFetch("https://dummyjson.com/products");
// console.log(products);
</script>


<template>
 <div>
  <!-- <SampleData 
   :products="products"
  />

  <SampleData3
   :products="products"
  /> -->

<Counter />
 </div>
</template>