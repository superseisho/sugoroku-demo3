<script lang="ts">
  import type { Socket } from "socket.io-client";
  import type { GameState, PlayerState } from "./util";
  

  export let socket: Socket

  let gameState: GameState;
  let playerState: PlayerState;

  socket.on("update", (data: GameState)=>{
    gameState = data;
    console.log(data);
  })

  socket.on("update_player_state", (data: PlayerState)=>{
    playerState = data;
    console.log(data);
  })

  function dice(){
    socket.emit("dice");
  }
</script>


{#if gameState != undefined && playerState != undefined}
<div>
  <h3>現在のプレイヤー：{gameState.currentPlayer} ({gameState.players[gameState.currentPlayer].name})</h3>
  <button id="diceButton" disabled={!playerState.playable} on:click={dice}>サイコロ</button>
  {#each gameState.players as player}
    <div class="player" style="left: {player.position * 2}rem; background-color: {player.position % 3 == 1 ? "rgba(255, 0, 0, 0.3)" : "rgba(255, 255, 255, 0.3)"}">{player.name}<br>{player.position}</div>
  {/each}
</div>
{/if}

<style>
  div.player{
    position: absolute;
    left: 0;
    top: 0;
    width: 2rem;
    height: 2rem;
    transition: all 0.2s;
  }
</style>