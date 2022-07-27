var html = document.getElementsByTagName('html').item(0);
var body = document.getElementsByTagName('body').item(0);
var table = document.getElementById('input-table');
var searchInput = document.getElementById('id_q');
var searchLabel = searchInput.parentElement.parentElement.firstElementChild.firstElementChild;
var inputGroupDiv = document.createElement('div');
var searchButton = document.getElementById('search-button');
var floatingLabelDiv = document.createElement('div');
var passwordManagerMenu = document.getElementById('password-manager-menu');

html.classList.add('h-100');

body.classList.add('h-100');

inputGroupDiv.classList.add('input-group', 'justify-content-center');
searchButton.classList.add('btn', 'btn-secondary');

floatingLabelDiv.classList.add('form-floating');
floatingLabelDiv.appendChild(searchInput);
floatingLabelDiv.appendChild(searchLabel);

inputGroupDiv.appendChild(floatingLabelDiv);
inputGroupDiv.appendChild(searchButton);

searchInput.classList.add('form-control');
searchInput.setAttribute('placeholder', searchLabel.innerHTML);

table.replaceWith(inputGroupDiv);

passwordManagerMenu.classList.add('active');
