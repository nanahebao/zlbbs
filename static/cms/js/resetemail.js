$(function () {
    $("#captcha-btn").click(function (event) {
        event.preventDefault();
        var email=$("input[name='email']").val();
        console.log(email)
        if (!email){
            zlalert.alertInfoToast("请输入邮箱！");
            return;
        }
        zlajax.get({
            'url':'http://127.0.0.1:5000/cms/email_captcha/',
            'data':{
                'email':email,

            },
            'success':function (data) {
                if (data['code']==200){
                    zlalert.alertSuccessToast("邮件发送成功，请注意查收！");
                }else {
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail':function (error) {

                    zlalert.alertNetworkError();
            }
        });
        
    });
    
});

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        var emailE=$('input[name="email"]');
        var captchaE=$('input[name="captcha"]');

        var email=emailE.val();
        var captcha=captchaE.val();

        zlajax.post({
            'url':'/cms/resetemail/',
            'data':{
                'email':email,
                'captcha':captcha
            },
            'success':function (data) {

                if (data['code']==200) {
                    zlalert.alertSuccessToast("恭喜邮箱修改成功！");
                }else {
                    zlalert.alertInfo(data['message']);
                }
            },
            'fail':function (error) {
                zlalert.alertNetworkError();
                
            }

        });

    });
    
});