'use strict';

const data = JSON.parse(document.querySelector('#js-data').textContent);

new DataTable('#patient-list', {
  language: {
    url: data.urls.datatablesLanguage
  },
  ajax: data.urls.patientList,
  columns: [
    { data: 'identification' },
    { data: 'first_name' },
    { data: 'last_name' },
    {
        data: 'id',
        orderable: false,
        searchable: false,
        render: function(id) {
          // A rather hacky way to render a template
          const viewURL = `${data.urls.viewPatient + id}/`
          const updateURL = `${data.urls.viewPatient + id}/`
          const deleteURL = `${data.urls.deletePatient + id}/`
          const template =
            `<div class="options-md">
              <a class="btn btn-outline-dark" href="${viewURL}"
                title="${data.lang.view}">
                <span class="fa-solid fa-eye"</span>
              </a>
              <a class="btn btn-outline-dark" href="${updateURL}"
                  title="${data.lang.edit}">
                <span class="fa-solid fa-pencil"</span>
              </a>
              <a class="btn btn-outline-dark" href="${deleteURL}"
                  title="${data.lang.delete}">
                <span class="fa-solid fa-trash-can"</span>
              </a>
            </div>

            <div class="dropdown options-sm">
              <button class="btn btn-secondary dropdown-toggle" type="button"
                  data-toggle="dropdown">
                <span class="fa-solid fa-bars"></span>
              </button>
              <div class="dropdown-menu">
                <a class="dropdown-item" href="${viewURL}">
                  ${data.lang.view}
                </a>
                <a class="dropdown-item" href="${updateURL}">
                  ${data.lang.edit}
                </a>
                <a class="dropdown-item" href="${deleteURL}">
                  ${data.lang.delete}
                </a>
              </div>
            </div>`;

            return template;
        },
    },
  ],
  orderMulti: false,
});
