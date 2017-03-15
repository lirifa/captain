/************************************************************************************************************
*
*                                      操 作
*
************************************************************************************************************/
$(function() {

/**************************** 加载datagrid 产品信息列表 ******************************************************/
    $('#product_table').datagrid({
        title: '>>>产品列表',
        loadFilter: pagerFilter,
        url: '/productinfo_json/',
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
            {field: 'pid',title: '产品编号',width: 120,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'pname',title: '产品名称',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'admin',title: '产品管理人',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'desc',title: '产品介绍',width: 200,editor: {type: 'validatebox',options: {required: true}}}
            ]],
    });
/************************************** END ****************************************************************/


/********************************* 新增产品 ****************************************************************/
    $('#product_add').bind('click', function() {
        $('#product').dialog({
            closed: false,
            title: '新增产品',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
        $("input[name='pid']").prev().prop("disabled",false)
    });
/************************************** END ****************************************************************/


/********************************** 修改产品信息 ***********************************************************/
    $('#product_edit').bind('click', function() {
        var row_select = $('#product_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#product').dialog({
                    closed: false,
                    title: '编辑产品信息',
                    cache: false
                });
                $('#fm').form("load", row_select)
                $("input[name='pid']").prev().prop("disabled",true)
                $('#add').hide()
                $('#modify').show()
            }
        } else {
            $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    });
/************************************** END ****************************************************************/


/************************************* 删除产品 ************************************************************/
    $('#product_delete').bind('click', function() {
        var ids = "";
        var pids = "";
        var row_select = $('#product_table').datagrid('getSelections'); //返回的是被选中行的对象
        console.log(row_select)
        for (var i = 0; i < row_select.length; i++) {
            ids += '#' + row_select[i].pid;
            pids += ' [' + row_select[i].pid + '] ';
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
                                $.messager.alert('message'+msg.accmsg,'info');
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
/************************************** END ****************************************************************/

});

/***********************************************************************************************************
*
*                                     函 数
*
***********************************************************************************************************/
/************************************ 搜索函数 *************************************************************/
function doSearch(value) {
    if (value) {
        alert('You input: ' + value);
    } else {
        alert('Please input ...');
    }
}
/************************************** END ****************************************************************/


/************************************ 新增产品函数 *****************************************************/
function productinfoadd() {
    if ($("input[name='pid']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='pid']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/productinfo_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/productinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ****************************************************************/


/************************************ 修改产品信息函数 *****************************************************/
function productinfomod() {
    if ($("input[name='pid']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='pid']").focus();
    } else{
        $.ajax({
            type: "GET",
            url: "/productinfo_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/productinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
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
