<template>
  <div id="app">
    <h3>Increment:</h3>
    <increment></increment>
    <h3>Increment amount:</h3>
    <increment-input></increment-input>
    <h3>Decrement</h3>
    <Decrement></Decrement>
    <h3>Counter:</h3>
    <counter></counter>
  </div>
</template>

<script>
import Counter from './components/CounterDisplay.vue'
import Increment from './components/IncrementButton.vue'
import Decrement from './components/DecrementButton.vue'
import IncrementInput from './components/IncrementAmount.vue'
import store from './store'

export default {
  components: {
    Counter,
    Increment,
    Decrement,
    IncrementInput
  },
  store // make this and all child components aware of the new store
}
</script>

<style>
</style>