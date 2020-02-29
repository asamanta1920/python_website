console.log("Hello World!");
// number, string, boolean, 
let a = 5;
let b = "hello";
let c = true;

console.log(a);
console.log(b);
console.log(c);

let list = [];

let object = {
    name: "Adrita",
    age: 11
};

for (let i = 10; i > 4; i--) {
    console.log(i)
}

$(function() {
    $("#hello").on("click", function() { 
        if ($(this).text() === "Hello") {
            $(this).text("Bye");
        } else {
            $(this).text("Hello");
        }
    })
})