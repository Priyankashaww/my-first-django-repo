$(document).ready(function(){
  $("#btnSignup").click(function(){
    var fullname = $("#nameFull").val();
    var username = $("#nameUser").val();
    var email = $("#textEmail").val();
    var number = $("#phoneNumber").val();
    var password = $("#txtPswd").val();
    var confirmpassword = $("#confmPswd").val();
    
    var errmsg = '';
    if(fullname == ''){
        errmsg = "- Enter your full name";
    }
    if(username == ''){
        if(errmsg == ''){
            errmsg = "- Enter your username";
          }else {
            errmsg += "\n - Enter your username";
          }
    }
    if(email == ''){
        if(errmsg == ''){
            errmsg = "- Enter Email";
          }else {
            errmsg += "\n - Enter Email";
          }
    }
    if(number == ''){
        if(errmsg == ''){
            errmsg = "-Enter your phone number";
          }else {
            errmsg += "\n -Enter your phone number";
          }
    }
    if(password == ''){
        if(errmsg== ''){
            errmsg ="- Enter the proper password";
        }else{
            errmsg +="\n -Enter the proper password";
        }
    }
    if(confirmpassword == ''){
        if(errmsg== ''){
            errmsg="-enter confim password";
        }else{
            errmsg +="\n- Enter confim password";
        }
    }else{
        if(password != confirmpassword)
        {
            if(errmsg== ''){
                errmsg="-Password and Confirm password should match";
            }else{
                errmsg +="\n- Password and Confirm password should match";
            }
        }
    }
    if (!$("input[type='radio']").is(':checked')) {
        if(errmsg== ''){
            errmsg="-Select Gender";
        }else{
            errmsg +="\n- Select Gender";
        }
     }
     
    if(errmsg == ''){
        return true;
    }else {
        alert(errmsg);
        return false;
    }
  });
});

$(document).ready(function(){
   $('phoneNumber').bind('keyup paste',function(){
       this.value = this.value.replace(/[^a-z A-Z]/g, '');
   });
   $('phoneNumber').bind('keyup paste',function(){
      this.value = this.value.replace(/[^0-9]/g, '');
   });
});










<script type="text/javascript">
var picPaths = ['iphone1.png','iphone2.png','iphone3.png'];
var curPic = -1;
//preload the images for smooth animation
var imgO = new Array();
for(i=0; i < picPaths.length; i++) {
imgO[i] = new Image();
imgO[i].src = picPaths[i];
}

function swapImage() {
curPic = (++curPic > picPaths.length-1)? 0 : curPic;
imgCont.src = imgO[curPic].src;
setTimeout(swapImage,2000);
}

window.onload=function() {
imgCont = document.getElementById('imgBanner');
swapImage();
}

</script>




function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
