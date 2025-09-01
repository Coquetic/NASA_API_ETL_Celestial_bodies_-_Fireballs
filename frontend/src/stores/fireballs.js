import { defineStore } from 'pinia'
import { ref, watch } from 'vue'
import axios from 'axios'

export const useFireballStore = defineStore('fireballs', () => {
  const fireballs = ref([])
  const topFireballs = ref([])
  const stats = ref(null)
  const regionCounts = ref([])
  const yearCounts = ref([])

  const startDate = ref(null)
  const endDate = ref(null)

  async function fetchFireballs() {
    try {
      const params = {}
      if (startDate.value) params.start_date = startDate.value
      if (endDate.value) params.end_date = endDate.value

      const res = await axios.get('http://127.0.0.1:8000/api/fireballs/', { params })
      fireballs.value = res.data
    } catch (error) {
      console.error('Erreur lors de la récupération des fireballs :', error)
    }
  }

  async function fetchTopFireballs() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/fireballs/top')
      topFireballs.value = res.data
    } catch (error) {
      console.error('Erreur lors de la récupération des top fireballs :', error)
    }
  }

  async function fetchStats() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/fireballs/stats')
      stats.value = res.data
    } catch (error) {
      console.error('Erreur lors de la récupération des stats :', error)
    }
  }

  async function fetchRegionCounts() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/fireballs/by-continents')
      regionCounts.value = res.data.data
    } catch (error) {
      console.error('Erreur lors de la récupération des comptes par région :', error)
    }
  }

  async function fetchYearCounts() {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/fireballs/year-counts')
      yearCounts.value = res.data.data
    } catch (error) {
      console.error('Erreur lors de la récupération des comptes par année :', error)
    }
  }

  // Watch pour relancer fetchFireballs si filtre date change
  watch([startDate, endDate], () => {
    fetchFireballs()
  })

  // Chargement initial
  fetchFireballs()
  fetchTopFireballs()
  fetchStats()
  fetchRegionCounts()
  fetchYearCounts()

  function setDateFilter(start, end) {
    startDate.value = start || null
    endDate.value = end || null
  }

  return {
    fireballs,
    topFireballs,
    stats,
    regionCounts,
    yearCounts,
    startDate,
    endDate,
    fetchFireballs,
    fetchTopFireballs,
    fetchStats,
    fetchRegionCounts,
    fetchYearCounts,
    setDateFilter
  }
})
