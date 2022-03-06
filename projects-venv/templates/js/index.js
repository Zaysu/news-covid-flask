function data(){
    const now = new Date;
    const time = now.getDate();
    const time2 = now.getMonth();
    const time3 = now.getFullYear();
    document.getElementById('data').innerHTML = `
    <p id="resultado-value">“Data Presente: ${time}/ ${time2}/ ${time3} ” </p>
  `; 

}