$( document ).ready(function() {
    console.log( "ready!" );
// alert('function')
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; 

var yyyy = today.getFullYear();
// alert(mm)
// alert(dd)
// alert(yyyy)
if(dd<10){
    dd='0'+dd;
} 
if(mm<10){
    mm='0'+mm;
} 
var t = String(yyyy)+"-"+String(mm)+"-"+String(dd)
// alert(t)
// 2142018
// 2018-02-13
    // $('#buttondata').val("2018-02-13");
    $('#buttondata').val(t);
    $('#buttonid').val(t);
    // alert('buttonid')

// var modal = document.getElementById('myPopupModal');
		  // var span = document.getElementsByClassName("close")[0];

		 // modal.style.display = "none";

		//  span.onclick = function() {
  //   		modal.style.display = "none";
		// }

});
// this for date getin details start
$("#date_submit_btn").click(function(){
  inputdat=$("#buttondata").val()
  inputdat2=$("#buttonid").val()
  // alert(inputdat);
  if(inputdat!="" && inputdat2!="")
  {
  	$.ajax({
			type:"GET",
			url:"/process/task_call/",
 			data:{"check_date1":inputdat,"check_date2":inputdat2},
 			success:function(data)
			{
				// alert(data.task_info);
				$("#tableData").html(data.task_info);
				// alert("success");
			}
		});
	}
	else{
		alert("Please select dates ")

	}

});
// this for date getin details end


// ##########  changing frames in rendre layers popup start  ########
function myFunction() {
    var x = document.getElementById("fname");   
    
    // $('#thirdinfo').val(finalinfo)
  // alert(finalinfo);
  // alert(event.target.id)
  first_id = event.target.id;
  newdata=first_id.split("-")[1]
  // alert(newdata);
  newfirstinfo="#firstinfo-"+newdata
  newsecondinfo="#secondinfo-"+newdata
  // alert(newsecondinfo)
  newthirdinfo="#thirdinfo-"+newdata
  // alert(newthirdinfo)
  f_value=$(newfirstinfo).val()
  s_value=$(newsecondinfo).val() 
  // chekboxdata=$(nam).val() 
  // alert(s_value);
  // alert(t_value);
  subinfo=s_value-f_value
  $(newthirdinfo).val(subinfo)
}

//  #########  changing frames in rendre layers popup end ########


// ######### render layers popup code start ######
$("#submitvar").click(function(){
// alert("sub")
iddetails=$('#getidinfo').html()
alert(iddetails);
aa=$('input[name="newcheck"]')
alert(aa.length)
var final_array = new Array();
for(i=0; i<aa.length; i++)
{
  if(aa[i].checked==true)
  {

    array1 = []
    // alert(aa[i].id)
    check_box_id = aa[i].id
    newdata=check_box_id.split("-")[1]
    alert(newdata)
    newfirstinfo="#firstinfo-"+newdata
    newsecondinfo="#secondinfo-"+newdata  
    newthirdinfo="#thirdinfo-"+newdata
    newfourthinfo="#priority-"+newdata
    newfifthinfo="#render-"+newdata
    from_frame=$(newfirstinfo).val()
    to_frame=$(newsecondinfo).val()
    total_frame=$(newthirdinfo).val()
    priority=$(newfourthinfo).val()
    render_depth=$(newfifthinfo).val()  
     array1.push(newdata)     
     array1.push(from_frame)
     array1.push(to_frame)
     array1.push(total_frame)
     array1.push(priority)
     array1.push(render_depth)
     array1.push(iddetails)

     final_array.push(array1)

  }
  else{
    alert("Please  check data")
  }

}
alert(final_array)

$.ajax({
  type:"GET",
      url:"/process/renderinfo/",
      data:{"renderdetails":final_array},
      success:function(data)
      {
        alert("hi success")
      }

  });

  //   $("input[name='newcheck']").each( function () {
  //       alert($(this).val());
  // });
});
// ######### render layers popup code end #####


// ######### Re-allotment popup code start #####

$(".reAllotBtn").click(function(){

	var modal = document.getElementById('myPopupModal');
		  var span = document.getElementsByClassName("close")[0];

		 modal.style.display = "none";

		 span.onclick = function() {
    		modal.style.display = "none";
		}

 		// alert("ds s done");
 		alert(this.id);
 		var task_id = this.id;
 		console.log(this.id);

		$("#task_id_popup").html("Reallotment of Task No: "+task_id)

 		// to visible our modal popup
 		modal.style.display = "block";

 			});

// ######### Re-allotment popup code end #####


// ========== Re-allotment update code start =======

$("#iddata").click(function(){
	var iddataget=$("#exampleFormControlSelect2").val();
	//alert(iddataget);
	task_id_from_h2 = 
	$("#task_id_popup").html();

	//  Reallotment of Task No: 13
	// alert(task_id_from_h2.split(":")[1]);
	var id = task_id_from_h2.split(":")[1];

	// to update task with assigned username
	console.log(id);
	console.log(iddataget);
	$.ajax({
			type:"GET",
			url:"/process/reallot_update/",
 			data:{"assign_id":iddataget,"task_id":id},
 			success:function(data)
			{
				// alert(data.msg);
				var modal = document.getElementById('myPopupModal');
				modal.style.display = "none";

			}
			});	


	});

// ========== Re-allotment update code end =======



//=========== Render layers popup code start =============

$(".renderbtn").click(function(){
  alert("hii")
  alert(this.id)
id=this.id  
$('#getidinfo').html(id.split("_")[1])

  var modal = document.getElementById('render_popupinfo');
      var span = document.getElementsByClassName("close1")[0];

     modal.style.display = "block";

     span.onclick = function() {
        modal.style.display = "none";
    }

  });

//=========== Render layers popup code end ============= 

//=========== Render layers popup code start =============

$(".RenderBtn").click(function(){
  alert("hii")
  alert(this.id)
id=this.id  
$('#getidinfo').html(id.split("_")[1])

  var modal = document.getElementById('render_popupinfo');
      var span = document.getElementsByClassName("close1")[0];

     modal.style.display = "block";

     span.onclick = function() {
        modal.style.display = "none";
    }

  });

//=========== Render layers popup code end ============= 