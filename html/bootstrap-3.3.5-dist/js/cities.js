
var app = angular.module('citiesPage', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller("CityTable",  function ($http) {
  var dict = this;
  this.loaded = false;
  this.data = {};


    $http.get("bootstrap-3.3.5-dist/js/3x3x3_cities_dataset.json").success(function(load){
      dict.data = load;
      dict.loaded = true;
    });
});

/* directive
*/
app.directive('cityTable2', function(){
  return{
    restrict: 'E',
    templateUrl: '"city-table.html"'
  };
});
