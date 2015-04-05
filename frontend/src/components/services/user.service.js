angular.module('frontend')
.service('User', function(localStorageService) {

    var User = {};
    var key = 'auth';

    User.setCredentials = function(email, authToken) {
        localStorageService.set(key, {
            email: email,
            authToken: authToken,
        });
    };

    User.getName = function() {
        var data = localStorageService.get(key);
        if (!data) {
            return null;
        }
        return data.email;
    };

    User.getToken = function() {
        var data = localStorageService.get(key);
        if (!data) {
            return null;
        }
        return data.authToken;
    };

    User.logout = function() {
        return localStorageService.remove(key);
    };

    return User;

});