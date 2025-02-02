'use strict';

function initDataTable() {
  const jsData = JSON.parse(document.querySelector('#js-data').textContent);
  const source = document.getElementById('options-template').innerHTML;
  const template = Handlebars.compile(source);

  new DataTable('#patient-list', {
    language: {
      url: jsData.urls.datatablesLanguage
    },
    ajax: jsData.urls.patientList,
    columns: [
      { data: 'identification' },
      { data: 'first_name' },
      { data: 'last_name' },
      {
        data: 'id',
        orderable: false,
        searchable: false,
        render: function (id) {
          const context = {
            urls: {
              view: `${jsData.urls.viewPatient + id}/`,
              update: `${jsData.urls.updatePatient + id}/`,
              delete: `${jsData.urls.deletePatient + id}/`,
            },
            lang: jsData.lang,
          };

          return template(context);
        },
      },
    ],
    orderMulti: false,
  });
};
initDataTable();
