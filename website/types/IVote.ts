export interface IVote {
  id?: number;
  creation?: string;
  modifier?: string;
  electeur: number;
  bureau_vote: number;
  candidature: number;
}
