<template>
  <div class="table-container">
    <h2>🔥 Top 20 Fireballs (5 dernières années)</h2>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Latitude</th>
          <th>Lat Dir</th>
          <th>Longitude</th>
          <th>Lon Dir</th>
          <th>Énergie (kT)</th>
          <th>Impact (GJ)</th>
          <th>Altitude (km)</th>
          <th>Vitesse (km/s)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(fb, index) in fireballs" :key="index">
          <td>{{ fb.date }}</td>
          <td>{{ fb.lat }}</td>
          <td>{{ fb['lat-dir'] }}</td>
          <td>{{ fb.lon }}</td>
          <td>{{ fb['lon-dir'] }}</td>
          <td>{{ fb.energy }}</td>
          <td>{{ fb['impact-e'] }}</td>
          <td>{{ fb.alt ?? '—' }}</td>
          <td>{{ fb.vel ?? '—' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const props = defineProps({
  fireballs: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.table-container {
  margin-top: 2rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #ffffff;
  padding: 1rem;
  overflow-x: auto;
  box-shadow: 0 2px 6px rgb(0 0 0 / 0.05);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  min-width: 700px;
}

th,
td {
  padding: 0.5rem;
  border: 1px solid #ddd;
  text-align: center;
  white-space: nowrap;
}

thead {
  background-color: #333;
  font-weight: 600;
}

h2 {
  margin-bottom: 1rem;
  color: #333;
}
</style>
