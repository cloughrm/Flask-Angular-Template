'use strict';

angular.module('PastryApp')
.controller('HomeCtrl', function($scope, PastryApi) {

    $scope.users = PastryApi.users.getList();

});
