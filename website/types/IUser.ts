import { IElecteur } from '~/types/IElecteur'

export interface IUser {
  id?: number;
  username: string;
  password?: string;
  email?: string;
  electeur?: IElecteur
}
