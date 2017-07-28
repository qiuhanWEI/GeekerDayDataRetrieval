/**
 * Created by weiqiuhan on 2017/7/22.
 */

var data = [{
    name : 'aaa',
    phone : '111',
    email : '111222',
    company : '111222',
    department : '111222',
    position : '111222'
    },

    {
    name : 'aaa',
    phone : '111',
    email : '111222',
    company : '111222',
    department : '111222',
    position : '111222'
    },

    {
    name : 'aaa2',
    phone : '111',
    email : '111222',
    company : '111222',
    department : '111222',
    position : '111222'
}];

//search
var $btn_search = $('#btn_search'),
    $input = $('.search_part input'),
    // search_data = {},
    $appear_more = $('.appear_more'),
    appear_num = 20,
    appear_length, appear_count = 0;
    content_name = {
        0 : 'name',
        1 : 'phone',
        2 : 'email',
        3 : 'company',
        4 : 'department',
        5 : 'position'
    };
$btn_search.bind('click', function () {
    var is_input = 0;
    var search_data = {};
    $new = $('.new');
    $new.remove();
    for (var i = 0; i < 6; i++){
        if($input[i].value){
            search_data[content_name[i]] = $input[i].value;
            is_input = 1;
        }
    }
    if(!is_input){
        alert('请至少输入一项以进行查询'); return;
    }

    $.ajax({
        type: "POST",
        url: "/select",
        data: search_data,
        success: function (data) {
            console.log(data);
            if(data.length <= appear_num){
                resultAppend(data, 0, data.length);
            }else{
                resultAppend(data, 0, appear_num);
                $appear_more.removeClass('hide_ele');
                appear_length = data.length - appear_num;
                appear_count = 1;
            }
        }
    });
});

$appear_more.bind('click',function () {
    if(appear_length > 0 && appear_length <= appear_num){
        resultAppend(data, appear_count * appear_num, data.length);
        $appear_more.addClass('hide_ele');
    }else{
        resultAppend(data, appear_count * appear_num, (appear_count + 1) * appear_num);
        appear_length -=appear_num;
        appear_count ++;
    }
});


//delete or modify
var $result_list = $('.result_list');
$result_list.bind('click',function (e) {
    var $target = $(e.target);
    if($target.hasClass('delete')){

        //send delete data
        var delete_data = {},
            $target_tr = $target.closest('tr'),
            $target_tr_val = $target.closest('tr').find('.result_text');
        for (var i = 0; i < 6; i++){
            if($target_tr_val[i].value){
                delete_data[content_name[i]] = $target_tr_val[i].value;
            }else{
                delete_data[content_name[i]] = 'NULL';
            }
        }
        if (sendAjax(delete_data, '删除', '/delete')) {
            $target_tr.remove();
        }
    }else if($target.hasClass('modify') && $target.text() == '修改 ') {
        $target.text('确认 ');
        $target.closest('tr').find('.result_text').attr("disabled", false);
        var $result_text = $target.closest('tr').find('td:first-child').find('.result_text'),
            result_text_val = $result_text.val();
        $result_text.val('').focus().val(result_text_val);
    }else if($target.hasClass('modify') && $target.text() == '确认 '){
        $target.text('修改 ');
        var $result_text = $target.closest('tr').find('.result_text');
        $result_text.attr("disabled",true);

        //send modified data
        var is_modify = 0,
            modify_data = {};
        for (var i = 0; i < 6; i++){
            if($result_text[i].value){
                modify_data[content_name[i]] = $result_text[i].value;
                is_modify = 1;
            }else{
                modify_data[content_name[i]] = 'NULL';
            }
        }
        if(!is_modify){
            alert('请至少输入一项');
        }

        console.log(modify_data);
        sendAjax(modify_data, '修改', '/update');
    }
});

function sendAjax(data, message, url) {
    console.log(data);
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function (data) {
            if(data.status == 1){
                alert(message + '成功');
                return true;
            }else{
                alert(message + '失败');
                return false;
            }
        }
    });
}


function resultAppend(data, start, length) {
    // console.log(data);
    for( var i = start; i < length; i++ ) {
        //动态创建一个tr行标签,并且转换成jQuery对象
        var $trTemp = $("<tr class='new'></tr>");

        //往行里面追加 td单元格
        $trTemp.append("<td class=\"result\">"+ "<input value="+data[i].name+" class='result_text' disabled>" +"</td>");
        $trTemp.append("<td class=\"result\">"+ "<input value="+data[i].phone+" class='result_text' disabled>" +"</td>");
        $trTemp.append("<td class=\"result\">"+ "<input value="+data[i].email+" class='result_text' disabled>" +"</td>");
        $trTemp.append("<td class=\"result result_comp\">"+ "<input value="+data[i].company+" class='result_text' disabled>" +"</td>");
        $trTemp.append("<td class=\"result\">"+ "<input value="+data[i].department+" class='result_text' disabled>" +"</td>");
        $trTemp.append("<td class=\"result\">"+ "<input value="+data[i].position+" class='result_text' disabled>" +"</td>");
        $trTemp.append("<td class=\"result\">"+ "<a class=\'modify\'>" + "修改 " + "</a>" +"|"+ "<a class=\'delete\'>"+ " 删除" +"</a>" + "</td>");
        // $("#J_TbData").append($trTemp);
        $trTemp.appendTo("#result_list");
    }
}


//clear
var $btn_clear = $('#btn_clear');
$btn_clear.bind('click',function () {
    for (var i = 0; i < 6; i++){
        if($input[i].value){
            $input[i].value = '';
        }
    }
    $('.new').remove();
    $('.appear_more').remove();
    is_input = 0;
});

//insert
var $btn_insert = $('#btn_insert'),
    insert_data = {};
$btn_insert.bind('click',function () {
    var is_input = 0;
    for (var i = 0; i < 6; i++){
        if($input[i].value){
            insert_data[content_name[i]] = $input[i].value;
            is_input = 1;
        }else{
            insert_data[content_name[i]] = 'NULL';
        }
    }
    if(!is_input){
        alert('请至少输入一项');
    }

    sendAjax(insert_data, '插入', '/insert');
});
