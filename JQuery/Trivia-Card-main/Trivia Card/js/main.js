$(document).ready(() =>{
    const $hintBox = $('.hint-box')
     const $wrongAnswerOne = $('.wrong-answer-one');
     const $wrongAnswerTwo = $('.wrong-answer-two');
     const $wrongAnswerThree = $('.wrong-answer-three');
     const $correctAnswer = $('.correct-answer');
   
   
     $hintBox.on('click', () => {
       $('.hint').slideToggle(300);
     })
   
   $wrongAnswerOne.on('click', () => {
     $('.wrong-text-one').fadeOut('slow');
     $('.frown').show();
   });
   
   $wrongAnswerTwo.on('click', () => {
     $('.wrong-text-two').fadeOut('slow');
     $('.frown').show();
   });
   
   $wrongAnswerThree.on('click', () => {
     $('.wrong-text-three').fadeOut('slow');
     $('.frown').show();
   });
   
   $correctAnswer.on('click', () => {
     $('.frown').hide();
     $('.smiley').show();
     $('.wrong-text-one').fadeOut('slow');
     $('.wrong-text-two').fadeOut('slow');
     $('.wrong-text-three').fadeOut('slow');
   })
   
   });