angular.module('PastryApp')
.factory('authInjector', function($location, User) {

    var authInjector = {
        request: function(config) {
            if (config.method !== 'OPTIONS') {
                if (!User.getToken()) {
                    $location.path('/login');
                }
                config.headers['Auth-Token'] = User.getToken();
            }
            return config;
        },
        responseError: function(response) {
            if (response.status === 401 && response.data.expired_token) {
                User.logout();
                $location.path('/login');
            }
            return response;
        },
    };
    return authInjector;

});