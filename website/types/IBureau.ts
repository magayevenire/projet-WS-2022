import { ICirconscription } from './ICirconscription'
import { ICommune } from './ICommune'

export interface IBureau extends ICirconscription {
  commune: ICommune;
  numero: number;
  nombre_inscrits: number;
}
