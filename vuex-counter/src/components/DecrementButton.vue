<template>
  <button @click.prevent="activate">-1</button>
</template>

<script>
import { decrementCounter } from '../actions'

export default {
  vuex: {
    actions: {
      decrement: decrementCounter
    }
  },
  methods: {
    activate () {
      this.decrement()
    }
  }
}
</script>

<style>
</style>