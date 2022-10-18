
// issued Documents
var buttonConfig = [];
var exportTitle = "ExportTableData"
buttonConfig.push({
                    extend:'copyHtml5',
                    text: '<i class="lar la-copy fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">Copy<span>',
                    exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                    title: "Issued Documenents"
                  });


buttonConfig.push({
                    extend:'excelHtml5',
                    text: '<i class="las la-file-excel fs-3" style="vertical-align: middle;"></i>'+
                    '<span style="vertical-align: middle;">Excel<span>', className: 'btn-success',
                    exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                    title: "Issued Documenents"
                  });

buttonConfig.push({
                  extend:'csvHtml5',
                  text: '<i class="las la-file-csv fs-3" style="vertical-align: middle;"></i>'+
                  '<span style="vertical-align: middle;">CSV<span>', className: 'btn btn-dark',
                  exportOptions: {columns: [ 0, 1, 2, 3, 4, 5, 6 ], rows: ':visible'},
                  title: "Issued Documenents"
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


var minDate, maxDate;
 
// Custom filtering function which will search data in column four between two values
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        let min = moment($('#min').val(), 'YYYY-MM-DD', true).isValid() ?
            moment($('#min').val(), 'YYYY-MM-DD', true).unix() :
            null;
        
         let max = moment($('#max').val(), 'YYYY-MM-DD').isValid() ?
             moment( $('#max').val(), 'YYYY-MM-DD', true ).unix():
             null;
        var date = moment( data[4], 'YYYY-MM-DD', true ).unix();
      
      console.log("min: " + min + ' ' + $('#min').val())
      console.log($('#min').val() + ": " + moment($('#min').val(), 'YYYY-MM-DD', true).isValid())
      console.log("max: " + max + ' ' + $('#min').val())

        if (
            ( min === null && max === null ) ||
            ( min === null && date <= max ) ||
            ( min <= date   && max === null ) ||
            ( min <= date   && date <= max )
        ) {
            return true;
        }
        return false;
    }
);

$(document).ready(function () {

    // Create date inputs
    minDate = new DateTime($('#min'), {
        format: 'YYYY-MM-DD'
    });
    maxDate = new DateTime($('#max'), {
        format: 'YYYY-MM-DD'
    });

    // DataTables initialisation
    var table = $('#report_table').DataTable({
        
        aaSorting: [[4, 'asc']],
        buttons:buttonConfig
    });
    table.buttons().container().appendTo($('#test'));

    yadcf.init(table, [
        {
            column_number : 2, 
            filter_default_label: "All Document",
            filter_container_id: "docu_type",
            data: ["Barangay Clearance", "Certificate of Indigency", "Business Permit", "Building Permit", "Certificate of Residency"],
            filter_match_mode : "exact",
            style_class: 'form-select',
            filter_reset_button_text: false

        }
  ]);

    // Refilter the table
    $('#min, #max').on('change', function () {
        table.draw();
    });

});
// issued Documents End