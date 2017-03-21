/*************************************** 操作部分 START ******************************************************************************/

$(function () {

/***************************************加载datagrid服务列表数据 ***************************************/
    $('#service_table').datagrid({
        title: '>>>服务列表',
        loadFilter: pagerFilter,
        url: '/serviceinfo_json/',
        width: '100%',
        height: $(window).height() - 31,
        border: true,//边框
        fitColumns: true,//设置为true将自动使列适应表格宽度以防止出现水平滚动,false则自动匹配大小
        striped:true,//隔行变色
        singleSelect: true,//单行选中，false可以选中多行
        pagination: true,//显示最下端的分页工具栏
        idField: 'ser_id', //标识列，一般设为id，可能会区分大小写
        pageSize: 25,////读取分页条数，即向后台读取数据时传过去的值
        pageList: [10, 15, 20, 25, 100],//可以调整每页显示的数据，即调整pageSize每次向后台请求数据时的数据
        // sortName: "ser_id",
        columns: [[
            // {field:'id',title:'序号',width:20},
            {field:'ser_id',title:'服务编号',width:40},
            {field:'ser_name',title:'服务名称',width:120,editor:{type:'validatebox',options:{required:true}}},
            {field:'ser_att',title:'服务属性',width:60,editor:{type:'validatebox',options:{required:true}}},
            {field:'ser_cfg',title:'配置名',width:150,editor:{type:'validatebox',options:{required:true}}},
            {field:'ser_port',title:'服务端口',width:80,editor:{type:'validatebox',options:{required:true}}},
            {field:'ser_srv',title:'所属主机',width:80,editor:{type:'validatebox',options:{required:true}}},
            {field:'desc',title:'备注',width:150,editor:{type:'validatebox',options:{required:true}}},
            {field:'ser_stat',title:'服务状态',width:50,align:'center',
                styler:function(value, row, index){
                    if (value == "UP") {
                        return 'color:green;';
                    }else if(value == "DOWN"){
                        return 'color:red;'
                    }else if(value == "检测出错"){
                        return 'color:red;';
                    }
                },
            },
            {field:'port_stat',title:'端口状态',width:50,align:'center',
                styler:function(value, row, index){
                    if (value == "UP") {
                        return 'color:green;';
                    }else if(value == "DOWN"){
                        return 'color:red;'
                    }else if(value == "检测出错"){
                        return 'color:red;';
                    }
                },
            },
            {field:'opt',title:'操作',width:200,align:'center',
                formatter: function(value, row, index) {
                    //var str = '<a name="check-btn" href="javascript:check_stat();"  title="check">检查</a><a name="start-btn" href="javascript:service_start();"  title="start">启动</a><a name="stop-btn" href="javascript:service_stop();"  title="stop">停止</a><a name="restart-btn" href="javascript:service_restart();"  title="restart">重启</a>';
                    var str = '<a name="start-btn" href="javascript:service_start();"  title="start">启动</a><a name="stop-btn" href="javascript:service_stop();"  title="stop">停止</a><a name="restart-btn" href="javascript:service_restart();"  title="restart">重启</a>';
                    return str; 
                } 
            }, 
            ]], 
        onLoadSuccess:function(data){ 
            //$("a[name='check-btn']").linkbutton({text:'检查',plain:true,iconCls:'icon-magnifier'});
            $("a[name='start-btn']").linkbutton({text:'启动',plain:true,iconCls:'icon-ok'});
            $("a[name='stop-btn']").linkbutton({text:'停止',plain:true,iconCls:'icon-cancel'});
            $("a[name='restart-btn']").linkbutton({text:'重启',plain:true,iconCls:'icon-reload'});
        },
    });
/*********************************END*******************************************************/


/*******************************点击添加服务进程********************************************/
    $('#service_add').bind('click', function(){
        $("#fm p:first").attr("style", "display:none;");
        $('#service').dialog({ 
            title:">>>新增服务进程",
            closed:false,
            cache:false
        });
        $('#fm').form('clear');
        $('#modify').hide()
        $('#add').show()
        //$('input[name="ser_id"]').prev().prop('disabled', false)
    });
/*********************************END*******************************************************/


/***************************** 加载服务器combobox ********************************************/
    $('#check_all_server').combobox({
        width:100,
        editable:false,
        panelHeight:'auto',
        url:'/serverinfo_combobox_json/',
        valueField:'srvnum',
        textField:'srvnum',
        value:'all',
        loadFilter : function (data) {
            if (data && data instanceof Array) {
                data.splice(0, 0, {srvnum: 'all', srvnum: 'all'});
            }
            return data;
        },
        onSelect:function (rec) {
            var url = '/serviceinfo_json/'+rec.srvnum
            $('#service_table').datagrid('reload',{"ser_srv":rec.srvnum})
        },
    })
/********************************* END ******************************************************/



/************************* 定时查询服务、端口状态 ******************************************/
    var time = setInterval('get_stat()',1000);
    // // 清除定时器
    // clearInterval(time)
/***************************** END *********************************************************/


/*************************检查服务器下所有服务、端口状态******************************/
    // $('#service_check').bind('click',function() {
    //     var srvnum = $('#check_all_server').val()
    //     $.ajax({
    //         url: '/ser_check_stat/',
    //         type: 'POST',
    //         dataType: 'json',
    //         data: {srvnum: srvnum},
    //         success:function (msg) {
    //             var rows = msg.rows
    //             for (i=0;i < rows.length;i++){
    //                 var id = rows[i].ser_id
    //                 var rowIndex = $('#service_table').datagrid('getRowIndex',id)
    //                 $('#service_table').datagrid('updateRow',{
    //                     index: rowIndex,
    //                     row:{
    //                         ser_stat: rows[i].ser_stat,
    //                         port_stat:rows[i].port_stat,
    //                     }
    //                 })
    //                 $("a[name='check-btn']").linkbutton({text:'检查',plain:true,iconCls:'icon-magnifier'});
    //                 $("a[name='start-btn']").linkbutton({text:'启动',plain:true,iconCls:'icon-ok'});
    //                 $("a[name='stop-btn']").linkbutton({text:'停止',plain:true,iconCls:'icon-cancel'});
    //                 $("a[name='restart-btn']").linkbutton({text:'重启',plain:true,iconCls:'icon-reload'});
    //             }
                
    //         }
    //     })
    // });
/*********************************END*******************************************************/


/**********************************修改服务信息*********************************************/
    $('#service_edit').bind('click',function(){
        var row_select = $('#service_table').datagrid('getSelected'); //返回的是被选中行的对象
        if (row_select) {
            if (row_select.length == 1) {
                $.messager.alert('警告', row_select.length, 'warning');
            } else {
                $('#service').dialog({
                    closed: false,
                    title: '>>>修改服务信息',
                    cache: false
                });
                $('#fm').form("load", row_select);
                $("#fm p:first").attr("style", "display:block;");
                $('input[name="ser_id"]').prev().prop('disabled', true)
                $('#add').hide()
                $('#modify').show()
            }
        } else {
            $.messager.alert('警告', '请先选中需要修改行！', 'warning');
        }
    })
/*********************************END*******************************************************/


/*********************************删除服务进程**********************************************/
    $('#service_delete').bind('click', function() {
        var services = "";
        var row_select = $('#service_table').datagrid('getSelections'); //返回的是被选中行的对象
        for (var i = 0; i < row_select.length; i++) {
            services += '#' + row_select[i].ser_id;
        }
        if (services == "") {
            $.messager.alert('警告', '请先选中需要删除的服务进程！', 'warning');
            return false;
        } else {
            $.messager.confirm('确认', '您确认想要删除此服务进程吗？', function(r) {
                if (r) {
                    $.ajax({
                        type: "GET",
                        cache: false,
                        url: "/service_del/",
                        data: {
                            "delinfo": services
                        },
                        dataType: 'json',
                        success: function(msg) {
                            if (msg.accmsg) {
                                $.messager.alert('message','服务进程'+msg.accmsg+"删除成功！",'info' );
                                $('#service_table').datagrid('reload', {"ser_srv":"all"});
                            } else {
                                $.messager.alert('message', msg.errmsg,'error');
                                $('#service_table').datagrid('reload', {});
                            }
                        }
                    });
                }
            });
        }
    });
/*********************************END*******************************************************/

});
/****************************** 操作部分 END *********************************************************************************/







