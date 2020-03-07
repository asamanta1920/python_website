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

let player_turn = 1;

$(function() {
    $("#zero").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#zero").prop("disabled", true);
    })
})

$(function() {
    $("#one").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#one").prop("disabled", true);
    })
})

$(function() {
    $("#two").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#two").prop("disabled", true);
    })
})

$(function() {
    $("#three").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#three").prop("disabled", true);
    })
})

$(function() {
    $("#four").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#four").prop("disabled", true);
    })
})

$(function() {
    $("#five").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#five").prop("disabled", true);
    })
})

$(function() {
    $("#six").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#six").prop("disabled", true);
    })
})

$(function() {
    $("#seven").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#seven").prop("disabled", true);
    })
})

$(function() {
    $("#eight").on("click", function() { 
        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
        } else {
            $(this).text("O");
            player_turn ++;
        }
        // player_turn ++;
        $("#eight").prop("disabled", true);
    })
})