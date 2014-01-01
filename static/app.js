var app = angular.module( 'LeadSheetApp', ['boostrapAudio'] );


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
            $scope.chords.splice( i, 1 );
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




var bootstrapAudio = angular.module('boostrapAudio', []);

bootstrapAudio.directive( 'musicPlayer', [  function( ){

   
   var audio = null;
   var chkTimeInterval = null;

   return {
      templateUrl: '/static/partials/music-player.html',
      scope: {src: '='},
      restrict: 'E',
      link: function( scope, $elm, attrs ){
         
         scope.currentTime = 0;         

         scope.$watch( 'src', function(){
            var newSrc = scope.src;
            console.log( scope );

            $elm.find( 'button' ).attr('disabled', true );
            
            audio = new Audio( newSrc );
            audio.preload = true;
            audio.autoplay = false; // just in case

            audio.addEventListener( 'canplaythrough', function(){
               
               $elm.find( '.play-btn' ).click( function(){
                  audio.play();
               }).attr( 'disabled', false );

               $elm.find( '.stop-btn' ).click( function(){
                  
                  audio.pause();
                  audio.load();
                  audio.currentTime = 0;
               }).attr( 'disabled', false );

            });
            
            $elm.find( '.hidden' ).empty().append( 
               audio   
            );

            chkTimeInterval = setInterval( function(){
               
               scope.currentTime = audio.currentTime
               if( scope.currentTime == Infinity ){
                  scope.currentTime = 0;
               }
               scope.$digest(); 
            }, 1000 );


         
         }); 
      
      
      
      }

   }

}]);


// format num seconds as time
bootstrapAudio.filter( 'timefmt', function( ){
   
   return function(t){
     var hours = Math.floor( t / (60 * 60) ); 
     var minutes = Math.floor( ( t / 60 ) - (hours * 60) );
     var seconds = Math.floor(t - (hours * 60 * 60) - (minutes * 60))
      
     hours = hours < 10 ? '0' + hours : hours;
     minutes = minutes < 10 ? '0' + minutes : minutes;
     seconds = seconds < 10 ? '0' + seconds : seconds;


     return hours + ":" + minutes + ":" + seconds;


   }

});
