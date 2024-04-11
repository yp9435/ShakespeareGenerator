document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    var form = document.getElementById('text-generation-form');

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Validate form input before submitting
        var lengthInput = document.getElementById('length');
        var temperatureInput = document.getElementById('temperature');

        if (!lengthInput.value || !temperatureInput.value) {
            alert('Please enter values for both length and temperature.');
            return;
        }

        // Submit the form if input is valid
        form.submit();
    });
});