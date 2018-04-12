<template>
  <div class="grid-container">
    <div class="map">
      <div v-for="(itemOuter, indexOuter) in myMap" v-bind:key="indexOuter" class="map_row">
        <div v-for="(itemInner, indexInner) in itemOuter" v-bind:key="indexInner" class="map_cell">
          {{itemInner}}
        </div>
      </div>
    </div>
    <div class="login">
      IP : <input type="text" v-model="form.ip">
      Port : <input type="text" v-model="form.port">
      Pseudo : <input type="text" v-model="form.pseudo">
      <button type="button">Connect</button>
      <textarea name="name" readonly="true" v-model="form.error"></textarea>
    </div>
    <div class="move">
      <div class="move_row">
        <div class="empty"></div>
        <button type="button" class="up">⬆</button>
        <div class="empty"></div>
      </div>
      <div class="move_row">
        <button type="button" class="left">⬅</button>
        <button type="button" class="right">➡</button>
      </div>
      <div class="move_row">
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
      },
      myMap: []
    }
  },
  methods: {
    r_loop () {
      console.log('heheh')
      let tempMap = []
      // -5 / +5
      for (let i = 0; i < 11; i++) {
        let tempArray = []
        for (let j = 0; j < 11; j++) {
          tempArray.push(i + ':' + j)
        }
        tempMap.push(tempArray)
      }
      this.myMap = tempMap
      console.log(this.myMap)
    }
  },
  mounted () {
    this.r_loop()
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
  flex-direction: column;
  overflow: auto;
}
  .map > .map_row {
    flex: 1;
    display: flex;
    flex-direction: row;
  }
    .map > .map_row > .map_cell {
      flex: 1;
      margin: 5px;
      background-color: crimson;
      min-width: 75px;
      min-height: 75px;
    }
.login {
  grid-area: login;
  background-color: green;
  display: flex;
  flex-direction: column;
  padding: 10px;
  min-width: 200px;
}
  .login > input {
    flex: 1;
    max-height: 1.5rem;
    margin: 10px 0;
    background-color: ghostwhite;
  }
  .login > button {
    font-size: 1.5rem;
    background-color: darkgrey;
    cursor: pointer;
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
  min-width: 200px;
}
  .move > .move_row {
    flex: 1;
    display: flex;
    flex-direction: row;
  }
    .move > .move_row > * {
      flex: 1;
      border: none;
      margin: 5px;
    }
    .move > .move_row > .empty {
      background-color: purple;
    }
    .move > .move_row > button {
      background-color: darkgrey;
      cursor: pointer;
      font-size: 1.5rem;
      line-height: 0;
    }
@media (max-width: 600px) {
  .grid-container {
    grid-template-areas:
      'map map'
      'map map'
      'login move';
  }
  .login {
    padding: 2px;
  }
  .login > input {
    margin: 2px 0;
  }
  .login > textarea {
    margin-top: 2px;
  }
  .move > .move_row > * {
    margin: 2px;
  }
}
@media (max-height: 500px) {
  .login {
    padding: 2px;
  }
  .login > input {
    margin: 2px 0;
  }
  .login > textarea {
    margin-top: 2px;
  }
  .move > .move_row > * {
    margin: 2px;
  }
}
</style>
