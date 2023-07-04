function toggleBalance() {
    var balanceElement = document.querySelector('.balance');
    var toggleButton = document.getElementById('toggle-button');
    var balanceValue = balanceElement.getAttribute('data-balance-value');
  
    if (toggleButton.textContent === 'Ocultar Saldo') {
      balanceElement.textContent = '******';
      toggleButton.textContent = 'Mostrar Saldo';
    } else {
      balanceElement.textContent = addDots(balanceValue);
      toggleButton.textContent = 'Ocultar Saldo';
    }
  }
  