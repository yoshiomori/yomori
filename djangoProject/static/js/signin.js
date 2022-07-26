var html = document.getElementsByTagName('html').item(0);
var body = document.getElementsByTagName('body').item(0);
var form = document.getElementById('form');
var tableHtmlCollection = form.getElementsByTagName('table');
var a = document.getElementById('login-menu');
var usernameInput = document.getElementById('id_username');

html.classList.add('h-100');

body.classList.add('h-100');
body.classList.add('text-center');

for(var index=0; index<tableHtmlCollection.length; index++){
    var tableNode = tableHtmlCollection.item(index);
    var inputNodeList = tableNode.querySelectorAll('input');
    var labelNodeList = tableNode.querySelectorAll('label');
    var nonfieldErrorLiNodeList = tableNode.querySelectorAll('ul.errorlist.nonfield li');
    var firstDiv = document.createElement('div');
    var currentDiv = firstDiv;
    var toastContainer = document.createElement('div');
    
    tableNode.parentNode.replaceChild(firstDiv, tableNode);
    toastContainer.classList.add('toast-container', 'p-3', 'bottom-0', 'end-0');
    
    nonfieldErrorLiNodeList.forEach(errorLi=>{
        var toast = document.createElement('div');
        var toastBody = document.createElement('div');
        var closeToastButton = document.createElement('button');
        closeToastButton.setAttribute('type', 'button');
        closeToastButton.setAttribute('data-bs-dismiss', 'toast');
        closeToastButton.setAttribute('aria-label', 'Close');
        closeToastButton.classList.add('btn-close', 'me-2', 'm-auto');
        toast.classList.add('toast', 'fade', 'show', 'd-flex', 'align-items-center',  'text-bg-danger', 'border-0');
        toastBody.classList.add('toast-body');
        toastContainer.appendChild(toast);
        toastBody.innerHTML = errorLi.innerHTML;
        toast.appendChild(toastBody);
        toast.appendChild(closeToastButton);
    });    
    body.appendChild(toastContainer);

    inputNodeList.forEach((inputNode, i)=>{
        var errorUlNodeList = inputNode.parentNode.querySelectorAll('ul.errorlist');
        var labelNode = labelNodeList.item(i);
        currentDiv.classList.add('form-floating');
        inputNode.classList.add('form-control');
        currentDiv.appendChild(inputNode);
        currentDiv.appendChild(labelNode);
        inputNode.setAttribute('placeholder', labelNode.innerHTML);
        if (errorUlNodeList.length>0) {
            var invalidFeedbackDiv = document.createElement('div');
            invalidFeedbackDiv.classList.add('invalid-feedback');
            inputNode.classList.add('is-invalid');
            errorUlNodeList.forEach(invalidFeedbackDiv.appendChild.bind(invalidFeedbackDiv));
            inputNode.parentNode.appendChild(invalidFeedbackDiv);
        }
        if (inputNodeList.length - 1 > i) {
            var div = document.createElement('div');
            currentDiv.parentNode.insertBefore(div, currentDiv.nextSibling);
            currentDiv = div;
        }
    });
}

a.classList.add('active');

usernameInput.focus();