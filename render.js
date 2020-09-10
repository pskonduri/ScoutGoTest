let input = document.querySelector('#input')
let result = document.querySelector('#result')
let btn = document.querySelector('#btn')

function onclick(){

  fetch(`http://127.0.0.1:5001/${input.value}`).then((data)=>{      
      return data.text();
      
  }).then((text)=>{
    console.log("data: ", text);
    result.textContent = text;
  }).catch(e=>{
    console.log(e);
  })

}


btn.addEventListener("click", () => {
  console.log("Click event listener");

  onclick();
});

btn.dispatchEvent(new Event("click"));

