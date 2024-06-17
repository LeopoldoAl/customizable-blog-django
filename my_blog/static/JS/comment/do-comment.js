// Page for working with response object
// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
let externClass = [];
let theId = [];
let input = [];
export let seen_not_seen = 0;
export let myVariables={
    'numberStarts':0,
};

export const nono = () => {
   const accesStars = document.getElementById('five-starts');
   const child = accesStars.children; // Collection of children from accessStars
   const longitude = child.length;
   for(let element=0; element<longitude;element++){
   child[element].addEventListener('click',function(e){
        buttons(longitude,child,e);
    }
    );
   }
};

/*
    long: Elements number inside obj
    obj:  Father object
    event: Event has produced inside object element
           that in this case is document.getElementById('five-starts')
*/
export function buttons(long, obj, event){
    if(!event) event=e.event;
    // Get the name the object changed to number
    myVariables.numberStars = parseNameToNumber(event.target.id);
    // We change the value of the button value
    document.querySelector('[name=value]').value = myVariables.numberStars;
    // Change the color to skyblue to the element clicked
    event.target.style.color='rgb(255, 255, 0)';

    /*
        We iterate the elements number inside the obj
        and we give color skyblue to the stars what to have the number on the name attribute
        less than that it but we give color yellow to all the others.
    */
    for(let i=0;i<long;i++){
       if(i<myVariables.numberStars)  obj[i].style.color="rgb(255, 255, 0)";
       else obj[i].style.color="rgb(255, 255, 255)";
   }
}

export function parseNameToNumber(name){
    let myNumber = 0;
    switch(name){
        case 'one':
            myNumber = 1;
            break;
        case 'two':
            myNumber = 2;
            break;
        case 'three':
            myNumber = 3;
            break;
        case 'four':
            myNumber = 4;
            break;
        case 'five':
            myNumber = 5;
            break;
        default:
            myNumber = 0;
    }
    return myNumber;
}

export function submitData(){

    // form contains the comment has been by user
    const form = document.querySelector('[name=comment]').value.trim();
    alert('ok');
    // We check if the user writes something
    let check= form!=='' ? true: false;
    // If check is true then we send the data
    if(check){

    const sendData = "comment="+encodeURIComponent(form);
    //alert(csrftoken);
    alert(sendData);
    ajaxMethod(sendData,'POST', '/comment', 'msg-comment','txt/html', getCookie('csrftoken'));
    }
}

export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export async function send2(url,data,msg, csrftoken){
try{
    const response = await fetch(url, {
      method: "POST", // or 'PUT'
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
      body: data,
      mode: 'same-origin',
    });

    // We empty the msg
    document.querySelector(`.${msg}`).innerHTML ='Please wait...';

    // We return javascript object from a json object
    const result = await response.text();
    // We access to the hello property from the object
      document.querySelector(`.${msg}`).innerHTML = result ;
      if(result.search('Wao, Nothing has found!')!==-1)
      {
        document.querySelector(`.${msg}`).innerHTML = `<div class='error-search'>${result}</div>`;
      }

}catch(error){
    console.log("Error:", error);
    document.querySelector(`.${msg}`).innerHTML = "There was an error unexpected!" ;
}
}

export async function send8(url,data,msg, csrftoken){
try{
    const response = await fetch(url, {
      method: "POST", // or 'PUT'
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
      body: data,
      mode: 'same-origin',
    });

    // We empty the msg
    //document.querySelector(`.${msg}`).innerHTML =`<div class='waiting'>Please wait...</div>`;

    // We return javascript object from a json object
    const result = await response.text();
    // We access to the hello property from the object
    if(result!=''){
      document.querySelector(`.${msg}`).innerHTML = result ;
      document.querySelector(`.${msg}`).style.opacity = '1';
      document.querySelector(`.${msg}`).style.transition = 'all 5s';
      seen_not_seen = 1;
      }else{
        document.querySelector(`.${msg}`).innerHTML = "Nothing was found" ;
      }


}catch(error){
    console.log("Error:", error);
    document.querySelector(`.${msg}`).innerHTML = "There was an error unexpected!" ;
}
}
export async function send(url,data,msg, csrftoken){
try{
    const response = await fetch(url, {
      method: "POST", // or 'PUT'
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
      body: data,
      mode: 'same-origin',
    });

    // We empty the msg
    document.querySelector(`#${msg}`).innerHTML ='Please wait...';

    // We return javascript object from a json object
    const result = await response.text();
    // We access to the hello property from the object
    if(result!='' && result!="Please, write a comment!")
        {

        if(result!="To comment first should be logged in"){
            document.querySelector(`#${msg}`).innerHTML ='Commentary sends successfully!';
            addHtmlComment(result);
            }
        else
            document.querySelector(`#${msg}`).innerHTML ='To comment first should be logged in';
        cleanDataForm();
        }
    else
        document.querySelector(`#${msg}`).innerHTML = result ;
}catch(error){
    console.log("Error:", error);
    document.querySelector(`#${msg}`).innerHTML = "There was an error unexpected!" ;
}
}

