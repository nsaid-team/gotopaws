$("#search").on("keyup", function() {
    var key = this.value;
    $(".tosearch").each(function() {
       var $this = $(this);
       $this.toggle($(this).text().indexOf(key) >= 0);
    });
});