angular.module('PastryApp')
.factory('PastryApi', function(Restangular) {

    var PastryApi = {};
    var v1 = 'api/v1/';

    PastryApi.login = Restangular.all(v1 + 'login');
    PastryApi.users = Restangular.all(v1 + 'users');

    return PastryApi;

});