"use strict";

const lang = JSON.parse(document.getElementById("app-lang").textContent);
const dateFormats = { "es": "dd/mm/yyyy" };

$("input[name='date_of_birth']").datepicker({
    format: dateFormats?.[lang],
    language: lang,
    endDate: "0d",
});
