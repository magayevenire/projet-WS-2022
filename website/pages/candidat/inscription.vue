<template>
  <div class="container w-1/2 mx-auto">
    <h1>Inscription Candidat</h1>
    <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
      <input type="hidden" name="remember" value="true" />
      <div class="rounded-md shadow-sm -space-y-px mb-1 flex flex-col gap-2">
        <div>
          <label for="partiName" class="sr-only">Nom de parti</label>
          <input
            v-model="candidature.nom_parti"
            id="partiName"
            name="partiName"
            required
            placeholder="Nom de parti"
          />
        </div>
        <div>
          <label for="elections" class="sr-only">election</label>
          <select name="elections" v-model="selectedElection" class="w-full">
            <option :value="null" disabled>Choisir une éléction</option>
            <option
              v-for="election in elections"
              :key="election.id"
              :value="election.id"
            >
              {{ election.nom }} - {{ election.jour_vote }}
            </option>
          </select>
        </div>
        <button class="button-primary" >S'inscrir</button>
      </div>
    </form>
  </div>
</template>
<script lang="ts" setup>
import { IUser } from "~/types/IUser";
import { IElecteur } from "~/types/IElecteur";
import { IElection } from "~/types/IElection";
import { ICandidature } from "~/types/ICandidature";
import { toast, snackbar } from 'tailwind-toast'

const conf = useRuntimeConfig();
const user = useState<IUser>("user");

let candidature = ref<ICandidature>({
  nom_parti: "",
  candidat: 0,
  election: null,
});
let elections = ref<IElection[]>(null);
let selectedElection = ref(null);

onMounted(async () => {
  const { data, error } = await useFetch<IElection[]>(
    `${conf.public.DJANGO_API_BASE}/election`,
    {
      method: "get",
    }
  );

  elections.value = data.value;
  console.log(elections, "list electiojns", error);
});

async function handleSubmit() {
  try {
    candidature.value.candidat = user.value?.electeur?.id;
    candidature.value.election = selectedElection.value;
    console.log(
      `candidat/inscription#handleSubmit@candidature`,
      candidature.value,
      user.value
    );
    const data = await $fetch(`${conf.public.DJANGO_API_BASE}/candidature/`, {
      method: "post",
      body: candidature.value,
    });
    toast()
    .default('Bien!', 'Votre candidature à bien été crée')
    .with({
      duration: 5000,
      positionX: 'end',
      positionY: 'top',
      color: 'bg-green-300 rounded-lg m-1 text-white',
    }).show()
    useRouter().push("/")
  } catch (error) {
    console.error("erreur durant l'ajout de candidature", error);
    toast()
    .default('Erreur!', JSON.stringify(error.data))
    .with({
      duration: 5000,
      positionX: 'end',
      positionY: 'top',
      color: 'bg-red-300 rounded-lg m-1 text-white',
    }).show()
  }
}
</script>