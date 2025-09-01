<template>
  <div class="closest-approaches-container">
    <div v-if="hasData" class="body-section" v-for="(approaches, body) in sortedData" :key="body">
      <h3>{{ body }}</h3>
      <table>
        <thead>
          <tr>
            <th>Designation</th>
            <th>Close Approach Date</th>
            <th>Min Distance (LD)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="approach in approaches" :key="approach.des">
            <td>{{ approach.des }}</td>
            <td>{{ approach.cd }}</td>
            <td>{{ approach.dist_min.toFixed(5) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-else>No closest approaches data available.</p>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  closestApproaches: {
    type: Object,
    default: () => ({})
  }
})

const hasData = computed(() => Object.keys(props.closestApproaches).length > 0)

// Tri par corps céleste pour cohérence
const sortedData = computed(() => {
  const result = {}
  Object.keys(props.closestApproaches).sort().forEach(body => {
    result[body] = props.closestApproaches[body]
  })
  return result
})
</script>

<style scoped>
.closest-approaches-container {
  margin: 2rem 0;
}

.body-section {
  margin-bottom: 2rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ccc;
  padding: 0.5rem 0.8rem;
  text-align: left;
}

th {
  background-color: #e6f2fa;
}

h3 {
  margin-bottom: 0.5rem;
  color: #0077be;
}
</style>
