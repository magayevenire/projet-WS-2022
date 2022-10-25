<template>
  <div class="container w-1/2 mx-auto">
    <h1>Inscription Candidat</h1>
    <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
      <input type="hidden" name="remember" value="true" />
      <div class="rounded-md shadow-sm -space-y-px mb-1 flex flex-col gap-2">
        <!-- <div>
          <label for="identification" class="sr-only">Identification</label>
          <input
            v-model="candidat.identification"
            id="identification"
            name="identification"
            required
            placeholder="Identification"
          />
        </div> -->
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
          <select name="elections" v-model="selectedElection">
            <option
              v-for="election in elections"
              :key="election.id"
              :value="election.id"
            >
              {{ election.nom }} - {{ election.jour_vote }}
            </option>
          </select>
        </div>
        <button>S'inscrir</button>
      </div>
    </form>
  </div>
</template>
<script lang="ts" setup>
import { IUser } from "~/types/IUser";
import { IElecteur } from "~/types/IElecteur";
import { IElection } from "~/types/IElection";
import { ICandidature } from "~/types/ICandidature";

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
  candidature.value.candidat = user.value.id;
  candidature.value.election = selectedElection.value;
  console.log(
    `candidat/inscription#handleSubmit@candidature`,
    candidature.value,
    user.value
  );
  const data = await useFetch(`${conf.public.DJANGO_API_BASE}/candidature/`, {
    method: "post",
    body: candidature.value,
  });
}
</script>