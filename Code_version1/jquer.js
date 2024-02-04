// this method test firt if the jQuery library is ready and then executes the code
// $(document).ready(function(){
//     jQuery('h1').css('color','red');
// })
// adding class to a header
$('h1').addClass("big-class");
// change text of document
$('h1').text("Liza");
//change the inner html of document
$('h1').html("<em>Liza</em>");
//change and display the attribute of tags
$('a').attr("href","www.yahoo.com");
//adding event listner 
$('h1').click(function(){
   $('h1').css('color','purple');
})
//add event listner to the set of codes
// for(var i=0;i<5;i++)
// {
// document.querySelectorAll('button')[i].addEventListener("click",function(){
//     document.querySelector('h1').style.color="purple";
// })
// }
$('button').click(function(){
    $('h1').css('color','red');
})
//detect a keypress
// $(document).keypress(function(event){
//     var k=(event.key);
//     $('h1').text(k);
// })
// to select any eventlistener we can use "on" in jQuery after that we have to write any of the event suppoorted
$('h1').on("mouseover",function(){
    $('h1').css("color",'yellow');
})
// after and before function
$('h1').before('<button>Ritwik</button>');
//prepend and append
$('h1').append('<button>Ritwik</button');
// hide the selected container
//$('h1').hide();
//toggle the button hide and show
// $('button').click(function(){
//     $('h1').toggle();
// })
//fadeOut  and fadeIn the document
//fadeToggle
$('button').click(function(){
    $('h1').slideToggle();
})
//slideUp and slideDown
//slideToggle
//customize the animations h1.animate()
//we have to stick to things which have numeric value
//$('h1').animate({opacity:0.3});
$('button').click(function(){
    $('h1').slideUp().slideDown().animate({opacity:0.3});
})