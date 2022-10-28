<script lang="ts" setup>
import { IElection } from "~/types/IElection";
import { IUser } from "~~/types/IUser";
import { IVote } from "~~/types/IVote";
import { toast, snackbar } from 'tailwind-toast'

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

    toast()
    .default('Bien!', 'vote enregistrer')
    .with({
      duration: 5000,
      positionX: 'end',
      positionY: 'top',
      color: 'bg-green-300 rounded-lg m-1 text-white',
    }).show()
    useRouter().push("/")
  } catch (error) {
    console.error(error);
    toast()
    .default('Erreur', JSON.stringify(error.data))
    .with({
      duration: 5000,
      positionX: 'end',
      positionY: 'top',
      color: 'bg-red-300 rounded-lg m-1 text-white',
    }).show()
    
  }
}
</script>
<template>
  <span v-if="!election">Chargement ...</span>
  <div v-else>
    <!-- <p>{{ $route.params.id }}</p> -->
    <h1>{{ election.nom }}</h1>
    <div class="flex flex-row flex-wrap gap-2 items-center justify-center">
      <Vote v-for="candidature in election.candidats" :key="candidature.id" :item="candidature" @selectCandidat="selectCandidat" :isSelected="selectedCandidat == candidature.id" />
    </div>
    <div class="flex flex-col justify-center items-center">
      <span class="text-2xl text-center">
        Je vote pour:
        <b v-if="selectedCandidat">{{election.candidats.find(can => can.id == selectedCandidat)?.nom_parti}}</b>
        <b v-else class="text-red-300">selectioner un candidat</b>
      </span>
      <button class="button-primary w-fit px-10" :disabled="!selectedCandidat" @click="submitVote" >Voter</button>
    </div>
  </div>
</template>