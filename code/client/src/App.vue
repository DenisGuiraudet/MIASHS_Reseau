<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {}
</script>

<style>
* {
  padding: 0;
  margin: 0;
}
#app {
  position: relative;
  min-width: 100vw;
  width: 100vw;
  max-width: 100vw;
  min-height: 100vh;
  height: 100vh;
  max-height: 100vh;
  overflow: hidden;
}
</style>
