<script setup lang="ts">
import { ref } from "@vue/reactivity";
import { userLogout } from "~/composables/useAuth";
import { useState } from "#app";
import { onClickOutside } from '@vueuse/core'
import { ChevronDownIcon, UserIcon } from '@heroicons/vue/20/solid'


const avatar = (given: string | undefined) => given ?? '/img/logo_short.jpg' //
const user = useState('user')
const logout = userLogout
const hideActions = ref(true)
const userActions = ref(null)
onClickOutside(userActions, () => hideActions.value = true)
</script>
  
<template>

  <button id="dropdownDefault" data-dropdown-toggle="dropdown"
    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-lg p-1 text-center inline-flex items-center justify-between dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    type="button"
  >
    <span class="grid grid-cols-3 items-center">
      <UserIcon class="scale-50" />
      {{user.username}}
      <ChevronDownIcon class="scale-50" />
    </span>
  </button>
  <!-- Dropdown menu -->
  <div id="dropdown" class="hidden z-10 w-44 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700"
    style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate(0px, 410px);"
    data-popper-reference-hidden="" data-popper-escaped="" data-popper-placement="bottom">
    <ul class="py-1 text-sm text-gray-700 list-none dark:text-gray-200" aria-labelledby="dropdownDefault">
      <li>
        <NuxtLink to="/dashboard" class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Dashboard</NuxtLink>
      </li>
      <li>
        <a href="#" class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Settings</a>
      </li>
      <li>
        <a href="#" class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Earnings</a>
      </li>
      <li>
        <a href="#" @click.prevent="logout" class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Sign out</a>
      </li>
    </ul>
  </div>

</template>