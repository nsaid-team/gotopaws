
    var app = angular.module("sheltersPage", []);
 
    app.controller("ShelterController", ['$http', function ($http) {
        var dict = this;
        dict.loaded = false;
        dict.data = {"all_shelters" :
        				[{"name": "Austin Pets Alive!","location": "Austin"},
            			{"name":"Your mom","location":"your house"},{"name":"Austin Humane Society"}]
            		};
        $http.get("/3x3x3_shelters_dataset.json").success(function(load){
        	dict.data = load;
        	dict.loaded = true;
        });
    }]);
