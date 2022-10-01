function openRequest(evt, documentType) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(documentType).style.display = "block";
    evt.currentTarget.className += " active";
  }

  
$(document).ready(function() {
    $('#residents').DataTable({

      filterDropDown:({
        columns: [
          {
            idx: 3,
							title: "Select Gender",
              autoSize: true
              
          },{
            title: "Select Purok",
            idx: 4,
          }
        ],
        bootstrap: false,
        label: "Filter Table"
      })
    });


    

    
});

// $(document).ready(function() {
//   $('#residents').DataTable({
//     "searching": true
//   });

//   var table = $('#residents').DataTable();

//   var genderIndex = 0;
//   $("#residents th").each(function (i) {
//     if ($($(this)).html() == "Gender") {
//       genderIndex = i; return false;
//     }
//   });

  
//   $.fn.dataTable.ext.search.push(
//     function (settings, data, dataIndex) {
//       var selectedGender = $('#genderFilter').val()
//       var gender = data[genderIndex];
//       if (selectedGender === "" || gender.includes(selectedGender)) {
//         return true;
//       }
//       return false;
//     }
//   );

//   $("#genderFilter").change(function (e) {
//     table.draw();
//   });

//   table.draw();

// });