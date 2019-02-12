var students = [];
var opt;
var name;
var exit = false;
while(!exit){
    opt = prompt("Choose a option\n 1) Add a student\n 2) Remove a student\n 3) Show student\n 4) Exit");
    console.log(opt);
    switch(opt){
        case "1":
            name = prompt("Name of the student to add.");
            students.push(name);
            alert("Student "+name+" added to the list");
            break;
        case "2":
            name = prompt("Name of the student to remove.");
            if( students.indexOf(name) !== -1  ){
                students.splice( students.indexOf(name), 1 );
                alert(name + " removed from list.");
            }else{
                alert("Student with the name "+ name + " does not exists.");
            }
            break;
        case "3":
            alert("We have "+ students + " as student(s).");
            break;
        case "4":
            exit = true;
            alert("Goodbye!");
            break;
        default:
            alert("Option not valid");
            break;
    }
}
