
//     document.getElementById("formdata").addEventListener("submit", function(e){
//     e.preventDefault();
  
//     name = document.getElementById("name").value;
//     email = document.getElementById("email").value
//     subject = document.getElementById("subject").value
	
//   const formData = new FormData();
//   //console.log(name);
//   formData.append('name', name);
//   formData.append('email', email);
//   formData.append('subject', subject);
//   formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');
//   console.log(formData);
//   fetch('{% url "contact" %}', {
//     method: 'POST',
//     body: formData
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log('Success:', data);
//   })
//   .catch(error => {
//     console.error('Error:', error);
//   });
//   });

document.querySelector("#momo").addEventListener('click', function(){
    document.querySelector("#payment_method").value = 'MO';
})
document.querySelector("#om").addEventListener('click', function(){
    document.querySelector("#payment_method").value = 'OM';
})
document.querySelector("#tron").addEventListener('click', function(){
    document.querySelector("#payment_method").value = 'TR';
})
document.querySelector("#usdt").addEventListener('click', function(){
    document.querySelector("#payment_method").value = 'US';
})