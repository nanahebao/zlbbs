var zlalert = {
	'alertError': function (msg) {
		swal('提示',msg,'error');
	},
	'alertInfo':function(msg){
		swal('提示',msg,'warning');
	},
	/*
		功能：可以自定义标题的信息提示
		参数：
		 	- msg:提示的内容（可选）
	*/
	'alertInfoWithTitle':function(title,msg){
		swal(title,msg);
	},
	/*
		功能：带有标题的成功提示
		参数：
			- title:提示框的标题（必须）
			- msg:提示的内容（必须）
	*/
	'alertSuccessWithTitle':function(title,msg){
		swal(title,msg,'success');
	},

	'alertConfirm':function(params){
		swal({
			'title':params['title']?params['title']:'提示',
			'showCancelButton':true,
			'showConfirmButton':true,
			'type':params['type']?params['type']:'',
			'confirmButtonText':params['confirmText']?params['confirmText']:'确定',
			'cancelButtonText':params['cancleText']?params['cancleText']:"取消",
			'text':params['msg']?params['msg']:''
		},function(isConfirm){
			if(isConfirm){
				if (params['confirmCallback']){
					params['confirmCallback']();
				}
			}else{
				if (params['cancelCallback']) {
					params['cancelCallback']();
				}
			}

		});
		},
	'alertConfirm':function(params){
		swal({
			'title':params['title']?params['title']:'提示',
			'showCancelButton':true,
			'showConfirmButton':true,
			'type':params['type']?params['type']:'',
			'confirmButtonText':params['confirmText']?params['confirmText']:'确定',
			'cancelButtonText':params['cancelText']?params['cancelText']:"取消",
			'text':params['msg']?params['msg']:''
		},function(isConfirm){
			if(isConfirm){
				if (params['confirmCallback']){
					params['confirmCallback']();
				}
			}else{
				if (params['cancelCallback']) {
					params['cancelCallback']();
				}
			}

		});
		},

	'alertOneInput':function(params){
		swal({
            'title':params['title']?params['title']:'提示',
            'text':params['text']?params['text']:'',
            'type':'input',
            'showCancelButton':true,
            'animation':'slide-from-top',
            'closeOnConfirm':false,
            'showLoaderOnConfirm':true,
            'inputPlaceholder':params['placeholder']?params['placeholder']:'',
            'confirmButtonText':params['confirmText']?params['confirmText']:'确定',
            'cancelButtonText':params['cancelText']?params['cancelText']:'取消',
        },function(inputValue){
           if(inputValue===false) return false;
           if(inputValue===''){
            swal.showInputError('输入框不能为空');
            return false;
           }
           if (params['confirmCallback']){
           	   params['confirmCallback'](inputValue)

           }

        });

		},
	'alertNetworkError':function () {
        this.alertErrorToast('网络错误');
    },
    /*
        功能：信息toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertInfoToast':function (msg) {
        this.alertToast(msg,'info');
    },
    /*
        功能：错误toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertErrorToast':function (msg) {
        this.alertToast(msg,'error');

	},

	'alertSuccessToast':function (msg) {
        if(!msg){msg = '成功！';}
        this.alertToast(msg,'success');
    },


	'alertToast':function (msg,type) {
        swal({
            'title': msg,
            'text': '',
            'type': type,
            'showCancelButton': false,
            'showConfirmButton': false,
            'timer': 1000,
        });

	},

	'close': function () {
        swal.close();
    }


	}
