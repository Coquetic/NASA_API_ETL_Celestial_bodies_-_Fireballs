<template>
  <header class="home-header">
    <img src="/nasa-logo.png" alt="NASA Logo" class="nasa-logo" />

    <nav class="nav-links">
      <RouterLink to="/fireballs">Dashboard Fireballs</RouterLink>
      <RouterLink to="/cad">Dashboard CAD</RouterLink>
      <RouterLink to="/about">About the Project</RouterLink>
    </nav>
  </header>

  <div class="home">
    <h1 class="main-title">☄️ NASA ETL Project</h1>

    <div class="animation-container">
      <EarthSatellites />
    </div>

    <div class="section-subtitle">
      <span class="subtitle-fade"></span>
      <h2>🔭 Choose your dashboard</h2>
    </div>

    <div class="buttons">
      <button @click="goToFireballs">Fireball Dashboard</button>
      <button @click="goToCAD">CAD Dashboard</button>
      <button @click="goToAbout" class="secondary">About the Project</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import EarthSatellites from '@/components/EarthSatellites.vue'

const router = useRouter()

function goToFireballs() {
  router.push('/fireballs')
}

function goToCAD() {
  router.push('/cad')
}

function goToAbout() {
  router.push('/about')
}
</script>

<style scoped>
.home-header {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  padding: 0.5rem 2rem;
  background-color: #f0f0f0;
  border-bottom: 1px solid #ccc;
  width: 100%;
}

.home {
  padding: 2rem;
  text-align: center;
}

.home-header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem 2rem;
}

.nasa-logo {
  width: 60px;
  height: auto;
}

.nav-links {
  margin-right: auto;
  display: flex;
  gap: 2rem;
}

.nav-links a {
  text-decoration: none;
  font-weight: 600;
  color: #2c3e50;
  transition: color 0.3s ease;
}

.nav-links a:hover {
  color: #0077cc;
}

.nav-links .router-link-exact-active {
  color: #42b983;
}

.main-title {
  font-size: 3rem;
  font-weight: 600;
  text-align: center;
  margin: 2rem 0 1.5rem;
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.animation-container {
  max-width: 700px;
  margin: 2rem auto;
}

.section-subtitle {
  margin-top: 2rem;
}

.section-subtitle h2 {
  font-size: 1.5rem;
  font-weight: 500;
  margin-bottom: 1rem;
  position: relative;
}

.subtitle-fade {
  display: block;
  height: 8px;
  width: 100px;
  margin: 0 auto 0.5rem;
  background: linear-gradient(to right, transparent, #888, transparent);
  border-radius: 4px;
}

.buttons {
  margin-top: 1.5rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  background-color: #0077be;
  color: white;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #005f94;
}

button.secondary {
  background-color: #e0e0e0;
  color: #333;
}

button.secondary:hover {
  background-color: #cfcfcf;
}
</style>
