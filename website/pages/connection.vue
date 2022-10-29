<script setup lang="ts">
import { ref } from "@vue/reactivity";
import { loginWithUsername } from "~/composables/useAuth";

const { $swal } = useNuxtApp()
const conf = useRuntimeConfig()
const testResult = ref(null);

const username = ref(null);
const password = ref(null);
async function postLoginForm() {
  try {
    await loginWithUsername(username.value, password.value);
  } catch (error) {
    console.error(error);
  }
}
async function runTest() {
  console.log($swal)
  $swal
    .mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger',
        closeButton: "ring-0 border-0",
        popup: "bg-red-500"
      },
      buttonsStyling: false
    })
    .fire({
      toast: true,
      title: 'Error!',
      // text: 'Do you want to continue',
      // icon: 'error',
      timerProgressBar: true,
      // timer: 5000,
      position: "top-end",
      showCloseButton: true,
      background: '#fff url(/images/trees.png)'
    })
}
</script>
  
<template>
  <div class="dark:bg-slate-800 h-screen">
    <button class="button-primary w-fit" @click="runTest">test</button>
    <pre>{{ testResult }}</pre>
    <div class="flex items-center justify-center px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full">
        <div>
          <h2 class="
              text-center text-3xl
              font-extrabold
              mt-5
              text-gray-900
              dark:text-white
            ">
            Connection
          </h2>
        </div>
        <form v-on:submit.prevent class="mt-8 space-y-6" action="#" method="POST">
          <input type="hidden" name="remember" value="true" />

          <div class="rounded-md shadow-sm -space-y-px mb-1">
            <div>
              <label for="username" class="sr-only">Nom d'Utilisateur</label>
              <input v-model="username" id="username" name="username" type="username" autocomplete="username" required
                class="
                  dark:bg-slate-500 dark:text-white dark:placeholder-white
                  appearance-none
                  rounded-none
                  relative
                  block
                  w-full
                  px-3
                  py-2
                  border border-gray-300
                  placeholder-gray-500
                  text-gray-900
                  rounded-t-md
                  focus:outline-none
                  focus:ring-indigo-500
                  focus:border-indigo-500
                  focus:z-10
                  sm:text-sm
                " placeholder="Nom d'Utilisateur" />
            </div>
          </div>
          <div>
            <label for="password" class="sr-only">Mot de passe</label>
            <input v-model="password" id="password" name="password" type="password" autocomplete="current-password"
              required class="
                dark:bg-slate-500 dark:text-white dark:placeholder-white
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-b-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              " placeholder="Mot de passe" />
          </div>

          <div class="flex items-center justify-between">
            <div class="text-sm">
              <a href="#" class="font-medium text-indigo-600 hover:text-indigo-500">
                Forgot your password?
              </a>
            </div>
          </div>

          <div></div>
        </form>
        <button @click.prevent="postLoginForm" class="
            mt-5
            group
            relative
            w-full
            flex
            justify-center
            py-2
            px-4
            border border-transparent
            text-sm
            font-medium
            rounded-md
            text-white
            bg-indigo-600
            hover:bg-indigo-700
            focus:outline-none
            focus:ring-2
            focus:ring-offset-2
            focus:ring-indigo-500
          ">
          <span class="absolute left-0 inset-y-0 flex items-center pl-3">
            <!-- Heroicon name: solid/lock-closed -->
            <svg class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
              <path fill-rule="evenodd"
                d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                clip-rule="evenodd" />
            </svg>
          </span>
          Login
        </button>
      </div>
    </div>
  </div>
</template>