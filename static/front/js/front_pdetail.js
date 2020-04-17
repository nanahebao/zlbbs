$(function () {
    var ue = UE.getEditor("editor", {
        'serverUrl': '/ueitor/upload/',
        toolbars: [
            [
                'undo',
                'redo',
                'bold',
                'italic',
                'source',
                'blockquote',
                'selectall',
                'insertcode',
                'fontfamily', //字体
                'fontsize', //字号
                'simpleupload', //单图上传
                'emotion', //表情

            ]
        ]
    });
    window.ue=ue
});
    
$(function () {
    $("#comment-btn").click(function (event) {
        event.preventDefault();
        var loginTag=$("#login-lag").attr('data-is-login');
        if(!loginTag){
            window.location='/signin/';
        }else {
            var content=window.ue.getContent();
            var post_id=$("#post-content").attr("data-id")
            zlajax.post({
                'url':'/acomment/',
                'data':{
                    'content':content,
                    'post_id':post_id
                },
                'success':function (data) {
                    if (data['code']==200){
                        window.location.reload();
                    }else {
                        zlalert.alertInfo(data['message']);
                    }

                }
            })
        }

    });


});