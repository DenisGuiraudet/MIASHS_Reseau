<template>
  <div class="grid-container">
    <div class="map">
      Map
    </div>
    <div class="login">
      IP : <input type="text" v-model="form.ip">
      Port : <input type="text" v-model="form.port">
      Pseudo : <input type="text" v-model="form.pseudo">
      <button type="button">Connect</button>
      <textarea name="name" readonly="true" v-model="form.error"></textarea>
    </div>
    <div class="move">
      <div class="row">
        <div class="empty"></div>
        <button type="button" class="up">⬆</button>
        <div class="empty"></div>
      </div>
      <div class="row">
        <button type="button" class="left">⬅</button>
        <button type="button" class="right">➡</button>
      </div>
      <div class="row">
        <div class="empty"></div>
        <button type="button" class="down">⬇</button>
        <div class="empty"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Map',
  data () {
    return {
      form: {
        ip: '',
        port: '',
        pseudo: '',
        error: 'Errors : '
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.grid-container {
  display: grid;
  grid-template-areas:
    'map map map login'
    'map map map move'
    'map map map move';
  grid-gap: 10px;
  background-color: black;
  min-width: inherit;
  width: inherit;
  max-width: inherit;
  min-height: inherit;
  height: inherit;
  max-height: inherit;
}
.map {
  grid-area: map;
  background-color: blue;
  display: flex;
}
.login {
  grid-area: login;
  background-color: green;
  display: flex;
  flex-direction: column;
  padding: 10px;
}
  .login > input {
    flex: 1;
    max-height: 1.5rem;
    margin: 10px 0;
    background-color: ghostwhite;
  }
  .login > button {
    font-size: 1.5rem;
    cursor: pointer;
    background-color: darkgrey;
  }
  .login > textarea {
    flex: 1;
    margin-top: 10px;
  }
.move {
  grid-area: move;
  background-color: red;
  display: flex;
  flex-direction: column;
}
  .move > .row {
    flex: 1;
    display: flex;
    flex-direction: row;
  }
    .move > .row > * {
      flex: 1;
      border: none;
      margin: 5px;
    }
    .move > .row > .empty {
      background-color: purple;
    }
    .move > .row > button {
      background-color: darkgrey;
      font-size: 3rem;
      line-height: 0;
    }
</style>
