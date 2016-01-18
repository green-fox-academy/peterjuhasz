$( function() {
  $( ".container" ).mixItUp( {
    animation: {
      duration: 400,
      effects: 'stagger(34ms) fade',
      easing: 'cubic-bezier(0.47, 0, 0.745, 0.715)'
    },

    layout: {
      display: 'block',
      containerClass: 'master-container'
    },
    selectors: {
      target: '.mix',
      filter: '.filter',
      sort: '.sort'
    }
  } );

  $( "#filter-select" ).on( "change", function() {
    $( ".container" ).mixItUp( 'filter', this.value );
  } );

  $( "#sort-select" ).on( "change", function() {
    $( ".container" ).mixItUp( 'sort', this.value );
  } );
} );
