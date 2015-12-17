import Ember from 'ember';

export default Ember.Route.extend({
    model(){
        return this.store.find('user');
    },
    actions: {
        save(model){
            this.store.save('user', model, {dataType: 'text'});
        },
        create(){
            let record = this.store.createRecord('user', {name: 'hello world', gender: 'f'});
            this.store.save('user', record);
        },
        remove(model){
            this.store.deleteRecord('user', model);
        },
        storePut(){
            this.store.request.put('/v1/user/1', {dataType: 'text'}).then(function(data){
                console.log(`store put call response ${data}`);
            })
        },  
        storeGet(){
            this.store.request.get('/v1/user').then(function(data){
                console.log(`store get call response ${data}`);
            })
        },
        storeDelete(){
            this.store.request.delete('/v1/user/1', {dataType: 'text'}).then(function(data){
                console.log(`store delete call response ${data}`);
            })
        },
        storePost(){
            this.store.request.post('/v1/user', {data: {name: 'name', gender: 'f'}, dataType: 'text'}).then(function(data){
                console.log(`store delete call response ${data}`);
            })
        },
        storeAjaxFail(){
            this.store.ajax('put', '/v1/user/1').then(function(data){
                console.log(`store ajax call response ${data}`);
            }).catch(function(reason){
                console.error(`store ajax call response ${reason}`);
            });
        },
        errorRequest(){
            this.store.ajax('put', '/v1/404/1').then(function(data){
                console.log(`store ajax call response ${data}`);
            }).catch(function(reason){
                console.error(`store ajax call response ${reason}`);
            });
        },
        storeAjaxSuccess(){
            this.store.ajax('put', '/v1/user/1', {dataType: 'text'}).then(function(data){
                console.log(`store ajax call response ${data}`);
            }).catch(function(reason){
                console.error(`store ajax call response ${reason}`);
            });
        },

        modelPut(){
            this.store.save('user', {'_id':1, name: 'name', gender: 'f'}).then(function(data){
                console.log(`model put call response ${data.msg}`);
            })
        },  
        modelGet(){
            this.store.find('user').then(function(data){
                console.log(`model get call response ${data}`);
            })
        },
        modelDelete(){
            this.store.deleteRecord('user', 1).then(function(data){
                console.log(`model delete call response ${data.msg}`);
            })
        },
        modelPost(){
            this.store.save('user', {name: 'name', gender: 'f'}).then(function(data){
                console.log(`model delete call response ${data.msg}`);
            })
        },
        modelAjaxFail(){
            this.store.modelFor('user').ajax('put', '/v1/user/1').then(function(data){
                console.log(`model ajax call response ${data.msg}`);
            }).catch(function(reason){
                console.error(`model ajax call response ${reason}`);
            });
        },
        modelAjaxSuccess(){
            this.store.modelFor('user').ajax('put', '/v1/user_json/1').then(function(data){
                console.log(`model ajax call response ${data.msg}`);
            }).catch(function(reason){
                console.error(`model ajax call response ${reason}`);
            });
        },
    }
});