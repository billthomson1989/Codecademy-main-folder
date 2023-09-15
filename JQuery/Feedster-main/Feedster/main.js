$(document).ready(() => {
    const $menu = $('.menu');
    const $navMenu = $('.nav-menu');
    const $button = $('.btn');
    const $postText = $('.postText');
    const $wordCount = $('.wordcount')
   
    $menu.on('mouseenter', () => {
      $navMenu.show();
    }).on('mouseleave', () => {
      $navMenu.hide();
    })
   
   $button.on('mouseenter', (event) => {
     $(event.currentTarget).addClass('btn-hover');
   }).on('mouseleave', (event) =>{
     $(event.currentTarget).removeClass('btn-hover');
   })
   
   $postText.on('keyup', (event) => {
     $postText.focus();
     let post = $(event.currentTarget).val();
     let remaining = 140 - post.length;
     if(remaining <= 0){
       $wordCount.addClass('red')
     }else{
       $wordCount.removeClass('red')
     }
     $('.characters').html(remaining);
   })
   
}); 
   