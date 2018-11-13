$(function () {
    $("#xiaoshuo_taolunqu").mouseover(function () {
        console.log("xiaoshuo_taolunqu 1");
        $('#xiaoshuo_zhangjie_init').hide();
        $(this).find('li').show()
    });
    $("#xiaoshuo_taolunqu>a").mouseleave(function () {
        console.log("xiaoshuo_taolunqu 2");
        $(this).find('li').hide();
    });
});

