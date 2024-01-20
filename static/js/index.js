document.addEventListener("DOMContentLoaded", function() {
    const input_text = document.getElementById("input_text");
    const pdf_view = document.getElementById("pdf_view");
    const input_text_size = document.getElementById("input_text_size");
    const alert_error = document.getElementById("alert_error");
    const url = "/latex";
    const pdf_filepath = "static/temp/temp.pdf";
    let timeout = null;

    function submit_latex(event) {
        // event.preventDefault();
        const xhr = new XMLHttpRequest();
        const file = new Blob([input_text.value], { type: "text/plain" });
        const formData = new FormData();
        formData.append("file", file, "temp.tex");
        xhr.open("POST", url, true);
        xhr.send(formData);
        xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              pdf_view.src = pdf_filepath;
            }
            else if(xhr.status === 415){
              const response = JSON.parse(xhr.responseText);
              alert_error.style.display = "block";
              alert_error.innerText = response.result;
              console.log(response.result);
              if (timeout) {
                  clearTimeout(timeout);
              }
              timeout = setTimeout(function() {
                  alert_error.style.display = "none";
              }, 2500);
            }
          }
        };
    }
    input_text.addEventListener('keyup', (event) => {
        if (timeout) {
            clearTimeout(timeout);
        }
        timeout = setTimeout(function() {
            //当输入停止0.8秒后将输入的内容传入处理函数
            submit_latex();
        }, 800);
    });
    input_text_size.addEventListener('keyup', (event) => {
        // console.log(input_text_size.value);
        // console.log(input_text.style.fontSize);
        console.log(event.keyCode);
        if (event.keyCode == 38){
            input_text_size.value = parseInt(input_text_size.value)+1;
        }
        else if(event.keyCode == 40){
            input_text_size.value = parseInt(input_text_size.value)-1;
        }
        input_text.setAttribute('style', 'font-size: ' + input_text_size.value + 'px');
    });
});