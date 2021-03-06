var app1 = angular.module("GoToPaws", []);

app1.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[{');
    $interpolateProvider.endSymbol('}]');
  });

app1.controller('templateController', function($scope, $location) {
    $scope.isActive = function(route) {
      console.log($location.path());
        return route === $location.path();
    }
});



app1.directive("navBar", function(){

  return{
    restrict: 'E',
    templateUrl: '/bootstrap-3.3.5-dist/templates/Navbar.html'
  };
});


  
    app1.controller('ExampleController', ['$scope', '$http', function($scope, $http) {
      $scope.list = [];
      $scope.text = "Unit Tests";
      var temp = this;
      $scope.submit = function() {
        $scope.list = [];
       $http.get("/test/").success(function(load){
            $scope.text = load.toString();
          });
       

      $scope.list.push(this.text);
      console.log(this.text);
      $scope.text = '';

       };
        
      
    }]);



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