export let work=(id)=>{
    const element = document.querySelector(`#${id}`);
    document.querySelector("#commentary").addEventListener('click',async (e) => {

    // We take the values that we need from a form
    const id = element.id
    const value = element.children[1].value;
    const form = element.children[4].children[0].value;

    // We create an object with data form
    let myobj = {
        'id': id,
        'value': value,
        'comment': form,
    };
    // We convert the object before into json notation
    const sendData=JSON.stringify(myobj);

    send(`${window.location.href}`,sendData,'msg-comment',getCookie('csrftoken'));
    });
};

export let searching=(id)=>
    {
        const element = document.querySelector('.section-middle .section-middle-wrap .section-middle-more-search');
        const elementbase = document.querySelector('.section-middle .section-middle-wrap .section-middle-more-action');
        elementbase.addEventListener('click',async (e) =>
        {
            // We take the values that we need from a form
            const textToSearch = element.value
            // We create an object with data form
            let myobj = {
                'id': id,
                'searching': textToSearch,
            };
            // We convert the object before into json notation
            const sendData=JSON.stringify(myobj);
            send2(`${window.location.href}`,sendData,'searching-exac',getCookie('csrftoken'));
        });
    };


export let notifying=(id)=>
    {

        const elementbase = document.querySelector('.notify');
        //notify.style.opacity = '0';
        if( elementbase!=null){
        elementbase.addEventListener('click',async (e) =>
        {

            // We create an object with data form
            let myobj = {
                'id': id,
                'indentify': seen_not_seen,
            };
            // We convert the object before into json notation
            const sendData=JSON.stringify(myobj);
            //console.log(sendData);
            send8(`${window.location.href}`,sendData,'my-notifications-main',getCookie('csrftoken'));
        });
        }
    };


export async function addHtmlComment(fragmentHtml)
    {
        const newComment = document.getElementById('unique');
        let myComment = document.querySelector('.comments');
        myComment.style.opacity= '0.5';
        externClass = [];
        theId = [];
        newComment.outerHTML = newComment.outerHTML + `${fragmentHtml}`;
        myComment.outerHTML = myComment.outerHTML;
        dateLocalForComment("js-comment-date");
        // We back to put the click event to the Public Comment button
        work('unique');
        addHtmlReply();
        // After we reset we back to put the value to t he myComment variable
        myComment = document.querySelector('.comments');
        myComment.style.transition= 'opacity 2s';
        myComment.style.opacity= '1';
        // We load click event to replies
        showRepliesToReply();
    }

let answer=(idBefore, objData, cookie, myele)=>
    {
        // We convert the object before into json notation
        const sendData=JSON.stringify(objData);
        send3(`${window.location.href}`,sendData,idBefore,cookie, myele);
    };

async function send4(url,data,msg, csrftoken)
{
    try
        {
            const response = await fetch(
               url,
               {
                  method: "POST", // or 'PUT'
                  headers:
                    {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json",
                    },
                  body: data,
                  mode: 'same-origin',
            });

            // We return javascript object from a json object
            const result = await response.text();
                document.querySelector(`.${msg}`).innerHTML=`
                        <div class='see-less'>See less</div>
                        ${result}
                    `;
                dateLocalForComment(`${msg} .js-comment-date`);

    }catch(error)
    {
                console.log("Error:", error);
                //document.querySelector(`#${msg}`).children[0].children[0].children[3].children[0].innerText=result;
    }
}

