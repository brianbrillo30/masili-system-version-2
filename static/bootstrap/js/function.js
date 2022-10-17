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
      "dom": '<"panel panel-default"<"panel-heading"<"row"<"col-md-6"l><"col-md-6 text-right"f>>>t<"panel-footer"<"row"<"col-md-6"i><"col-md-6 text-right"p>>>>',

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

var buttonConfig = [];
var exportTitle = "ExportTableData"
buttonConfig.push({
                    extend:'copyHtml5',
                    text: '<i class="lar la-copy fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">Copy<span>',
                    exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'}
                  });


buttonConfig.push({
                    extend:'excelHtml5',
                    text: '<i class="las la-file-excel fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">Excel<span>', className: 'btn-success',
                    exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'}
                  });

buttonConfig.push({
                  extend:'csvHtml5',
                  text: '<i class="las la-file-csv fs-3" style="vertical-align: middle;"></i>'+
                  '<span style="vertical-align: middle;">CSV<span>', className: 'btn btn-dark',
                  exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'}
                  });

buttonConfig.push({
                  extend:'pdfHtml5',
                  text: '<i class="lar la-file-pdf fs-3" style="vertical-align: middle;"></i>'+
                  '<span style="vertical-align: middle;">PDF<span>',className: 'btn btn-danger',
                  exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                  title: "Issued Documenents"
                  });
                          
buttonConfig.push({
                  extend:'print',
                  text: '<i class="las la-print fs-3" style="vertical-align: middle;"></i>'+
                  '<span style="vertical-align: middle;">Print<span>',className: 'btn-warning',
                  exportOptions: { columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible' },
                                 title: "Issued Documenents",
                                 
                  });

$.fn.dataTable.Buttons.defaults.dom.button.className = 'btn btn-primary'
$(document).ready(function () {
  var table = $('#report_table').DataTable({

      filterDropDown:({
        columns: [
          {
              idx: 2,
              title: "All",
              autoSize: true
              
          }
        ],
        bootstrap: false,
        label: "Filter Table"
      }),
      aaSorting: [[4, 'asc']],
      "dom": '<"panel panel-default"<"panel-heading"<"row"<"col-md-6"l><"col-md-6 text-right"f>>>t<"panel-footer"<"row"<"col-md-6"i><"col-md-6 text-right"p>>>>',

      buttons:buttonConfig
  });table.buttons().container().appendTo($('#test'));
});

$(document).ready( function () {
  $('#doc_track').DataTable({
    aaSorting: [[2, 'desc']],
    filterDropDown:({
      columns: [
        {
            idx: 1,
            title: "All Document",
            autoSize: true
            
        },
        {
          idx: 5,
          title: "All Status",
          autoSize: true
          
        }
      ],
      bootstrap: false,
      label: "Filter Document"
    })
  });
} );
