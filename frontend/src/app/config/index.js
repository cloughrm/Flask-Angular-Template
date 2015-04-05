'use strict';

angular.module('PastryApp', [
    'ngAnimate',
    'ngCookies',
    'ngSanitize',
    'restangular',
    'ngRoute',
    'ui.bootstrap',
    'LocalStorageModule',
])
.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('{{API_URL}}');
})
.config(function(localStorageServiceProvider) {
    localStorageServiceProvider.setPrefix('Pastry');
})
.config(function($httpProvider) {
    $httpProvider.interceptors.push('authInjector');
})
.config(function(RestangularProvider) {
    RestangularProvider.addResponseInterceptor(function(data, operation, what, url, response, deferred) {
        var extractedData;
        if (operation === 'getList') {
            extractedData = data.objects;
        } else {
            extractedData = data;
        }
        return extractedData;
    });
})
.run(function($location, $rootScope) {
    // Set the page title
    $rootScope.$on('$routeChangeSuccess', function(event, current, previous) {
        $rootScope.title = current.$$route.title;
    });
})
;