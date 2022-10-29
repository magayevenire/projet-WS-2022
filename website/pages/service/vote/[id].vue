<script lang="ts" setup>
import { IElection } from "~/types/IElection";
import { IUser } from "~~/types/IUser";
import { IVote } from "~~/types/IVote";

const { $swal } = useNuxtApp();
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
  electeur: user.value.electeur?.id
};

const selectedCandidat = ref<number>(null)
function selectCandidat(candidatureId) {
  selectedCandidat.value = candidatureId
}

async function submitVote() {
  try {
    vote.candidature = selectedCandidat.value
    const res = await $fetch(`${conf.public.DJANGO_API_BASE}/vote/`, {
      method: "post",
      body: vote
    })

    console.log('vote/id#submiteVote@res', res)

    useRouter().push("/")
  } catch (error) {
    console.log(error.data);
    $swal.fire({
      toast: true,
      position: "top-end",
      timer: 15000,
      timerProgressBar: true,

      title: error.name,
      icon: 'error',
      showCloseButton: true,
      showConfirmButton: false,
    })
  }
}
</script>
<template>
  <span v-if="!election">Chargement ...</span>
  <div v-else>
    <h1>{{ election.nom }}</h1>
    <div v-if="user.electeur.elections.includes(+$route.params.id)" class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800" role="alert">
      <span class="font-medium">Vote impossible!</span> Vous avez déja voter pour cette élection.
    </div>
    <div class="flex flex-row flex-wrap gap-2 items-center justify-center">
      <Vote v-for="candidature in election.candidats" :key="candidature.id" :item="candidature"
        @selectCandidat="selectCandidat" :isSelected="selectedCandidat == candidature.id" />
    </div>
    <div class="flex flex-col justify-center items-center">
      <span class="text-2xl text-center">
        Je vote pour:
        <b v-if="selectedCandidat">{{ election.candidats.find(can => can.id == selectedCandidat)?.nom_parti }}</b>
        <b v-else class="text-red-300">selectioner un candidat</b>
      </span>
      <button class="button-primary w-fit px-10" :disabled="!selectedCandidat || user.electeur.elections.includes(+$route.params.id)" @click="submitVote">Voter</button>
    </div>
  </div>
</template>