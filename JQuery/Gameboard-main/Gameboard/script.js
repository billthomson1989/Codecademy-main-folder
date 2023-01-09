var main = function() {
    const $moreButton = $('.more-btn');
    const $share = $('.share');
    
    $moreButton.on('click', (event) => {
      $(event.currentTarget).siblings('.more-menu').toggle();
    })
    
    $share.on('click', (event) => {
      $(event.currentTarget).next('.share-menu').toggle();
    })
    
    $('.notification').on('click', (event) => {
      $(event.currentTarget).toggleClass('active')
    });
    };
    
    $(document).ready(main);