<template>
  <div>
    <canvas id="cad-polar-chart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, watch } from 'vue'
import { Chart, PolarAreaController, RadialLinearScale, ArcElement, Tooltip, Legend } from 'chart.js'
import { useCADStore } from '@/stores/cad'

Chart.register(PolarAreaController, RadialLinearScale, ArcElement, Tooltip, Legend)

const cadStore = useCADStore()

let chartInstance = null

function renderChart() {
  const labels = Object.keys(cadStore.bodyCounts)
  const data = Object.values(cadStore.bodyCounts)

  const ctx = document.getElementById('cad-polar-chart').getContext('2d')

  if (chartInstance) chartInstance.destroy()

  chartInstance = new Chart(ctx, {
    type: 'polarArea',
    data: {
      labels,
      datasets: [{
        label: 'Number of records per Celestial body ',
        data,
        backgroundColor: [
          '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'
        ],
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'right' }
      },
      scales: {
        r: {
          beginAtZero: true
        }
      }
    }
  })
}

onMounted(() => {
  renderChart()
})

watch(() => cadStore.bodyCounts, () => {
  renderChart()
}, { deep: true })
</script>

<style scoped>
canvas {
  max-width: 100%;
  max-height: 400px;
}
</style>
