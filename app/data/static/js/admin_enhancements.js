django.jQuery(document).ready(function() {
    django.jQuery("textarea").each(function(n, obj) {
        CKEDITOR.replace(obj.id)
        //fck.BasePath = "/static/js/fckeditor/"
        //fck.ReplaceTextarea()
    });
});
