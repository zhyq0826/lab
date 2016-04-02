// An action will recieve the store as the first argument.
// Since we are only interested in the dispatch (and optionally the state)
// We can pull those two parameters using the ES6 destructuring feature
export const incrementCounter = function ({ dispatch, state }, value = 1) {
  dispatch('INCREMENT', value)
}

export const decrementCounter = function ({ dispatch, state }, value = -1) {
  dispatch('DECREMENT', value)
}
