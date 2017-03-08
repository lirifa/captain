/******************************************* 操作部分 START *************************************************************************/

$(function() {

/********************************* 加载datagrid 策略信息列表 **********************************************/
    $('#strategy_table').datagrid({
        title: '>>>策略列表',
        url: '/strategyinfo_json/',
        width: '100%',
        border: true,
        fitColumns: true,
        striped:true,
        singleSelect: true,
        pagination: false,
        idField: 'id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'id',title: '序号',width: 35},
            {field: 'sid',title: '策略编号',width: 120,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'sname',title: '策略名称',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'scfg',title: '对应配置名',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'port',title: '策略端口',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'ssrv',title: '所属主机',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'product',title: '所属产品',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'master_acc',title: '总账号',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'sub_acc',title: '子账号',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'desc',title: '策略介绍',width: 200,editor: {type: 'validatebox',options: {required: true,}}}
        ]],
    });
/************************************** END ***************************************************************/



/************************************** 新增策略 **********************************************************/
    $('#strategy_add').bind('click', function() {
        $('#strategy').dialog({
            closed: false,
            title: '新增策略',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
    });
/************************************** END **************************************************************/


/********************************* 点击修改策略 *********************************************************/
    $('#strategy_edit').bind('click', function() {
        var row_select = $('#strategy_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#strategy').dialog({
                    closed: false,
                    title: '编辑策略信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $("input[name='sid']").prev().prop('disabled', true)
                $('#modify').show();
                $('#add').hide();
            }
        } else {
            $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    });
/*************************************** END ***************************************************************/


/*********************************** 点击删除策略 **********************************************************/
    $('#strategy_delete').bind('click', function() {
        var sids = "";
        var row_select = $('#strategy_table').datagrid('getSelections'); //返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            sids += '#' + row_select[i].sid;
        }
        if (sids == "") {
            $.messager.alert('警告', '请先选中需要删除的策略！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此策略吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/strategyinfo_del/",
                        data: {
                            "delinfo": sids
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('策略删除成功' + msg.accmsg, 'info');
                                $('#strategy_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#strategy_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/************************************* END ******************************************************************/


/********************** 对validatebox控件正则表达式验证数据有效性扩展 **************************************/
    $.extend($.fn.validatebox.defaults.rules, {
        strip: {
            validator: function(value) {
                var re = /^[\d+\.\d+\.\d+\.\d+]/;
                if (re.test(value))
                    return false;
                else
                if (RegExp.$1 < 256 && RegExp.$2 < 256 && RegExp.$3 < 256 && RegExp.$4 < 256)
                    return true;
                else
                    return false;
            },
            message: '只能输入IP格式！'
        },
        strChinese: {
            validator: function(value) {
                var re = /[^\u4e00-\u9fa5]/;
                if (re.test(value))
                    return false;
                else
                    return true;
            },
            message: '只能输入中文！'
        },
        strEngNum: {
            validator: function(value) {
                var re = /[^\w+$]/;
                if (re.test(value))
                    return false;
                else
                    return true;
            },
            message: '只能输入英文、数字或下划线！'
        }
    });
/**************************************** END ************************************************************/

});
/************************************* 操作部分 END *******************************************************************************/






/************************************ 函部分数 START ******************************************************************************/

/************************************ 新增策略函数 ********************************************************/
function strategyinfoadd() {
    if ($("input[name='sid']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='sid']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/strategyinfo_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/strategyinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************ 修改策略函数 ********************************************************/
function strategyinfomod() {
    if ($("input[name='sid']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='sid']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/strategyinfo_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/strategyinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************** 搜索函数 ***********************************************************/
function doSearch(value){
    if(value){
        alert('You input: ' + value);
    }else{
        alert('Please input ...');
    }
}
/************************************** END ****************************************************************/

/************************************** 函数部分END *******************************************************************************/
