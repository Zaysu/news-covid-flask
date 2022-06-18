const floating_btn = document.querySelector('.floating-btn');
const close_btn = document.querySelector('.close-btn');
const social_panel_container = document.querySelector('.social-panel-container');

floating_btn.addEventListener('click', () => {
	social_panel_container.classList.toggle('visible')
});

close_btn.addEventListener('click', () => {
	social_panel_container.classList.remove('visible')
});

function verifica() {
	if (document.forms[0].email.value.length == 0) {
	  alert('Por favor, informe o seu EMAIL.');
	  document.frmEnvia.email.focus();
	  return false;
	}
	return true;
  }
  
function checarEmail(){
  if( document.forms[0].email.value=="" 
	 || document.forms[0].email.value.indexOf('@')==-1 
	   || document.forms[0].email.value.indexOf('.')==-1 )
	  {
		 alert( "Por favor, informe um E-MAIL válido!" );
		 return false;
	  }
  }