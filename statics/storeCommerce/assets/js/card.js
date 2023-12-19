
(function( d ) {

  var inp = d.querySelector( 'input[name="card_number"]' )
  var date = d.querySelector( 'input[type="input_date"]' ) 
      inp.addEventListener( 'keyup',
  function(){
   if ( inp.value.length == 4 || inp.value.length == 9 || inp.value.length == 14  )  {
        inp.value = inp.value +  ' ';
    }
     
  }, false);

  date.addEventListener( 'keyup',
  function(){
   if ( date.value.length == 2  )  {
        date.value = date.value +  '/';
    }
     
  }, false);

  
}( document ));