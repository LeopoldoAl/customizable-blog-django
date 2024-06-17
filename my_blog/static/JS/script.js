window.addEventListener('load',function(){

let dataAll = {
		'menu':document.getElementsByClassName('logomenu')[0],
		'logoSign':document.getElementsByClassName('logoSign')[0],
		'elementNotify':document.querySelector('.notify'),
		'notification':document.querySelector('.my-notifications-main'),
		'logo':document.getElementsByClassName('logo')[0],
		'gostmenu':document.getElementsByClassName('gostmenu')[0],
		'gostdata':document.querySelector('.gostdata'),
		'truegostm':true,
		'truegostd':true,
		'trueNotify':true,
		};


//  We access to all of the links of our page
const links = document.getElementsByTagName('a');
//  We store the amount of links on the page
const amountLink = links.length;

/*
    We assign the click event to all of the links on the page
    like this we prevent that gostdata be showed  when the user is log out and retun
    to before page
*/
for(let i=0; i<amountLink;i++){
    links[i].addEventListener('click', function(){
        dataAll['gostdata'].style.display = 'none';
    });
}

dataAll['menu'].addEventListener('click',function(){
	if( dataAll['truegostm'])	{
		dataAll['positionOfMenuPhotoYGet']=dataAll['menu'].getBoundingClientRect().height;
		dataAll['gostmenu'].style.display = 'flex';
		//dataAll['gostmenu'].style.top = dataAll['positionOfMenuPhotoYGet'] + "px";
		//dataAll['gostmenu'].style.height = (window.innerHeight-dataAll['positionOfMenuPhotoYGet']-1)*1 + "px";
		//dataAll['gostmenu'].style.width = (window.innerWidth)*0.80 + "px";
		//dataAll['gostmenu'].style.overflow = "auto";
		dataAll['truegostm'] = false;
		dataAll['gostdata'].style.display = 'none';
		dataAll['notification'].style.display = 'none';
		dataAll['truegostd'] = true;
	}else{
		dataAll['gostmenu'].style.display = 'none';
		dataAll['truegostm'] = true;
	}
});

dataAll['logoSign'].addEventListener('click',function(){
	if(dataAll['truegostd']) {
		dataAll['positionOfMenuPhotoYGet']=dataAll['logoSign'].getBoundingClientRect().height;
		dataAll['gostdata'].style.display = 'flex';
		//dataAll['gostdata'].style.top = dataAll['positionOfMenuPhotoYGet'] + "px";
		//dataAll['gostdata'].style.height = "fit-content";//(window.innerHeight-dataAll['positionOfMenuPhotoYGet']-1)*1 + "px";
		//dataAll['gostdata'].style.width = "10%";
		//dataAll['gostdata'].style.overflow = 'auto';
		dataAll['truegostd'] = false;
		dataAll['gostmenu'].style.display = 'none';
		dataAll['notification'].style.display = 'none';
		dataAll['truegostm'] = true;
		dataAll['trueNotify'] = true;
	}else{
		dataAll['gostdata'].style.display = 'none';
		dataAll['truegostd'] = true;
	}
});

if(dataAll['elementNotify']!=null){
dataAll['elementNotify'].addEventListener('click',function(){
	if(dataAll['trueNotify']) {
		dataAll['positionOfMenuPhotoYGet']=dataAll['logoSign'].getBoundingClientRect().height;
		dataAll['notification'].style.opacity = '0';
		dataAll['notification'].style.display = 'block';
		//dataAll['gostdata'].style.top = dataAll['positionOfMenuPhotoYGet'] + "px";
		//dataAll['gostdata'].style.height = "fit-content";//(window.innerHeight-dataAll['positionOfMenuPhotoYGet']-1)*1 + "px";
		//dataAll['gostdata'].style.width = "10%";
		//dataAll['gostdata'].style.overflow = 'auto';
		dataAll['truegostd'] = false;
		dataAll['gostmenu'].style.display = 'none';
		dataAll['gostdata'].style.display = 'none';
		dataAll['truegostm'] = false;
		dataAll['trueNotify'] = false;
	}else{
		dataAll['notification'].style.display = 'none';
		dataAll['trueNotify'] = true;
	}
});
}
/*
document.body.addEventListener('click',function(event){
	console.log('X: '+ event.pageX+' Y: '+event.pageY);
});
*/

this.addEventListener('click', function(event){
	// It works only in the perimeter of the photos menu and sign.
		dataAll['positionOfMenuPhotoXGet']=dataAll['menu'].getBoundingClientRect().width;
		dataAll['positionOfMenuPhotoYGet']=dataAll['logoSign'].getBoundingClientRect().height;
		dataAll['positionOfProfilePhotoX'] = dataAll['logoSign'].getBoundingClientRect().x;
        if(dataAll['elementNotify']!=null)
        dataAll['positionOfNotifyX'] = dataAll['elementNotify'].getBoundingClientRect().x;
        if(dataAll['elementNotify']!=null)
        dataAll['positionOfNotifyHeightY'] = dataAll['elementNotify'].getBoundingClientRect().height;

	// It works only in the perimeter of the boxes gostmenu and gostdata.
		dataAll['gostmenuX'] =dataAll['gostmenu'].getBoundingClientRect().width;
		dataAll['gostmenuY'] = dataAll['gostmenu'].getBoundingClientRect().y+dataAll['gostmenu'].getBoundingClientRect().height;
		dataAll['gostdataX'] = dataAll['gostdata'].getBoundingClientRect().x
		dataAll['gostdataY'] = dataAll['gostdata'].getBoundingClientRect().y+dataAll['gostdata'].getBoundingClientRect().height;
		if(dataAll['elementNotify']!=null)
		dataAll['positionOfNotifyWidthX'] =dataAll['elementNotify'].getBoundingClientRect().width;
		dataAll['positionOfNotifyBodyX'] =dataAll['notification'].getBoundingClientRect().x;
        dataAll['positionOfNotifyY'] = dataAll['notification'].getBoundingClientRect().y+dataAll['notification'].getBoundingClientRect().height;

	// Position of the mouse pointer everytime.
		dataAll['distancePointerMouseX'] = event.clientX;
		dataAll['distancePointerMouseY'] = event.clientY;


if(dataAll['positionOfNotifyWidthX']<dataAll['distancePointerMouseX']
	&& dataAll['distancePointerMouseX']<dataAll['positionOfNotifyX']
	&& 74>dataAll['distancePointerMouseY']
	){

		if(dataAll['trueNotify']==false) {
		dataAll['notification'].style.display = 'none';
		dataAll['trueNotify']=true;
		}
		 if( dataAll['truegostm']==false){
		dataAll['gostmenu'].style.display = 'none';
		dataAll['truegostm'] = true;
		}
		 if( dataAll['truegostd']==false){
		dataAll['gostdata'].style.display = 'none';
		dataAll['truegostd'] = true;
		}
	}


	if(dataAll['positionOfMenuPhotoXGet']<dataAll['distancePointerMouseX']
	&& dataAll['distancePointerMouseX']<dataAll['positionOfProfilePhotoX']
	&& dataAll['positionOfMenuPhotoYGet']>dataAll['distancePointerMouseY']
	){

		if(dataAll['truegostd']==false) {
		dataAll['gostdata'].style.display = 'none';
		dataAll['truegostd'] = true;
		}
		 if( dataAll['truegostm']==false){
		dataAll['gostmenu'].style.display = 'none';
		dataAll['truegostm'] = true;
		}

	}

	if(dataAll['truegostm']==false){
	let condition1=dataAll['gostmenuX']<dataAll['distancePointerMouseX'] 
		&& dataAll['positionOfMenuPhotoYGet']<dataAll['distancePointerMouseY'] && dataAll['distancePointerMouseY']<dataAll['gostmenuY'];
	let condition2=dataAll['gostmenuY']<dataAll['distancePointerMouseY'];
	if(condition1 || condition2){
		dataAll['gostmenu'].style.display = 'none';
		dataAll['truegostm'] = true;
	}
}
	if(dataAll['truegostd']==false){
			let condition1=dataAll['gostdataX']>dataAll['distancePointerMouseX'] 
		&& dataAll['positionOfMenuPhotoYGet']<dataAll['distancePointerMouseY'] && dataAll['distancePointerMouseY']<dataAll['gostdataY'];
			let condition2=dataAll['gostdataY']<dataAll['distancePointerMouseY'];
		if(condition1 || condition2){
			dataAll['gostdata'].style.display = 'none';
			dataAll['truegostd'] = true;
		}
	}

		if(dataAll['trueNotify']==false){
			let condition1=dataAll['positionOfNotifyBodyX']>dataAll['distancePointerMouseX']
		&& 74<dataAll['distancePointerMouseY'] && dataAll['distancePointerMouseY']<dataAll['positionOfNotifyY'];
			let condition2=dataAll['positionOfNotifyY']<dataAll['distancePointerMouseY'];
		if(condition1 || condition2){
			dataAll['notification'].style.display = 'none';
			dataAll['trueNotify'] = true;
		}
	}

    if(dataAll['truegostd']==false){
			let condition1=dataAll['positionOfProfilePhotoX']>dataAll['distancePointerMouseX'];
			 let condition2=dataAll['distancePointerMouseY']<74;
		if(condition1 && condition2){
			dataAll['gostdata'].style.display = 'none';
			dataAll['truegostd'] = true;
		}
    }

    if(dataAll['truegostm']==false){
	let condition1=dataAll['distancePointerMouseX']>(dataAll['positionOfMenuPhotoXGet']+dataAll['menu'].getBoundingClientRect().x);
     let condition2=dataAll['distancePointerMouseY']<74;

	if(condition1 && condition2){
		dataAll['gostmenu'].style.display = 'none';
		dataAll['truegostm'] = true;
	}
}


/*
for(var eve in event){
//console.log(`${eve} :  ${event[eve]}`);
//console.log(`${eve} :  ${event.target[eve]}`);
}
*/
});

document.body.onresize =function(event){

	 if(document.body.clientWidth<603){
	/* 
		We get the position both MenuPhoto as of ProfilePhoto with these data I'm going to get the maximum distance that logo image can have of width
		besides logo image's height will be the same like 	MenuPhoto.These data I allow me give it a position appropiated to logo image
	*/

		dataAll['positionOfMenuPhotoXGet']=dataAll['menu'].getBoundingClientRect().width;	// x position of the right border of MenuPhoto
		dataAll['positionOfProfilePhotoX'] = dataAll['logoSign'].getBoundingClientRect().x;		// x position of ProfilePhoto
		dataAll['positionOfMenuPhotoYGet']=dataAll['logoSign'].getBoundingClientRect().height; 	// Heigth
;
		
		dataAll['intervalLogoMenu'] = (dataAll['positionOfProfilePhotoX']-dataAll['positionOfMenuPhotoXGet'])*1; // Difference tween [ x position of ProfilePhoto] and [x position of the right border of MenuPhoto]
		
		dataAll['logo'].style.marginLeft = (dataAll['positionOfMenuPhotoXGet'] +1)*1+"px";
		dataAll['logoWidth']=dataAll['logo'].getBoundingClientRect().width;
		if(dataAll['intervalLogoMenu']<dataAll['logoWidth'] && dataAll['intervalLogoMenu']>0){
			dataAll['logo'].style.minWidth = ((dataAll['intervalLogoMenu']-2)*1)*1 +"px";
		}
		
	}else{
		dataAll['logo'].style.marginLeft = "0px";
	}
		
};

/*--------------------------------------Only when it loads the page it's executed this------------------------------------------*/
	 if(document.body.clientWidth<603){
	/*
		We get the position both MenuPhoto as of ProfilePhoto with these data I'm going to get the maximum distance that logo image can have of width
		besides logo image's height will be the same like 	MenuPhoto.These data I allow me give it a position appropiated to logo image
	*/

		dataAll['positionOfMenuPhotoXGet']=dataAll['menu'].getBoundingClientRect().width;	// x position of the right border of MenuPhoto
		dataAll['positionOfProfilePhotoX'] = dataAll['logoSign'].getBoundingClientRect().x;		// x position of ProfilePhoto
		dataAll['positionOfMenuPhotoYGet']=dataAll['menu'].getBoundingClientRect().height; 	// Heigth
;

		dataAll['intervalLogoMenu'] = (dataAll['positionOfProfilePhotoX']-dataAll['positionOfMenuPhotoXGet'])*1; // Difference tween [ x position of ProfilePhoto] and [x position of the right border of MenuPhoto]

		dataAll['logo'].style.marginLeft = (dataAll['positionOfMenuPhotoXGet'] +1)*1+"px";
		if(dataAll['intervalLogoMenu']<dataAll['logo'].getBoundingClientRect().width){
			dataAll['logo'].style.minWidth = ((dataAll['intervalLogoMenu']-2)*1)*1 +"px";
			//console.log("dataAll['intervalLogoMenu'] "+dataAll['intervalLogoMenu']+"  dataAll['logo'].clientWidth "+dataAll['logo'].getBoundingClientRect().width);
		}
	}
/*--------------------------------------Only when it loads the page it's executed this------------------------------------------*/

});