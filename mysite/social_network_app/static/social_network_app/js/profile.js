
function addClickListenerToAddFriendButton(currentUserPk, profileUserPk, token) {
    const addFriendButton = document.querySelector('#add-friend-button');
    console.log(addFriendButton)

    addFriendButton.addEventListener('click', () => {
        console.log('click')
        $.ajax({
            type: "POST",
            url: "/social-network/add-friend/",
            data: {
                'current_user_pk': currentUserPk,
                'profile_user_pk':profileUserPk,
                'csrfmiddlewaretoken': token
            },
            dataType: "html",
            success: function (response) {
                addFriendButton.textContent = 'Added';
            },
        })
    })
}

