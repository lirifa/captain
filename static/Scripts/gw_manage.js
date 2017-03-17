/*************************************** 操作部分 START ******************************************************************************/

$(function() {
/****************************** 加载datagrid GW信息列表 *********************************************/
    $('#gw_table').datagrid({
        title: '>>>网关列表',
        loadFilter: pagerFilter,
        url: '/gwinfo_json/',
        width: '100%',
        height: $(window).height() - 33,
        border: true,
        fitColumns: true,
        singleSelect: true,
        pagination: true,
        rownumbers:true,
        idField: 'id',
        pageSize: 25,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'gw_id',title: '网关编号',width: 20},
            {field: 'gw_name',title: '网关名称',width: 80},
            {field: 'gw_cfg',title: '对应配置名',width: 80,},
            {field: 'port',title: '端口',width: 35,},
            {field: 'gw_srv',title: '所属主机',width: 80,},
            {field: 'product',title: '所属产品',width: 80,},
            {field: 'desc',title: '备注',width: 100,},
            ]],
    });
/************************************* END ************************************************************/


/*********************************** 点击弹出新增gw界面 ***********************************************/
    $('#gw_add').bind('click',function () {
        $('#gateway').dialog({
            closed: false,
            title: '>>>新增网关',
            cache: false,
        });
        $('#fm').form('clear');
        $('#modify').hide();
        $('#add').show();
        $("input[name='gw_id']").prev().prop('disabled', false);
    });
/************************************* END ************************************************************/


/*********************************** 点击弹出修改gw信息界面 *******************************************/
    $('#gw_edit').bind('click', function() {
        var row_select = $('#gw_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('message', row_select.length, 'warning');
            } else {
                $('#gateway').dialog({
                    closed: false,
                    title: '>>>修改网关信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $("input[name='gw_id']").prev().prop('disabled', true)
                $('#modify').show();
                $('#add').hide();
            }
        } else {
            $.messager.alert('message', '请先选中需要修改行！', 'warning');
        }
    });
/************************************* END ************************************************************/


/*********************************** 点击删除gw ******************************************************/
    $('#gw_delete').bind('click', function() {
        var gw_ids = "";
        var row_select = $('#gw_table').datagrid('getSelections'); //返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            gw_ids += '#' + row_select[i].gw_id;
        }
        if (gw_ids == "") {
            $.messager.alert('message', '请先选中需要删除的网关！', 'warning');
            return false;
        } else {
            $.messager.confirm('message', '您确认想要删除此网关吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "POST",
                        cache: false,
                        url: "/gw_del/",
                        data: {
                            "delinfo": gw_ids
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('message', msg.accmsg, 'info');
                                $('#gw_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('message', msg.errmsg, 'error');
                                $('#gw_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/************************************* END ******************************************************************/

});
/****************************** 操作部分 END *********************************************************************************/





/************************************ 函部分数 START ******************************************************************************/

/************************************ 新增GW函数 ********************************************************/
function gateway_add() {
    if ($("input[name='gw_id']").val() == "") {
        $.messager.alert('message', '输入内容不可为空!', 'warning');
        $("input[name='gw_id']").focus();
    } else {
        console.log($("#fm").serialize())
        $.ajax({
            type: "POST",
            url: "/gw_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message', msg.accmsg, 'info');
                    location.href = "/gw_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        })
    }
}
/************************************** END ***************************************************************/


/************************************ 修改GW函数 ********************************************************/
function gateway_mod() {
    if ($("input[name='gw_id']").val() == "") {
        $.messager.alert('message', '输入内容不可为空!', 'warning');
        $("input[name='gw_id']").focus();
    } else {
        console.log($("#fm").serialize())
        $.ajax({
            type: "POST",
            url: "/gw_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message','网关'+msg.accmsg+'删除成功！', 'info');
                    location.href = "/gw_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        })
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


/************************************** 函数部分END *******************************************************************************/