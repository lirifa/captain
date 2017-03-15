/********************************************** 操作 START **************************************************************************/

$(function(){

/***********************************加载datagrid服务器主机信息列表**********************************************/
    $('#server_table').datagrid({
        title:'>>>服务器信息列表',
        loadFilter: pagerFilter,
        url:'/serverinfo_json/',
        width:'100%',
        height: $(window).height() - 31,
        border:true,
        fitColumns:true,
        striped:true,
        singleSelect:true,
        pagination:true,
        idField:'id',
        pageSize:10,
        pageList:[10,15,20,25,100],
        columns:[[
            {field:'id',title:'序号',width:35},
            {field:'srvnum',title:'服务器编号',width:120,editor:{type:'validatebox',options:{required:true}}},
            {field:'ip',title:'IP地址',width:200,editor:{type:'validatebox',options:{required:true}}},
            {field:'user',title:'用户名',width:150,editor:{type:'validatebox',options:{required:true}}},
            {field:'passwd',title:'密码',width:200,editor:{type:'validatebox',options:{required:true}}},
            {field:'port',title:'SSH端口',width:100,editor:{type:'validatebox',options:{required:true}}},
            {field:'productadmin',title:'产品管理人',width:100,editor:{type:'validatebox',options:{required:true}}},
            {field:'desc',title:'业务描述',width:200,editor:{type:'validatebox',options:{required:true,validType:'strChinese'}}}
        ]],
        onLoadSuccess:function(data){
            $("#server_table").datagrid("hideColumn", "passwd"); // 设置隐藏列    
            $("#passwd_hide").hide();
        }
    })
/************************************** END ****************************************************************/


/*****************************新增服务器主机****************************************************************/
    $('#server_add').bind('click', function(){
        $('#server').dialog({closed:false,title:'>>>新增服务器',cache:false});
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
    });
/************************************** END ****************************************************************/


/**********************************修改主机信息**************************************************************/
    $('#user_edit').bind('click', function(){
        var row_select = $('#server_table').datagrid('getSelected');//返回的是被选中行的对象
        if(row_select){
            if(row_select.length == 1){
                $.messager.alert('警告',row_select.length,'warning');
            }else{
                $('#server').dialog({closed:false,title:'>>>编辑服务器',cache:false});
                $('#fm').form("load",row_select);
                $('#add').hide()
                $('#modify').show()
            }
        }else{
            $.messager.alert('警告','请先选中需要修改行！','warning'); 
        }
    });
/************************************** END ****************************************************************/


/************************************ 删除主机 *************************************************************/
    $('#user_delete').bind('click', function(){
        var srvnums = "";
        var ips = "";
        var row_select = $('#server_table').datagrid('getSelections');//返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            srvnums += '#' + row_select[i].srvnum;
            ips += ' [' + row_select[i].ip + '] ';
            }
        if(srvnums == ""){
            $.messager.alert('警告','请先选中需要删除的行！','warning'); 
            return false;
        }else{
            $.messager.confirm('确认','您确认想要删除 ' + ips + ' 主机吗？',function(r){
                if (r){
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/serverinfo_del/",
                        data: {"delinfo":srvnums},
                        dataType:'json',
                        success: function(msg){
                            if(msg.accmsg){
                                $.messager.alert('成功','成功删除' + msg.accmsg,'info');
                                $('#server_table').datagrid('reload',{});
                            }else{
                                $.messager.alert('错误',msg.errmsg,'error');
                                $('#server_table').datagrid('reload',{});
                            }
                        } 
                    });
                }
            });
        }
    });
/************************************** END ****************************************************************/


/********************************* 密码显示隐藏 ************************************************************/
            $('#passwd_show').bind('click', function(){
                $("#server_table").datagrid("showColumn", "passwd");
                $("#passwd_show").hide();
                $("#passwd_hide").show();
            });
            $('#passwd_hide').bind('click', function(){
                $("#server_table").datagrid("hideColumn", "passwd");
                $("#passwd_show").show();
                $("#passwd_hide").hide();
            });
/************************************** END ****************************************************************/


});
/************************************** 操作部分 END *******************************************************************************/









/***************************************** 函数部分 START **************************************************************************/

/************************************** 搜索函数 ***********************************************************/
function doSearch(value){
    if(value){
        alert('You input: ' + value);
    }else{
        alert('Please input ...');
    }
}
/************************************** END ****************************************************************/


/************************************** 新增主机函数 *******************************************************/
function serverinfoadd() {
    if ($("input[name='ip']").val() == "") {
        $.messager.alert('警告','输入内容不可为空!','warning'); 
        $("input[name='ip']").focus();
    } else {
        $.ajax({
            type: "GET", 
            url: "/serverinfo_add/",
            data: $("#fm").serialize(), 
            success: function(msg){
                if(msg.accmsg){
                    $.messager.alert('恭喜',msg.accmsg,'info');
                    location.href = "/serverinfo/";
                }else{
                    $.messager.alert('警告',msg.errmsg,'error'); 
                }
            }
        });
    }
}
/************************************** END ****************************************************************/


/************************************** 修改主机信息函数 ***************************************************/
function serverinfomod() {
    if ($("input[name='srvnum']").val() == "") {
        $.messager.alert('警告','输入内容不可为空!','warning'); 
        $("input[name='srvnum']").focus();
    } else {
        $.ajax({
            type: "GET", 
            url: "/serverinfo_mod/",
            data: $("#fm").serialize(), 
            success: function(msg){
                if(msg.accmsg){
                    $.messager.alert('恭喜',msg.accmsg,'info');
                    location.href = "/serverinfo/";
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


/************************************ 函数部分 END *********************************************************************************/