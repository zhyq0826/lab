<template>
  <button @click.prevent="activate">+1</button>
</template>

<script>
import { incrementCounter } from '../actions'

// We have a new object vuex.actions which includes the new action
// We didn't specify which store, object, state etc. Vuex wires everything up for us.
// We can call the action either by using this.increment() in any method.
// We can also call the action using the @click parameter making increment like any regular vue component method.
// The action is called incrementCounter but we can use any name which is appropriate.
export default {
  vuex: {
    actions: {
      increment: incrementCounter
    }
  },
  methods: {
    activate () {
      this.increment()
    }
  }
}
</script>

<style>
</style>