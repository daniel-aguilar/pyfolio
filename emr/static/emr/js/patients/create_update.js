"use strict";

$(function() {
    $("input[name='date_of_birth']").datepicker({
        format: "dd/mm/yyyy",
        language: "es",
        endDate: "0d",
    });
});
