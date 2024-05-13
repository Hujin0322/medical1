$(function(){
    $.ajax({
        url:"",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            alert("success")

            htmldata = "";
            for (let i=0;i<data.lengh;i++){
                htmldata += "<tr>";
                htmldata += "<td><input type='checkbox' name='stuChk' id='stuChk' value='stuChk'></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "<td></td>";
                htmldata += "</tr> ";
                
            }
        },
        error:function(){
            alert("error")
        }

    });//ajax
});//Jquery