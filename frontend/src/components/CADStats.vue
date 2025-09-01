<template>
  <section v-if="hasStats" class="kpi-section" aria-label="Global CAD statistics">
    <!-- Total Approaches -->
    <div class="category">
      <div class="category-header">
        <div class="category-title">☄️ Total Approaches</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card">
          <div class="kpi-label">Count</div>
          <div class="kpi-value">{{ stats.total_approaches }}</div>
        </div>
      </div>
    </div>

    <!-- Celestial Bodies -->
    <div class="category">
      <div class="category-header">
        <div class="category-title">🌍 Celestial Bodies</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card">
          <div class="kpi-label">Distinct Bodies</div>
          <div class="kpi-value">{{ stats.bodies_count }}</div>
        </div>
      </div>
    </div>

    <!-- Distance -->
    <div v-if="stats.distance" class="category">
      <div class="category-header">
        <div class="category-title">Distance (LD)</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in distanceStats" :key="key">
          <div class="kpi-label">{{ key }}</div>
          <div class="kpi-value">{{ format(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Velocity v_rel -->
    <div v-if="stats.v_rel" class="category">
      <div class="category-header">
        <div class="category-title">💨 Relative Velocity (km/s)</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in vRelStats" :key="key">
          <div class="kpi-label">{{ key }}</div>
          <div class="kpi-value">{{ format(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Velocity v_inf -->
    <div v-if="stats.v_inf" class="category">
      <div class="category-header">
        <div class="category-title">🚀 Hyperbolic Excess (km/s)</div>
      </div>
      <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in vInfStats" :key="key">
          <div class="kpi-label">{{ key }}</div>
          <div class="kpi-value">{{ format(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Magnitude -->
    <div v-if="stats.magnitude" class="category">
    <div class="category-header">
        <div class="category-title">⭐ Absolute Magnitude (H)</div>
    </div>
    <div class="kpi-row">
        <div class="kpi-card" v-for="(val, key) in magnitudeStats" :key="key">
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
  if (num === null || num === undefined) return "-"
  return Number(num).toFixed(2)
}

function statsSubset(obj) {
  if (!obj) return {}
  return {
    Min: obj.min,
    Max: obj.max,
    Average: obj.average,
    Median: obj.median
  }
}

const distanceStats = computed(() => statsSubset(props.stats.distance))
const vRelStats = computed(() => statsSubset(props.stats.v_rel))
const vInfStats = computed(() => statsSubset(props.stats.v_inf))
const magnitudeStats = computed(() => statsSubset(props.stats.magnitude))
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
