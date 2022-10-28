<template>
  <div
    class="p-6 max-w-sm cursor-pointer bg-white hover:no-underline hover:bg-gray-100 w-56 h-56 flex flex-col justify-center items-center text-center text-xl hover:font-bold text-slate-500 hover:text-blue-500 rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700 duration-75"
    :class="isSelected == true && 'bg-green-300 hover:bg-green-400 text-white border border-green-600'"
    @click="$emit('selectCandidat', item.id)"
  >
  <span>{{ item.nom_parti }}</span>
  <span class="text-sm">{{ item.candidat.nom }} {{ item.candidat.prenom }}</span>
  </div>
</template>

<script lang="ts" setup>

const { item, isSelected } = defineProps(['item', 'isSelected'])

onMounted(() => {
  console.log('a candidat: ', item, isSelected)
})

</script>
