<template>
  Count is {{ counter }}
</template>

<script>
import { getCount } from '../getters'
// We may want to define getters with computed values (think totals, averages, etc.).

// Many components in a larger app can use the same getter function.

// If the value is moved from say store.count to store.counter.value you'd have to update one getter instead of dozens of components.

export default {
  vuex: {
    getters: {
      counter: getCount
    }
  }
}
</script>
<style>
</style>