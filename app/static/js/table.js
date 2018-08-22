/**
 * Functioning initialising the JQuery Datatable with the specified settings.
 */
function initialiseDatatable(){
    $(document).ready(function () {
        $('#raw_data_table').DataTable({
            "order": [[0, "desc"]],
            "iDisplayLength": 15,
            "lengthMenu": [[10, 15, 25, 50, -1], [10, 15, 25, 50, "All"]]
        });
    });
}
