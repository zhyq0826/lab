module.exports = function(app) {

    app.get('/v1/user', function(req, res) {
        res.send([{
            _id:1,
            name: 'name',
            gender: 'f'
        }, {
            _id:2,
            name: 'name',
            gender: 'f'
        }, {
            _id:3,
            name: 'name',
            gender: 'f'
        }])
    });

    app.post('/v1/user', function(req, res) {
        res.send('post ok');
    });

    app.put('/v1/user/*', function(req, res){
        res.send('put ok');
    })

    app.delete('/v1/user/*', function(req, res){
        res.send('delete ok');
    })


    app.get('/v1/user_json', function(req, res) {
        res.send([{
            _id:1,
            name: 'name',
            gender: 'f'
        }, {
            _id:2,
            name: 'name',
            gender: 'f'
        }, {
            _id:3,
            name: 'name',
            gender: 'f'
        }])
    });

    app.post('/v1/user_json', function(req, res) {
        res.send({code: 0, res:{}, 'msg': 'post ok'});
    });

    app.put('/v1/user_json/*', function(req, res){
        res.send({code: 0, res:{}, 'msg': 'put ok'});
    })

    app.delete('/v1/user_json/*', function(req, res){
        res.send({code: 0, res:{}, 'msg': 'delete ok'});
    })
};