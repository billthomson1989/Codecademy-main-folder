$(document).ready(() => {
    const $text = $('#text');
    const $font = $('#font');
  
    $text.on('keyup', (event) => {
      $('.preview').html($(event.currentTarget).val());
    })
    $font.on('change', event => {
      $('.preview').css('fontFamily', $(event.currentTarget).val());
    })
  $('#weight').on('change', event => {
      $('.preview').css('fontWeight', $(event.currentTarget).val());
    })
  $('#size').on('keyup', event => {
        let fontSize= $(event.currentTarget).val();
        fontSize = fontSize + 'px';
        $('.preview').css('fontSize', fontSize);
      })
  })