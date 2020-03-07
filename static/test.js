// console.log("Hello World!");
// // number, string, boolean, 
// let a = 5;
// let b = "hello";
// let c = true;

// console.log(a);
// console.log(b);
// console.log(c);

// let list = [];

// let object = {
//     name: "Adrita",
//     age: 11
// };

// for (let i = 10; i > 4; i--) {
//     console.log(i)
// }

// $(function() {
//     $("#hello").on("click", function() { 
//         if ($(this).text() === "Hello") {
//             $(this).text("Bye");
//         } else {
//             $(this).text("Hello");
//         }
//     })
// })

$(function() {
    let player_turn = 1;
    let board = new Array(9).fill("_");
    $(".game").on("click", function() { 
        let id = $(this).prop("id");

        if (player_turn % 2 === 0) {
            $(this).text("X");
            player_turn ++;
            board[id] = "X";
        } else {
            $(this).text("O");
            player_turn ++;
            board[id] = "O";
        }
        let status = checkWin(board);
        console.log(status);

        if (status === "X" || status === "O") {
            $(".game").prop("disabled", true);
            $("#winner").text(`Player ${status} wins!`);
            $("#reload").show();
            sendResult(status);
        } else if (status === "T") {
            $("#winner").text("It's a tie");
            $("#reload").show();
            sendResult(status);
        }

        // player_turn ++;
        $(this).prop("disabled", true);
        console.log(board);
    })
    $("#reload").on("click", function() {
        player_turn = 1;
        board = new Array(9).fill("_");
        $(this).hide();
        $(".game").prop("disabled", false).text('_');
        $("#winner").text("");
    })
})

function sendResult(status) {
    $.post("/scoreUpload", {status: status});
}

function checkWin(board) {
    if(board[0] == board[1] && board[1] == board[2] && board[0] != "_") {
        return board[0];
    } else if(board[3] == board[4] && board[4] == board[5] && board[3] != "_") {
        return board[3];
    } else if(board[6] == board[7] && board[7] == board[8] && board[6] != "_") {
        return board[6];
    } else if(board[0] == board[3] && board[3] == board[6] && board[0] != "_") {
        return board[0];
    } else if(board[1] == board[4] && board[4] == board[7] && board[1] != "_") {
        return board[1];
    } else if(board[2] == board[5] && board[5] == board[8] && board[2] != "_") {
        return board[2];
    } else if(board[0] == board[4] && board[4] == board[8] && board[0] != "_") {
        return board[0];
    } else if(board[2] == board[4] && board[4] == board[6] && board[2] != "_") {
        return board[2];
    } else if(board.includes("_")) {
        return "Keep Playing!";
    } else {
        return "T";
    }
}