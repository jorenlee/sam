<script setup>


import { useCounterStore } from '@/stores/counter'

const dataAPI = useCounterStore()

// dataAPI.count++
// // with autocompletion ✨
// dataAPI.$patch({ count: dataAPI.count + 1})
// // or using an action instead
// dataAPI.increment()


</script>


<template>
 <div>
<!-- 
  <div>Current Count: {{ dataAPI.count }}</div> -->

  <div>
color : {{dataAPI.cars.color}} <br>
model: {{dataAPI.cars.model}} <br>
brand: {{dataAPI.cars.brand}} <br>




  </div>
 </div>
</template>