var app1 = angular.module("GoToPaws",  function($interpolateProvider) {
    $interpolateProvider.startSymbol('[{');
    $interpolateProvider.endSymbol('}]');
});



app1.controller('templateController', function($scope, $location) {
    $scope.isActive = function(route) {
      console.log(route);
      console.log($location.path());
        return route === $location.path();
    }
});



app1.directive("navBar", function(){
  console.log("directive");
  return{
    restrict: 'E',
    templateUrl: '/bootstrap-3.3.5-dist/templates/Navbar.html'
  };
});

// app.directive('cityShelters', function(){
//   return{
//     restrict: 'E',
//     templateUrl: '/bootstrap-3.3.5-dist/templates/Shelter_fill.html'
//   };
// });

// app.directive('cityPets', function(){
//   return{
//     restrict: 'E',
//     templateUrl: '/bootstrap-3.3.5-dist/templates/Pet_fill.html'
//   };
// });

// app.directive('cityVets', function(){
//   return{
//     restrict: 'E',
//     templateUrl: '/bootstrap-3.3.5-dist/templates/Vet_fill.html'
//   };
// });










