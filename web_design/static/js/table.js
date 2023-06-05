    
    async function updateTable(e) {
        const selectType = document.getElementById('transaction_type');
        var selectedType = selectType.value;
        const response = await fetch(`get-table/${selectedType}`)
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
            "dom":'ltpr',
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
            "orderFixed":[0,'desc'],
            autowidth:true,
        });

        //unable ordering after fixed in date
        table.ordering=false;
        var select = $('<select><option value=""></option></select>')
        .appendTo(
            table.column('tipo:name').header())
        
        var transactionType=$('#transaction_type').on('change',function() {
            console.log($(this).val());
            table.column('tipo:name').search($(this).val()).draw();
       
        })

        //show transaction ordered by date 
        table.column(1).order('asc').draw()
        }
    