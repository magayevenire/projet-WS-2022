<script setup lang="ts">
import { IElecteur } from '~~/types/IElecteur';

const conf = useRuntimeConfig()
const route = useRoute()

const { data: electeur, error } = await useAsyncData('electeur', () => $fetch<IElecteur>(`${conf.public.DJANGO_API_BASE}/electeur/${route.params.id}`))

if(electeur.value == null && error.value == true) {

}
</script>
<template>
  <div>
    <h1>Vérification de mon inscription sur la liste éléctorale</h1>
    <div v-if="electeur && electeur.id && !error">
      <span>Vous êtes bien inscrit</span>
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400 rounded-lg">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th class="p-3">Numéro CNI</th>
            <th class="p-3">Nom</th>
            <th class="p-3">Prénom</th>
            <th class="p-3">Date de naissance</th>
            <th class="p-3">Adresse</th>
            <th class="p-3">Bureau de vote</th>
          </tr>
        </thead>
        <tbody>
          <tr class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap bg-gray-300 dark:text-white">
            <td class="p-3">{{electeur.numero_cni}}</td>
            <td class="p-3">{{electeur.nom}}</td>
            <td class="p-3">{{electeur.prenom}}</td>
            <td class="p-3">{{electeur.date_naissance}}</td>
            <td class="p-3">{{electeur.adresse}}</td>
            <td class="p-3">{{electeur.bureau_vote}}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else class="bg-red-500 p-2 rounded-lg shadow-lg">
      <span class="text-white">Vous n'êtes pas inscrit sur la liste éléctorale allez <NuxtLink to="/electeur/inscription">ICI</NuxtLink> pour vous inscrir</span>
    </div>
  </div>
</template>