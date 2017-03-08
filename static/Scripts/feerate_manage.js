/*************************************** 操作部分 START ******************************************************************************/

$(function() {
/****************************** 加载datagrid 费率信息列表 *********************************************/
    $('#feerate_table').datagrid({
        title: '>>>费率列表',
        url: '/feerate_json/',
        width: '100%',
        border: true,
        fitColumns: true,
        striped: true,
        singleSelect: true,
        pagination: false,
        idField: 'id',
        pageSize: 10,
        pageList: [10, 15, 20, 25, 100],
        columns: [[
        {field: 'bid',title: '经纪商',width: 35},
        {field: 'exchange_id',title: '交易所',width: 120,editor: {type: 'validatebox',options: {required: true}}},
        {field: 'contract_id',title: '合约品种',width: 200,editor: {type: 'validatebox',options: {required: true}}},
        {field: 'biz_type',title: '开平标志',width: 150,editor: {type: 'validatebox',options: {required: true    }}},
        {field: 'feerate_by_amt',title: '手续费率（按金额）',width: 200,editor: {type: 'validatebox', options: {required:true }}},
        {field: 'feerate_by_qty',title: '手续费率（按手数）',width: 100,editor: {type: 'validatebox', options: {required: true}}}
        ]],
    });
/************************************* END ************************************************************/

});

/****************************** 操作部分 END *********************************************************************************/









/********************************** 函数部分 START *****************************************************************************/


/************************************** 搜索函数 ***********************************************************/
function doSearch(value){
    if(value){
        alert('You input: ' + value);
    }else{
        alert('Please input ...');
    }
}
/************************************** END ****************************************************************/


/************************************* 函数部分 END ********************************************************************************/