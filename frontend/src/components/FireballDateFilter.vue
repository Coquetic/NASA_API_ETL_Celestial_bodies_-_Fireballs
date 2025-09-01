<template>
  <div class="filter-container">
    <label for="start">📅 Du :</label>
    <input type="date" id="start" v-model="startDate" />

    <label for="end">📅 Au :</label>
    <input type="date" id="end" v-model="endDate" />

    <button @click="emitDateChange" class="filter-button">Filtrer</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['update:dates'])

const startDate = ref(null)
const endDate = ref(null)

function emitDateChange() {
  emit('update:dates', {
    start: startDate.value || null,
    end: endDate.value || null,
  })
}
</script>

<style scoped>
.filter-container {
  display: flex;
  gap: 1rem;
  align-items: center;
  padding: 1rem;
  background-color: #f9f9f9;
  border-radius: 8px;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

label {
  font-weight: 600;
  font-size: 1rem;
  user-select: none;
}

input[type='date'] {
  padding: 0.5rem;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-width: 140px;
}

/* Bouton filtre, inverse du bouton secondary du Home */
.filter-button {
  padding: 0.5rem 1rem;
  background-color: var(--color-nasa-blue, #2c3e50);
  color: white;
  border: 2px solid var(--color-nasa-blue, #2c3e50);
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.filter-button:hover,
.filter-button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(44, 62, 80, 0.3);
}
</style>
