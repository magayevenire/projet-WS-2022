export default defineEventHandler((event) => {
  console.log(`Nouvelle requête (${new Date()})`, event.req.url)
})