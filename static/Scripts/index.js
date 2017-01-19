$(function () {
    //日历
    $("#datepicker").datepicker();
    //左边菜单
    $('.one').click(function () {
        $('.one').removeClass('one-hover');
        $(this).addClass('one-hover');
//        $(this).children(".kid").get(0).toggle();

    });
    var Accordion = function(el, multiple) {
        this.el = el || {};
        this.multiple = multiple || false;

        // Variables privadas
        var links = this.el.find('.link');
        // Evento
        links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
    }

    Accordion.prototype.dropdown = function(e) {
        var $el = e.data.el;
            $this = $(this),
            $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
        };
    }   

    var accordion = new Accordion($('#accordion'), false);


    //影藏菜单
    var l = $('.left_c');
    var r = $('.right_c');
    var c = $('.Conframe');
    $('.nav-tip').click(function () {
        if (l.css('left') == '8px') {
            l.animate({
                left: -300
            }, 500);
            r.animate({
                left: 21
            }, 500);
            c.animate({
                left: 29
            }, 500);
            $(this).animate({
                "background-position-x": "-12"
            }, 300);
        } else {
            l.animate({
                left: 8
            }, 500);
            r.animate({
                left: 260
            }, 500);
            c.animate({
                left: 268
            }, 500);
            $(this).animate({
                "background-position-x": "0"
            }, 300);
        };
    })
    //横向菜单
    $('.top-menu-nav li').click(function () {
        $('.kidc').hide();
        $(this).find('.kidc').show();
        
    })
    $('.kidc').bind('mouseleave', function () {
        $('.kidc').hide();
    }) 

})
