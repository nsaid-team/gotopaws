var app = angular.module("mapModule" [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
app.controller("MapController", function{
	
	geocoder = new google.maps.Geocoder();
	geocoder.geocode({ 'address': address }, function(results, status) {
	  if (status == google.maps.GeocoderStatus.OK) {
	    map.setCenter(results[0].geometry.location);
	    var marker = new google.maps.Marker({
	    map: map,
	    position: results[0].geometry.location
	  });



});




  app.controller('MyCtrl', ['$scope', '$http', function($scope, $http) {
  	$scope.currentUrl = $location.path;
    $scope.test = "Hola";
    delete $http.defaults.headers.common['X-Requested-With'];
    $http.get(currentUrl + '/json').success(function(data) {
      $scope.results = data;
      console.log(data);
    }).error(function(data, status) {
      $scope.data = data || "Request failed";
      $scope.status = status;
      console.log(data);
    });
}]);

