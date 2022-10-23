<script lang="ts" setup>
import { IElection } from "~/types/IElection";

const route = useRoute();
const conf = useRuntimeConfig();

const election = ref<IElection>(null);

onMounted(async () => {
  election.value = await $fetch(
    `${conf.public.DJANGO_API_BASE}/election/${route.params.id}`
  );
});
console.log(`vote/id#setup@election`, election);
</script>
<template>
  <span v-if="!election">Chargement ...</span>
  <div v-else>
    <h1>Resultat definitif</h1>
    <h2>{{ election.nom }} - {{election.jour_vote}}</h2>

    <!-- <pre>{{ election }}</pre> -->


    <div class="overflow-x-auto relative my-10">
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead
          class="
            text-xs text-gray-700
            uppercase
            bg-gray-50
            dark:bg-gray-700 dark:text-gray-400
          "
        >
          <tr>
            <th scope="col" class="py-3 px-6">Parti</th>
            <th scope="col" class="py-3 px-6">Candidat</th>
            <th scope="col" class="py-3 px-6">Nombre de Vote</th>
            <th scope="col" class="py-3 px-6">Pourcentage</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="candidature in election.candidats" :key="candidature.id" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
            <th
              scope="row"
              class="
                py-4
                px-6
                font-medium
                text-gray-900
                whitespace-nowrap
                dark:text-white
              "
            >
              {{candidature.nom_parti}}
            </th>
            <td class="py-4 px-6">{{candidature.candidat?.nom}} {{candidature.candidat?.prenom}}</td>
            <td class="py-4 px-6">{{candidature?.votes}}</td>
            <td class="py-4 px-6">{{candidature.candidat?.pourcentage}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>