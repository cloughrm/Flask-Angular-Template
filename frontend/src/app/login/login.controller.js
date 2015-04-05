'use strict';

angular.module('PastryApp')
.controller('LoginCtrl', function($scope, $location, PastryApi, User) {

    $scope.login = function() {

        PastryApi.login.post({
            username: $scope.username,
            password: $scope.password,
        }).then(function(resp) {
            $scope.error = null;
            User.setCredentials($scope.username, resp['Auth-Token']);
            $location.path('/');
        }, function(resp) {
            $scope.error = resp.data;
        });

    };

});