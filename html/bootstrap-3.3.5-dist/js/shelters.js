
var app = angular.module('sheltersPage', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller("ShelterTable",  function ($http) {
  var dict = this;
  this.loaded = false;
  this.data = {"name":"empty"};

  // this.set_dict = function(val){
  //   dict.data = {};
  //   var temp = {};
    

  //   for (var i = 0, len = val.length; i < len; i++) {
  //       temp['id']= val[i][1];
  //       temp['name']= val[i][2];
  //       temp['address']= val[i][3];
  //       temp['city'] = val[i][4];
  //       temp['state']= val[i][5];
  //       temp['phone']= val[i][6];
  //       temp['email']=val[i][7];
  //       temp['hours']=val[i][8];

  //       dict.data[val[i][0]] = temp;

  //   }
  //   dict.loaded = true;
  // };
});
/*
    $http.get("bootstrap-3.3.5-dist/js/3x3x3_shelters_dataset.json").success(function(load){
      dict.data = load;
      dict.loaded = true;
    });
*/
/* directive

app.directive('shelterTable2', function(){
  return{
    restrict: 'E',
    templateUrl: '"shelter-table.html"'
  };
});
*/
