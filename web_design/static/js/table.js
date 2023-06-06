    //updates the table, it contains listener  for  the filters
    async function updateTable(e) {
        const selectType = document.getElementById('transaction_type');
        var selectedType = selectType.value;
        const response = await fetch(`get-table`)
        const data = await response.json();
        var tableBody=document.getElementById('home-table-body')
        tableBody.innerHTML='';

        for(var i in data){
            var transaction=data[i];
            tableBody.innerHTML+=`<tr>\
            <th>${transaction['set_at']}</th>\
            <td>${transaction['description']}</td>\
            <td>${transaction['amount']}</td>\
            <td>${transaction['category']}</td>\
            <td>${transaction['type']}</td>
            <td><i class="fa-solid fa-pen"></i> <i class="fa-sharp fa-solid fa-trash"></i></td></tr>`
            /*ultima  columna  es para  para borrar y modificar, si quieren acceder al id  de la transaccion  deben pedir transaction['id'], 
            como  está  todo en una tabla  se debe recuperar si  es  Ingreso o Egreso */
            /* console.log(transaction['id']) */
                        }    
            
        var table=$('#home-table').DataTable({
            "dom":'rtp',
            columns: [
                { name: 'fecha' },
                { name: 'descripcion',"orderable":false},
                { name: 'categoria',"orderable":false },
                { name: 'valor',"orderable":false },
                { name: 'tipo',"orderable":false },
                { name: 'opciones',"orderable":false }
            ],
            paging:true,
            info:true,
            searching:true,
            "orderFixed":[0,'desc'],//fixed order by date
            autowidth:true,
        });

        //filter by transaction type
        $('#transaction_type').on('change',function() {
            if($(this).val()=='All'){
            table.column('tipo:name').search("").draw()    
            }
            else{
            table.column('tipo:name').search($(this).val()).draw()}
        })

        //filter by date range 
        $('#min-date, #max-date').on('change', function () {
            $.fn.dataTable.ext.search.push(function( settings, searchData, index, rowData, counter ){
                var min = new Date( $('#min-date').val());
                var max = new Date($('#max-date').val());
                var date = new Date( searchData[0] );
              
                 if (
                     ( isNaN(min.valueOf()) && isNaN(max.valueOf()) ) ||
                     ( isNaN(min.valueOf())  && date <= max ) ||
                     ( min <= date   && isNaN(max.valueOf())) ||
                     ( min <= date   && date <= max )
                 ) {
                     return true;
                 }
                 return false;
            })
            table.draw()
            }
            );

    }
    