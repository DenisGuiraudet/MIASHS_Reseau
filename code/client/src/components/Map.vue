<template>
  <div class="grid-container">
    <div class="map img_cover">
      <div v-for="(itemOuter, indexOuter) in this.myMap" v-bind:key="indexOuter" class="map_row">
        <div v-for="(itemInner, indexInner) in itemOuter" v-bind:key="itemInner[0] + indexInner" class="map_column">
          <div v-if="indexOuter === 5 && indexInner === 5" class="map_cell map_cell_player img_contain"></div>
          <div v-else-if="itemInner instanceof Object" class="map_cell map_cell_other img_contain"></div>
          <div v-else class="map_cell"></div>
        </div>
      </div>
    </div>
    <div class="login">
      <div v-if="isConnected !== true" class="login_box">
        Host : <input type="text" v-model="form.host">
        Port : <input type="number" v-model="form.port">
        Pseudo : <input type="text" v-model="form.pseudo">
        <button v-on:click="r_connect" type="button">Connect</button>
      </div>
      <div v-else-if="isInit !== true" class="login_box">
        X : <input type="number" v-model="form.x">
        Y : <input type="number" v-model="form.y">
        <button v-on:click="r_init" type="button">Init robot</button>
      </div>
      <div class="textarea img_cover">
        <textarea name="name" readonly="true" v-model="form.error"></textarea>
      </div>
    </div>
    <div class="move">
      <div class="move_row">
        <div class="empty"></div>
        <button v-on:click="r_up" type="button" class="up">⬆</button>
        <div class="empty"></div>
      </div>
      <div class="move_row">
        <button v-on:click="r_left" type="button" class="left">⬅</button>
        <button v-on:click="r_right" type="button" class="right">➡</button>
      </div>
      <div class="move_row">
        <div class="empty"></div>
        <button v-on:click="r_down" type="button" class="down">⬇</button>
        <div class="empty"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Map',
  data () {
    return {
      isConnected: false,
      isInit: false,
      form: {
        host: 'http://localhost',
        port: 8070,
        pseudo: 'JoeLeTaxi',
        x: 0,
        y: 0,
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
      console.log('r_loop')
      let tempMap = []
      for (let i = 0; i < 11; i++) {
        let tempArray = []
        for (let j = 0; j < 11; j++) {
          tempArray.push('X')
        }
        tempMap.push(tempArray)
      }
      let that = this
      axios.get(this.form.host + ':' + this.form.port + '/', {
        params: {
          QUERY: ('GETMAP')
        }})
        .then(function (response1) {
          that.request = JSON.parse(response1.data.replace(/'/g, '"'))
          axios.get(that.form.host + ':' + that.form.port + '/', {
            params: {
              QUERY: ('GETMYPOS ' + that.form.pseudo)
            }})
            .then(function (response2) {
              let center = JSON.parse(response2.data.replace(/'/g, '"'))
              that.center_x = parseInt(center[0][0])
              that.center_y = parseInt(center[0][1])
              for (let elem in that.request) { // FIND OTHER ROBOT THAT ARE NEAR
                if (parseInt(that.request[elem][1]) >= (that.center_x - 5) && parseInt(that.request[elem][1]) <= (that.center_x + 5)) {
                  if (parseInt(that.request[elem][2]) >= (that.center_y - 5) && parseInt(that.request[elem][2]) <= (that.center_y + 5)) {
                    tempMap[parseInt(that.request[elem][1]) - that.center_x + 5][parseInt(that.request[elem][2]) - that.center_y + 5] = that.request[elem]
                  }
                }
              }
              that.myMap = tempMap
            })
            .catch(function (error) {
              console.log(error)
            })
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    forceLoop () {
      if (this.isConnected === true) {
        if (this.loopR !== null) {
          clearInterval(this.loopR)
          this.loopR = null
        }
        this.r_loop()
        let that = this
        this.loopR = setInterval(function () {
          that.r_loop()
        }, 500)
      }
    },
    r_connect () {
      console.log('r_connect')
      let that = this
      axios.get(this.form.host + ':' + this.form.port + '/', {
        params: {
          QUERY: ('CONNECT ' + this.form.pseudo)
        }})
        .then(function (response1) {
          that.isConnected = true
          axios.get(that.form.host + ':' + that.form.port + '/', {
            params: {
              QUERY: ('ISINIT')
            }})
            .then(function (response2) {
              if (response2.data === 'True') {
                that.isInit = true
                that.forceLoop()
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    r_init () {
      console.log('r_init')
      let that = this
      axios.get(this.form.host + ':' + this.form.port + '/', {
        params: {
          QUERY: ('INIT ' + this.form.x + ' ' + this.form.y)
        }})
        .then(function (response) {
          that.isInit = true
          that.forceLoop()
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    r_up () {
      console.log('r_up')
      this.move(-1, 0)
    },
    r_down () {
      console.log('r_down')
      this.move(1, 0)
    },
    r_left () {
      console.log('r_left')
      this.move(0, -1)
    },
    r_right () {
      console.log('r_right')
      this.move(0, 1)
    },
    move (shiftX, shiftY) {
      if (this.isConnected && this.isInit) {
        let that = this
        axios.get(this.form.host + ':' + this.form.port + '/', {
          params: {
            QUERY: ('GETMYPOS')
          }})
          .then(function (response1) {
            let center = JSON.parse(response1.data.replace(/'/g, '"'))
            that.center_x = parseInt(center[0][0])
            that.center_y = parseInt(center[0][1])
            axios.get(that.form.host + ':' + that.form.port + '/', {
              params: {
                QUERY: ('MOVETO ' + (that.center_x + shiftX) + ' ' + (that.center_y + shiftY))
                // QUERY: ('MOVETO 3 3')
              }})
              .then(function (response2) {
                that.forceLoop()
              })
              .catch(function (error) {
                console.log(error)
              })
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  },
  mounted () {
    /* INIT MAP */
    if (this.r_loop !== null) {
      clearInterval(this.r_loop)
    }
    let tempMap = []
    for (let i = 0; i < 11; i++) {
      let tempArray = []
      for (let j = 0; j < 11; j++) {
        tempArray.push('X')
      }
      tempMap.push(tempArray)
    }
    this.myMap = tempMap
    /* SETUP REQUEST */
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
  background-color: DarkGoldenRod;
  display: flex;
  flex-direction: column;
  padding: 10px;
  min-width: 200px;
}
  .login > .login_box {
    display: flex;
    flex-direction: column;
  }
    .login > .login_box > input {
      flex: 1;
      width: 100%;
      max-height: 1.5rem;
      margin-bottom: 10px;
      background-color: ghostwhite;
    }
    .login > .login_box > button {
      font-size: 1.5rem;
      background-color: darkgrey;
      cursor: pointer;
      margin-bottom: 10px;
    }
    .login > .login_box > button:hover {
      background-color: grey;
    }
    .login >  .textarea {
      background-image: url(../assets/musk.jpg);
      flex: 1;
      display: flex;
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
  background-color: Chocolate ;
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
      margin: 2px;
    }
    .move > .move_row > .empty {
      background-color: Brown ;
    }
    .move > .move_row > button {
      background-color: darkgrey;
      cursor: pointer;
      font-size: 1.5rem;
      line-height: 0;
    }
    .move > .move_row > button:hover {
      background-color: grey;
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
