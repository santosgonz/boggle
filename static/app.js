let score = 0;
const time_element = document.getElementById("seconds");
let time_left = 60;
function countdown(){
   if (time_left > 0){
    time_left --;
    time_element.innerHTML = time_left;
    console.log(time_left);
    // timer to handle well timer lol
    // 
   } 
   else {
    clearInterval(interval)
    alert("Time is up! Your total score is " + score)
   }
}
const interval = setInterval(countdown, 1000);
document.getElementById("word_form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const word_input = document.getElementById("word_input").value;
    

    try {
        // Make the AJAX request using Axios and await the response
        const response = await axios.post("/check_word", { word: word_input });

        //POST http://127.0.0.1:5000/check_word 500 (INTERNAL SERVER ERROR)
        // Handle the response here
        // let score = 0;
    
        if (response.data.result === "ok") {
            score += 1;
            const resultDiv = document.getElementById("result");
            resultDiv.innerHTML = "Score: " + score;
            // alert(score)
            // alert("Congratulations! You found a valid word: " + word_input)
            alert("Youre score is " + score)
        } else if (response.data.result === "not-on-board") {
            alert("The word " + word_input + " is not on the board.");
        } else if (response.data.result === "not-a-word") {
            alert("Sorry, " + word_input + " is not a valid word.");
        }
        // console.log("I like food!");

    } catch (error) {
        console.error(error);
    }

});