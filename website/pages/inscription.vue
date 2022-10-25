<script setup lang="ts">
import { ref } from "@vue/reactivity";
import { registerWithUsername } from "~/composables/useAuth";

const password = ref(null);
const username = ref(null);

async function postRegisterForm() {
  try {
    await registerWithUsername(username.value, password.value);
  } catch (error) {
    console.error(error);
  }
}
</script>
  
  <template>
  <div class="dark:bg-slate-800 h-screen">
    <div class="flex items-center justify-center px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full">
        <div>
          <h2
            class="
              text-center text-3xl
              font-extrabold
              mt-5
              text-gray-900
              dark:text-white
            "
          >
            Inscription
          </h2>
        </div>
        <form
          v-on:submit.prevent
          class="mt-8 space-y-6"
          action="#"
          method="POST"
        >
          <input type="hidden" name="remember" value="true" />
          <div class="rounded-md shadow-sm -space-y-px mb-1">
            <div>
              <label for="email-address" class="sr-only">Username</label>
              <input
                type="email"
                v-model="username"
                id="username"
                name="username"
                required
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
                "
                placeholder="username"
              />
            </div>
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              v-model="password"
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
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
                rounded-b-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Password"
            />
          </div>
        </form>
        <button
          @click.prevent="postRegisterForm"
          class="
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
          "
        >
          S'inscrir
        </button>
      </div>
    </div>
  </div>
</template>