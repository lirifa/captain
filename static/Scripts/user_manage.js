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


/**********************************修改用户信息************************************************************/
    $('#user_edit').bind('click', function(){
        var row_select = $('#user_table').datagrid('getSelected');//返回的是被选中行的对象
        if(row_select){
            if(row_select.length == 1){
                $.messager.alert('警告',row_select.length,'warning');
            }else{
                $('#user').dialog({closed:false,title:'>>>编辑用户信息',cache:false});
                $('#fm').form("load",row_select);
                $('#add').hide()
                $('#modify').show()
                $('input[name="username"]').prev().prop('disabled', true)
            }
        }else{
            $.messager.alert('警告','请先选中需要修改的用户！','warning'); 
        }
    });
/************************************** END ***************************************************************/


/************************************ 删除用户 *************************************************************/
    $('#user_delete').bind('click', function(){
        var users = "";
        var ips = "";
        var row_select = $('#user_table').datagrid('getSelections');//返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            users += '#' + row_select[i].username;
            }
        if(users == ""){
            $.messager.alert('警告','请先选中需要删除的用户！','warning'); 
            return false;
        }else{
            $.messager.confirm('确认','您确认想要删除用户【' + users + '】吗？',function(r){
                if (r){
                    $.ajax({
                        type: "POST",
                        cache: false,
                        url: "/user_del/",
                        data: {"delinfo":users},
                        dataType:'json',
                        success: function(msg){
                            if(msg.accmsg){
                                $.messager.alert('成功', '用户'+msg.accmsg+'删除成功','info');
                                $('#user_table').datagrid('reload',{});
                            }else{
                                $.messager.alert('错误',msg.errmsg,'error');
                                $('#user_table').datagrid('reload',{});
                            }
                        } 
                    });
                }
            });
        }
    });
/************************************** END ****************************************************************/

});
/************************************* 操作部分 END *********************************************************************************/



/************************************ 函部分数 START *******************************************************************************/

/************************************ 新增用户函数 **************************************************/
function user_add() {
    if ($("input[name='username']").val() == "") {
        $.messager.alert('message', '用户名不可为空!', 'warning');
        $("input[name='username']").focus();
    }
    else if ($("input[name='passwd']").val() == "") {
        $.messager.alert('警告','密码不可为空!','warning'); 
        $("input[name='passwd']").focus();
    }
    else {
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
/************************************** END *********************************************************/


/************************************** 修改主机信息函数 ***************************************************/
function user_mod() {
    if ($("input[name='passwd']").val() == "") {
        $.messager.alert('警告','密码不可为空!','warning'); 
        $("input[name='passwd']").focus();
    }
    else if ($("input[name='email']").val() == "") {
        $.messager.alert('警告','邮箱不可为空!','warning'); 
        $("input[name='email']").focus();
    } 
    else {
        $.ajax({
            type: "POST", 
            url: "/user_mod/",
            data: $("#fm").serialize(), 
            success: function(msg){
                if(msg.accmsg){
                    $.messager.alert('恭喜',msg.accmsg,'info');
                    location.href = "/user_manage/";
                }else{
                    $.messager.alert('警告',msg.errmsg,'error'); 
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

/************************************* 函数部分END *********************************************************************************/