'use strict';

angular.module('PastryApp')
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'app/home/home.html',
        controller: 'HomeCtrl',
        title: 'Home',
      })
      .when('/login', {
        templateUrl: 'app/login/login.html',
        controller: 'LoginCtrl',
        title: 'Login',
      })
      .otherwise({
        redirectTo: '/'
      });
  });
