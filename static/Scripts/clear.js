/*************************************** 操作部分 START ******************************************************************************/

$(function() {
/****************************** 加载datagrid GW信息列表 *********************************************/
    $('#gateway_table').datagrid({
        title: '>>>GW列表',
        loadFilter: pagerFilter,
        url: '/gatewayinfo_json/',
        width: '100%',
        height: $(window).height() - 31,
        border: true,
        fitColumns: true,
        singleSelect: true,
        pagination: false,
        idField: 'id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'id',title: '序号',width: 35},
            {field: 'gw_id',title: 'GW编号',width: 35},
            {field: 'gw_name',title: 'GW名称',width: 80},
            {field: 'gw_cfg',title: '配置名',width: 80,},
            {field: 'port',title: '端口',width: 35,},
            {field: 'gw_srv',title: '所属主机',width: 80,},
            {field: 'cl_stat',title: '清算状态',width: 30,},
            {field: 'desc',title: '备注',width: 100,},
            {title: '操作',field: 'opt',width: 100,align: 'center',
                formatter: function(value, row, index) {
                    var str = '<a name="clear-btn"  href="javascript:update();"  title="清算">清算</a> | <a name="clearbk-btn"  href="javascript:update();"  title="回退">回退</a>';
                    return str;
                }
            }
                ]],
        onLoadSuccess:function(data){
            $("a[name='clear-btn']").linkbutton({text:'清算',plain:true,iconCls:'icon-reload'});
            $("a[name='clearbk-btn']").linkbutton({text:'回退',plain:true,iconCls:'icon-undo'});
        }, 
    });
/************************************* END ************************************************************/


/*********************************** 点击弹出新增gw界面 ***********************************************/
    $('#gateway_add').bind('click',function () {
        $('#gateway').dialog({
            closed: false,
            title: '>>>新增GW',
            cache: false,
        });
        $('#fm').form('clear');
        $('#modify').hide();
        $('#add').show();
    });
/************************************* END ************************************************************/


/*********************************** 点击弹出修改gw信息界面 *******************************************/
    $('#gateway_edit').bind('click', function() {
        var row_select = $('#gateway_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#gateway').dialog({
                    closed: false,
                    title: '>>>编辑GW信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $("input[name='gw_id']").prev().prop('disabled', true)
                $('#modify').show();
                $('#add').hide();
            }
        } else {
            $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    });
/************************************* END ************************************************************/


/*********************************** 点击删除gw ******************************************************/
    $('#gateway_delete').bind('click', function() {
        var gw_ids = "";
        var row_select = $('#gateway_table').datagrid('getSelections'); //返回的是被选中行的对象
        console.log(row_select)
        for (var i = 0; i < row_select.length; i++) {
            gw_ids += '#' + row_select[i].gw_id;
        }
        if (gw_ids == "") {
            $.messager.alert('警告', '请先选中需要删除的GW！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此GW吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/gatewayinfo_del/",
                        data: {
                            "delinfo": gw_ids
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('GW删除成功' + msg.accmsg, 'info');
                                $('#gateway_table').datagrid('reload', {});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#gateway_table').datagrid('reload', {});
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
function gatewayinfo_add() {
    if ($("input[name='sid']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='sid']").focus();
    } else {
        console.log($("#fm").serialize())
        $.ajax({
            type: "GET",
            url: "/gatewayinfo_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/gatewayinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        })
    }
}
/************************************** END ***************************************************************/


/************************************ 修改GW函数 ********************************************************/
function gatewayinfo_mod() {
    if ($("input[name='sid']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='sid']").focus();
    } else {
        console.log($("#fm").serialize())
        $.ajax({
            type: "GET",
            url: "/gatewayinfo_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/gatewayinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
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