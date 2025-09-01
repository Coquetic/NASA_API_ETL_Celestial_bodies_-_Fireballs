import { defineStore } from 'pinia'
import { ref, watch } from 'vue'
import axios from 'axios'

export const useCADStore = defineStore('cad', () => {
  const cadRecords = ref([])
  const bodyCounts = ref({})
  const stats = ref(null)
  const byMonth = ref([])
  const closestApproaches = ref({})

  const startDate = ref(null)
  const endDate = ref(null)

  async function fetchCAD() {
    try {
      const params = {}
      if (startDate.value) params.start_date = startDate.value
      if (endDate.value) params.end_date = endDate.value

      const res = await axios.get('http://127.0.0.1:8000/api/cad/', { params })
      cadRecords.value = res.data

      const counts = {}
      cadRecords.value.forEach(c => {
        counts[c.body] = (counts[c.body] || 0) + 1
      })
      bodyCounts.value = counts

    } catch (error) {
      console.error('Erreur lors de la récupération des CAD :', error)
    }
  }

  async function fetchStats() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/cad/stats')
      stats.value = res.data
    } catch (error) {
      console.error('Erreur lors de la récupération des stats CAD :', error)
    }
  }

  async function fetchByMonth() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/cad/by-month')
      byMonth.value = res.data.data
    } catch (error) {
      console.error('Erreur lors de la récupération des CAD par mois :', error)
    }
  }

  async function fetchClosestApproaches(limit = 3) {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/api/cad/closest-approaches?limit=${limit}`)
      closestApproaches.value = res.data.data
    } catch (error) {
      console.error('Erreur lors de la récupération des closest approaches CAD :', error)
    }
  }

  watch([startDate, endDate], () => {
    fetchCAD()
  })

  function setDateFilter(start, end) {
    startDate.value = start || null
    endDate.value = end || null
  }

  fetchCAD()
  fetchStats()
  fetchByMonth()
  fetchClosestApproaches()

  return {
    cadRecords,
    bodyCounts,
    stats,
    byMonth,
    closestApproaches,
    startDate,
    endDate,
    fetchCAD,
    fetchStats,
    fetchByMonth,
    fetchClosestApproaches,
    setDateFilter
  }
})
