// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  app: {
    head: {
      script: [{ src: "https://unpkg.com/flowbite@latest/dist/flowbite.js" }],
    },
  },
  modules: ["@nuxtjs/tailwindcss", "@nuxtjs/color-mode", "@nuxt/content"],
  content: {
    // https://content.nuxtjs.org/api/configuration
  },
  tailwindcss: {
    cssPath: "~/assets/css/tailwind.css",
    configPath: "tailwind.config.js",
    exposeConfig: false,
    // config: {},
    injectPosition: 0,
    viewer: true,
  },
  colorMode: {
    classSuffix: "",
  },
  runtimeConfig: {
    // The private keys which are only available within server-side
    apiSecret: "123",
    // Keys within public, will be also exposed to the client-side
    public: {
      apiBase: "/api",
      DJANGO_API_BASE: "http://localhost:8000/api",
    },
  },
  plugins: [
    "~/plugins/sweetalert2.ts"
  ]
});
