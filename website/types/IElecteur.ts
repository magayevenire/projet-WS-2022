export interface IElecteur {
  id?: number;
  adresse?: string;
  bureau_vote?: number;
  candidatures?: [];
  date_naissance?: string;
  nom?: string;
  numero_cni?: string;
  prenom?: string;
  user: number;
  votes?: [];
}