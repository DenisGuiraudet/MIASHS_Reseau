<template>
  <div class="grid-container">
    <div class="map img_cover">
      <div v-for="(itemOuter, indexOuter) in myMap" v-bind:key="indexOuter" class="map_row">
        <div v-for="(itemInner, indexInner) in itemOuter" v-bind:key="indexInner" class="map_column">
          <div v-if="indexOuter === 5 && indexInner === 5" class="map_cell map_cell_player img_contain"></div>
          <div v-else-if="itemInner !== ''" class="map_cell map_cell_other img_contain"></div>
          <div v-else class="map_cell"></div>
        </div>
      </div>
    </div>
    <div class="login">
      IP : <input type="text" v-model="form.ip">
      Port : <input type="text" v-model="form.port">
      Pseudo : <input type="text" v-model="form.pseudo">
      <button v-on:click="r_connect" type="button">Connect</button>
      <div class="textarea img_cover">
        <textarea name="name" readonly="true" v-model="form.error"></textarea>
      </div>
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
        done: false,
        ip: '',
        port: '',
        pseudo: '',
        error: 'Errors : '
      },
      myMap: [],
      username: 'Michel',
      center_x: 0,
      center_y: 0,
      request: {
        '127.0.0.1': ['Jacquie', 'play', {'x': 7, 'y': 5, 'res': 1}],
        '127.0.0.2': ['Michel', 'play', {'x': 4, 'y': 5, 'res': 5}],
        '127.0.0.3': ['Billy', 'play', {'x': 6, 'y': 3, 'res': 3}],
        '127.0.0.4': ['Oui', 'play', {'x': 16, 'y': 3, 'res': 3}]
      }
    }
  },
  methods: {
    r_loop () {
      let tempMap = []
      // -5 / +5
      for (let i = 0; i < 11; i++) {
        let tempArray = []
        for (let j = 0; j < 11; j++) {
          tempArray.push('')
        }
        tempMap.push(tempArray)
      }
      tempMap[5][5] = 'MDR'
      for (let elem in this.request) { // FIND YOUR ROBOT
        if (this.request[elem][0] === this.username) {
          this.center_x = this.request[elem][2].x
          this.center_y = this.request[elem][2].y
          break
        }
      }
      for (let elem in this.request) { // FIND OTHER ROBOT THAT ARE NEAR
        if (this.request[elem][2].x >= (this.center_x - 5) && this.request[elem][2].x <= (this.center_x + 5)) {
          if (this.request[elem][2].y >= (this.center_y - 5) && this.request[elem][2].y <= (this.center_y + 5)) {
            if (this.request[elem][0] !== this.username) {
              console.log(this.request[elem])
              tempMap[this.request[elem][2].x - this.center_x + 5][this.request[elem][2].y - this.center_y + 5] = this.request[elem]
            }
          }
        }
      }
      this.myMap = tempMap
      console.log(this.myMap)
    },
    r_connect () {
      console.log('r_connect')
    },
    r_up () {
      console.log('r_connect')
    },
    r_left () {
      console.log('r_connect')
    },
    r_right () {
      console.log('r_connect')
    },
    r_down () {
      console.log('r_connect')
    }
  },
  mounted () {
    this.r_loop()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img_cover {
  background: no-repeat center center;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
.img_contain {
  background: no-repeat center center;
  -webkit-background-size: contain;
  -moz-background-size: contain;
  -o-background-size: contain;
  background-size: contain;
}
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
  display: flex;
  flex-direction: column;
  overflow: auto;
  background-image: url(../assets/flatEarth.jpg);
  border: solid 1px black;
}
  .map > .map_row {
    flex: 1;
    display: flex;
    flex-direction: row;
  }
    .map > .map_row > .map_column {
      flex: 1;
      display: flex;
    }
      .map > .map_row > .map_column > .map_cell {
        flex: 1;
        min-width: 75px;
        min-height: 75px;
        border: solid 1px black;
      }
      .map > .map_row > .map_column > .map_cell_player {
        background-image: url(../assets/hero.png)
      }
      .map > .map_row > .map_column > .map_cell_other {
        background-image: url(../assets/ufo.png)
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
  .login > .textarea {
    background-image: url(../assets/musk.jpg);
    flex: 1;
    display: flex;
    margin-top: 10px;
  }
  .login > .textarea > textarea {
    resize: none;
    flex: 1;
    background: none;
    border: none;
    margin: 5px;
    color: ghostwhite;
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
  .login > .textarea > textarea {
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
