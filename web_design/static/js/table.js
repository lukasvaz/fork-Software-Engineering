    
    /* this function get the selected value in transactio_type option field and send an ajax request  to the database 
        and  rendering the Json response into the table in an  asychronus way */
       
        async function updateTable(e) {
            const selectType = document.getElementById('transaction_type');
        var selectedType = selectType.value;
        const xhttp = new XMLHttpRequest();
        var url = "get-table/"+selectedType;        
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                const response = this.response;
                var table=document.getElementById('home-table')
                table.innerHTML='';
                var json_response=JSON.parse(response)
                
                for(var i in json_response){
                    var transaction=json_response[i];
                    table.innerHTML+=`<tr>\
                    <th>${transaction['set_at']}</th>\
                    <th>${transaction['description']}</th>\
                    <th>${transaction['amount']}</th>\
                    <th>${transaction['category']}</th>\
                    <th>${transaction['type']}</th>\
                    `
                }
          }
        }
        xhttp.open("GET", url);
        xhttp.send();
    }