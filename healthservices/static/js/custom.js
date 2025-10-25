  (function ($) {
  
  "use strict";

    // COUNTER NUMBERS
    jQuery('.counter-thumb').appear(function() {
      jQuery('.counter-number').countTo();
    });

    // BACKSTRETCH SLIDESHOW
    $('.hero-section').backstretch([
      "{% static 'images/services/ambulance1.png' %}",
      "{% static 'images/services/ambulance4.png' %}",
      "{% static 'images/services/ambulance2.png' %}"
    ],  {duration: 2000, fade: 750});
    
    // CUSTOM LINK
    $('.smoothscroll').click(function(){
      var el = $(this).attr('href');
      var elWrapped = $(el);
  
      scrollToDiv(elWrapped);
      return false;
  
      function scrollToDiv(element){
        var offset = element.offset();
        var offsetTop = offset.top;
        var totalScroll = offsetTop-navheight;
  
        $('body,html').animate({
        scrollTop: totalScroll
        }, 300);
      }
    });
    
  })(window.jQuery);


// Plugin initializations (backstretch.js, countTo.js, etc.) must be loaded BEFORE this.

(function ($) {
  "use strict";

  // COUNTER
  jQuery('.counter-thumb').appear(function () {
    jQuery('.counter-number').countTo();
  });


})(jQuery);
