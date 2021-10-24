/* eslint-disable @typescript-eslint/prefer-namespace-keyword */
// eslint-disable-next-line @typescript-eslint/no-namespace
export module ServerResponse
{
    export interface RaceData
    {
        black: number,
        white: number,
        asian: number,
        hispanic: number,
    }

    export interface Gender
    {
        female: number,
        male: number,
        nonbinary: number
    }

    export interface DemographicData {
        race: RaceData,
        gender: Gender
    }
}