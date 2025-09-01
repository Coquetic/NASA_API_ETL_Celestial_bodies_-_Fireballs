<template>
  <div class="chart-container">
    <h2>🌍 Fireballs by Continent</h2>
    <Bar
      v-if="chartData.labels.length"
      :data="chartData"
      :options="chartOptions"
    />
    <p v-else>No data available</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, CategoryScale, LinearScale, BarElement)

const props = defineProps({
  regionCounts: {
    type: Array,
    default: () => []
  }
})

const sortedCounts = computed(() =>
  [...props.regionCounts].sort((a, b) =>
    a.region.localeCompare(b.region)
  )
)

const chartData = computed(() => ({
  labels: sortedCounts.value.map(entry => entry.region),
  datasets: [{
    label: 'Fireballs',
    backgroundColor: '#0077be',
    data: sortedCounts.value.map(entry => entry.count)
  }]
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true
    }
  }
}
</script>

<style scoped>
.chart-container {
  margin: 2rem 0;
  padding: 1rem;
  background: white;
  border: 1px solid #ccc;
  border-radius: 8px;
  height: 400px;
}
</style>
