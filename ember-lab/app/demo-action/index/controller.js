import Ember from 'ember';

export default Ember.Controller.extend({
    count: 0,
    text: null,
    alertValue: 'I am is a alertValue',
    actions: {
        pressEnter(value){
            this.set('text', value);
        },
        alertSome(){
            let v = [].slice.apply(arguments);
            alert(v.join(' '));
        }
    }
});