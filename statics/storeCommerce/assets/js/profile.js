var btnUpload_img = $("#inputUpImage"),
		btnOuter_img = $(".button_outer_img");
	btnUpload_img.on("change", function(e){
		var ext = btnUpload_img.val().split('.').pop().toLowerCase();
		if($.inArray(ext, ['gif','png','jpg','jpeg']) == -1) {
			$(".error_msg_img").text("Not an Image...");
		} else {
			$(".error_msg_img").text("");
			btnOuter_img.addClass("file_uploading_img");
			setTimeout(function(){
				btnOuter_img.addClass("file_uploaded_img");
			},3000);
			var uploadedFile_img = URL.createObjectURL(e.target.files[0]);
			setTimeout(function(){
				$("#uploaded_view_img").append('<img src="'+uploadedFile_img+'" />').addClass("show");
			},3500);
		}
	});
	$(".file_remove_img").on("click", function(e){
		$("#uploaded_view_img").removeClass("show");
		$("#uploaded_view_img").find("img").remove();
		btnOuter_img.removeClass("file_uploading_img");
		btnOuter_img.removeClass("file_uploaded_img");
	});







$(".nav ul li").click(function() {
    $(this)
      .addClass("active")
      .siblings()
      .removeClass("active");
  });
  
  const tabBtn = document.querySelectorAll(".nav ul li");
  const tab = document.querySelectorAll(".tab");
  
  function tabs(panelIndex) {
    tab.forEach(function(node) {
      node.style.display = "none";
    });
    tab[panelIndex].style.display = "block";
  }
  tabs(0);
  
  let bio = document.querySelector(".bio");
  const bioMore = document.querySelector("#see-more-bio");
  const bioLength = bio.innerText.length;
  
  function bioText() {
    bio.oldText = bio.innerText;
  
    bio.innerText = bio.innerText.substring(0, 100) + "...";
    bio.innerHTML += `<span onclick='addLength()' id='see-more-bio'>See More</span>`;
  }
  //        console.log(bio.innerText)
  
  bioText();
  
  function addLength() {
    bio.innerText = bio.oldText;
    bio.innerHTML +=
      "&nbsp;" + `<span onclick='bioText()' id='see-less-bio'>See Less</span>`;
    document.getElementById("see-less-bio").addEventListener("click", () => {
      document.getElementById("see-less-bio").style.display = "none";
    });
  }
  if (document.querySelector(".alert-message").innerText > 9) {
    document.querySelector(".alert-message").style.fontSize = ".7rem";
  }

  