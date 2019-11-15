var toons = JSON.parse(document.getElementById('eve_characters').textContent);

function set_active_character(id) {
    localStorage.setItem('selected_character', id);
    render_active_character();
}

function get_active_character() {
    var current = localStorage.getItem('selected_character');

    if (current == null || !(current in toons)) {
        console.log("Lmao");
        current = Object.keys(toons)[0];
        localStorage.setItem('selected_character', current);
    }

    return current;
}

function render_active_character() {
    var current = get_active_character();
    $("#current_character_avatar")[0].src = "https://image.eveonline.com/Character/" + current + "_32.jpg";
    $("#current_character_name")[0].textContent = toons[current].name;
}

function populate_character_selector() {
    var container = $("#character_select_list");
    var url = "/auth/login"

    Object.keys(toons).forEach(function (key) {
        container.append(
            '<a class="dropdown-item" href="javascript:set_active_character(' + key + 
            ');"><img src="https://image.eveonline.com/Character/' + 
            key + '_32.jpg" height="24px" class="avatar mr-2" />' + toons[key].name + '</a>'
        );
    });

    container.append(
        '<a class="dropdown-item" href="' + 
        url + 
        '"><i class="fas fa-plus ml-1 mr-2"></i></i>' +
        '  <span class="ml-1">Add character</span></a>'
    )
}

document.addEventListener('DOMContentLoaded', (event) => { 
    if (user_logged_in) {
        render_active_character(); 
        populate_character_selector(); 
    }
});