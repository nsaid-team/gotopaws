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
    templateUrl: '{% static "templates/Shelter_fill.html" %}'
  };
});

app.directive('cityPets', function(){
  return{
    restrict: 'E',
    templateUrl: '{% static "templates/Pet_fill.html" %}'
  };
});

app.directive('cityVets', function(){
  return{
    restrict: 'E',
    templateUrl: '{% url {% static "templates/Vet_fill.html" %}%}'
  };
});