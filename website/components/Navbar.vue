<template>
  <nav class="
      bg-transparent
      border-gray-200
      px-2
      sm:px-4
      py-2.5
      rounded
      dark:bg-gray-900
    ">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <a href="/" class="flex items-center">
        <span class="
            self-center
            text-xl
            font-semibold
            whitespace-nowrap
            dark:text-white
          ">Fale Sunu Ndjit</span>
      </a>
      <div class="flex items-center md:order-2">
        <User v-if="user" />
        <button data-collapse-toggle="mobile-menu-2" type="button" class="
            inline-flex
            items-center
            p-2
            ml-1
            text-sm text-gray-500
            rounded-lg
            md:hidden
            hover:bg-gray-100
            focus:outline-none focus:ring-2 focus:ring-gray-200
            dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600
          " aria-controls="mobile-menu-2" aria-expanded="false">
          <span class="sr-only">Open main menu</span>
          <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"></path>
          </svg>
        </button>
      </div>
      <div class="
          hidden
          justify-between
          items-center
          w-full
          md:flex md:w-auto md:order-1
        " id="mobile-menu-2">
        <ul class="
            flex flex-col
            p-4
            mt-4
            bg-gray-50
            rounded-lg
            border border-gray-100
            md:flex-row
            md:space-x-8
            md:mt-0
            md:text-sm
            md:font-medium
            md:border-0
            list-none
            md:bg-white
            dark:bg-gray-800
            md:dark:bg-gray-900
            dark:border-gray-700
          ">
          <li>
            <NuxtLink to="/" class="
                block
                py-2
                pr-4
                pl-3
                text-gray-700
                rounded
                hover:bg-gray-100
                md:hover:bg-transparent md:hover:text-blue-700 md:p-0
                dark:text-gray-400
                md:dark:hover:text-white
                dark:hover:bg-gray-700 dark:hover:text-white
                md:dark:hover:bg-transparent
                dark:border-gray-700

                hover:no-underline
              " aria-current="page" :class="$route.path == '/' ? 'bg-blue-700 md:text-blue-700 md:bg-inherit md:font-bold' : ''">Accueil</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/service" class="
                block py-2 pr-4 pl-3 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700

                hover:no-underline
              "  :class="$route.path == '/service' ? 'bg-blue-700 md:text-blue-700 md:bg-inherit md:font-bold' : ''">
              Services
            </NuxtLink>
          </li>
          <template v-if="!user">
            <li>
              <NuxtLink to="/connection" class="
                  block
                  py-2
                  pr-4
                  pl-3
                  text-gray-700
                  rounded
                  hover:bg-gray-100
                  md:hover:bg-transparent md:hover:text-blue-700 md:p-0
                  dark:text-gray-400
                  md:dark:hover:text-white
                  dark:hover:bg-gray-700 dark:hover:text-white
                  md:dark:hover:bg-transparent
                  dark:border-gray-700

                  hover:no-underline
                "  :class="$route.path == '/connection' ? 'bg-blue-700 md:text-blue-700 md:bg-inherit md:font-bold' : ''">Connection</NuxtLink>
            </li>
            <li>
              <NuxtLink to="/inscription" class="
                  block
                  py-2
                  pr-4
                  pl-3
                  text-gray-700
                  rounded
                  hover:bg-gray-100
                  md:hover:bg-transparent md:hover:text-blue-700 md:p-0
                  dark:text-gray-400
                  md:dark:hover:text-white
                  dark:hover:bg-gray-700 dark:hover:text-white
                  md:dark:hover:bg-transparent
                  dark:border-gray-700

                  hover:no-underline
                "  :class="$route.path == '/inscription' ? 'bg-blue-700 md:text-blue-700 md:bg-inherit md:font-bold' : ''">Inscription</NuxtLink>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import {
  SunIcon,
  HomeIcon,
  ListBulletIcon,
  FolderIcon,
} from "@heroicons/vue/24/outline";

const route = useRoute()

const current = ref('')
onUpdated(() => {
  console.log('*updated*', route)

})

const user = useState("user");
const setColorTheme = (newTheme) => {
  useColorMode().preference = newTheme;
};
</script>