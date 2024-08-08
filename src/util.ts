type Player = {
  name: string,
  position: number,
  sid: string
}

export type GameState = {
  "players": Player[],
  "turn": number
  "currentPlayer": number,
  "gameover": boolean,
}

export type PlayerState = {
  "name": string,
  "playable": boolean,
}