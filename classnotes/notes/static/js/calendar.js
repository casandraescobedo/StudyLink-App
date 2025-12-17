 $(document).ready(function() {
        $('#Register').click(function() {
        event.preventDefault(); 
        window.location.href = '../html/register.html'; 
        });

        $('#Login').click(function() {
        event.preventDefault(); 
        window.location.href = '../html/createsession.html'; 
        });
      });