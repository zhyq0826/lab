<template>
  <input type="number" v-model="amount" @change.prevent="activate" number>
</template>

<script>
import { incrementCounter } from '../actions'

export default {
  data: function () {
    return {amount: 0}
  },
  vuex: {
    actions: {
      increment: incrementCounter
    }
  },
  methods: {
    activate () {
      this.increment(this.amount)
    }
  }
}
</script>

<style>
</style>