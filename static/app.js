var app = angular.module( 'LeadSheetApp', [] );


app.controller( 'LeadSheetController', [
      '$scope', '$http',
      function( $scope, $http  ) {
         
         var chords = $scope.chords = [];
         

         $scope.addChord = function( chord ){
            $scope.chords.push( chord );
         }

         $scope.generateMusic = function(){
            var url =  '/music?' +  $.param({chords: chords, tempo: 120});
            $scope.musicUrl = url;
         }

         $scope.removeChord = function( i ){
            chords.splice( i, 1 );
         }
      

      }]
);