/********************************** 函数部分 START ****************************************************************************/


/********************************* 新增服务函数 ***********************************************/
function service_add() {
    if ($("input[name='ser_name']").val() == "") {
        $.messager.alert('警告','输入内容不可为空!','warning'); 
        $("input[name='ser_name']").focus();
    } else {
        $.ajax({
            type: "GET", 
            url: "/service_add/",
            data: $("#fm").serialize(), 
            success: function(msg){
                if(msg.accmsg){
                    $.messager.alert('恭喜',msg.accmsg,'info');
                    location.href = "/serviceinfo/";
                }else{
                    $.messager.alert('警告',msg.errmsg,'error'); 
                }
            }
        });
    }
}
/*********************************** END *****************************************************/


/*********************************** 修改服务信息函数 ****************************************/
function service_mod() {
    if ($("input[name='ser_id']").val() == "") {
        $.messager.alert('警告', '输入内容不可为空!', 'warning');
        $("input[name='ser_name']").focus();
    } else {
        $.ajax({
            type: "GET",
            url: "/service_mod/",
            data: $("#fm").serialize(),
            success: function(msg) {
                if (msg.accmsg) {
                    $.messager.alert('恭喜', msg.accmsg, 'info');
                    location.href = "/serviceinfo/";
                } else {
                    $.messager.alert('警告', msg.errmsg, 'error');
                }
            }
        });
    }
}
/***************************************** END ************************************************/


