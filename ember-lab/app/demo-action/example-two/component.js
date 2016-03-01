import Ember from 'ember';
import layout from './template';

export default Ember.Component.extend({
    layout: layout,
    keyUp(event) {
        if (event.which === 13) {
          this.attrs['on-enter'](this.$('input').val());
        }
    }
})