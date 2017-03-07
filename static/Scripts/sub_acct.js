/******************************************* 操作部分 START ************************************************************************/
$(function() {

/**************************** 加载datagrid 总账号信息列表 ******************************************************/
    $('#sub_acct_table').datagrid({
        title: '>>>子账号列表',
        url: '/sub_acct_json/',
        width: '100%',
        border: true,
        fitColumns: true,
        striped: true,
        singleSelect: true,
        pagination: false,
        idField: 'id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'id',title: '序号',width: 35},
            {field: 'acc_num',title: '账户号',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'acc_name',title: '账户名',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'master_acct',title: '关联总账号',width: 120,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'equity',title: '客户权益',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'buy_margin',title: '多仓保证金',width: 200,editor: {type: 'validatebox',options: {required: true,}}},
            {field: 'sell_margin',title: '空仓保证金',width: 200,editor: {type: 'validatebox',options: {required: true,}}},
            {field: 'margin_locked',title: '保证金占用',width: 150,editor: {type: 'validatebox',options: {required: true}}},
             {field: 'fund_avaril',title: '可用资金',width: 150,editor: {type: 'validatebox',options: {required: true}}}
            ]],
    });
/************************************** END ******************************************************************/


/*********************************** 点击弹出出入金界面 ******************************************************/
    $('#fund_change_btn').bind('click', function() {
        $('#fund_change').dialog({
            closed: false,
            title: '出入金',
            cache: false
        });
    });
/************************************** END ******************************************************************/


/*********************************** 点击修改子账号信息 *****************************************************/
    $('#sub_acct_edit').bind('click', function() {
        var row_select = $('#sub_acct_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#sub_acct').dialog({
                    closed: false,
                    title: '编辑子账号信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $('input[name="acc_num"]').prev().prop('disabled', true)
                $('#add').hide()
                $('#modify').show()
            }
        } else {
            $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    });
/************************************** END ******************************************************************/


/************************************ 点击删除子账号 ********************************************************/
    $('#sub_acct_delete').bind('click', function() {
        var acc_nums = "";
        var row_select = $('#sub_acct_table').datagrid('getSelections'); //返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            acc_nums += '#' + row_select[i].acc_num;
        }
        if (acc_nums == "") {
            $.messager.alert('警告', '请先选中需要删除的子账号！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此子账号吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/sub_acct_del/",
                        data: {
                            "delinfo": acc_nums
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('message' + msg.accmsg, 'info');
                                $('#sub_acct_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#sub_acct_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/************************************** END ******************************************************************/

});
/************************************** 操作部分 END ***********************************************************************************/









/************************************ 函数部分 START ***********************************************************************************/

/************************************ 新增子账号函数 *****************************************************/
function subacctinfoadd() {
    if ($("input[name='acc_num']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='acc_num']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/sub_acct_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/sub_acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************** 修改子账号函数 *****************************************************/
function subacctinfomod() {
    if ($("input[name='acc_num']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='acc_num']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/sub_acct_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/sub_acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/********************************** 出入金函数 ************************************************************/
function fund_change() {
    if ($("input[name='fund_change']").val() == "") {
        $.messager.alert('警告', '出入金不可为空!', 'warning');
        $("input[name='fund_change']").focus();
    } else if ($("input[name='change_acct']").val() == "") {
        $.messager.alert('警告', '请选取出入金总账号！!', 'warning');
    } else {
        $.ajax({
            type: "POST",
            url: "/sub_acct_fund_change/",
            data: $("#fund_change_fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/sub_acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/*************************************** END ******************************************************************/

/************************************** 函数部分 END *******************************************************************************/
