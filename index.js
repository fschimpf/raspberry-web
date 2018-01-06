angular
.module('automasjonApp', [])
.controller('AutomasjonCtrl', ['$http', function($http) {
  console.log("Intialising AutomasjonCtrl...");
  var self = this;

  self.errorMsg = null;
  self.lightStatus = null;

  this.toggleLight = function() {
    self.lightStatus = null;
    $http.post('/toggleLight')
      .then(function(resp) {
        self.lightStatus = resp.data.status;
      })
      .catch(function(err) {
        self.errorMsg = err;
      });
  }
}]);