/******************************** 操作部分 START *****************************************************************************/
$(function () {

/********************************* 加载数据源折叠面板 *****************************************************/
    $('#data_origin').panel({
        // width:1000,
        // height:120,
        title:'数据源',
        iconCls:'icon-large-smartart',
        region:'north',
        collapsible:true,
        tools:[{
            iconCls:'icon-save',
            handler:function(){alert('save')}
        }]
    }); 
/************************************** END **************************************************************/

})
/******************************* 操作部分 END ********************************************************************************/






/********************************** 函数部分 START ****************************************************************************/





/********************************** 函数部分 END ******************************************************************************/