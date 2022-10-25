<script lang="ts" setup>
import { IElection } from "~/types/IElection";
import { IUser } from "~~/types/IUser";
import { IVote } from "~~/types/IVote";

const route = useRoute();
const conf = useRuntimeConfig();
const user = useState<IUser>('user')

const election = ref<IElection>(null);

onMounted(async () => {
  election.value = await $fetch(
    `${conf.public.DJANGO_API_BASE}/election/${route.params.id}`
  );
});
console.log(`vote/id#setup@election`, election, user);

const vote: IVote = {
  bureau_vote: user.value.electeur.bureau_vote,
  candidature: null,
  electeur: user.value.electeur.id
};
async function submitVote(candidatureId) {
  vote.candidature = candidatureId
  const res = await $fetch(`${conf.public.DJANGO_API_BASE}/vote/`, {
    method: "post",
    body: vote
  })

  console.log('vote/id#submiteVote@res', res)
}
</script>
<template>
  <span v-if="!election">Chargement ...</span>
  <div v-else>
    <!-- <p>{{ $route.params.id }}</p> -->
    <h1>{{ election.nom }}</h1>
    <span>Je vote pour: </span>
    <ul class="list-disc list-inside">
      <li v-for="candidature in election.candidats" :key="candidature.id">
        <a
          href="#"
          target="_self"
          rel="noopener noreferrer"
          @click="submitVote(candidature.id)"
          >{{ candidature.candidat.nom }} {{ candidature.candidat.prenom }} -
          {{ candidature.nom_parti }}</a
        >
      </li>
    </ul>
  </div>
</template>