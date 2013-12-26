var app = angular.module( 'LeadSheetApp', [] );


app.controller( 'LeadSheetController', [
      '$scope', '$http',
      function( $scope, $http  ) {
         
         $scope.chords = [];
         $scope.musicInfo = {tempo: '120'};

         $scope.addChord = function( chord ){
            $scope.chords.push( chord );
         }

         $scope.generateMusic = function(){
            var url =  '/music?' +  $.param({chords: $scope.chords, tempo: $scope.musicInfo.tempo });
            $scope.musicUrl = url;
         }

         $scope.removeChord = function( i ){
            chords.splice( i, 1 );
         }
      

      }]
);


app.directive( 'chordSelector', [ function(){
   return {
      scope: {
         chordAdder: '='
      },
      templateUrl: '/static/partials/chord-selector.html',
      restrict: 'E'
   }      

}]);

