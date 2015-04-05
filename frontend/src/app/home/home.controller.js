'use strict';

angular.module('frontend')
.controller('HomeCtrl', function($scope, PastryApi) {

    $scope.users = PastryApi.users.getList();

});
