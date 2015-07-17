var app = angular.module("GoToPaws", []);


app.directive('navBar', function(){
  return{
    restrict: 'E',
    templateUrl: '/bootstrap-3.3.5-dist/templates/Navbar.html'
  };
});

app.directive('cityShelters', function(){
  return{
    restrict: 'E',
    templateUrl: '"/bootstrap-3.3.5/templates/Shelter_fill.html"'
  };
});

app.directive('cityPets', function(){
  return{
    restrict: 'E',
    templateUrl: '/bootstrap-3.3.5-dist/templates/Pet_fill.html'
  };
});

app.directive('cityVets', function(){
  return{
    restrict: 'E',
    templateUrl: '"/bootstrap-3.3.5/templates/Vet_fill.html"'
  };
});
