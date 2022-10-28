import { ICirconscription } from './ICirconscription'
import { IRegion } from './IRegion';

export interface IDepartement extends ICirconscription {
  region: IRegion;
}
