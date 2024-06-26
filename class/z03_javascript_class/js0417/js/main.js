$(function(){
    //전역변수
    
    // let no = [1,2,3,4,5,6,7,8,9,10];
    // let name = ['홍길동','유관순','이순신','김구','강감찬','홍길순','홍길자','최현묵','이규원','너누구'];
    // let kor = [59,82,98,63,63,78,58,70,67,71];
    // let eng = [81,67,53,66,84,98,54,83,87,54];
    // let math = [81,53,95,54,54,92,71,59,86,57];
    // let total = [221,202,246,183,201,268,183,210,240,182];
    // let avg = [73,67,82,61,67,89,61,70,80,60];
    
    let s_count = 1;//학생번호
    let o_id = "";
    let o_no = 0; //학번
    let o_name = "";
    let o_kor = 0;
    let o_eng = 0;
    let o_math = 0;
    
    //최초 데이터 불러오기
    $.ajax({
        url:"http://127.0.0.1:5500/js0417/json/stu_score.json", //-> ../json/stu_score.json (가능)
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            //alert("데이터 보내기 성공")
            console.log(data);
            s_count = data.length

            let htmlData = "";
            for (let i=0;i<data.length;i++){
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
            };//for
                $("#body").html(htmlData);
        }, //success
        
        error:function(){
            alert("에러")
        }//error

    });//ajax
    
    
//최초 실행 부분---------------------------------------------------------------------------

    //검색버튼 클릭
    $("#searchBtn").click(function(){
        //alert("test")
        if ($("#s_word").val().length<1){
            alert("검색어를 입력하세요.")
            return false;
        };//if문


        let s_word = $("#s_word").val();
        console.log("검색어: "+s_word);

        //최초 데이터 불러오기
        $.ajax({
            url:"http://127.0.0.1:5500/js0417/json/stu_score.json",
            type:"get",
            data:{},
            dataType:"json",
            success:function(data){
                console.log(data);
                s_count = data.length
    
                let htmlData = "";
                for (let i=0;i<data.length;i++){
                    //검색어 if문
                    if (data[i].name.indexOf(s_word) != -1){
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
                    }//검색어 if문

                };//for

                $("#body").html(htmlData);
            }, //success
            
            error:function(){
                alert("에러")
            }//error
    
        });//ajax


    });//검색버튼 클릭


    //입력창 display
    $("#writeBtn").click(function(){
        if ($(".stuChk:checked").length>=1){
            alert("학생 입력을 위해 체크 자동 해제합니다.");
            
            //체크 모두 해제
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });//체크 모두 해제
        }

        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);

    });

    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        //초기화
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });//입력창 display


    //학생입력, 수정 확인 버튼
    $("#confirmBtn").click(function(){
        if ($("#id").val() == ""){ //학생성적입력창 - id value 값이 없는 경우
            //글자: text()-innerText, input의 글자: val()-value, html()-innerHTML 
            console.log("이름: "+$("#name").val());
    
    
            //공백 확인 (name~math까지 if 필요)
            if($("#name").val().length<2){
                alert("이름을 입력해야 등록이 가능합니다.");
                $("#name").focus();
                return false;
            }; //공백 확인
            
            s_count = c_count + 1
            //번호 생성은 DB에서 자동으로 부여
            // let i_no = Math.max.apply(null,no);
            // no.push(i_no);
            let i_no = s_count+1
            let i_name = $("#name").val() //String
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor+i_eng+i_math;
            let i_avg = (i_total/3).toFixed(2); //소수점 2자리 반올림
            let i_rank = 0;
    
            //table tr추가
            let htmlData = "";
            htmlData += "<tr id="+s_count+">";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
            htmlData += "<td>"+i_no+"</td>";
            htmlData += "<td>"+i_name+"</td>";
            htmlData += "<td>"+i_kor+"</td>";
            htmlData += "<td>"+i_eng+"</td>";
            htmlData += "<td>"+i_math+"</td>";
            htmlData += "<td>"+i_total+"</td>";
            htmlData += "<td>"+i_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";
    
            
            //html소스를 tbody에 추가
            //$("#body").html(htmlData); //기존 html에 덮어쓰기
            //$("#body").prepend(htmlData); //기존 html 위쪽에 추가
            $("#body").append(htmlData); //기존 html 뒤쪽에 추가
    
            //input 초기화
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");


        }else{//학생성적수정창 - id value 값이 존재하는 경우
            //alert("학생성적수정창 클릭");
            o_no = $("#id").val();
            o_name = $("#name").val();
            o_kor = Number($("#kor").val());
            o_eng = Number($("#eng").val());
            o_math = Number($("#math").val());
            let o_total = o_kor + o_eng + o_math;
            let o_avg = o_total/3;

            console.log("id: "+o_no);
            console.log("kor: "+o_kor);
            console.log("eng: "+o_eng);
            console.log("math: "+o_math);

            let htmlData = "";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData += "<td>"+o_no+"</td>";
            htmlData += "<td>"+o_name+"</td>";
            htmlData += "<td>"+o_kor+"</td>";
            htmlData += "<td>"+o_eng+"</td>";
            htmlData += "<td>"+o_math+"</td>";
            htmlData += "<td>"+o_total+"</td>";
            htmlData += "<td>"+o_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";
            
            $("#"+o_no).html(htmlData);

            //input 초기화
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");

        };//if, else

    });//학생입력, 수정 버튼


    //전체선택, 취소
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            })
        }     
    });//전체선택, 취소


    //table에 있는 삭제버튼 클릭
    $(document).on("click",".delBtn",function(){ //document의 내용을 처음부터 불러오기
        console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
        if (confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    }); //table 삭제
    
    //동적으로 할당 (=문서 읽은 후 새롭게 추가된 내용)될 경우 실행이 안됨.
    // $(".delBtn").click(function(){
    //     console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
    //     if (confirm("정말 삭제하시겠습니까?")){
    //         $("#"+$(this).parent().parent().attr("id")).remove();
    //     }
    // }); //table 삭제


    //학생수정버튼 클릭
    $("#modifyBtn").click(function(){
        console.log("체크박스에서 체크된 개수: "+$(".stuChk:checked").length);
        
        //1명만 선택 가능
        if ($(".stuChk:checked").length != 1){
            alert("학생 1명만 선택하시오.");
            return false;
        };

        //선택된 체크 데이터 가져오기
        o_id = $(".stuChk:checked").parent()
        o_no = o_id.next().text();
        o_name = o_id.next().next().text();
        o_kor = o_id.next().next().next().text();
        o_eng = o_id.next().next().next().next().text()
        o_math = o_id.next().next().next().next().next().text()
        
        console.log("학번: "+o_id.next().text());
        
        //수정창 열기
        $(".p_all").css("display","block");
        $("#name").prop("readonly",true);
        
        //수정 창 타이틀 변경
        $(".p_main h2").text("학생성적수정");
        $("#id").val(o_no);
        $("#name").val(o_name);
        $("#kor").val(o_kor);
        $("#eng").val(o_eng);
        $("#math").val(o_math);
    
    });//학생수정버튼 클릭


    //하단 삭제 버튼 클릭
    $("#deleteBtn").click(function(){
        //alert("test");
        console.log("체크박스 개수: "+$(".stuChk").length);
        // console.log("체크박스에서 체크된 개수: "+$("input:checkbox[name='stu']:checked").length);
        console.log("체크박스에서 체크된 개수: "+$(".stuChk:checked").length);
        
        //체크되어 있는 것이 없을 경우
        if ($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크하세요.");
            return false;
        }//체크 if

        //현재 체크박스가 체크가 되어 있는지 확인
        if (!confirm("정말 삭제하시겠습니까?")){
            return false; // no 클릭 --> 다시 돌아감.
        }//삭제 if

        //모든 체크박스를 가져오기
        $(".stuChk").each(function(){
            if ($(this).is(":checked") == true){
                console.log("현재 선택된 class 값: "+$(this).val());
                console.log("현재 선택된 id 값: "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        }); //each

    });//하단 삭제 버튼

});//제이쿼리