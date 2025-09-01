<template>
  <section v-if="hasStats" class="kpi-section" aria-label="Global fireball statistics">
    <!-- Total Fireballs -->
    <div class="category">
      <div class="category-header">
        <div class="category-title">☄️ Total Fireballs</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card">
          <div class="kpi-label">Count</div>
          <div class="kpi-value">{{ stats.total_fireballs }}</div>
        </div>
      </div>
    </div>

    <!-- Energy -->
    <div v-if="stats.energy" class="category">
      <div class="category-header">
        <div class="category-title">⚡ Energy (kt)</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in energyStats" :key="key">
          <div class="kpi-label">{{ key }}</div>
          <div class="kpi-value">{{ format(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Altitude -->
    <div v-if="stats.altitude" class="category">
      <div class="category-header">
        <div class="category-title">🛫 Altitude (km)</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in altitudeStats" :key="key">
          <div class="kpi-label">{{ key }}</div>
          <div class="kpi-value">{{ format(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Velocity -->
    <div v-if="stats.velocity" class="category">
      <div class="category-header">
        <div class="category-title">💨 Velocity (km/s)</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in velocityStats" :key="key">
          <div class="kpi-label">{{ key }}</div>
          <div class="kpi-value">{{ format(val) }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  stats: {
    type: Object,
    default: () => ({})
  }
})

const hasStats = computed(() => props.stats && Object.keys(props.stats).length > 0)

function format(num) {
  return Number(num).toFixed(1)
}

const energyStats = computed(() => statsSubset(props.stats.energy))
const altitudeStats = computed(() => statsSubset(props.stats.altitude))
const velocityStats = computed(() => statsSubset(props.stats.velocity))

function statsSubset(obj) {
  if (!obj) return {}
  return {
    Min: obj.min,
    Max: obj.max,
    Average: obj.average,
    Median: obj.median
  }
}
</script>

<style scoped>
.kpi-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin: 2rem 0;
}

.category {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.category-header {
  display: inline-flex;
  align-items: center;
  padding: 0.3rem 0.8rem;
  background-color: #e6f2fa;
  border-left: 5px solid #0077be;
  border-radius: 4px;
  font-weight: bold;
  color: #333;
  font-size: 1rem;
  width: fit-content;
}

.kpi-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
}

.kpi-card {
  background: white;
  border: 1px solid #ccc;
  border-left: 4px solid #0077be;
  border-radius: 5px;
  padding: 0.5rem 0.8rem;
  text-align: center;
  width: 110px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.kpi-label {
  font-size: 0.8rem;
  color: #666;
  margin-bottom: 0.3rem;
}

.kpi-value {
  font-size: 1.3rem;
  font-weight: bold;
  color: #0077be;
}
</style>
