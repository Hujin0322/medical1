$(function(){

    $.ajax({
        url:"http://127.0.0.1:5500/students/json/stu_score.json",
        type:"get",
        data: {},
        dataType: "json",
        success:function(data){
            c_count = data.length;
            //alert("success")

            let htmlData = "";
            for(let i=0;i<10;i++){
                htmlData += "<tr id="+data[i].no+">";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                htmlData += "<td>"+data[i].no+"</td>";
                htmlData += "<td>"+data[i].name+"</td>";
                htmlData += "<td>"+data[i].kor+"</td>";
                htmlData += "<td>"+data[i].eng+"</td>";
                htmlData += "<td>"+data[i].math+"</td>";
                htmlData += "<td>"+data[i].total+"</td>";
                htmlData += "<td>"+data[i].avg+"</td>";
                htmlData += "<td>0</td>";
                htmlData += "<td><button class='delBtn'>삭제</button></td>";
                htmlData += "</tr>";

            }//for
            $("#body").html(htmlData);

        },//success

        error:function(){alert("error")}//error

    });//ajax
//-----------------------------------------------------------------------------------------

    $("#writeBtn").click(function(){
        //입력 창 
        if ($(".stuChk:checked").length >= 1){
            alert("학생 입력을 위해 체크 자동 해제합니다.");
            
            //체크 모두 해제
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
            //체크 모두 해제
        }//if

        $(".p_all").css("display","block");
        $("#pop_h2").text("학생성적입력");
        $("#name").css("readonly",false);
    
    });//학생 입력

        //학생 입력 취소
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        //초기화
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        
    });//학생 입력 취소
    

    //학생입력 확인 버튼
    $("#confirmBtn").click(function(){
        //입력 창 
        let s_no = c_count + 1
        let s_name = $("#name").val();
        let s_kor = Number($("#kor").val());
        let s_eng = Number($("#eng").val());
        let s_math = Number($("#math").val());
        let s_total = s_kor + s_eng + s_math
        let s_avg = (s_total/3).toFixed(2)
        
        let htmlData = "";
        htmlData += "<tr id="+s_no+">";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+s_no+"'></td>";
        htmlData += "<td>"+s_no+"</td>";
        htmlData += "<td>"+s_name+"</td>";
        htmlData += "<td>"+s_kor+"</td>";
        htmlData += "<td>"+s_eng+"</td>";
        htmlData += "<td>"+s_math+"</td>";
        htmlData += "<td>"+s_total+"</td>";
        htmlData += "<td>"+s_avg+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
        
        $("#body").append(htmlData);
        $(".p_all").css("display","none");
        //input 초기화

    });//입력 확인 버튼


    //입력 수정
    $("#modifyBtn").click(function(){
        $(".p_all").css("display","block");
        $("#pop_h2").text("학생성적수정");
        $("#name").css("readonly","true");


    });//입력 수정


    //1개씩 삭제
    $(document).on("click",".delBtn",function(){
        let del_id = $(this).parent().parent().attr("id");
        confirm("삭제하시겠습니까?")
        
        if (confirm){
            alert(del_id+"번 학생을 삭제합니다.")
            $("#"+del_id).remove();};

    });//1개씩 삭제


    //All check
    $("#allChk").click(function(){
        if ($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            });
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
        }
    });//All check

    //하단 삭제 버튼
    $("#deleteBtn").click(function(){

        //체크 확인
        console.log("체크된 갯수: ",$(".stuChk:checked").length);
        if ($(".stuChk:checked").length == 0){
            alert("삭제할 데이터를 체크하세요.")
            return false;
        }//체크 확인
        
        //삭제 전 확인
        if (!confirm("정말 삭제하시겠습니까?")){
            return false; // no 클릭 --> 다시 돌아감.
        }//삭제 전 확인


        //모든 체크된 박스 삭제
        $(".stuChk").each(function(){
            if ($(this).is(":checked") == true){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });//모든 체크된 박스 삭제

    });//하단 삭제 버튼


});//Jquery