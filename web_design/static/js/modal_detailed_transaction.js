$(document).ready(function () { 
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
        $("#detailed-transaction-modal").modal();
    });

    function getRowData(row) {
        const date = row.find("td:eq(0)").text();
        const description = row.find("td:eq(1)").text();
        const amount = row.find("td:eq(2)").text();
        const category = row.find("td:eq(3)").text();
        const type = row.find("td:eq(4)").text();

        return {
            date,
            description,
            amount,
            category,
            type,
        };
    }
});