<script setup>
const route = useRoute()

</script>


<template>
  <div>
    <p>{{ route.params.id }}</p>
  </div>
</template>
