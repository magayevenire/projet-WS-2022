export interface IElection {
  id: number
  nom: string
  periode_inscription_debut?: string
  periode_inscription_fin?: string
  periode_depot_canditature_debut?: string
  periode_depot_canditature_fin?: string
  jour_vote?: string
  creation?: string
  modifier?: string

  candidats? : any[]
}