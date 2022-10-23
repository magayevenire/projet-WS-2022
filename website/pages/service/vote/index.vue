<script setup lang="ts">
import { IElection } from '~/types/IElection'
const elections = ref<IElection[]>([])
const { data } = await useAsyncData("election", () =>
  $fetch<[]>(`${useRuntimeConfig().public.DJANGO_API_BASE}/election/`)
);

elections.value = data.value
</script>

<template>
  <div>
    <h1>Je vote</h1>

    <ul class="list-disc list-inside">
      <li v-for="election in elections" :key="election.id">
        <NuxtLink :to="`/service/vote/${election.id}`">
          {{election.nom}} - {{election.jour_vote}}
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>