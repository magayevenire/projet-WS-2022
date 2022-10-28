import { ICirconscription } from './ICirconscription'
import { IDepartement } from './IDepartement'

export interface ICommune extends ICirconscription {
  departement: IDepartement;
}
