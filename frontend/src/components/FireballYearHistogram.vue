<template>
  <div class="chart-container">
    <h2>📅 Fireballs per Year</h2>
    <Bar v-if="chartData.labels.length" :data="chartData" :options="chartOptions" />
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
  yearCounts: {
    type: Array,
    required: true
  }
})

const sortedCounts = computed(() => {
  return [...props.yearCounts].sort((a, b) => a.year - b.year)
})

const chartData = computed(() => ({
  labels: sortedCounts.value.map(entry => entry.year),
  datasets: [{
    label: 'Fireballs',
    backgroundColor: '#ff7043',
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
