
var app = angular.module('sheltersPage', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});




app.controller("Test controller", function($scope) {
    $scope.value = "working";

});

app.controller("ShelterTest", function(){
    this.value = "working";
});





app.controller("ShelterTable",  function ($http) {
  var dict = this;
  this.loaded = false;
  this.data = {};


    $http.get("3x3x3_shelters_dataset.json").success(function(load){
      dict.data = load;
      dict.loaded = true;
    });
});

/* directive
*/
app.directive('shelterTable2', function(){
  return{
    restrict: 'E',
    templateUrl: '"shelter-table.html"'
  };
});
