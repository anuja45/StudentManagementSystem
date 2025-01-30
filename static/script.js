document.addEventListener("DOMContentLoaded", function() {
    const deleteLinks = document.querySelectorAll("a[href^='/delete/']");
    
    deleteLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            if (!confirm("Are you sure you want to delete this student?")) {
                event.preventDefault();
            }
        });
    });
});

function deleteStudent(id) {
    if (confirm("Are you sure you want to delete this student?")) {
        window.location.href = `/delete/${id}`;
    }
}

function editStudent(id, name, email, age, course) {
    document.querySelector("input[name='name']").value = name;
    document.querySelector("input[name='email']").value = email;
    document.querySelector("input[name='age']").value = age;
    document.querySelector("input[name='course']").value = course;
    document.getElementById("studentForm").action = `/update/${id}`;
}
