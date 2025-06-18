const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});


document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault(); // Empêche le rechargement de la page
    
    // Récupération des valeurs
    const first_name = document.querySelector('[name="first_name"]').value.trim();
    const last_name = document.querySelector('[name="last_name"]').value.trim();
    const email = document.querySelector('[name="email"]').value.trim();
    const password = document.querySelector('[name="password"]').value.trim();
    
    // Réinitialisation des erreurs
    clearErrors();
    
    // Validation
    let isValid = true;
    
    // Validation du prénom
    if (!first_name || first_name.length < 2) {
        showError('first_name', "Le prénom doit contenir au moins 2 caractères");
        isValid = false;
    } else if (!/^[a-zA-ZÀ-ÿ\- ]+$/.test(first_name)) {
        showError('first_name', "Caractères invalides dans le prénom");
        isValid = false;
    }
    
    // Validation du nom
    if (!last_name || last_name.length < 2) {
        showError('last_name', "Le nom doit contenir au moins 2 caractères");
        isValid = false;
    } else if (!/^[a-zA-ZÀ-ÿ\- ]+$/.test(last_name)) {
        showError('last_name', "Caractères invalides dans le nom");
        isValid = false;
    }
    
    // Validation de l'email
    if (!email) {
        showError('email', "L'email est obligatoire");
        isValid = false;
    } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
        showError('email', "Format d'email invalide");
        isValid = false;
    }
    
    // Validation du mot de passe
    if (password.length < 8) {
        showError('password', "Le mot de passe doit contenir au moins 8 caractères");
        isValid = false;
    } else if (!/[A-Z]/.test(password)) {
        showError('password', "Le mot de passe doit contenir au moins une majuscule");
        isValid = false;
    } else if (!/[0-9]/.test(password)) {
        showError('password', "Le mot de passe doit contenir au moins un chiffre");
        isValid = false;
    }
    
    // Si tout est valide, soumettre le formulaire
    if (isValid) {
        this.submit();
    }
});

// Fonctions utilitaires
function showError(fieldName, message) {
    const field = document.querySelector(`[name="${fieldName}"]`);
    field.classList.add('is-invalid');
    
    let errorElement = field.nextElementSibling;
    if (!errorElement || !errorElement.classList.contains('invalid-feedback')) {
        errorElement = document.createElement('div');
        errorElement.className = 'invalid-feedback';
        field.parentNode.insertBefore(errorElement, field.nextSibling);
    }
    
    errorElement.textContent = message;
}

function clearErrors() {
    document.querySelectorAll('.is-invalid').forEach(el => {
        el.classList.remove('is-invalid');
    });
    
    document.querySelectorAll('.invalid-feedback').forEach(el => {
        el.textContent = '';
    });
}
document.addEventListener('DOMContentLoaded', function () {
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
      var toast = new bootstrap.Toast(toastEl);
      toast.show();
    });
  });
