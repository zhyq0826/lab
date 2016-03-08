import Ember from 'ember';
import layout from './template';
console.log(layout);

export default Ember.Component.extend({
    layout: layout,
    click(){
        this.attrs.count.update(this.attrs.count.value+1);
    }
})