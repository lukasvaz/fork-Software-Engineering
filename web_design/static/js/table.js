async function updateTable(e) {
  // Actualiza la tabla y contiene los listeners para los filtros
  const response = await fetch('../get-raw-transactions');
  const data = await response.json();
  var tableBody = document.getElementById('home-table-body');
  tableBody.innerHTML = '';

  for (var i in data) {
    var transaction = data[i];
    const type_url_parameter = transaction['type'] == 'Ingreso' ? 'income' : 'outcome';
    tableBody.innerHTML += `<tr>\
      <th>${transaction['set_at']}</th>\
      <td>${transaction['description']}</td>\
      <td>${transaction['amount']}</td>\
      <td>${transaction['category']}</td>\
      <td>${transaction['type']}</td>\
      <td><a href=${'../modify/' + type_url_parameter + '/' + transaction['id']}><i class="fa-solid fa-pen" id="edit_button"></i></a> \
      <a href=${'../delete/' + type_url_parameter + '/' + transaction['id']}><i class="fa-sharp fa-solid fa-trash"></i></a> \
      <button class="show-modal-transaction" style="border: none; cursor: pointer"><i class="fa-solid fa-eye" style="color: #ed333b;"></i></button></td>\
    </tr>`;
  }

  // Renderiza la tabla con DataTable
  var table = $('#home-table').DataTable({
    dom: 'rtp',
    columns: [
      { name: 'fecha' },
      { name: 'descripcion', orderable: false },
      { name: 'valor', orderable: false },
      { name: 'categoria', orderable: false },
      { name: 'tipo', orderable: false },
      { name: 'opciones', orderable: false }
    ],
    paging: true,
    info: true,
    searching: true,
    orderFixed: [0, 'desc'], // Orden fijo por fecha
    autowidth: true,
  });

  // Agrega categorías al select (utiliza jQuery para categorías personalizadas agregadas por el usuario)
  table.column('categoria:name').data().unique().each(function (value) {
    $('#select-category').append(`<option value=${value}>${value}</option>`);
  });

  // Filtrar por tipo de transacción
  $('#transaction_type').on('change', function () {
    if ($(this).val() == 'All') {
      table.column('tipo:name').search('').draw();
    } else {
      table.column('tipo:name').search($(this).val()).draw();
    }
  });

  // Filtrar por categoría
  $('#select-category').on('change', function () {
    if ($(this).val() == 'All') {
      table.column('categoria:name').search('').draw();
    } else {
      table.column('categoria:name').search($(this).val()).draw();
    }
  });

  // Filtrar por rango de fechas
  $('#min-date, #max-date').on('change', function () {
    $.fn.dataTable.ext.search.push(function (settings, searchData) {
      var min = new Date($('#min-date').val());
      var max = new Date($('#max-date').val());
      var date = new Date(searchData[0]);

      if (
        (isNaN(min.valueOf()) && isNaN(max.valueOf())) ||
        (isNaN(min.valueOf()) && date <= max) ||
        (min <= date && isNaN(max.valueOf())) ||
        (min <= date && date <= max)
      ) {
        return true;
      }
      return false;
    });
    table.draw();
  });
  const showModalButtons = $(".show-modal-transaction");

  showModalButtons.click(function() {
      const rowData = getRowData($(this).closest("tr"));
      const htmlContent = `
      <p>Tipo: ${rowData.type}</p>
      <p>Monto: ${rowData.amount}</p>
      <p>Fecha: ${rowData.date}</p>
      <p>Categoria: ${rowData.category}</p>
      <p>Descripcion: ${rowData.description}</p>`;

      $("#detailed-transaction-modal").html(htmlContent);
      $("#detailed-transaction-modal").modal({
        fadeDuration: 200
      });
  });

  function getRowData(row) {
      const date = row.find("th:eq(0)").text();
      const description = row.find("td:eq(0)").text();
      const amount = row.find("td:eq(1)").text();
      const category = row.find("td:eq(2)").text();
      const type = row.find("td:eq(3)").text();

      return {
          date,
          description,
          amount,
          category,
          type,
      };
  }
}