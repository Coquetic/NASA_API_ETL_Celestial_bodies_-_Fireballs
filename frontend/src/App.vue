<template>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
}

.logo {
  height: 50px;
}

nav a {
  margin: 0 1rem;
  text-decoration: none;
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
