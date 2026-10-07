let calmSongs = ["Calmly", "Calming", "Calm Song", "Song"];
let sadSongs = ["Sadly", "Saddening", "Sad Song", "Boo Hoo"];
let happySongs = ["Happily", "Cheering", "Happy Song", "Woo Hoo"];
let hypeSongs = ["Get Hype", "Hyped Up", "Get Pumped", "Lets Go"];

function listCalmSongs() {
    console.log("--Printing Calm Songs--")
    for (let i = 0; i < calmSongs.length; i++) {
        console.log(calmSongs[i]);
    }
}

function listSadSongs() {
    console.log("--Printing Sad Songs--")
    for (let i = 0; i < sadSongs.length; i++) {
        console.log(sadSongs[i]);
    }
}

function listHappySongs() {
    console.log("--Printing Sad Songs--")
    for (let i = 0; i < happySongs.length; i++) {
        console.log(happySongs[i]);
    }
}

function listHypeSongs() {
    console.log("--Printing Sad Songs--")
    for (let i = 0; i < hypeSongs.length; i++) {
        console.log(hypeSongs[i]);
    }
}

document.getElementById("buttonCalm").addEventListener("click", listCalmSongs);
document.getElementById("buttonSad").addEventListener("click", listSadSongs);
document.getElementById("buttonHappy").addEventListener("click", listHappySongs);
document.getElementById("buttonHype").addEventListener("click", listHypeSongs);