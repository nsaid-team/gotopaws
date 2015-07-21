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


  
    app1.controller('ExampleController', ['$scope', '$http', function($scope, $http) {
      $scope.list = [];
      $scope.text = "Unit Tests";
      $scope.submit = function() {
       $http.get("/unit_test").success(function(load){
            $scope.text = load;
          });
        };

      $scope.list.push(this.text);
      $scope.text = '';
        
      };
    }]);


it('should check ng-submit', function() {
  expect(element(by.binding('list')).getText()).toBe('list=[]');
  element(by.css('#submit')).click();
  expect(element(by.binding('list')).getText()).toContain('hello');
  expect(element(by.model('text')).getAttribute('value')).toBe('');
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










