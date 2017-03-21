/******************************************* 操作部分 START *************************************************************************/
$(function() {
    
/**************************** 加载datagrid 总账号信息列表 ******************************************************/
    $('#master_acct_table').datagrid({
        title: '>>>总账号列表',
        loadFilter: pagerFilter,
        url: '/master_acct_json/',
        width: '100%',
        height: $(window).height() - 31,
        border: true,
        fitColumns: true,
        striped: true,
        singleSelect: true,
        pagination: true,
        idField: 'id',
        pageSize: 25,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'id',title: '序号',width: 35},
            {field: 'acc_num',title: '总账号',width: 120,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'acc_name',title: '账号名',width: 120,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'trdacct',title: '关联资金账户',width: 120,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'equity',title: '客户权益',width: 150,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'buy_margin',title: '多仓保证金',width: 200,editor: { type: 'validatebox', options: { required: true}}},
            {field: 'sell_margin',title: '空仓保证金',width: 200,editor: {type: 'validatebox', options: { required: true}}},
            {field: 'margin_locked',title: '保证金占用',width: 150,editor: {type: 'validatebox', options: {required: true}}},
            {field: 'fund_avaril',title: '可用资金',width: 150,editor: {type: 'validatebox',options: { required: true}}},
            ]],
    });
/************************************** END ******************************************************************/


/********************************* 添加总账号 **************************************************************/
    $('#master_acct_add').bind('click', function() {
        $('#master_acct').dialog({
            closed: false,
            title: '新增总账号',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
    });
/************************************** END ******************************************************************/


/*********************************** 出入金 *****************************************************************/
    $('#fund_change_btn').bind('click', function() {
        $('#fund_change').dialog({
            closed: false,
            title: '出入金',
            cache: false
        });
    });
/************************************** END *****************************************************************/


/********************************* 修改总账号信息 **********************************************************/
    $('#master_acct_edit').bind('click', function() {
        var row_select = $('#master_acct_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#master_acct').dialog({
                    closed: false,
                    title: '编辑总账号信息',
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
/************************************** END *****************************************************************/


/************************************点击删除总账号*********************************************************/
    $('#master_acct_delete').bind('click', function() {
        var acc_nums = "";
        var row_select = $('#master_acct_table').datagrid('getSelections'); //返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            acc_nums += '#' + row_select[i].acc_num;
        }
        if (acc_nums == "") {
            $.messager.alert('警告', '请先选中需要删除的资金账户！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此资金账户吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/master_acct_del/",
                        data: {
                            "delinfo": acc_nums
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('message' + msg.accmsg, 'info');
                                $('#master_acct_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#master_acct_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/************************************** END *****************************************************************/

});
/************************************* 操作部分 END ********************************************************************************/







/************************************ 函部分数 START ******************************************************************************/

/************************************ 新增总账号函数 *****************************************************/
function masteracctinfoadd() {
    if ($("input[name='acc_num']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='acc_num']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/master_acct_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/master_acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ****************************************************************/


/************************************ 修改总账号函数 *****************************************************/
function masteracctinfomod() {
    if ($("input[name='acc_num']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='acc_num']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/master_acct_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/master_acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END **************************************************************/


/************************************ 出入金函数 ********************************************************/
function fund_change() {
    if ($("input[name='fund_change']").val() == "") {
        $.messager.alert('警告', '出入金不可为空!', 'warning');
        $("input[name='fund_change']").focus();
    } else if ($("input[name='change_acct']").val() == "") {
        $.messager.alert('警告', '请选取出入金总账号！!', 'warning');
    } else {
        $.ajax({
            type: "POST",
            url: "/master_acct_fund_change/",
            data: $("#fund_change_fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/master_acct/";
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

/******************************* 分页显示数据函数 ***************************************************/
function pagerFilter(data) {
        if (typeof data.length == 'number' && typeof data.splice == 'function') { // 判断数据是否是数组
            data = {
                total: data.length,
                rows: data
            }
        }
        var dg = $(this);
        var opts = dg.datagrid('options');
        var pager = dg.datagrid('getPager');
        pager.pagination({
            onSelectPage: function(pageNum, pageSize) {
                opts.pageNumber = pageNum;
                opts.pageSize = pageSize;
                pager.pagination('refresh', {
                    pageNumber: pageNum,
                    pageSize: pageSize
                });
                dg.datagrid('loadData', data);
            }
        });
        if (!data.originalRows) {
            data.originalRows = (data.rows);
        }
        var start = (opts.pageNumber - 1) * parseInt(opts.pageSize);
        var end = start + parseInt(opts.pageSize);
        data.rows = (data.originalRows.slice(start, end));
        return data;
    }
/***************************************** END ****************************************************/


/************************************** 函数部分END ***********************************************************************************/