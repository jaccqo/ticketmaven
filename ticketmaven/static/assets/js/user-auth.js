$(document).ready(function() {

    const login=()=>{

        $('#login-form').submit(function(e) {
            e.preventDefault(); // Prevent form submission
      
            // Gather form data
            var email = $('#email').val();
            var password = $('#password').val();
            var remember = $('#remember').is(':checked');
            var loginUrl = $(this).data('login-url');
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

            if (!email || !password) {
                $('#login-status').html('<div class="alert alert-danger" role="alert">Please enter both email and password</div>');
                return;
            }

            if (!validateEmail(email)) {
                $('#login-status').html('<div class="alert alert-danger" role="alert">Please enter a valid email address</div>');
                return;
            }
      
            // Send AJAX request
            
            $.ajax({
              url: loginUrl,
              method: 'POST',
              headers: { "X-CSRFToken": csrfToken }, 
              data: {
                email: email,
                password: password,
                remember: remember
              },
              success: function(response) {
                // Handle successful login

                if (response.status === 'success') {
                    $('#login-status').html('<div class="alert alert-success" role="alert">' + response.message + '</div>');
                    setTimeout(function() {
                        window.location.href = response.redirect_url;
                    }, 2000); // 5000 milliseconds = 5 seconds
                } else if (response.status === 'error') {
                    $('#login-status').html('<div class="alert alert-danger" role="alert">' + response.message + '</div>');
                    // Make the login-status yellow
            
                }


              },
              error: function(xhr, status, error) {
                // Handle login error
                console.error(xhr.responseText);
                $('#login-status').html('<div class="alert alert-danger" role="alert">Error: ' + xhr.responseText + '</div>');
              }
            });
          });

    }


    const signup=()=>{

        $('#register-form').submit(function(event) {
            event.preventDefault(); // Prevent the default form submission
            
            // Get form data
            var name = $('#name').val();
            var email = $('#email').val();
            var password = $('#password').val();
            var confirmPassword = $('#password-confirm').val();
            var agreeTerms = $('#terms').prop('checked');
            var signupUrl = $(this).data('signup-url');
            var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
      
            // Validate form fields
            if (!name || !email || !password || !confirmPassword ) {
              $('#signup-status').html('<div class="alert alert-danger" role="alert">All fields are required.</div>');
              return;
            }
            if (!agreeTerms) {
                $('#signup-status').html('<div class="alert alert-danger" role="alert">You must agree to the Terms & Conditions to sign up.</div>');

                return;
              }
      
            if (password !== confirmPassword) {
              $('#signup-status').html('<div class="alert alert-danger" role="alert">Passwords do not match.</div>');
              return;
            }
      
            // AJAX request to sign up the user
            $.ajax({
              type: 'POST',
              headers: { "X-CSRFToken": csrfToken }, 
              url: signupUrl,
              data: {
                name: name,
                email: email,
                password: password,
               
              },
              success: function(response) {
                if (response.status === 'success') {
                  // If signup is successful, display success message
                  $('#signup-status').html('<div class="alert alert-success" role="alert">' + response.message + '</div>');

                  setTimeout(function() {
                  
                }, 2000); // 5000 milliseconds = 5 seconds

                } else {
                  // If there's an error, display error message
                  $('#signup-status').html('<div class="alert alert-danger" role="alert">' + response.message + '</div>');
                }
              },
              error: function(xhr, textStatus, errorThrown) {
                // If there's an error with the AJAX request, display error message
                $('#signup-status').html('<div class="alert alert-danger" role="alert">Error occurred while processing the request.</div>');
              }
            });
          });
    }

    // Function to validate email format using regular expression
    function validateEmail(email) {
        var emailRegex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
        return emailRegex.test(email);
    }


    login();

    signup();

    
  });