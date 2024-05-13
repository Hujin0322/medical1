$(function(){

    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [59,82,98,63,63,78,58,70,67,71];
    let eng = [81,67,53,66,84,98,54,83,87,54];
    let math = [81,53,95,54,54,92,71,59,86,57];
    let total = [221,202,246,183,201,268,183,210,240,182];
    let avg = [73,67,82,61,67,89,61,70,80,60];
    

    //tbody부분 10개 행 생성
    let htmlData = "";
    for (let i=0;i<no.length;i++){
        htmlData += "<tr id="+no[i]+">";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        htmlData += "<td>"+no[i]+"</td>";
        htmlData += "<td>"+name[i]+"</td>";
        htmlData += "<td>"+kor[i]+"</td>";
        htmlData += "<td>"+eng[i]+"</td>";
        htmlData += "<td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td>";
        htmlData += "<td>"+avg[i]+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
    } //for
    

    //html소스를 tbody에 추가
    $("#body").html(htmlData);
    

//최초 실행 부분---------------------------------------------------------------------------


    //입력창 display
    $("#writeBtn").click(function(){
        //alert("test");
        $(".p_all").css("display","block");
    });

    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
    });//입력창 display


    //학생입력확인 버튼
    $("#confirmBtn").click(function(){
        //제이쿼리 --> 괄호O - 자바스크립트 --> 괄호X / 
        //글자: text()-innerText, input의 글자: val()-value, html()-innerHTML 
        console.log("이름: "+$("#name").val());
        //apply(null,arr=배열): 함수 호출
        //console.log(Math.max.apply(null,no)+1); //배열에서 최대값 구하기
        //no.push(Math.max.apply(null,no)+1); //배열 추가
        

        //공백 확인 (name~math까지 if 필요)
        if($("#name").val().length<2){
            alert("이름을 입력해야 등록이 가능합니다.");
            $("#name").focus();
            return false;
        }
        

        //번호 생성은 DB에서 자동으로 부여
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val() //String
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2); //소수점 2자리 반올림
        let i_rank = 0;


        //table tr추가
        let htmlData = "";
        htmlData += "<tr id="+i_no+">";
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

        

    });//학생입력버튼


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