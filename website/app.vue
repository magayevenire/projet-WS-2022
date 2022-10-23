<script setup lang="ts">

// useHead({
//   script: [
//     {
//       src: "./node_modules/flowbite/dist/flowbite.js",
//       body: false
//     }
//   ]
// })

const nuxtApp = useNuxtApp()

nuxtApp.hook("page:finish", () => {
  window.scrollTo(0, 0)
})

const user = useUser()
</script>

<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
