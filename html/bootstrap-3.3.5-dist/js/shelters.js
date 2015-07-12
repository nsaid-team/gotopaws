function(){
    var app = angular.module("sheltersPage2", []);


    app.controller("Test controller", function($scope) {
        $scope.value = "working";

    });
    
    app.controller("ShelterTest", function(){
        this.value = "working";
    });





    app.controller("ShelterTable2", ['$http', function ($http) {
      var dict = this;
      this.loaded = false;
      dict.data = {"all_shelters": 
                    [{"country":{"$t":"US"},
                    "longitude":{"$t":"-97.766"},
                    "name":{"$t":"Austin Pets Alive!"},
                    "phone":{},
                    "state":{"$t":"TX"},
                    "address2":{},
                    "email":{"$t":"adopt@austinpetsalive.org"},
                    "city":{"$t":"Austin"},
                    "zip":{"$t":"78704"},
                    "fax":{},
                    "latitude":{"$t":"30.2458"},
                    "id":{"$t":"TX1218"},
                    "address1":{"$t":"1156 West Cesar Chavez"},
                    "pets":["32251618"]
                    },
                    {"country":{"$t":"US"},
                    "longitude":{"$t":"-122.4183"},
                    "name":{"$t":"Muttville Senior Dog Rescue"},
                    "phone":{"$t":"(415) 272-4172  "},
                    "state":{"$t":"CA"},
                    "address2":{},
                    "email":{"$t":"adoptions@muttville.org"},
                    "city":{"$t":"San Francisco"},
                    "zip":{"$t":"94141"},
                    "fax":{"$t":"415-842-0320"},
                    "latitude":{"$t":"37.775"},
                    "id":{"$t":"CA1287"},
                    "address1":{"$t":"255 Alabama St"},
                    "pets":["32607766"]
                    },
                    {"country":{"$t":"US"},
                    "longitude":{"$t":"-95.3631"},
                    "name":{"$t":"Homeless Pet Placement League"},
                    "phone":{"$t":"(713) 862-7387   "},
                    "state":{"$t":"TX"},
                    "address2":{},
                    "email":{"$t":"hppl@hppl.org"},
                    "city":{"$t":"Houston"},
                    "zip":{"$t":"77277"},
                    "fax":{},
                    "latitude":{"$t":"29.7631"},
                    "id":{"$t":"TX154"},
                    "address1":{"$t":"P. O. Box 273027"},
                    "pets":["20758336"]
                    }]
    };

    $http.get('"3x3x3_shelters_dataset.json"').success(function(load){
      dict.data = load;
      dict.loaded = true;
    });
  }]);
/* directive
*/
    app.directive('shelterTable2', function(){
      return{
        restrict: 'E',
        templateUrl: '"shelter-table.html"'
      };
    });
};