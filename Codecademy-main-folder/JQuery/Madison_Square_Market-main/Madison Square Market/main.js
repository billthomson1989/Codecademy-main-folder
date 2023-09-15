$(document).ready(() => {
    const $dropDown = $('.dropdown-menu');
    
    const $cart = $('#cart');
    $cart.on('click', () => {
      $('#cartMenu').show();
    });
    $cart.on('mouseleave', () => {
      $dropDown.hide();
    });
  
   const $account = $('#account');
    $account.on('click', () => {
      $('#accountMenu').show();
    })
    $account.on('mouseleave', () => {
      $dropDown.hide();
    });
  
  
   const $help = $('#help');
    $help.on('click', () => {
      $('#helpMenu').show()
    })
    $help.on('mouseleave', () => {
      $dropDown.hide();
    });
  
   
});