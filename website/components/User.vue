<script setup lang="ts">
import { ref } from "@vue/reactivity";
import { userLogout } from "~/composables/useAuth";
import { useState } from "#app";
import { onClickOutside } from '@vueuse/core'
import { ChevronDownIcon, UserIcon } from '@heroicons/vue/20/solid'
import { IUser } from "~~/types/IUser";


const avatar = (given: string | undefined) => given ?? '/img/logo_short.jpg' //
const user = useState<IUser>('user')
console.log('User#setup@user', user)
const logout = userLogout
const hideActions = ref(true)
const userActions = ref(null)
onClickOutside(userActions, () => hideActions.value = true)
</script>
  
<template>

  <div id="dropdownDefault" data-dropdown-toggle="dropdown"
    class="text-white w-fit flex flex-row items-center justify-center cursor-pointer bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-full p-1 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    type="button">
    <UserIcon class="w-8" />
    <span>{{ user.username }}</span>
    <ChevronDownIcon class="w-8" />
  </div>
  <!-- Dropdown menu -->
  <div id="dropdown" class="hidden z-10 w-44 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700"
    style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(0px, 410px);"
    data-popper-reference-hidden="" data-popper-escaped="" data-popper-placement="bottom">
    <ul class="py-1 text-sm text-gray-700 list-none dark:text-gray-200" aria-labelledby="dropdownDefault">
      <li>
        <NuxtLink :to="`/electeur/${user.electeur?.id}`"
          class="block py-2 px-4 hover:no-underline hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
          Vérifier mon inscription</NuxtLink>
      </li>
      <li>
        <a href="#" @click.prevent="logout"
          class="block py-2 px-4 hover:bg-gray-100 hover:no-underline dark:hover:bg-gray-600 dark:hover:text-white">Deconnexion</a>
      </li>
    </ul>
  </div>

</template>