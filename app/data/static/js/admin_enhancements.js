$(document).ready(function() {
    $("textarea").each(function(n, obj) {
        fck = new FCKeditor(obj.id) ;
            fck.BasePath = "/media/js/fckeditor/" ;
            fck.ReplaceTextarea() ;
    });
});
