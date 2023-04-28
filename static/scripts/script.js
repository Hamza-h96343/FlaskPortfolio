$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        } else {
            $('.navbar').removeClass("sticky");
        }
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    });

    //slide up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
    });

    //toggle menu/navbar script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

    //typing animation script
    var typed = new Typed(".typing", {
        strings: ["Designer", "Engineer", "Developer"],
        typeSpeed: 100,
        backSpeed: 60,
        loop:true
    });

    var typed = new Typed(".typing-2", {
        strings: ["Designer", "Engineer", "Developer"],
        typeSpeed: 100,
        backSpeed: 60,
        loop:true
    });


});

function openProjects(evt, cityName) {
      // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "flex";
  evt.currentTarget.className += " active";
}

var slidePositionHardware = 1;
SlideShowHardware(slidePositionHardware);

// forward/Back controls
function plusSlidesHardware(n) {
  SlideShowHardware(slidePositionHardware += n);
}

//  images controls

function SlideShowHardware(n) {
  var i;
  var slides = document.getElementsByClassName("Containers-Hardware");

  if (n > slides.length) {slidePositionHardware = 1}
  if (n < 1) {slidePositionHardware = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }

  slides[slidePositionHardware-1].style.display = "block";
}

var slidePositionSoftware = 1;
SlideShowSoftware(slidePositionSoftware);

// forward/Back controls
function plusSlidesSoftware(n) {
  SlideShowSoftware(slidePositionSoftware += n);
}

//  images controls

function SlideShowSoftware(n) {
  var i;
  var slides = document.getElementsByClassName("Containers-software");

  if (n > slides.length) {slidePositionSoftware = 1}
  if (n < 1) {slidePositionSoftware = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }

  slides[slidePositionSoftware-1].style.display = "block";
}