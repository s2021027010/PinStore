var ischatopen = false;
var ele = document.getElementById("chatbar");

function openChatBox()
{
  if(ischatopen == false)
    {
       ele.classList.add("toggle");
       ischatopen = true;
       document.getElementById("chatOpen").classList.remove("fa-comments");
document.getElementById("chatOpen").classList.add("fa-times");
      
    }
  else {
     ele.classList.remove("toggle");
     ischatopen = false;
    document.getElementById("chatOpen").classList.add("fa-comments");
document.getElementById("chatOpen").classList.remove("fa-times");
  }
}

 

