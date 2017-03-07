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
            striped:true,
            singleSelect: true,
            pagination: false,
            idField: 'id',
            pageSize: 10,
            pageList: [10, 15, 20, 25, 100],
            columns: [[
                {field: 'id',title: '序号',width: 35},
                {field: 'pid',title: '产品编号',width: 120,editor: {type: 'validatebox',options: {required: true}}},
                {field: 'pname',title: '产品名称',width: 200,editor: {type: 'validatebox',options: {required: true}}},
                {field: 'admin',title: '产品管理人',width: 150,editor: {type: 'validatebox',options: {required: true}}},
                {field: 'desc',title: '产品介绍',width: 200,editor: {type: 'validatebox',options: {required: true,validType:'strChinese'}}}
                ]],
        });
        
        /*************************点击添加用户******************************/
        $('#product_add').bind('click', function() {
            $('#product').dialog({
                closed: false,
                title: '新增产品',
                cache: false
            });
            $('#fm').form('clear');
            $('#modify').hide()
            $('#add').show()
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

        /*************************点击删除产品******************************/
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