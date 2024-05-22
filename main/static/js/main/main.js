window.onload(toglMenu())

function scr(targetId){
  const targetElement = document.getElementById(targetId);
  console.log(targetElement.offsetTop)
  console.log((targetElement.offsetTop)-20)
  window.scrollTo({
    top: (targetElement.offsetTop)-80,
    behavior: 'smooth'
  });
  toglMenu()
}
function Menu() {
  let navMenu = document.querySelector('.nav');
  document.querySelector('.hamburger').style.display = 'none'
  document.querySelector('.close-btn').style.display = 'block'
  if(!navMenu.classList.contains('navColumn')) {
    navMenu.classList.add('navColumn');
  }
}
function toglMenu(){
  let navMenu = document.querySelector('.nav');
  document.querySelector('.hamburger').style.display = 'flex'
  document.querySelector('.close-btn').style.display = 'none'
  if(navMenu.classList.contains('navColumn')){
  navMenu.classList.remove('navColumn');
}
}