function addClickReplies(e)
{
  const numberReplies = Number(e.target.parentElement.parentElement.children[0].children[0].innerText);

   // Only run this routines if the replies number is greater than zero;
  if(numberReplies>0){
        if(e.target.className==='s-replies'){
            const actualComment = e.target.parentElement.parentElement.parentElement.parentElement;

            // id of the actual commentary
            const id = Number(actualComment.id.substr(11, actualComment.id.length-11));

            const newElement = document.createElement('div');
            newElement.className = `r${this} twinkling`;
            //newElement.style.display ="flex";
            newElement.style.position ="relative";
            //newElement.style.justifyContent = "end";
            newElement.style.borderTop = "1px solid rgb(0,0,0)";
            newElement.style.borderLeft = "1px solid transparent";
            newElement.style.borderRight = "1px solid transparent";
            newElement.style.borderRadius = "10px";
            //newElement.style.height="30px";
            newElement.style.marginLeft = '43px';
            newElement.style.marginTop = '20px';
            newElement.style.paddingTop = '20px';
            newElement.style.marginBottom = '20px';


            actualComment.after(newElement);
            e.target.className="n-replies";
            newElement.className = `r${this} twinkling-stop`;
            // We transform the object in an JSON object
            const myObject = JSON.stringify({'id':'showReplies','id_value':id,});
            send4(`${window.location.href}`,myObject,`r${this}`, getCookie('csrftoken'));
        }else{
            document.querySelector(`.r${this}`).remove();
            e.target.className="s-replies";
        }
    }
};
function showRepliesToReply()
{
    // Reset the element with the 's-replies' class
    document.querySelectorAll('.comment-reply>.right-side>.re-sen-com>.comment-reply-re').forEach(
        function(e){
            e.children[0].className="s-replies";
        }
    );

    document.querySelectorAll('.comment-reply>.right-side>.re-sen-com>.comment-reply-re').forEach(
        function(element, index){
            // If there is a new comment we delete all of the element with class r${index}
            const deleted =  cleanRepliesToReply(index);
            if(deleted===0) element.children[0].className="s-replies";
            element.addEventListener('click', addClickReplies.bind(index));

        }
    );
}

function cleanRepliesToReply(index){
    const longitude = document.querySelectorAll(`.r${index}`).length;
    if(longitude>0) {document.querySelector(`.r${index}`).remove(); return 0;}
    return 1;
}
showRepliesToReply();

export function addHtmlReply(numberElement=11)
    {
        // we access to all form elements on the page
        document.querySelectorAll('.comment-reply').forEach((element, index)=>{
        let myId = element.id;
                if(myId != undefined)
                {
                    if (myId.substring(0,numberElement)=='old-comment')
                    {
                         input = element.children[1].children[3].children[2].children[0];

                         /*
                           Inside of externClass we put all of boolean values that change when the user does
                           click on the Ryply button.
                           Besides inside the theId we put all of the ids of the form that contains
                           the Reply button
                          */
                          externClass.push(true);
                          theId.push(myId);
                          // With addClickComment.bind we pass an array with the variable
                          // that we will use.
                          input.addEventListener('click',
                          addClickComment.bind([externClass,theId, myId, element]), true);

                    }
                }
        });

    }

function addClickComment(e)
{
    let ino1=-1;
    /*
        We accesss to the index where i is equal to myId and the return inside of
        ino1
    */
    this[1].filter((i,index)=>{if(i==this[2]){ino1=index; return i;}});
    // We access to the corresponding boolean value keep it on the externClass variable
    if(this[0][ino1]==true)
    {
                const childCreated = document.createElement("div");
                // We access to the full name of user
                const full_name = this[3].children[1].children[1].children[0].innerText.trim();
                /*
                    We divide the full_name with 'split(' ') and return the elements of the recent created
                    array that it's not empty.
                */
                const arrayFullName = full_name.split(' ').filter((i) => {return i;},'');
                const first_name = arrayFullName[0];// We access to the first name
                const last_name = arrayFullName[1];// We access to the last name
                childCreated.innerHTML = `
                                            <div class='answer'>
                                                <div class='userProfile-left'><div class='img-wrap'><img class='userProfile-img' alt='${document.querySelector('.logoSign .logo-sign').alt}' src="${document.querySelector('.logoSign .logo-sign').src}"></div></div>
                                                <div class='userProfile-right'>
                                                    <div class='reply-to-name'>Reply to ${first_name} ${last_name}</div>
                                                    <div class='reply-meta-wrap'><textarea rows='4' class='reply-meta'  placeholder='Write your reply here.'></textarea></div>
                                                    <div class='the-father'><input  class='reply-button ${this[2]}' reply-to-name'' type='button'  value='Public Commentary'></div>
                                                </div>
                                            </div>
                                            `;
                this[3].after(childCreated);
                if(ino1>=0){externClass[ino1] = false;}
                    document.querySelector(`.${this[2]}`).addEventListener('click',(e) =>
                    {
                            let myObj =
                            {
                                    'id': 'answers',
                                    'id_comment':document.querySelector(`.${this[2]}`).className.split(' ')[1].substring(11),
                                    'first_name':first_name,
                                    'last_name':last_name,
                                    'value':document.querySelector(`#${this[2]}`).children[1].children[0].children.length,
                                    'comment':document.querySelector(`#${this[2]}`).children[1].children[2].innerText,
                                    'reply': document.querySelector(`.${this[2]}`).parentElement.parentElement.children[1].children[0].value,
                            };
                            if (myObj.reply=='') {alert('Please, write a reply'); ;return;}
                            answer(this[2], myObj,getCookie('csrftoken'), ino1);
                    }
                    );
    }else
    {
        // We remove the parent element that contains this[2]
        document.querySelector(`.${this[2]}`).parentElement.parentElement.parentElement.parentElement.remove();
        // We put the oldest value by default to true
        this[0][ino1] = true;
    }

}


