
var app = angular.module('sheltersPage', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller("ShelterTable",  function ($http) {
  var dict = this;
  this.loaded = false;
  this.data = {};

  this.set_dict = function(val){
    dict.data = {};
    var temp = {}
    for each (shelter in val){
        dict.data[shelter[0]] = temp;
   
        temp['id']= shelter[1];
        temp['name']= shelter[2];
        temp['address']= shelter[3];
        temp['city'] = shelter[4];
        temp['state']= shelter[5];
        temp['phone']= shelter[6];
        temp['email']=shelter[7];
        temp['hours']=shelter[8];
        dict.loaded = true;
    }
  };

/*
    $http.get("bootstrap-3.3.5-dist/js/3x3x3_shelters_dataset.json").success(function(load){
      dict.data = load;
      dict.loaded = true;
    });
*/
});

/* directive
*/
app.directive('shelterTable2', function(){
  return{
    restrict: 'E',
    templateUrl: '"shelter-table.html"'
  };
});
