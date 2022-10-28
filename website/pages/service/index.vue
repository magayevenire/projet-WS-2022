<script lang="ts" setup>
const services = [
  { key: 7, title: "Inscription electeur", page: "/electeur/inscription" },
  { key: 8, title: "Inscription candidat", page: "/candidat/inscription" },
  { key: 0, title: "Demande de changement de bureau de vote", page: "/service/changer/bureau" },
  { key: 1, title: "Voter", page: "/service/vote" },
  { key: 2, title: "Visualisation des résultats provisoire", page: "/service/resultat/provisoire" },
  { key: 3, title: "Visualisation des résultats définitives", page: "/service/resultat/definitif" },
  { key: 4, title: "Publication des résultats", page: "/service/resultat" },
  { key: 5, title: "Rapport", page: "/service/rapport" },
  { key: 6, title: "Gestion des contestations", page: "/service/contestation" },
]
</script>
<template>
  <div>
    <h1>Les services</h1>

    <div class="flex flex-row flex-wrap gap-2 items-center justify-center">
      <Service v-for="service in services" :key="service.key" :item="service"></Service>
    </div>

    <!-- <ul class="list-disc ml-5">
      <li v-for="service in services" :key="service.key" >
        <NuxtLink :to="service.page">{{service.title}}</NuxtLink>
      </li>
    </ul> -->
  </div>
</template>