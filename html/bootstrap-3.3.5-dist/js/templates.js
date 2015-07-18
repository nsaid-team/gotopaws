var app = angular.module("GoToPaws", ['mapModule'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}).run(function($rootScope, $location) {
    $rootScope.location = $location;
});;


app.directive('navBar', function(){
  return{
    restrict: 'E',
    templateUrl: '/bootstrap-3.3.5-dist/templates/Navbar.html'
  };
});

app.directive('cityShelters', function(){
  return{
    restrict: 'E',
    templateUrl: '/bootstrap-3.3.5-dist/templates/Shelter_fill.html'
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
    templateUrl: '/bootstrap-3.3.5-dist/templates/Vet_fill.html'
  };
});


var app2 = angular.module("mapModule", [], function(){});

// app2.controller("MapController", function{
  
//   geocoder = new google.maps.Geocoder();
//   geocoder.geocode({ 'address': address }, function(results, status) {
//     if (status == google.maps.GeocoderStatus.OK) {
//       map.setCenter(results[0].geometry.location);
//       var marker = new google.maps.Marker({
//       map: map,
//       position: results[0].geometry.location
//     })}
//     });



// });




  app.controller('MyCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.test = "Hola";
    var loc = $location.path;
    delete $http.defaults.headers.common['X-Requested-With'];
    $http.get(loc + '/json').success(function(data) {
      $scope.results = data;
      console.log(data);
    }).error(function(data, status) {
      $scope.data = data || "Request failed";
      $scope.status = status;
      console.log(data);
    });
}]);