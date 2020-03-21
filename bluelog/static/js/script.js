jQuery(function () {
    $.noConflict();  // 让3.4.1放弃$使用权
    function render_time() {
        return moment($(this).data('timestamp')).format('lll')
    }
    $('[data-toggle="tooltip"]').tooltip(
        {title: render_time}
    );
});
