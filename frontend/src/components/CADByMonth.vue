<template>
  <div class="chart-container">
    <h2>📅 CAD by Month</h2>
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
  byMonth: {
    type: Array,
    default: () => []
  }
})

// Sort by ascendant date
const sortedByMonth = computed(() =>
  [...props.byMonth].sort((a, b) => a.month.localeCompare(b.month))
)

const chartData = computed(() => ({
  labels: sortedByMonth.value.map(entry => entry.month),
  datasets: [{
    label: 'Close Approaches',
    backgroundColor: '#0077be',
    data: sortedByMonth.value.map(entry => entry.count)
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
