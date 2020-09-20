$(document).ready(function () {

    $('.loader').hide()

    $(this).ajaxStart(function () {
        $('.loader').show()
        $('.submit').hide()
        console.log('ajax start')
    }).ajaxStop(function () {
        $('.submit').show()
        $('.loader').hide()
        console.log('ajax stop')
    });

    $('.submit').bind('click', function () {

        var paragraph = $(".textarea").val()
        var num = $("input[name='high-low']:checked").val()
        console.log('input : ', paragraph, num)

        if ((paragraph.split(" ")).length < 200) {
            alert(`Paragraph should me minimum 200 words!`)
        }

        else {

            $.ajax({
                url: "/result/", //the page containing python script
                type: "POST", //request type,
                data: { 'paragraph': paragraph, 'num': num }, //num - 1 for high, 0 for low, to change toggle value in template>index.html
                cache: false,
                async: true,

                success: function (response) {

                    response = JSON.parse(response)
                    console.log('response recieved', response)
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
                               <span style='font-weight: bolder;'>Ans: ${response[i].answer}</span>
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
                                <span style='font-weight: bolder;'>Ans: ${response[i].answer}</span>
                            </ul>
                        </div>`)
                        }
                    }
                    $(document).scrollTop($(document).height());
                }
            })
        }
    })
});