<template>
  <NuxtLink
    class="p-6 cursor-pointer max-w-sm bg-white hover:no-underline hover:bg-gray-100 w-56 h-56 flex flex-col justify-center items-center text-center text-xl hover:font-bold text-slate-500 hover:text-blue-500 rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
    :to="`/service/vote/${item.id}`">
    <span>{{ item.nom }}</span>
    <span class="text-sm font-light">{{ item.jour_vote }}</span>
  </NuxtLink>
</template>

<script lang="ts" setup>

const { item } = defineProps(['item'])

onMounted(() => {
  // console.log('a service: ', item)
})

</script>
