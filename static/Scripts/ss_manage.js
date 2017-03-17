/******************************************* 操作部分 START *************************************************************************/

$(function() {

/********************************* 加载datagrid 策略信息列表 **********************************************/
    $('#ss_table').datagrid({
        title: '>>>策略列表',
        loadFilter: pagerFilter,
        url: '/ssinfo_json/',
        width: '100%',
        height: $(window).height() - 31,
        border: true,
        fitColumns: true,
        striped:true,
        singleSelect: true,
        pagination: true,
        rownumbers: true,
        idField: 'id',
        pageSize: 25,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'ss_id',title: '策略编号',width: 40,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'ss_name',title: '策略名称',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'ss_cfg',title: '对应配置名',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'port',title: '策略端口',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'ss_srv',title: '所属主机',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'product',title: '所属产品',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'master_acc',title: '总账号',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'sub_acc',title: '子账号',width: 150,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'desc',title: '策略介绍',width: 200,editor: {type: 'validatebox',options: {required: true,}}}
        ]],
    });
/************************************** END ***************************************************************/



/************************************** 新增策略 **********************************************************/
    $('#ss_add').bind('click', function() {
        $('#strategy').dialog({
            closed: false,
            title: '新增策略',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
        $("input[name='ss_id']").prev().prop('disabled', false)
    });
/************************************** END **************************************************************/


/********************************* 点击修改策略 *********************************************************/
    $('#ss_edit').bind('click', function() {
        var row_select = $('#ss_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('message', row_select.length, 'warning');
            } else {
                $('#strategy').dialog({
                    closed: false,
                    title: '编辑策略信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $("input[name='ss_id']").prev().prop('disabled', true)
                $('#modify').show();
                $('#add').hide();
            }
        } else {
            $.messager.alert('message', '请先选中需要修改行！', 'warning');
        }
    });
/*************************************** END ***************************************************************/


/*********************************** 点击删除策略 **********************************************************/
    $('#ss_delete').bind('click', function () {
        strategy_del();
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
function strategy_add() {
    if ($("input[name='ss_id']").val() == "") {
        $.messager.alert('message', '输入内容不可为空!', 'warning');
        $("input[name='ss_id']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/ss_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message', msg.accmsg, 'info');
                    location.href = "/ss_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************ 修改策略函数 ********************************************************/
function strategy_mod(){
    if ($("input[name='ss_id']").val() == "") {
        $.messager.alert('message', '输入内容不可为空!', 'warning');
        $("input[name='ss_id']").focus();
    } else {
        $.ajax({
            type: "POST",
            url: "/ss_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message', msg.accmsg+"策略信息修改成功！", 'info');
                    location.href = "/ss_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************ 删除策略函数 ********************************************************/
function strategy_del(){
    var ss_ids = "";
    var row_select = $('#ss_table').datagrid('getSelections'); //返回的是被选中行的对象
    for (var i = 0; i < row_select.length; i++) {
        ss_ids += '#' + row_select[i].ss_id;
    }
    if (ss_ids == "") {
        $.messager.alert('message', '请先选中需要删除的策略！', 'warning');
        return false;
    } else {
        $.messager.confirm('确认', '您确认想要删除此策略吗？', function(r) {
            if (r) {
                $.ajax({
                    type: "GET",
                    cache: false,
                    url: "/ss_del/",
                    data: {
                        "delinfo": ss_ids
                    },
                    dataType: 'json',
                    success: function(msg) {
                        if (msg.accmsg) {
                            $.messager.alert('message','策略：'+ msg.accmsg + '删除成功！', 'info');
                            $('#ss_table').datagrid('reload', {});
                        } else {
                            $.messager.alert('错误', msg.errmsg);
                            $('#ss_table').datagrid('reload', {});
                        }
                    }
                });
            }
        });
    }
};
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
