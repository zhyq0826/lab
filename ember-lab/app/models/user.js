import model from 'ember-easy-orm/mixins/model';


export default Ember.Object.extend(model, {
    model: {
        name: 'hello',
        gender: ''
    },
    url: '/v1/user_json',
    ajaxSettings: {
        traditional: true,
        dataType: 'json'
    },
    RESTSerializer: function(data){
        console.log(data);
        return data;
    }
});