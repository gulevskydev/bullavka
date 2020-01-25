

$(document).ready(function() {


  $('.burger, .overlay').click(function(){
    $('.burger').toggleClass('clicked');
    $('.overlay').toggleClass('show');
    $('nav').toggleClass('show');
    $('body').toggleClass('overflow');
  });

	$('.rslides').slick({

		 dots: true
		,autoplay: true
		,infinite: true
		,speed: 500
		,fade: true
		,cssEase: 'linear'

	});



});
$(document).ready(function() {
  $(".textBoxAccordionEl:not(.fixed) .textBoxAccordionElTitle").click(function() {
      $(this).closest(".textBoxAccordionEl").toggleClass("open")
  });
});

$(document).ready(function(){
	$('.collapsible').collapsible({
		accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
	});
	function DropDown(el) {
		this.dd = el;
		this.placeholder = this.dd.children('span');
		this.opts = this.dd.find('ul.dropdown > li');
		this.val = '';
		this.index = -1;
		this.initEvents();
		}
		DropDown.prototype = {
		initEvents : function() {
		var obj = this;

		obj.dd.on('click', function(event){
		$(this).toggleClass('active');
		return false;
		});

		obj.opts.on('click',function(){
		var opt = $(this);
		obj.val = opt.text();
		obj.index = opt.index();
		obj.placeholder.text('Gender: ' + obj.val);
		});
		},
		getValue : function() {
		return this.val;
		},
		getIndex : function() {
		return this.index;
		}
		}
});

$(document).ready(function() {

  $('input[name="dropp"]').on("change", function(e){
    var value = $(this).val();
    $('.js-value').text(value);
  });

// Keyboard events---------------------

  $('.dropp-header').keyup(function(){
    $(this).addClass('focused');
    $('.dropp-body').addClass('open');
    $('input[name="dropp"]:first').focus();
  });

  $('input[name="dropp"]').keyup(function(e){
    if(e.which == 13 || e.which == 32 || e.which == 9){// on enter, space or tab key press
      $('.dropp-header').removeClass('focused');
      $('.dropp-body').removeClass('open');
    }
  });

// End Keyboard events------------------

});
var x, i, j, selElmnt, a, b, c;
/*look for any elements with the class "custom-select":*/
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  /*for each element, create a new DIV that will act as the selected item:*/
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /*for each element, create a new DIV that will contain the option list:*/
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < selElmnt.length; j++) {
    /*for each option in the original select element,
    create a new DIV that will act as an option item:*/
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /*when an item is clicked, update the original select box,
        and the selected item:*/
        var y, i, k, s, h;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        h = this.parentNode.previousSibling;
        for (i = 0; i < s.length; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            for (k = 0; k < y.length; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }
        h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
      /*when the select box is clicked, close any other select boxes,
      and open/close the current select box:*/
      e.stopPropagation();
      closeAllSelect(this);
      this.nextSibling.classList.toggle("select-hide");
      this.classList.toggle("select-arrow-active");
    });
}
function closeAllSelect(elmnt) {
  /*a function that will close all select boxes in the document,
  except the current select box:*/
  var x, y, i, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  for (i = 0; i < y.length; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < x.length; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

document.addEventListener("click", closeAllSelect);







var rect = $('#container')[0].getBoundingClientRect();
var mouse = {x: 0, y: 0, moved: false};

$("#container").mousemove(function(e) {
  mouse.moved = true;
  mouse.x = e.clientX - rect.left;
  mouse.y = e.clientY - rect.top;
});

// Ticker event will be called on every frame
TweenLite.ticker.addEventListener('tick', function(){
  if (mouse.moved){
    parallaxIt(".slide", -100);
    parallaxIt(".bg-cloud", -30);
  }
  mouse.moved = false;
});

function parallaxIt(target, movement) {
  TweenMax.to(target, 0.3, {
    x: (mouse.x - rect.width / 2) / rect.width * movement,
    y: (mouse.y - rect.height / 2) / rect.height * movement
  });
}

$(window).on('resize scroll', function(){
  rect = $('#container')[0].getBoundingClientRect();
})
$("ul").on("click", ".init", function() {
  $(this).closest("ul").children('li:not(.init)').toggle();
});

var allOptions = $("ul").children('li:not(.init)');
$("ul").on("click", "li:not(.init)", function() {
  allOptions.removeClass('selected');
  $(this).addClass('selected');
  $("ul").children('.init').html($(this).html());
  allOptions.toggle();
});
