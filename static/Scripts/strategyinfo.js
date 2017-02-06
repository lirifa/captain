    $(function() {
        var editRow = '';
        var permission = [{
            "value": "管理员",
            "text": "管理员"
        }, {
            "value": "IT业务",
            "text": "IT业务"
        }];
        $('#product_table').datagrid({
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
                    },{
                        field: 'strategy_id',
                        title: '策略编号',
                        width: 120,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true
                            }
                        }
                    }, {
                        field: 'strategy_name',
                        title: '策略名称',
                        width: 200,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true
                            }
                        }
                    }, {
                        field: 'strategy_product',
                        title: '所属产品',
                        width: 150,
                        editor: {
                            type: 'validatebox',
                            options: {
                                required: true
                            }
                        }
                    },
                    //   {field:'passwd',title:'密码',width:200,editor:{type:'validatebox',options:{required:true}}},
                    //   {field:'port',title:'SSH端口',width:100,editor:{type:'validatebox',options:{required:true}}},
                    {
                        field: 'strategy_desc',
                        title: '策略介绍',
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
        /*************************点击添加用户******************************/
        $('#product_add').bind('click', function() {
            $('#product').dialog({
                closed: false,
                title: '>>>新增产品',
                cache: false
            });
            $('#fm').form('clear');
        });

        /*************************点击修改用户******************************/
        $('#product_edit').bind('click', function() {
            var row_select = $('#product_table').datagrid('getSelected'); //返回的是被选中行的对象
            if (row_select) {
                if (row_select.length == 1) {
                    $.messager.alert('警告', row_select.length, 'warning');
                } else {
                    $('#product').dialog({
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
        $('#product_delete').bind('click', function() {
            var ids = "";
            var product_nums = "";
            var row_select = $('#product_table').datagrid('getSelections'); //返回的是被选中行的对象
            console.log(row_select)
            for (var i = 0; i < row_select.length; i++) {
                ids += '#' + row_select[i].id_db;
                product_nums += ' [' + row_select[i].product_num + '] ';
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
                                    $.messager.alert('产品删除成功');
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

        /*************************passwd  hide  show************/
        $('#passwd_show').bind('click', function() {
            $("#product_table").datagrid("showColumn", "passwd");
            $("#passwd_show").hide();
            $("#passwd_hide").show();
        });
        $('#passwd_hide').bind('click', function() {
            $("#product_table").datagrid("hideColumn", "passwd");
            $("#passwd_show").show();
            $("#passwd_hide").hide();
        });

        /**************对validatebox控件正则表达式验证数据有效性扩展**************/
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
    });

    function doSearch(value) {
        if (value) {
            alert('You input: ' + value);
        } else {
            alert('Please input ...');
        }
    }

