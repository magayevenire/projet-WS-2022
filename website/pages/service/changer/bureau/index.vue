<script lang="ts" setup>
import { IElecteur } from '~~/types/IElecteur';
import { IUser } from '~~/types/IUser';
import { IBureau } from '~~/types/IBureau';
import { toast, snackbar } from 'tailwind-toast'


const conf = useRuntimeConfig()

const regions = ref([])
const departements = ref([])
const communes = ref([])
const bureaux = ref([])
const { data } = await useAsyncData('region', () => $fetch<[]>(`${conf.public.DJANGO_API_BASE}/region/`))
regions.value = data.value
const user = useState<IUser>('user')
const { data: currentBureau } = await useAsyncData('bureau', () => $fetch<IBureau>(`${conf.public.DJANGO_API_BASE}/bureau/${user.value.electeur?.bureau_vote}`))


const selectedRegion = ref(null)
async function handleRegionChange() {
  departements.value = []
  communes.value = []
  bureaux.value = []
  fetchDepartement()
}
async function fetchDepartement() {
  console.log('---', selectedRegion.value)
  if (selectedRegion.value != null) {
    const data = await $fetch<[]>(`${conf.public.DJANGO_API_BASE}/departement/?region=${selectedRegion.value}`)
    departements.value = data
  }
}
const selectedDepartement = ref(null)
async function handleDepartementChange() {
  communes.value = []
  bureaux.value = []
  fetchCommune()
}
async function fetchCommune() {
  if (selectedDepartement.value != null) {
    const data = await $fetch<[]>(`${conf.public.DJANGO_API_BASE}/commune/?departement=${selectedDepartement.value}`)
    communes.value = data
  }
}
const selectedCommune = ref(null)
async function handleCommuneChange() {
  bureaux.value = []
  fetchBureau()
}
async function fetchBureau() {
  if (selectedCommune.value != null) {
    const data = await $fetch<[]>(`${conf.public.DJANGO_API_BASE}/bureau/?commune=${selectedCommune.value}`)
    bureaux.value = data
  }
}
const selectedBureau = ref(null)
async function handleBureauChange() {
  electeur.value.bureau_vote = selectedBureau
}
const electeur = ref<IElecteur>({ user: user.value.id });
const router = useRouter()
async function handleSubmit() {
  console.log(`electeur/inscription#handleSubmit@electeur`, electeur.value, user.value);
  const { data, error } = await useFetch<IElecteur>(`${conf.public.DJANGO_API_BASE}/electeur/${user.value.electeur.id}/`, {
    method: "patch",
    body: electeur.value
  })
  if (error.value) {
    console.error(error.value)
    return 0
  }
  toast()
    .default('Bien!', 'Votre bureau à été mit à jour')
    .with({
      duration: 5000,
      positionX: 'end',
      positionY: 'top',
      color: 'bg-green-300 rounded-lg m-1 text-white',
    }).show()
  router.push("/")
}

onMounted(() => { })
</script>
<template>
  <div>
    <h1>Changement de bureau de vote</h1>


    <template v-if="user?.electeur?.id">
      <div>
        <span>Bureau de vote actuel: </span>
        <b v-if="currentBureau">
          {{ currentBureau.commune.departement.region.nom }}, {{ currentBureau.commune.departement.nom }} -
          {{ currentBureau.commune.nom }}: bureau n°{{ currentBureau.numero }}
        </b>
        <span v-else class="text-red-500">Bureau inconnue</span>
      </div>
      <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px mb-1 flex flex-col gap-2">
          <div>
            <label for="region" class="sr-only">Région</label>
            <select v-model="selectedRegion" id="region" name="region" required @change="handleRegionChange">
              <option value="null" disabled>Région</option>
              <option v-for="bureau in regions" :value="bureau.id" :key="bureau.id">{{ bureau.nom }}</option>
            </select>
          </div>
          <div v-if="departements && departements.length > 0">
            <label for="department" class="sr-only">Département</label>
            <select v-model="selectedDepartement" id="department" name="department" required
              @change="handleDepartementChange">
              <option value="null" disabled>Département</option>
              <option v-for="departement in departements" :value="departement.id" :key="departement.id">
                {{ departement.nom }}</option>
            </select>
          </div>
          <div v-if="communes && communes.length > 0">
            <label for="communes" class="sr-only">Commune</label>
            <select v-model="selectedCommune" id="communes" name="communes" required @change="handleCommuneChange">
              <option value="null" disabled>Commune</option>
              <option v-for="commune in communes" :value="commune.id" :key="commune.id">{{ commune.nom }}</option>
            </select>
          </div>
          <div v-if="bureaux && bureaux.length > 0">
            <label for="bureaux" class="sr-only">Bureau</label>
            <select v-model="selectedBureau" id="bureaux" name="bureaux" required @change="handleBureauChange">
              <option value="null" disabled>Bureau</option>
              <option v-for="bureau in bureaux" :value="bureau.id" :key="bureau.id">{{ bureau.numero }}</option>
            </select>
          </div>
          <button class="button-primary w-fit">Changer de bureau</button>
        </div>
      </form>
    </template>

    <div v-else class="bg-red-500 p-2 rounded-lg shadow-lg">
      <span class="text-white">Vous n'êtes pas inscrit sur la liste éléctorale allez <NuxtLink to="/electeur/inscription">ICI</NuxtLink> pour vous inscrir</span>
    </div>
  </div>
</template>