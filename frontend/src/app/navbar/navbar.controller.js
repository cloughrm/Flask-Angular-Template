'use strict';

angular.module('PastryApp')
.controller('NavbarCtrl', function($scope, $location, User) {
    $scope.isCollapsed = true;

    $scope.loggedIn = User.getName();
    $scope.$on('$locationChangeStart', function(event) {
        $scope.loggedIn = User.getName();
    });

    $scope.logout = function() {
        User.logout();
        $location.path('/login');
    };

});