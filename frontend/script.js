$(document).ready(function () {
    $('.submit').bind('click', function () {
        var paragraph = $(".textarea").val()

        if ((paragraph.split(" ")).length < 200) {
            alert(`Paragraph should me minimum 400 words!`)
        }
        else {

            $.ajax({
                url: "test1", //the page containing python script
                type: "post", //request type,
                data: paragraph,
                contentType: false,
                cache: false,
                processData: false,
                async: true,

                success: function (response) {

                    $('.submit').hide();
                    $('.loader').show();
                    $('.output').empty();
                    $('.output').append('<div class="header oSub"><p>Questions</p></div>');
                    $('.output').show();
                    var temp = ''

                    for (var i = 0; i < response.length; i++) {

                        temp = ''
                        if (response[i].extras.length > 0) {
                            for (var j = 0; j < response[i].extras.length; j++) {
                                temp += `<option>${response[i].extras[j]}</option>`
                            }
                        }

                        if (response[i].options.length == 4) {
                            $('.output').append(`<div class="question">
                            <p><span class="bold">Q${i + 1}.</span>${response[i].question}</p>
                            <ul>
                                <li>${response[i].options[0]}</li>
                                <li>${response[i].options[1]}</li>
                                <li>${response[i].options[2]}</li>
                                <li>${response[i].options[3]}</li>
                                ${temp.length > 0 ? `<li><select><option disabled selected>More Options..</option>${temp}</select></li>` : ''}
                                <li>Answer: <span style="color: rgb(11, 206, 11); font-weight: bolder;">${response[i].answer}</span></li>
                            </ul>
                        </div>`)
                        }

                        else {
                            $('.output').append(`<div class="question">
                            <p><span class="bold">Q${i + 1}.</span>${response[i].question}</p>
                            <ul>
                                <li>${response[i].options[0]}</li>
                                <li>${response[i].options[1]}</li>
                                <li>${response[i].options[2]}</li>
                                ${temp.length > 0 ? `<li><select><option disabled selected>More Options..</option>${temp}</select></li>` : ''}
                                <li>Answer: <span style="color: rgb(11, 206, 11); font-weight: bolder;">${response[i].answer}</span></li>
                            </ul>
                        </div>`)
                        }
                    }
                    $('.submit').show();
                    $('.loader').hide();
                    $(document).scrollTop($(document).height());
                }
            })
        }
    })
});