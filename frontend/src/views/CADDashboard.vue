<template>
  <main class="dashboard" aria-label="CAD Dashboard detected by NASA">
    <div class="top-actions">
      <button
        class="back-home"
        @click="goHome"
        aria-label="Return to Home page"
      >
        Home
      </button>

      <button 
        class="download-btn"
        @click="downloadCsv"
        aria-label="Download all CAD as CSV"
      >
        📥 Download CSV
      </button>
    </div>

    <h1 class="main-title">🪐 NASA CAD Dashboard</h1>

    <!-- Introduction -->
    <h2 class="section-subtitle">Explanations CAD</h2>
    <p class="intro-text">
      Close-Approach Data (CAD) describe near-Earth objects passing close to our planet. 
      They help NASA monitor potential hazards and study orbital dynamics. 
      This dashboard visualizes CAD records to better understand their distribution.
    </p>

    <!-- Section Stats -->
    <h2 class="section-subtitle">🌐 Global Statistics</h2>
    <section class="stats-section" aria-label="Global CAD Stats">
      <CadStats :stats="cadStore.stats" />
    </section>

    <!-- Polar Chart -->
    <h2 class="section-subtitle">📊 CAD Distribution by Body</h2>
    <section class="polar-chart-section" aria-label="Polar chart CAD">
      <CadPolarChart :cadData="cadStore.cadRecords" />
    </section>

    <!-- By Month Chart -->
    <h2 class="section-subtitle">📊 CAD Distribution by month</h2>
    <section class="bymonth-section" aria-label="CAD repartition by month">
      <CadByMonth :byMonth="cadStore.byMonth" />
    </section>

    <!-- Closest Approaches -->
    <h2 class="section-subtitle">Closest Approaches per celestial bodies</h2>
    <section class="closest-section" aria-label="CAD Closest Approaches">
      <CadClosestApproaches :closestApproaches="cadStore.closestApproaches"/>
    </section>
  </main>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCADStore } from '@/stores/cad'

import CadPolarChart from '@/components/CADPolarChart.vue'
import CadStats from '@/components/CADStats.vue'
import CadByMonth from '@/components/CADByMonth.vue'
import CadClosestApproaches from '@/components/CADClosestApproaches.vue'

const router = useRouter()
const cadStore = useCADStore()

function goHome() {
  router.push('/')
}

onMounted(() => {
  // Chargement initial
  cadStore.setDateFilter(null, null)
})

async function downloadCsv() {
  try {
    const response = await fetch("/api/cad/download", { method: "GET" })
    if (!response.ok) throw new Error("Error during download CSV")

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = "cad.csv"
    document.body.appendChild(a)
    a.click()
    a.remove()
    window.URL.revokeObjectURL(url)
  } catch (err) {
    console.error(err)
    alert("Impossible to download CSV")
  }
}
</script>

<style scoped>
.top-actions {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.back-home {
  padding: 0.4rem 1rem;
  background-color: var(--color-nasa-blue, #2c3e50);
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.back-home:hover,
.back-home:focus-visible {
  background-color: var(--color-nasa-red, #d32f2f);
  outline: none;
  box-shadow: 0 0 0 3px rgba(211, 47, 47, 0.7);
}

.dashboard {
  padding: 1rem;
  max-width: 1000px;
  margin: 0 auto;
}

.main-title {
  font-size: 3rem;
  font-weight: 600;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

.section-subtitle {
  position: relative;
  font-size: 1.6rem;
  margin-top: 4rem;
  margin-bottom: 1.2rem;
  padding-bottom: 0.2rem;
  text-align: center;
  font-weight: 600;
}

.section-subtitle::before {
  content: "";
  position: absolute;
  top: -1.5rem;
  left: 50%;
  transform: translateX(-50%);
  width: 400px;
  height: 3px;
  background: linear-gradient(to right, transparent, #0077be, transparent);
  opacity: 0.4;
  border-radius: 2px;
}

.intro-text {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 1.5rem;
  font-size: 1rem;
  line-height: 1.6;
  color: #444;
}

.stats-section {
  margin: 1rem 0;
}
</style>
