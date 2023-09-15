<?php

function magic8Ball(){
  echo "Ask me anything, I'll tell your fortune!";
  echo "\n\n";
 
  $question = readline(">>");
  echo "\n";

  echo "So your question is ${question}, hu?... well the great spirits have sopoken! Ready or not your answer is: ";
  echo "\n";
  $choice = rand(0, 19);

  switch ($choice){
   case "0":
     echo "\n"."It is certain."."\n";
     break;
   case "1":
     echo "\n"."It is decidedly so."."\n";
     break;
   case "2":
     echo "\n"."Without a doubt"."\n";
     break;
   case "3":
     echo "\n"."Yes - definitely."."\n";
     break;
   case "4":
     echo "\n"."You may rely on it."."\n";
     break;
   case "5":
     echo "\n"."As I see it, yes."."\n";
     break;
   case "6":
     echo "\n"."Most likely"."\n";
     break;
   case "7":
     echo "\n"."Outlook good."."\n";
     break;
   case "8":
     echo "\n"."Yes."."\n";
     break;
   case "9":
     echo "\n"."Signs point to yes"."\n";
     break;
   case "10":
     echo "\n"."Reply hazy, try again."."\n";
     break;
   case "11":
     echo "\n"."Ask again later."."\n";
     break;
   case "12":
     echo "\n"."Better not tell you now."."\n";
     break;
   case "12":
     echo "\n"."Cannot predict now."."\n";
     break;
   case "12":
     echo "\n"."Concentrate and ask again."."\n";
     break;
   case "13":
     echo "\n"."Don't count on it."."\n";
     break;
   case "14":
     echo "\n"."My reply is no"."\n";
     break;
   case "15":
     echo "\n"."My sources say no."."\n";
     break;
   case "16":
     echo "\n"."Outlook not so good."."\n";
     break;
   Default:
     echo "\n"."Very doubtful."."\n";
     break;
}
echo "\n"; 

}

echo magic8Ball();


