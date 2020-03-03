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
    })
})