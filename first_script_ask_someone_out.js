<html>
<head>
<title>1st JS Program 2007 bc i fell in <3 w/an engineer</title>
<script language="JavaScript">
<!--
/*
Code goes below this comment block
*/
var strName = prompt('Hi! What is your name? (Gotta make sure you are you!):', ' ') //Can you read between the lines? hehe...
var strGreeting = "Welcome " + strName + "!"
var strA = "Perhaps this is the beginning of something great?"// my 1st original program 
var strB = "Would you like to go out with me sometime?"//
var C = strName
var yes = "yes"
var y = "y"
var Y = "Y"
//----------------------------establishing the variables ^
alert(strGreeting)
document.write(strName)
alert(strA)
alert(C + "...")
alert(strB) //if your the hacker i hope you are: i just want to spend time with you - doesn't matter what we do/where we go~
//----------------------------first bunch of commands ^
var Places = "Places I('d) like to go to: Midevil Times, Melting Pot, Pittsburgh, Pat's in Phili, Aquarium, Science Center"
var Things = "Things I'd like to do with you: Hiking - there's a cool place in DC/VA, Scenic walk, video games (some type of arcade), jam - if you have musical talent~" 
var Hobby = "Things I like to do in general: Photography, any type of creative art/activity, music, drive, dancing with glow sticks, explore...i don't mind getting dirty~"
var Color = "My favorite color is chrome...pink too~" //i wanted to get your attention~ but i didnt' know how
var misc = "Misc info: i LOVE furry white Benji sized dogsw/cold wet black noses!! i have a wild imagination and am easily amused by the small things"
var True = "!!Yeah!! :)"
var False = "Well, it was worth a try :)"
//----------------------------variables ^
var strAnswer = prompt('Please enter Yes or No:',' ')
//----------------------------prompt ^
var strLater = "Sure, we can talk later~"
if (strAnswer == "Yes" ) {
		alert(True);
var strQue = prompt('So... would you like to know something about me?','Y or N');
} 
else {alert(False);
}
//------------------------------------------------------------------------------------------------------------main answer and prompt y/n ^
function myfunction() //-------------------------------FUNCTION activated by button
{
if (strQue == "Y") {var strMe = prompt('Enter the word Places, Things, Hobbies, Color, or Misc to learn more about me','');
} 
else {
}
//-------------------------minor answer and category prompt ^
if (strMe == "Places" || strMe == "places") {
	alert(Places);
}
else if (strMe == "Things" || strMe == "things") {
	alert(Things);
}		
else if (strMe == "Hobbies" || strMe == "hobbies") {
	alert(Hobby);
}		
else if (strMe == "Color" || strMe == "color") {
	alert(Color);
}		
else if (strMe == "Misc" || strMe == "misc") {
	alert(misc);
}
else {
}		
//-------------------------categories ^

}
//-------------------------END FUNCTION
document.write(",\r\Have a great day!");
document.write("\r\n:)")
// -->
</script>
</head>
<body>
<FONT FACE = "Arial">
<form>
<input type="button" 
onclick="myfunction()" 
value="Tell me more...">
</form>

<p>Press the button to find out a little bit about me~ <br>
(The button doesn't work when you say "No" - hehe :P)</p>
</body>
</html>