/************************************ 检查服务状态函数 ****************************************/
function check_stat() {
    var row_select = $('#service_table').datagrid('getSelected')
    var ser_cfg = row_select.ser_cfg
    var ser_port = row_select.ser_port
    var ser_srv = row_select.ser_srv
    $.ajax({
        type:"POST",
        url:"/check_stat/",
        data:{ser_cfg,ser_port,ser_srv},
        success: function (msg) {
            $('#service_table').datagrid('updateRow',{
                index:$('#service_table').datagrid('getRowIndex',$('#service_table').datagrid('getSelected')),
                row:{
                    ser_stat: msg.ser_stat,
                    port_stat:msg.port_stat,
                }
            })
            $("a[name='check-btn']").linkbutton({text:'检查',plain:true,iconCls:'icon-magnifier'});
            $("a[name='start-btn']").linkbutton({text:'启动',plain:true,iconCls:'icon-ok'});
            $("a[name='stop-btn']").linkbutton({text:'停止',plain:true,iconCls:'icon-cancel'});
            $("a[name='restart-btn']").linkbutton({text:'重启',plain:true,iconCls:'icon-reload'});
        }
    })
}
/************************************ END ***************************************************/

/************************************ 服务启动函数 ******************************************/
function service_start() {
    var row_select = $('#service_table').datagrid('getSelected')
    var ser_cfg = row_select.ser_cfg
    var ser_port = row_select.ser_port
    var ser_srv = row_select.ser_srv
    $.ajax({
        url: '/path/to/file',
        type: 'POST',
        dataType: 'json',
        data: {ser_cfg,ser_port,ser_srv},
        success: function(msg){
            // 看后端怎么回数据
            $("a[name='check-btn']").linkbutton({text:'检查',plain:true,iconCls:'icon-magnifier'});
            $("a[name='start-btn']").linkbutton({text:'启动',plain:true,iconCls:'icon-ok'});
            $("a[name='stop-btn']").linkbutton({text:'停止',plain:true,iconCls:'icon-cancel'});
            $("a[name='restart-btn']").linkbutton({text:'重启',plain:true,iconCls:'icon-reload'});
        }
    })
    // .done(function() {
        // check_stat();
    // })
    .fail(function() {
        console.log("启动失败");
    })
}
/************************************ END ********************************************************/


/***************************** 获取服务状态及端口状态函数 *****************************************/
function get_stat(){
    var srvnum = $('#check_all_server').val()
    $.ajax({
        url: '/get_stat/',
        type: 'POST',
        dataType: 'json',
        data: {srvnum,},
        success:function (msg) {
            var m_rows = msg.rows
            for (i=0;i < m_rows.length;i++){
                 var id = m_rows[i].ser_id
                var rows = $('#service_table').datagrid('getRows')
                for (j=0;j < rows.length; j++){
                    if (rows[j].ser_id == id){
                        var rowIndex = $('#service_table').datagrid('getRowIndex',id)
                        $('#service_table').datagrid('updateRow',{
                            index: rowIndex,
                            row:{
                            ser_stat: m_rows[i].ser_stat,
                            port_stat:m_rows[i].port_stat,
                            }
                        })
                    }
                }
            }
            $("a[name='start-btn']").linkbutton({text:'启动',plain:true,iconCls:'icon-ok'});
            $("a[name='stop-btn']").linkbutton({text:'停止',plain:true,iconCls:'icon-cancel'});
            $("a[name='restart-btn']").linkbutton({text:'重启',plain:true,iconCls:'icon-reload'});
        }
    })
}
/************************************** END **********************************************************/


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


/************************************* 函数部分 END ********************************************************************************/
