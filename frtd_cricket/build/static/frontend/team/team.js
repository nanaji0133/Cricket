let container = document.getElementById("container");

(function ()
{
    let xhr = new XMLHttpRequest;
    let xhr1 = new XMLHttpRequest;

    xhr.open("GET", "http://127.0.0.1:8000/team/", true)

    xhr.onload = function ()
    {
        if (this.status === 200)
        {
            let teams = JSON.parse(this.responseText);
            console.log(teams)
            let output = "";


            for (let i in teams)
            {

                output += `<div class="teams"> 
                
                <h1> team name - ${teams[i].team_name}</h1>
                <p> team rank - ${teams[i].team_rank}</p>
                <p> team players - ${teams[i].players} </p>              
                </div>`
            }
            container.innerHTML = output
        }
    }
    xhr.send()
}
)()