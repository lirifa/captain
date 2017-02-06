$(function() {
        var editRow = '';
        var permission = [{
            "value": "管理员",
            "text": "管理员"
        }, {
            "value": "IT业务",
            "text": "IT业务"
        }];

        /**********************加载产品列表*******************************/
        $('#server_table').datagrid({
            title: '>>>产品列表',
            url: '/productinfo_json/',
            width: '100%',
            border: true,
            fitColumns: true,
            singleSelect: false,
            pagination: false,
            idField: 'id',
            pageSize: 10,
            pageList: [10, 15, 20, 25, 100],
            columns: [
                [{
                        field: 'id',
                        title: '序号',
                        width: 35
                    },
                    //   {field:'id_db',title:'数据库id',width:80,hidden:true},
                    {
                        field: 'product_num',
                        title: '产品编号',
                        width: 120,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true
                            }
                        }
                    }, {
                        field: 'product_name',
                        title: '产品名称',
                        width: 200,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true
                            }
                        }
                    }, {
                        field: 'product_admin',
                        title: '产品管理人',
                        width: 150,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true
                            }
                        }
                    },
                    {
                        field: 'desc',
                        title: '产品介绍',
                        width: 200,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true,
                                validType: 'strChinese'
                            }
                        }
                    }
                ]
            ],
        });

        /*************************点击添加产品******************************/
        $('#server_add').bind('click', function() {
            $('#server').dialog({
                closed: false,
                title: '>>>新增产品',
                cache: false
            });
            $('#fm').form('clear');
        });

        /*************************点击修改产品信息******************************/
        $('#user_edit').bind('click', function() {
            var row_select = $('#server_table').datagrid('getSelected'); //返回的是被选中行的对象
            if (row_select) {
                if (row_select.length == 1) {
                    $.messager.alert('警告', row_select.length, 'warning');
                } else {
                    $('#server').dialog({
                        closed: false,
                        title: '>>>编辑服务器',
                        cache: false
                    });
                    $('#fm').form("load", row_select);
                }
            } else {
                $.messager.alert('警告', '请先选中需要修改行！', 'warning');
            }
        });

        /*************************点击删除产品******************************/
        $('#user_delete').bind('click', function() {
            var ids = "";
            var ips = "";
            var row_select = $('#server_table').datagrid('getSelections'); //返回的是被选中行的对象
            for (var i = 0; i < row_select.length; i++) {
                ids += '#' + row_select[i].id_db;
                ips += ' [' + row_select[i].ip + '] ';
            }
            if (ids == "") {
                $.messager.alert('警告', '请先选中需要删除的行！', 'warning');
                return false;
            } else {
                $.messager.confirm('确认', '您确认想要删除 ' + ips + ' 记录吗？', function(r) {
                    if (r) {
                        $.ajax({
                            type: "GET",
                            cache: false,
                            url: "/serverinfo_del/",
                            data: {
                                "delinfo": ids
                            },
                            dataType: 'json',
                            success: function(msg) {
                                if (msg.accmsg) {
                                    $.messager.alert('恭喜你', '成功删除' + msg.accmsg, 'info');
                                    $('#server_table').datagrid('reload', {});
                                } else {
                                    $.messager.alert('错误', msg.errmsg);
                                    $('#server_table').datagrid('reload', {});
                                }
                            }
                        });
                    }
                });
            }
        });
    });