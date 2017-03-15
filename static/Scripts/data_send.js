/******************************** 操作部分 START *****************************************************************************/
$(function(){

/********************************* 加载datagrid数据发送配置列表 ************************************************/
    $('#data_send').datagrid({
        title:'>>>配置列表',
        url:'/data_send_json/',
        width:'100%',
        border:true,
        fitColumns:true,
        striped:true,
        singleSelect:true,
        pagination:false,
        idField:'id',
        pageSize:10,
        pageList:[10,15,20,25,100],
        columns:[[
            {field:'id',title:'序号',width:35},
            {field:'d_name',title:'数据名称',width:120,editor:{type:'validatebox',options:{required:true}}},
            {field:'o_srv',title:'源服务器',width:200,editor:{type:'validatebox',options:{required:true}}},
            {field:'o_dir',title:'源目录',width:150,editor:{type:'validatebox',options:{required:true}}},
            {field:'p_srv',title:'目标服务器',width:200,editor:{type:'validatebox',options:{required:true}}},
            {field:'p_dir',title:'目标目录',width:100,editor:{type:'validatebox',options:{required:true}}},
            {field:'ops',title:'操作',width:100,align:'center',
                formatter: function(value, row, index) {
                    var str = '<a name="start-btn" href="javascript:send_data();"  title="send">发送</a>';
                    return str; 
                } 
            },
        ]],
         onLoadSuccess:function(data){ 
            $("a[name='send-btn']").linkbutton({text:'发送',plain:true,iconCls:'icon-send'});
        }
    })
/************************************** END ********************************************************/


/********************************* 新增发送数据配置 ************************************************/
    $('#data_add').bind('click',function () {
        $('#data').dialog({ 
            title:">>>新增发送配置",
            closed:false,
            cache:false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
    })
/************************************** END ********************************************************/


/********************************* 修改发送数据配置 ************************************************/
    $('#data_edit').bind('click',function () {
        var row_select = $('#data_send').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#data').dialog({
                    title: '>>>修改发送配置',
                    closed: false,
                    cache: false
                });
                $('#fm').form("load", row_select);
                $('#add').hide()
                $('#modify').show()
            }
        } else {
            $.messager.alert('警告', '请点击先选中需要修改行！', 'warning');
        }
    })
/************************************** END ********************************************************/

/********************************* 删除数据发送配置 **********************************************/
    $('#data_delete').bind('click', function() {
        var datas = "";
        var row_select = $('#data_send').datagrid('getSelections'); //返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            datas += '#' + row_select[i].id;
        }
        if (datas == "") {
            $.messager.alert('警告', '请先点击选中要删除的配置！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认要删除此配置吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/data_send_del/",
                        data: {
                            "delinfo": datas
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('message','配置'+msg.accmsg+"删除成功！" );
                                $('#data_send').datagrid('reload', {"ser_srv":"all"});
                            } else {
                                $.messager.alert('错误', msg.errmsg);
                                $('#data_send').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/********************************* END *******************************************************/

});
/******************************* 操作部分 END ********************************************************************************/






/********************************** 函数部分 START ****************************************************************************/


/************************************* 搜索函数 ***************************************************/
function doSearch(value){
    if(value){
        alert('You input: ' + value);
    }else{
        alert('Please input ...');
    }
}
/***************************************** END ****************************************************/


/************************************* 新增发送配置函数 ***********************************************/
function data_add() {
    
}


/************************************* 发送数据函数 ***********************************************/
function send_data() {
    var row_select = $('#send_data').datagrid('getSelected')
    var d_name = row_select.d_name
    var o_srv = row_select.o_srv
    var o_dir = row_select.o_dir
    var p_srv = row_select.p_srv
    var p_dir = row_select.p_dir
    $.ajax({
        type:"POST",
        url:"/send_data/",
        data:{o_srv,o_dir,p_srv,p_dir},
        success: function (msg) {
            if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/serviceinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            $("a[name='send-btn']").linkbutton({text:'发送',plain:true,iconCls:'icon-send'});
        }
    })
}
/***************************************** END ****************************************************/

/********************************** 函数部分 END ******************************************************************************/