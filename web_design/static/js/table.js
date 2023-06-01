    
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
                            </tr>`
                        }                
        $('#home-table').DataTable();}
    