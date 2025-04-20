function showForm(formId) {
    const forms = document.querySelectorAll('.form-container');
    forms.forEach(form => form.style.display = 'none');
  
    const target = document.getElementById(formId);
    if (target) {
      target.style.display = 'block';
    }
  }
  