<template>
  <div class="about">
    <button class="back-home" @click="goHome">Home</button>

    <h1>About this project</h1>
    <p>
      This project is an application for visualizing meteors (fireballs) & CAD (Close-Approach Data) detected by NASA.
      It allows you to explore data, filter by date, and visualize events on an interactive map.
    </p>

    <section>
      <h2>Main features</h2>
      <ul>
        <li>Interactive display of detected meteors</li>
        <li>Filtering by date ranges</li>
        <li>Visualization on a map with details of each event</li>
        <li>In-depth analysis of meteors and objects approaching celestial bodies</li>
      </ul>
    </section>

    <section>
      <h2>Technologies used</h2>
      <ul>
        <li>Frontend : Vue 3 with Pinia, Vue Router</li>
        <li>Backend : API REST avec FastAPI</li>
        <li>Mapping : Leaflet</li>
        <li>Animation : Three.js</li>
        <li>Deployment : Vite for frontend & uvicorn for backend</li>
      </ul>
    </section>

    <section>
      <h2>Contact</h2>
      <p>
        For any questions or suggestions, you can contact me at <a href="mailto:arno.coquet35@gmail.com">arno.coquet35@gmail.com</a>.
      </p>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goHome() {
  router.push('/')
}
</script>

<style scoped>
.about {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1rem 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  background: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
}

.back-home {
  margin-bottom: 1rem;
  padding: 0.4rem 1rem;
  background-color: var(--color-nasa-blue, #2c3e50);
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.back-home:hover {
  background-color: var(--color-nasa-red, #d32f2f);
}

h1 {
  margin-bottom: 1rem;
  color: var(--color-nasa-blue, #2c3e50);
}

h2 {
  margin-top: 2rem;
  margin-bottom: 0.5rem;
  color: var(--color-nasa-blue, #34495e);
}

p, ul {
  font-size: 1.1rem;
  line-height: 1.6;
}

ul {
  padding-left: 1.5rem;
  list-style-type: disc;
}

a {
  color: var(--color-nasa-blue, #2c3e50);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
