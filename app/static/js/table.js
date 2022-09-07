/**
 * Functioning initialising the JQuery Datatable with the specified settings.
 */
function initialiseDatatable(){
    $(document).ready(function () {
        $('#raw_data_table').DataTable({
            iDisplayLength: 15,
            lengthMenu: [[10, 15, 25, 50, -1], [10, 15, 25, 50, "All"]],
            responsive: {
                details: {
                    type: "column",
                    target: "tr"
                }
            },
            columnDefs: [{
                className: "control",
                orderable: false,
                targets: 0
            }],
            order: [[0, "desc"]],
        });
    });
}
