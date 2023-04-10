'use strict';

$(function() {
    const DATATABLES_LANGUAGE_URL = '/emr/api/datatables/language/';
    const PATIENT_LIST_URL = '/emr/api/patients/';
    const VIEW_PATIENT_URL = '/emr/patients/';
    const UPDATE_PATIENT_URL = '/emr/patients/update/';
    const DELETE_PATIENT_URL = '/emr/patients/delete/';

    $('#patient-list').DataTable({
        language: {
            url: DATATABLES_LANGUAGE_URL,
        },
        ajax: PATIENT_LIST_URL,
        columns: [
            {data: 'identification'},
            {data: 'first_name'},
            {data: 'last_name'},
            {
                data: 'id',
                orderable: false,
                render: function(data, type, row, meta) {
                    var template =
                        '<div>' +
                        '   <a class="btn btn-default" href="' + VIEW_PATIENT_URL + data + '"><span class="glyphicon glyphicon-eye-open" title="Ver"></span></a>' +
                        '   <a class="btn btn-default" href="' + UPDATE_PATIENT_URL + data + '"><span class="glyphicon glyphicon-pencil" title="Editar"></span></a>' +
                        '   <a class="btn btn-default" href="' + DELETE_PATIENT_URL + data + '"><span class="glyphicon glyphicon-trash" title="Borrar"></span></a>' +
                        '</div>';

                    return template;
                },
            },
        ],
        orderMulti: false,
    });
});