export async function cleanDataForm()
    {
        document.querySelector('[name=value]').value=0;
        document.querySelector('[name=comment]').value='';
    }


export async function send3(url,data,msg, csrftoken, var1)
    {
        try
        {
            const response = await fetch(
               url,
               {
                  method: "POST", // or 'PUT'
                  headers:
                    {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json",
                    },
                  body: data,
                  mode: 'same-origin',
            });

            // We empty the msg
            //document.querySelector(`#${msg}`).innerHTML ='Please wait...';

            // We return javascript object from a json object
            const result = await response.text();
            // We access to the hello property from the object
            if(result==='To comment first should be logged in')
                {
                    alert(result) ;
                    document.querySelector(`.${msg}`).parentElement.parentElement.parentElement.parentElement.remove();
                    externClass[var1]=true;
                }else if(result==='Please, write a reply'){
                    alert(result) ;
                }else{
                    const replyActual = Number(document.querySelector(`#${msg} .comment-number>p`).innerText);
                    document.querySelector(`#${msg} .comment-number>p`).innerText=Number(result)+replyActual;
                    document.querySelector(`.${msg}`).parentElement.parentElement.parentElement.parentElement.remove();;
                    externClass[var1]=true;
                }
        }catch(error)
        {
            console.log("Error:", error);
            //document.querySelector(`#${msg}`).children[0].children[0].children[3].children[0].innerText=result;
        }
    }

function changeShitfComment(dateAndTime){
    if(dateAndTime.search('Written,')===-1) return -1;
    const divideSpace = Number(dateAndTime.split(' ')[1]);
    const whatIs = dateAndTime.split(' ')[2];
    let countMilliseconds = 0;
    switch(whatIs){
        case 'second':
            countMilliseconds = Math.round(divideSpace * 1000);
            break;
        case 'seconds':
            countMilliseconds = Math.round(divideSpace * 1000);
            break;
        case 'minute':
            countMilliseconds = Math.round(divideSpace * 60 * 1000);
            break;
        case 'minutes':
            countMilliseconds = Math.round(divideSpace * 60 * 1000);
            break;
        case 'hour':
            countMilliseconds = Math.round(divideSpace * 60 * 60 * 1000);
            break;
        case 'hours':
            countMilliseconds = Math.round(divideSpace * 60 * 60 * 1000);
            break;
        case 'day':
            countMilliseconds = Math.round(divideSpace * 24 * 60 *60 * 1000);
            break;
        case 'days':
            countMilliseconds = Math.round(divideSpace * 24 * 60 *60 * 1000);
            break;
        case 'year':
            countMilliseconds = Math.round(divideSpace * 365 * 24 * 60 *60 * 1000);
            break;
        case 'years':
            countMilliseconds = Math.round(divideSpace * 365 * 24 * 60 *60 * 1000);
            break;
        case 'century':
            countMilliseconds = Math.round(divideSpace * 100 * 365 * 24 * 60 *60 * 1000);
            break;
        case 'centuries':
            countMilliseconds = Math.round(divideSpace * 100 * 365 * 24 * 60 *60 * 1000);
            break;
        case 'millennium':
            countMilliseconds = Math.round(divideSpace * 100 * 365 * 24 * 60 *60 * 1000);
            break;
        case 'millenniums':
            countMilliseconds = Math.round(divideSpace * 100 * 365 * 24 * 60 *60 * 1000);
    }
    return countMilliseconds;
}

// This function puts the date when the comment has produced in the same way that the user server
export function dateLocalForComment(names){
        document.querySelectorAll(`.${names}`).forEach((element, i) =>
            {
                const distanceFromToday = changeShitfComment(element.innerText);
                if(distanceFromToday!==-1 && confirmShowComment() === 0)
                {
                    const today = Date.now();
                    const dateOfComment = new Date(today - distanceFromToday).toLocaleString();

                    element.innerText = dateOfComment;
                    element.style.transition = `opacity ${2*i}s`;
                    element.style.opacity = '1';
                }else{
                    element.style.transition = `opacity ${2*i}s`;
                    element.style.opacity = '1';
                }

            }
        );

}
function confirmShowComment()
{
    const get = Number(document.querySelector(".js-show").innerText);
    return get
}