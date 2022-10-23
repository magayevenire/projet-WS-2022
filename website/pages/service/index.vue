<script lang="ts" setup>
const services = [
  { key: 0, name: "Demande de changement de bureau de vote", page: "/service/changer/bureau" },
  { key: 1, name: "Voter", page: "/service/vote" },
  { key: 2, name: "Visualisation des résultats provisoire", page: "/service/resultat/provisoire" },
  { key: 3, name: "Visualisation des résultats définitives", page: "/service/resultat/definitif" },
  { key: 4, name: "Publication des résultats", page: "/service/resultat" },
  { key: 5, name: "Rapport", page: "/service/rapport" },
  { key: 6, name: "Gestion des contestations", page: "/service/contestation" },
  { key: 7, name: "Inscription electeur", page: "/electeur/inscription" },
  { key: 8, name: "Inscription candidat", page: "/candidat/inscription" },
]
</script>
<template>
  <div>
    <h1>Les services</h1>

    <ul class="list-disc ml-5">
      <li v-for="service in services" :key="service.key" >
        <NuxtLink :to="service.page">{{service.name}}</NuxtLink>
      </li>
    </ul>
  </div>
</template>