<template>
  <div class="container w-1/2 mx-auto">
    <h1>Inscription Electeur</h1>
    <form @submit.prevent="handleSubmit" class="mt-8 space-y-6">
      <input type="hidden" name="remember" value="true" />
      <div class="rounded-md shadow-sm -space-y-px mb-1 flex flex-col gap-2">
        <div>
          <label for="cni" class="sr-only">Numéro de carte d'identité nationale</label>
          <input
            v-model="electeur.numero_cni"
            id="cni"
            name="cni"
            required
            placeholder="Numéro de carte d'identité nationale"
          />
        </div>
        <div>
          <label for="lastname" class="sr-only">Nom</label>
          <input
            v-model="electeur.nom"
            id="lastname"
            name="lastname"
            required
            placeholder="Nom"
          />
        </div>
        <div>
          <label for="firstname" class="sr-only">Prénom</label>
          <input
            v-model="electeur.prenom"
            id="firstname"
            name="firstname"
            required
            placeholder="Prénom"
          />
        </div>
        <div>
          <label for="birthdate" class="sr-only">Date de naissance</label>
          <input
            type="date"
            v-model="electeur.date_naissance"
            id="birthdate"
            name="birthdate"
            required
            placeholder="Date de naissance"
          />
        </div>
        <div>
          <label for="address" class="sr-only">adresse de domicile</label>
          <input
            v-model="electeur.adresse"
            id="address"
            name="address"
            required
            placeholder="adresse de domicile"
          />
        </div>
        <div>
          <label for="region" class="sr-only">Région</label>
          <select
            class="w-full"
            v-model="selectedRegion"
            id="region"
            name="region"
            required
            @change="handleRegionChange"
          >
            <option value="null" disabled>Région</option>
            <option v-for="bureau in regions" :value="bureau.id" :key="bureau.id">{{bureau.nom}}</option>
          </select>
        </div>
        <div v-if="departements && departements.length > 0">
          <label for="department" class="sr-only">Département</label>
          <select
            class="w-full"
            v-model="selectedDepartement"
            id="department"
            name="department"
            required
            @change="handleDepartementChange"
          >
            <option value="null" disabled>Département</option>
            <option v-for="departement in departements" :value="departement.id" :key="departement.id">{{departement.nom}}</option>
          </select>
        </div>
        <div v-if="communes && communes.length > 0">
          <label for="communes" class="sr-only">Commune</label>
          <select
            class="w-full"
            v-model="selectedCommune"
            id="communes"
            name="communes"
            required
            @change="handleCommuneChange"
          >
            <option value="null" disabled>Commune</option>
            <option v-for="commune in communes" :value="commune.id" :key="commune.id">{{commune.nom}}</option>
          </select>
        </div>
        <div v-if="bureaux && bureaux.length > 0">
          <label for="bureaux" class="sr-only">Bureau</label>
          <select
            class="w-full"
            v-model="selectedBureau"
            id="bureaux"
            name="bureaux"
            required
            @change="handleBureauChange"
          >
            <option value="null" disabled>Bureau</option>
            <option v-for="bureau in bureaux" :value="bureau.id" :key="bureau.id">{{bureau.numero}}</option>
          </select>
        </div>
      </div>
      <div>
        <button class="button-primary">
          S'inscrir
        </button>
      </div>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { IUser } from '~/types/IUser'
import { IElecteur } from '~/types/IElecteur'

const conf = useRuntimeConfig()

const regions = ref([])
const departements = ref([])
const communes = ref([])
const bureaux = ref([])
const { data } = await useAsyncData('region', ()=> $fetch<[]>(`${conf.public.DJANGO_API_BASE}/region/`))
regions.value = data.value
const user = useState<IUser>('user')


const selectedRegion = ref(null)
async function handleRegionChange(){
  departements.value = []
  communes.value = []
  bureaux.value = []
  fetchDepartement()
}
async function fetchDepartement(){
  console.log('---', selectedRegion.value)
  if (selectedRegion.value != null) {
    const data = await $fetch<[]>(`${conf.public.DJANGO_API_BASE}/departement/?region=${selectedRegion.value}`)
    departements.value = data
  }
}
const selectedDepartement = ref(null)
async function handleDepartementChange(){
  communes.value = []
  bureaux.value = []
  fetchCommune()
}
async function fetchCommune(){
  if (selectedDepartement.value != null) {
    const data = await $fetch<[]>(`${conf.public.DJANGO_API_BASE}/commune/?departement=${selectedDepartement.value}`)
    communes.value = data
  }
}
const selectedCommune = ref(null)
async function handleCommuneChange(){
  bureaux.value = []
  fetchBureau()
}
async function fetchBureau(){
  if (selectedCommune.value != null) {
    const data = await $fetch<[]>(`${conf.public.DJANGO_API_BASE}/bureau/?commune=${selectedCommune.value}`)
    bureaux.value = data
  }
}
const selectedBureau = ref(null)
async function handleBureauChange(){
  electeur.value.bureau_vote = selectedBureau
}
const electeur = ref<IElecteur>({ user: user.value.id });

async function handleSubmit() {
  try {
    console.log(`electeur/inscription#handleSubmit@electeur`, electeur.value, user.value);
    const data = await $fetch<IElecteur>(`${conf.public.DJANGO_API_BASE}/electeur/`, {
      method: "post",
      body: Object.assign(electeur.value, { user: user.value.id })
    })
    console.log(`electeur/inscription#handleSubmit@data`, data);
    useRouter().push('/')
  } catch (error) {
    console.error(error);
  }
}
</script>