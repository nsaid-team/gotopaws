
var app = angular.module('petssPage', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller("PetTable",  function ($http) {
  var dict = this;
  this.loaded = false;
  this.data = {};


    $http.get("bootstrap-3.3.5-dist/js/3x3x3_pets_dataset.json").success(function(load){
      dict.data = load;
      dict.loaded = true;
    });
});

/* directive
*/
app.directive('petTable2', function(){
  return{
    restrict: 'E',
    t