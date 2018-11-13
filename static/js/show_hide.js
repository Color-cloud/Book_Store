$(function () {

    $("#xiaoshuo_zhangjie>ul").mouseover(function () {
        $('#xiaoshuo_taolunqu_init').hide();
        $('#xiaoshuo_zhangjie_init').show();
    });
    $("#xiaoshuo_taolunqu>ul").mouseover(function () {
        $('#xiaoshuo_taolunqu_init').show();
        $('#xiaoshuo_zhangjie_init').hide();
    });


});

