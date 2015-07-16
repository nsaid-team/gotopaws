var app = angular.module("GoToPaws", []);

app.directive('navBar', function(){
  return{
    restrict: 'E',
    templateUrl: '"Navbar.html"'
  };
});

app.directive('cityShelters', function(){
  return{
    restrict: 'E',
    templateUrl: '"Shelter_fill.html"'
  };
});

app.directive('cityPets', function(){
  return{
    restrict: 'E',
    templateUrl: '"Pet_fill.html"'
  };
});

app.directive('cityVets', function(){
  return{
    restrict: 'E',
    templateUrl: '"Vet_fill.html"'
  };
});