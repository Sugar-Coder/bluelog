$(document).ready(function() {
            $(window).scroll(function () {
                var scrolldist = $('body').scrollTop()+$('html').scrollTop();
                if (scrolldist > 100) {
                    $("#rocket").css({
                        opacity: '1',
                    })
                    $('#rocket').show("1000");
                } else {
                    $('#rocket').fadeOut("slow");
                }
            });

            $('#rocket').click(function () {
                $("body, html").animate({
                    scrollTop: 0
                }, 500);
                $("#rocket").animate({
                    bottom: '100px',
                    opacity: '0',
                }, 400, function () {
                    $("#rocket").css({
                        bottom: '0px',
                    });
                });
            });
        })