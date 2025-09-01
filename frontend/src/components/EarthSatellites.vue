<template>
  <canvas ref="canvas" class="earth-canvas"></canvas>
</template>

<script setup>
import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
import { onMounted, onBeforeUnmount, ref } from 'vue'
import earthTextureUrl from '@/assets/world.jpg'

const canvas = ref(null)
let scene, camera, renderer, earth, satellites = [], animationId
let satelliteModel = null

const satelliteCount = 5

function createEarth() {
  const geometry = new THREE.SphereGeometry(1, 64, 64)
  const textureLoader = new THREE.TextureLoader()
  const texture = textureLoader.load(earthTextureUrl)

  const material = new THREE.MeshStandardMaterial({
    map: texture,
    metalness: 0.3,
    roughness: 0.7,
  })

  return new THREE.Mesh(geometry, material)
}

function createModelSatellite() {
  if (!satelliteModel) return new THREE.Mesh()
  const modelClone = satelliteModel.clone(true)
  modelClone.scale.set(0.015, 0.015, 0.015)
  return modelClone
}

function loadSatelliteModel() {
  return new Promise((resolve, reject) => {
    const loader = new GLTFLoader()
    loader.load('/models/satellite.glb', gltf => {
      satelliteModel = gltf.scene
      resolve()
    }, undefined, reject)
  })
}

async function init() {
  await loadSatelliteModel()

  scene = new THREE.Scene()

  camera = new THREE.PerspectiveCamera(50, 2, 0.1, 100)
  camera.position.set(0, 0, 4)

  renderer = new THREE.WebGLRenderer({
    canvas: canvas.value,
    alpha: true,
    antialias: true,
  })
  renderer.setClearColor(0x000000, 0)

  earth = createEarth()
  scene.add(earth)

  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6)
  scene.add(ambientLight)

  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8)
  directionalLight.position.set(5, 3, 5)
  scene.add(directionalLight)

  satellites = []

  for (let i = 0; i < satelliteCount; i++) {
    const sat = createModelSatellite()
    sat.userData = {
      radius: 1.25 + Math.random() * 0.45,
      speed: 0.5 + Math.random(),
      angle: Math.random() * Math.PI * 2,
      axis: new THREE.Vector3(Math.random(), Math.random(), Math.random()).normalize(),
    }
    scene.add(sat)
    satellites.push(sat)
  }

  onResize()
}

function animate() {
  try {
    animationId = requestAnimationFrame(animate)
  } catch (err) {
    console.error('Error in animate(): ', err)
  }

  if (earth && earth.rotation) {
    earth.rotation.y += 0.0015
  } else {
    console.error('⛔ earth is undefined or has no rotation property')
  }

  satellites.forEach(sat => {
    sat.userData.angle += sat.userData.speed * 0.01

    const x = Math.cos(sat.userData.angle) * sat.userData.radius
    const y = Math.sin(sat.userData.angle) * sat.userData.radius
    const pos = new THREE.Vector3(x, y, 0)

    const quat = new THREE.Quaternion()
    quat.setFromAxisAngle(sat.userData.axis, sat.userData.angle)
    pos.applyQuaternion(quat)

    sat.position.copy(pos)
  })

  if (renderer && scene && camera) {
    renderer.render(scene, camera)
  }
}

function onResize() {
  if (!canvas.value || !renderer) return

  const width = canvas.value.clientWidth
  const height = width / 2

  renderer.setSize(width, height, false)
  camera.aspect = width / height
  camera.updateProjectionMatrix()
}

onMounted(() => {
  window.onerror = (message, source, lineno, colno, error) => {
    console.log('🛑 Global error caught:')
    console.log({ message, source, lineno, colno, error })
  }

  try {
    init().then(() => {
      console.log('✅ Init done')
      animate()
      console.log('✅ Animation started')
    }).catch(err => {
      console.error('Error during init():', err)
    })
  } catch (err) {
    console.error("Error in onMounted try/catch", err)
  }

  window.addEventListener('resize', onResize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', onResize)
  if (animationId) cancelAnimationFrame(animationId)
  if (renderer) renderer.dispose()
})
</script>

<style scoped>
.earth-canvas {
  width: 100%;
  aspect-ratio: 2 / 1;
  display: block;
  margin: 1rem auto;
  border-radius: 8px;
  background: transparent;
}
</style>
