<script lang="ts" setup>
import { IElection } from "~/types/IElection";

const conf = useRuntimeConfig()
const elections = ref<IElection[]>([]);

const { data } = await useAsyncData("election", () =>
  $fetch<[]>(`${conf.public.DJANGO_API_BASE}/election/`)
);

elections.value = data.value;
</script>
<template>
  <div>
    <h1>Résultat</h1>
    <ul class="list-disc list-inside">
      <li v-for="election in elections" :key="election.id">
        <NuxtLink :to="`/service/resultat/definitif/${election.id}`">
          {{ election.nom }} - {{ election.jour_vote }}
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>