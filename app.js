// create the module
var app = angular.module("myApp", ['ngRoute']);

app.controller('CryptographyController', function($scope) {
    $scope.message = 'Hello from FirstController';
})