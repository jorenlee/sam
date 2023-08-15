<script setup>

defineProps(['products'])

</script>

<template>
  <div>
    <ol>
      <li v-for="(p, i) in products.products" :key="i" style="border: 1px solid red">
        <a :href="`/${p.id}`">
          {{ p.title }}
          {{ p.brand }}

          <div style="color: red" v-for="(img, i) in p.images" :key="i">
            <img :src="img" style="width: 100px" />
          </div>
        </a>
      </li>
    </ol>
    <!-- 
    {{products.brand}}
     <img :src="products.thumb" /> -->
  </div>
</template>
