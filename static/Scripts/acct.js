/*************************************** 操作部分 START ******************************************************************************/

$(function() {

/******************************************加载datagrid资金账户列表*********************************************/
    $('#acct_table').datagrid({
        title: '>>>资金账户列表',
        loadFilter: pagerFilter,
        url: '/acct_json/',
        width: '100%',
        height: $(window).height() - 31,
        border: true,
        fitColumns: true,
        striped:true,
        singleSelect: true,
        pagination: true,
        idField: 'id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'id',title: '序号',width: 35},
            {field: 'trdacct',title: '资金账户号',width: 120,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'acc_name',title: '账户名称',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'bid',title: '经纪商',width: 200,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'pid',title: '所属产品',width: 200,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'equity',title: '客户权益',width: 150,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'margin_locked',title: '保证金占用',width: 150,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'fund_avaril',title: '可用资金',width: 150,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'risk_degree',title: '风险度',width: 200,editor: { type: 'validatebox', options: { required: true,}}}
        ]],
    });
/**************************************END******************************************************************/


/************************************点击添加资金账户*******************************************************/
    $('#acct_add').bind('click', function() {
        $('#acct').dialog({
            closed: false,
            title: '新增资金账户',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
        $('input[name="trdacct"]').prev().prop('disabled', false)
    });
/**************************************END******************************************************************/


/**************************************出入金代码******************************************************/
    $('#fund_change_btn').bind('click', function() {
        $('#fund_change').dialog({
            closed: false,
            title: '出入金',
            cache: false
        });
    });
/**************************************END******************************************************************/


/***********************************点击修改资产账户信息***************************************************/
    $('#acct_edit').bind('click', function() {
        var row_select = $('#acct_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#acct').dialog({
                    closed: false,
                    title: '编辑资产账户信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $('input[name="trdacct"]').prev().prop('disabled', true)
                $('#add').hide()
                $('#modify').show()
            }
    } else {
        $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    });
/**************************************END******************************************************************/


/****************************************点击删除产品*******************************************************/
    $('#acct_delete').bind('click', function() {
        var trdaccts = "";
        var row_select = $('#acct_table').datagrid('getSelections'); //返回的是被选中行的对象
        console.log(row_select)
        for (var i = 0; i < row_select.length; i++) {
            trdaccts += '#' + row_select[i].trdacct;
        }
        if (trdaccts == "") {
            $.messager.alert('警告', '请先选中需要删除的资金账户！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此资金账户吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/acct_del/",
                        data: {
                            "delinfo": trdaccts
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('message' + msg.accmsg + 'info');
                                $('#acct_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#acct_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/**************************************END******************************************************************/


});
/****************************** 操作部分 END *********************************************************************************/



/********************************** 函数部分 START ****************************************************************************/


/********************************* 新增资金账户函数 ******************************************/
function acctinfoadd() {
    if ($("input[name='trdacct']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='trdacct']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/acct_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/*********************************** END *****************************************************/


/********************************* 修改资金账户函数 ******************************************/
function acctinfomod() {
    if ($("input[name='trdacct']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='trdacct']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/acct_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/*********************************** END *****************************************************/


/******************************** 出入金函数 *************************************************/
function fund_change() {
    if ($("input[name='fund_change']").val() == "") {
        $.messager.alert('警告', '出入金不可为空!', 'warning');
        $("input[name='fund_change']").focus();
    }
    else if ($("input[name='change_acct']").val() == ""){
        $.messager.alert('警告', '请选取出入金资金账户！!', 'warning');
    }
    else{
        $.ajax({
            type: "POST",
            url: "/acct_fund_change/",
            data: $("#fund_change_fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/acct/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/*********************************** END *****************************************************/


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

/************************************* 函数部分 END ********************************************************************************/