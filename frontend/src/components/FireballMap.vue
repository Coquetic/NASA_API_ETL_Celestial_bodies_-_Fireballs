<template>
  <div id="map" class="map-container" aria-label="Carte des météores détectés"></div>
</template>

<script setup>
import { onMounted, watch, nextTick, onBeforeUnmount } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

import fireballLow from '@/assets/fireballs_icons/fireball-low.png'
import fireballMedium from '@/assets/fireballs_icons/fireball-medium.png'
import fireballHigh from '@/assets/fireballs_icons/fireball-high.png'

const props = defineProps({
  fireballs: {
    type: Array,
    default: () => []
  }
})

let map
let markersLayer

function convertCoord(value, direction) {
  if (value === null || value === undefined || !direction) return null
  return direction === 'S' || direction === 'W' ? -Math.abs(value) : Math.abs(value)
}

function getFireballIcon(energy) {
  let iconUrl = fireballLow
  let className = 'fireball-low'

  if (energy >= 10 && energy < 30) {
    iconUrl = fireballMedium
    className = 'fireball-medium'
  } else if (energy >= 30) {
    iconUrl = fireballHigh
    className = 'fireball-high'
  }

  return L.icon({
    iconUrl,
    iconSize: [18, 18],
    iconAnchor: [9, 9],
    popupAnchor: [0, -9],
    className: `fireball-icon ${className}`,
  })
}

function addMarkers() {
  if (!map) return
  if (!markersLayer) {
    markersLayer = L.layerGroup().addTo(map)
  }

  markersLayer.clearLayers()

  const bounds = []

  props.fireballs.forEach((fb) => {
    const lat = convertCoord(fb.lat, fb['lat-dir'])
    const lon = convertCoord(fb.lon, fb['lon-dir'])

    if (lat === null || lon === null) return

    const tooltip = `
      <b>Date:</b> ${fb.date}<br/>
      <b>Énergie:</b> ${fb.energy} kT<br/>
      <b>Impact:</b> ${fb['impact-e']} GJ<br/>
      <b>Vitesse:</b> ${fb.vel !== null ? fb.vel : 'N/A'} km/s<br/>
      <b>Altitude:</b> ${fb.alt !== null ? fb.alt : 'N/A'} km
    `

    const icon = getFireballIcon(fb.energy)

    const marker = L.marker([lat, lon], { icon }).bindPopup(tooltip)
    markersLayer.addLayer(marker)

    bounds.push([lat, lon])
  })

  if (bounds.length > 0) {
    map.fitBounds(bounds, { padding: [40, 40], maxZoom: 6 })
  } else {
    map.setView([20, 0], 2)
  }
}

onMounted(async () => {
  await nextTick()

  const mapContainer = document.getElementById('map')
  if (!mapContainer) {
    console.error('Map container not found')
    return
  }

  map = L.map(mapContainer).setView([20, 0], 2)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; OpenStreetMap contributors',
  }).addTo(map)

  addMarkers()
})

watch(
  () => props.fireballs,
  () => {
    addMarkers()
  },
  { deep: true, immediate: true }
)

onBeforeUnmount(() => {
  if (map) {
    map.remove()
    map = null
    markersLayer = null
  }
})
</script>

<style scoped>
.map-container {
  height: 100%;
  width: 100%;
}

/* Animation rebond douce au hover */
.fireball-icon:hover {
  animation: bounce 0.6s ease;
  will-change: transform;
}

@keyframes bounce {
  0%   { transform: translateY(0); }
  30%  { transform: translateY(-6px); }
  50%  { transform: translateY(0); }
  70%  { transform: translateY(-3px); }
  100% { transform: translateY(0); }
}
</style>
