import Ember from 'ember';

const {get, getOwner} = Ember;

export default Ember.Route.extend({
    init(){
        this._super(...arguments);
        let v = getOwner(this).lookup('template:application');
    }
});