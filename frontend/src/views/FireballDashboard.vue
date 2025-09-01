<template>
  <main class="dashboard" aria-label="Fireballs Dashboard detected by NASA">
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
        aria-label="Download all fireballs as CSV"
      >
        📥 Download CSV
      </button>
    </div>

    <h1 class="main-title">☄️ NASA Fireball Dashboard</h1>

    <h2 class="section-subtitle">🌐 Global Statistics</h2>
    <section class="stats-section" aria-label="Statistiques globales">
      <FireballStats :stats="fireballStore.stats" />
    </section>

    <h2 class="section-subtitle">📅 Date-Based Fireball Mapping</h2>
    <FireballDateFilter 
      :startDate="fireballStore.startDate" 
      :endDate="fireballStore.endDate" 
      @update:dates="handleDateChange" 
    />

    <section class="map-section" aria-label="Carte des météores">
      <FireballMap :fireballs="fireballStore.fireballs" />
    </section>

    <h2 class="section-subtitle">📊 Fireball Distribution & Analysis</h2>
    <section class="histogram-section" aria-label="Histogramme par année">
      <FireballYearHistogram :yearCounts="fireballStore.yearCounts" />
    </section>

    <section class="heatmap-section" aria-label="Carte des continents">
      <FireballContinentHeatmap :regionCounts="fireballStore.regionCounts" />
    </section>

    <section class="table-section" aria-label="Top météores">
      <template v-if="fireballStore.loading">
        <p class="loading">Loading the data…</p>
      </template>
      <template v-else>
        <TopFireballsTable :fireballs="fireballStore.topFireballs" />
      </template>
    </section>
  </main>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useFireballStore } from '@/stores/fireballs'

import FireballMap from '@/components/FireballMap.vue'
import FireballDateFilter from '@/components/FireballDateFilter.vue'
import TopFireballsTable from '@/components/TopFireballsTable.vue'
import FireballStats from '@/components/FireballStats.vue'
import FireballContinentHeatmap from '@/components/FireballContinentHeatmap.vue'
import FireballYearHistogram from '@/components/FireballYearHistogram.vue'

const router = useRouter()
const fireballStore = useFireballStore()

function goHome() {
  router.push('/')
}

const today = new Date()
const fiveYearsAgo = new Date(today)
fiveYearsAgo.setFullYear(today.getFullYear() - 5)
// const defaultStart = fiveYearsAgo.toISOString().split('T')[0]
// const defaultEnd = today.toISOString().split('T')[0]

onMounted(() => {
  fireballStore.setDateFilter(null, null)
})

function handleDateChange({ start, end }) {
  fireballStore.setDateFilter(start, end)
}

async function downloadCsv() {
  try {
    const response = await fetch("/api/fireballs/download", {
      method: "GET",
    })

    if (!response.ok) throw new Error("Error during download CSV")

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = "fireballs.csv"
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
  align-items: center;
  margin-bottom: 1rem;
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

.back-home:hover,
.back-home:focus-visible {
  background-color: var(--color-nasa-red, #d32f2f);
  outline: none;
  box-shadow: 0 0 0 3px rgba(211, 47, 47, 0.7);
}

.dashboard {
  padding: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

.main-title {
  font-size: 3rem;
  font-weight: 600;
  text-align: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.section-subtitle {
  position: relative;
  font-size: 1.6rem;
  margin-top: 3rem;
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


.stats-section {
  margin: 1rem 0;
}

.map-section {
  margin: 2rem 0;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
}

.table-section {
  max-height: 400px;
  overflow-y: auto;
}

.loading {
  font-style: italic;
  color: #666;
}
</style>
