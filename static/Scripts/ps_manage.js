/************************************* 操作部分 START ******************************************************************************/

$(function () {
/********************************* 加载datagrid 策略信息列表 **********************************************/
    $('#ps_table').datagrid({
        title: '>>>行情列表',
        loadFilter: pagerFilter,
        url: '/psinfo_json/',
        width: '100%',
        height: $(window).height() * 0.5,
        border: true,
        fitColumns: true,
        striped:true,
        singleSelect: true,
        pagination: true,
        rownumbers: true,
        idField: 'ps_id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'ps_id',title: '行情编号',width: 35},
            {field: 'ps_name',title: '行情名称',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'ps_cfg',title: '对应配置名',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'port',title: '行情端口',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'ps_srv',title: '所属主机',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'desc',title: '备注',width: 200,editor: {type: 'validatebox',options: {required: true,}}}
        ]],
        onClickRow:function(index,row){
            $('#watch_name').textbox('setValue',row["ps_name"])
            $('#watch_cfg').textbox('setValue',row["ps_cfg"])
            $('#watch_port').textbox('setValue',row["port"])
            $('#watch_srv').textbox('setValue',row["ps_srv"])
        }
    });
/************************************** END ***************************************************************/

/************************************** 新增策略 **********************************************************/
    $('#ps_add').bind('click', function() {
        $('#priceserver').dialog({
            closed: false,
            title: '新增行情',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
        $("input[name='ps_id']").prev().prop('disabled', false)
    });
/************************************** END **************************************************************/


/********************************* 点击修改策略 *********************************************************/
    $('#ps_edit').bind('click', function() {
        var row_select = $('#ps_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('message', row_select.length, 'warning');
            } else {
                $('#priceserver').dialog({
                    closed: false,
                    title: '编辑行情信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $("input[name='ps_id']").prev().prop('disabled', true)
                $('#modify').show();
                $('#add').hide();
            }
        } else {
            $.messager.alert('message', '请先选中需要修改行！', 'warning');
        }
    });
/*************************************** END ***************************************************************/


/*********************************** 点击删除策略 **********************************************************/
    $('#ps_delete').bind('click', function () {
        priceserver_del();
    });
/************************************* END *****************************************************************/

/********************************* 加载 ps_watcher panel *************************************************/
    $('#ps_watcher').panel({
        width:'100%',
        height: ($(window).height()-$('#DataGrid').height() - 34),
        title:'行情数据查看',
    })

/************************************** END ***************************************************************/


/********************************* 获取选中行数据到ps_watcher *********************************************/

/************************************** END ***************************************************************/

});
/************************************* 操作部分 END *********************************************************************************/



/************************************ 函部分数 START *******************************************************************************/


/************************************ 新增行情函数 ********************************************************/
function priceserver_add() {
    if ($("input[name='ps_id']").val() == "") {
        $.messager.alert('message', '输入内容不可为空!', 'warning');
        $("input[name='ps_id']").focus();
    } else {
        $.ajax({
            type: "POST",
            url: "/ps_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message', msg.accmsg, 'info');
                    location.href = "/ps_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************ 修改行情函数 ********************************************************/
function priceserver_mod(){
    if ($("input[name='ps_id']").val() == "") {
        $.messager.alert('message', '输入内容不可为空!', 'warning');
        $("input[name='ps_id']").focus();
    } else {
        $.ajax({
            type: "POST",
            url: "/ps_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message', msg.accmsg+"策略信息修改成功！", 'info');
                    location.href = "/ps_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        });
    }
}
/************************************** END ***************************************************************/


/************************************ 删除行情函数 ********************************************************/
function priceserver_del(){
    var ps_ids = "";
    var row_select = $('#ps_table').datagrid('getSelections'); //返回的是被选中行的对象
    for (var i = 0; i < row_select.length; i++) {
        ps_ids += '#' + row_select[i].ps_id;
    }
    if (ps_ids == "") {
        $.messager.alert('message', '请先选中需要删除的行情！', 'warning');
        return false;
    } else {
        $.messager.confirm('message', '您确认想要删除此行情吗？', function(r) {
            if (r) {
                $.ajax({
                    type: "POST",
                    cache: false,
                    url: "/ps_del/",
                    data: {
                        "delinfo": ps_ids
                    },
                    dataType: 'json',
                    success: function(msg) {
                        if (msg.accmsg) {
                            $.messager.alert('message','行情：'+ msg.accmsg + '删除成功！', 'info');
                            $('#ps_table').datagrid('reload', {});
                        } else {
                            $.messager.alert('message', msg.errmsg);
                            $('#ps_table').datagrid('reload', {});
                        }
                    }
                });
            }
        });
    }
};
/************************************** END ***************************************************************/


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


/************************************* 搜索函数 ***************************************************/
function doSearch(value){
    if(value){
        alert('You input: ' + value);
    }else{
        alert('Please input ...');
    }
}
/***************************************** END ****************************************************/


/************************************* 搜索函数 ***************************************************/
function watch_ps() {
    var watch_name =  $("#watch_name").textbox('getValue')
    var cfg = $('#watch_cfg').textbox('getValue')
    var port = $('#watch_port').textbox('getValue')
    var srv = $('#watch_srv').textbox('getValue')
    var Ukey = $('#Ukey').textbox('getValue')
    var sleeptime = $('#sleeptime').combobox('getValue')
    if (watch_name == "") {
        $.messager.alert('message', '请先选择行情!', 'warning');
    }
    else if (Ukey == "") {
        $.messager.alert('message', '请输入Ukey!', 'warning');
    }
    else {
        $.messager.confirm('message', '请确认查看此行情数据！', function(r) {
            if(r){
                $.ajax({
                    url: '/ps_watch/',
                    type: 'POST',
                    dataType: 'json',
                    data: {cfg,port,srv,Ukey,sleeptime},
                    beforeSend:ajaxLoading,
                    success:function (msg) {
                        ajaxLoadEnd()
                        $.messager.alert('message', msg.hello, 'info');
                    }
                })
            }
        })
    }
}

/***************************************** END ****************************************************/


/************************************* loading界面控制函数 *****************************************/
function ajaxLoading(){
    $("<div id=\"i_mask \" class=\"datagrid-mask\"></div>").css({display:"block",width:"100%",height:$(window).height()}).appendTo("body");
    $("<div id=\"i_mask_msg\" class=\"datagrid-mask-msg\"></div>").html("正在处理，请稍候。。。").appendTo("body").css({display:"block",left:($(document.body).outerWidth(true) - 190) / 2,top:($(window).height() - 45) / 2});
 }
 function ajaxLoadEnd(){
    $(".datagrid-mask").remove();
    $(".datagrid-mask-msg").remove();
} 
/***************************************** END ****************************************************/


/************************************* 函数部分END *********************************************************************************/