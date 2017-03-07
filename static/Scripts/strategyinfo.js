$(function() {

/*********************************加载datagrid 策略信息列表*****************************************************/
    $('#strategy_table').datagrid({
        title: '>>>策略列表列表',
        url: '/strategyinfo_json/',
        width: '100%',
        border: true,
        fitColumns: true,
        singleSelect: false,
        pagination: false,
        idField: 'id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'id',title: '序号',width: 35},
            {field: 'strategy_id',title: '策略编号',width: 120,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'strategy_name',title: '策略名称',width: 200,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'strategy_product',title: '所属产品',width: 150,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'strategy_desc',title: '策略介绍',width: 200,editor: {type: 'validatebox',options: {required: true,validType: 'strChinese'}}},
            ]],
    });
/**************************************END******************************************************************/



/**************************************添加用户************************************************************/
    $('#product_add').bind('click', function() {
        $('#product').dialog({
            closed: false,
            title: '>>>新增产品',
            cache: false
        });
        $('#fm').form('clear');
    });

    function strategyinfoadd() {
        if ($("input[name='sid']").val() == "") {
            $.messager.alert('警告', '输入内容不可为空!', 'warning');
            $("input[name='sid']").focus();
        } else {
            console.log($("#fm").serialize())
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
/**************************************END******************************************************************/


/************************************* 修改用户 *********************************************************/
    $('#product_edit').bind('click', function() {
        var row_select = $('#product_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#product').dialog({
                    closed: false,
                    title: '>>>编辑服务器',
                    cache: false
                });
                $('#fm').form("load", row_select);
            }
        } else {
            $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    });

    function strategyinfomod() {
        if ($("input[name='sid']").val() == "") {
            $.messager.alert('警告', '输入内容不可为空!', 'warning');
            $("input[name='sid']").focus();
        } else {
            console.log($("#fm").serialize())
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
/**************************************END******************************************************************/


/************************************** 删除产品 ************************************************************/
    $('#product_delete').bind('click', function() {
        var ids = "";
        var product_nums = "";
        var row_select = $('#product_table').datagrid('getSelections'); //返回的是被选中行的对象
        console.log(row_select)
        for (var i = 0; i < row_select.length; i++) {
            ids += '#' + row_select[i].id_db;
            product_nums += ' [' + row_select[i].product_num + '] ';
        }
        if (ids == "") {
            $.messager.alert('警告', '请先选中需要删除的产品！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此产品吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/productinfo_del/",
                        data: {
                            "delinfo": ids
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('产品删除成功');
                                $('#product_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#product_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/**************************************END******************************************************************/

});
