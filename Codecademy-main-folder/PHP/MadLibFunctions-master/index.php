<?php
function generateStory($singular_noun, $verb, $color, $distance_unit){
  $story = "\nThe {$singular_noun}s are lovely,\n
{$color}, and deep.\n
But I have promises to keep,\n
And miles to go before I {$verb},\n
And miles to go before I {$verb}.\n";
 
$costume_story = str_replace ( "mile" , $distance_unit , $story);

return $costume_story;
}

echo generateStory("bed", "sleep", "red", "mile");

echo generateStory("card", "take", "blue", "mile");

echo generateStory("leaf", "shake", "green", "kilometer");
