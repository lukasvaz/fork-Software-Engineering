
function createColumn(row,transaction,atr,type){
        var column=document.createElement(type);
        column.innerText=transaction[atr];
        row.appendChild(column)
    }
