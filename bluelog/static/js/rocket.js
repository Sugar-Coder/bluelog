jQuery(document).ready(function() {
            jQuery(window).scroll(function () {
                var scrolldist = jQuery('body').scrollTop()+jQuery('html').scrollTop();
                if (scrolldist > 100) {
                    jQuery("#rocket").css({
                        opacity: '1',
                    })
                    jQuery('#rocket').show("1000");
                } else {
                    jQuery('#rocket').fadeOut("slow");
                }
            });

            jQuery('#rocket').click(function () {
                jQuery("body, html").animate({
                    scrollTop: 0
                }, 500);
                jQuery("#rocket").animate({
                    bottom: '150px',
                    opacity: '0',
                }, 500, function () {
                    jQuery("#rocket").css({
                        bottom: '50px',
                    });
                });
            });
        })