<script setup lang="ts">
import { IElection } from '~/types/IElection'
import { IUser } from '~/types/IUser'

const user = useState<IUser>('user')

const elections = ref<IElection[]>([])
const { data } = await useAsyncData("election", () =>
  $fetch<[]>(`${useRuntimeConfig().public.DJANGO_API_BASE}/election/`)
);

elections.value = data.value
</script>

<template>
  <div>
    <h1>Je vote</h1>

    <div v-if="user?.electeur?.id" class="flex flex-row flex-wrap gap-2 items-center justify-center">
      <Election v-for="election in elections" :key="election.id" :item="election" />
    </div>
    <div v-else class="bg-red-500 p-2 rounded-lg shadow-lg">
      <span class="text-white">Vous n'êtes pas inscrit sur la liste éléctorale allez <NuxtLink
          to="/electeur/inscription">ICI</NuxtLink> pour vous inscrir</span>
    </div>
  </div>
</template>