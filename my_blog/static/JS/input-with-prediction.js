/*
    The resize event inside the load event is triggered
    when the page has been loaded
*/
window.addEventListener('load', function(){
    function changeSizeTypeahead()
    {
            let onetwo = document.querySelector(`.tt-hint`);
            let two = document.querySelector(`.tt-dataset`);
            two.style.width = `${onetwo.clientWidth}px`;
        }

    this.addEventListener('resize', changeSizeTypeahead);
});
// Execute when the DOM is fully loaded
$(document).ready(function() {
// Configure typeahead
    $(".typeahead").typeahead(
    {
        hint: true,
        highlight: true,
        minLength: 1,
        searchOnFocus: true,
        autoselect: true,
        // https://github.com/corejavascript/typeahead.js/blob/master/doc/jquery_typeahead.md#class-names
        className: {
            input:'tt-input',
            hint:'tt-hint',
            menu: 'tt-menu',
            dataset: 'tt-dataset',
            suggestion:'tt-suggestion',
            empty:' tt-empty',
            open:'tt-open',
            cursor:'tt-cursor',
            highlight:'tt-highlight',
            selectable: 'Typeahead-selectable'
        },

    },
    {
        display: function(suggestion)
        {
            return `${suggestion.fields.title}`;

        },
        limit: 10,
        source: search,
        templates: {
            suggestion: Handlebars.compile(
                "<div>" +
                "{{fields.title}}"+
                "</div>"
            )
        },
    });

    $('.typeahead').bind('typeahead:active', function(ev, suggestion) {
        let onetwo = document.querySelector(`.tt-hint`);
        let two = document.querySelector(`.tt-dataset`);
        two.style.width = `${onetwo.clientWidth}px`;
    });

    $('.typeahead').bind('typeahead:cursorchange', function(ev, suggestion, name) {
            let onetwo = document.querySelector(`.section-middle-more-search`);
            let allElements = document.querySelectorAll(`.tt-suggestion`);
            allElements.forEach
            (
                function(element, index)
                {
                    if(suggestion != null)
                    {
                        if(element.textContent.search(suggestion.fields.title) != -1){
                            element.style.backgroundColor = "rgb(200, 200, 200)";
                        }else{
                            element.style.backgroundColor = "white";
                        }
                    }
                }
            );
    });

    // When typeahead is selected from drop-down
    $(".typeahead").on("typeahead:select", function(eventObject, suggestion, name) {

        //console.log(suggestion.fields.title, name);
        window.location.href = suggestion.fields.slug;
    });

// Search database for typeahead's suggestions
function search(query, syncResults, asyncResults)
{
    // Get ready the matches query (asynchronously)
    let parameters = {
        q: query
    };
    $.getJSON("/user/searching", parameters, function(data, textStatus, jqXHR) {

        // Call typeahead's callback with search results (i.e., places)
        asyncResults(data);
    });
}
});

