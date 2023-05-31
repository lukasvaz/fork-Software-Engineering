    
    /* this function get the selected value in transactio_type option field and send an ajax request  to the database 
        and  rendering the Json response into the table in an  asychronus way */
        async function updateTable(e) {
            const selectType = document.getElementById('transaction_type');
        var selectedType = selectType.value;
        const xhttp = new XMLHttpRequest();
        var url = "get-table/All".replace(/0/, selectedType.toString());
        
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                const response = this.response;
                var table=document.getElementById('home-table')
                table.innerHTML='';
                var json_response=JSON.parse(response)
                
                for(var i in json_response){
                    var transaction=json_response[i];
                    var row=document.createElement('tr');                
                    createColumn(row,transaction,'set_at','th')
                    createColumn(row,transaction,'description','td')
                    createColumn(row,transaction,'amount','td')
                    createColumn(row,transaction,'category','td')
                    createColumn(row,transaction,'type','td')
                    table.appendChild(row);
                }
          }
        }
        xhttp.open("GET", url);
        xhttp.send();
    }
    /* this function get a  row and add columns nodes to it */
    function createColumn(row,transaction,atr,type){
        var column=document.createElement(type);
            column.innerText=transaction[atr];
            row.appendChild(column)
        }
