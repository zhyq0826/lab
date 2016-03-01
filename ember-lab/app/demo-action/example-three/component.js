import Ember from 'ember';
import layout from './template';

export default Ember.Component.extend({
    layout: layout,
    actions: {
        clickfirst(){
            this.attrs.alert();
        },
        clicktwo(){
            this.attrs.alert('i am appended to end');
        }
    }
})