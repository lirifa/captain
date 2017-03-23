/*************************************** 操作部分 START ******************************************************************************/

$(function() {

/******************************************加载datagrid资金账户列表*********************************************/
    $('#user_table').datagrid({
        title: '>>>用户列表',
        loadFilter: pagerFilter,
        url: '/userinfo_json/',
        width: '100%',
        height: $(window).height() - 31,
        border: true,
        fitColumns: true,
        striped:true,
        singleSelect: true,
        pagination: true,
        rownumbers: true,
        pageSize: 25,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
            {field: 'username',title: '用户名',width: 120,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'passwd',title: '用户密码',width: 200,editor: {type: 'validatebox',options: {required: true}}},
            {field: 'tel',title: '联系电话',width: 200,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'email',title: '联系邮件',width: 200,editor: { type: 'validatebox', options: { required: true }}},
            {field: 'permission',title: '权限等级',width: 150,editor: {type: 'validatebox',options: { required: true}}},
            {field: 'desc',title: '备注',width: 150,editor: {type: 'validatebox',options: { required: true}}},
        ]],
    });
/**************************************END******************************************************************/

/************************************** 新增用户 **********************************************************/
    $('#user_add').bind('click', function() {
        $('#user').dialog({
            closed: false,
            title: '新增用户',
            cache: false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
    });
/************************************** END **************************************************************/

});
/************************************* 操作部分 END *********************************************************************************/



/************************************ 函部分数 START *******************************************************************************/

/************************************ 新增用户函数 ********************************************************/
function user_add() {
    if ($("input[name='username']").val() == "") {
        $.messager.alert('message', '用户名不可为空!', 'warning');
        $("input[name='username']").focus();
    } else {
        $.ajax({
            type: "POST",
            url: "/user_add/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('message', msg.accmsg, 'info');
                    location.href = "/user_manage/";
                } else {
                    $.messager.alert('message', msg.errmsg, 'error');
                }
            }
        });
    }
}
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

/************************************* 函数部分END *********************************************************************************/