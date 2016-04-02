import Vue from 'vue'
import Vuex from 'vuex'

// Make vue aware of vuex
Vue.use(Vuex)

// We create an object to hold the initial state when
// the app starts up
const state = {
  // TODO: Set up our initial state
  count: 0
}

// Create an object storing various mutations. We will write the mutation
const mutations = {
  // TODO: set up our mutations
  INCREMENT (state, amount) {
    state.count += amount
  },
  DECREMENT (state, amount) {
    state.count -= amount
  }
}

// We combine the intial state and the mutations to create a vuex store.
// This store can be linked to our app.
export default new Vuex.Store({
  state,
  mutations
})
