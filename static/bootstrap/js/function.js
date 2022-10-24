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


  
// Resident Table List
  var buttonConfigResident = [];
  var exportTitle = "ExportTableData"
  buttonConfigResident.push({
                      extend:'copyHtml5',
                      text: '<i class="lar la-copy fs-3" style="vertical-align: middle;"></i>'+
                      '<span style="vertical-align: middle;">Copy<span>',
                      exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                      title: "Registered Resident"
                    });
  
  
  buttonConfigResident.push({
                      extend:'excelHtml5',
                      text: '<i class="las la-file-excel fs-3" style="vertical-align: middle;"></i>'+
                      '<span style="vertical-align: middle;">Excel<span>', className: 'btn-success',
                      exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                      title: "Registered Resident"
                    });
  
  buttonConfigResident.push({
                    extend:'csvHtml5',
                    text: '<i class="las la-file-csv fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">CSV<span>', className: 'btn btn-dark',
                    exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                    title: 'Registered Resident'
                    });
  
  buttonConfigResident.push({
                    extend:'pdfHtml5',
                    text: '<i class="lar la-file-pdf fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">PDF<span>',className: 'btn btn-danger',
                    exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                    title: "Registered Resident"
                    });
                            
  buttonConfigResident.push({
                    extend:'print',
                    text: '<i class="las la-print fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">Print<span>',className: 'btn-warning',
                    exportOptions: { columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible' },
                                   title: "Registered Resident",
                                   
                    });
  
$(document).ready(function() {
    var table = $('#residents').DataTable({
      buttons: buttonConfigResident,
      stateSave: true
    });
    table.buttons().container().appendTo($('#test'));

    yadcf.init(table, [
      {
          column_number : 3, 
          filter_default_label: "All",
          filter_container_id: "gender",
          data: ["Male", "Female"],
          filter_match_mode : "exact",
          style_class: 'form-select',
          filter_reset_button_text: false

      },
      {
        column_number : 4, 
        filter_default_label: "All",
        filter_container_id: "purok",
        filter_match_mode : "exact",
        data: ["Purok I", "Purok II", "Purok III", "Purok IV", "Purok V", "Purok VI"],
        style_class: 'form-select',
        filter_reset_button_text: false

    }
  
    ]);
});

$('span').each(function(){
  $(this).html(
       $(this).html()
      .replace(
             /(?<!-)(\Male\b)(?!([^<]+)?>)(?!-)/, 
            '<span class="male-style"><i class="las la-male"></i>Male</span>'
       )
   );
});

$('span').each(function(){
  $(this).html(
       $(this).html()
      .replace(
             /(?<!-)(\Female\b)(?!([^<]+)?>)(?!-)/, 
            '<span class="female-style"><i class="las la-female"></i>Female</span>'
       )
   );
});
// End Resident Table List


$(document).ready( function () {
  var table = $('#doc_track').DataTable({
    aaSorting: [[2, 'desc']]
  });

  $('#doc_track')
  .find('span')
    .each(function () {
      if ($(this).html() == 'Released') {
        $(this).addClass('released-status');
      }
      if ($(this).html() == 'Ready') {
        $(this).addClass('ready-status');
      }
      if ($(this).html() == 'Pending') {
        $(this).addClass('pending-status');
      }
  });

  yadcf.init(table, [
    {
        column_number : 1, 
        filter_default_label: "All Document",
        filter_container_id: "docu_type",
        data: ["Barangay Clearance", "Certificate of Indigency", "Business Permit", "Building Permit", "Certificate of Residency"],
        filter_match_mode : "exact",
        style_class: 'form-select',
        filter_reset_button_text: false

    },

    {
      column_number : 5, 
      filter_default_label: "All",
      filter_container_id: "status",
      data: ["Pending", "Ready", "Released"],
      style_class: 'form-select',
      filter_reset_button_text: false

    }
]);
});
